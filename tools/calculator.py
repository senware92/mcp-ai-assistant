import ast
import operator

ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def eval_expr(expr):
    node = ast.parse(expr, mode='eval').body

    if isinstance(node, ast.Num):
        return node.n

    if isinstance(node, ast.BinOp):
        return ops[type(node.op)](eval_expr(ast.unparse(node.left)), eval_expr(ast.unparse(node.right)))

def calculate_expression(query):
    try:
        expr = ''.join(c for c in query if c in "0123456789+-*/(). ")
        return eval(expr)
    except:
        return "Invalid expression"