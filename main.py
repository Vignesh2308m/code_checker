import inspect
import ast
from ast import parse


######## Checks Every Part of the Code ########
class CodeChecker(ast.NodeVisitor):
    def __init__(self):
        self.function_calls = []
        super().__init__()

    def visit_Call(self, node):
        self.function_calls.append(node.func.id)
        self.generic_visit(node)


######### Security Prone Code #########
def prone_code(expr):
    eval(expr) #eval is prone to security issues
    return True





def main():
    code = inspect.getsource(prone_code)
    

    checker = CodeChecker()
    checker.visit(parse(code))

    for i in checker.function_calls:
        if 'eval'==i:
            print("Security Issue found in your code:\n",
                f"\tRestricted method used: {i}")

    

if __name__ == '__main__':  
    main()