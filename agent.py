from tools.search import search_docs
from tools.calculator import calculate_expression
from tools.summarize import summarize_text


class MCPAgent:
    def __init__(self):
        self.tools = {
            "search": {
                "description": "Retrieve relevant info from documents",
                "fn": search_docs
            },
            "calculator": {
                "description": "Perform math computations",
                "fn": calculate_expression
            },
            "summarize": {
                "description": "Summarize text",
                "fn": summarize_text
            }
        }

    def route(self, query):
        q = query.lower()

        if any(x in q for x in ["+", "-", "*", "/", "calculate"]):
            return "calculator"

        if "summarize" in q or "summary" in q:
            return "summarize"

        return "search"

    def run(self, query):
        tool_name = self.route(query)
        tool = self.tools[tool_name]["fn"]

        output = tool(query)

        return f"""
Query: {query}
Tool Used: {tool_name}
Result: {output}
"""