from agent import MCPAgent

def main():
    agent = MCPAgent()

    print("MCP-Style AI Research Assistant\n")

    while True:
        query = input(">> ").strip()
        if query.lower() in ["exit", "quit"]:
            break

        result = agent.run(query)
        print(result)
        print()

if __name__ == "__main__":
    main()