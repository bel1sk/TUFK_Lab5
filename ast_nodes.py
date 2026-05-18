class SymbolTable:
    def __init__(self):
        self.symbols = {}
        
    def declare(self, name, var_type, row, col):
        if name in self.symbols:
            return False
        self.symbols[name] = {'type': var_type, 'row': row, 'col': col}
        return True
        
    def lookup(self, name):
        return self.symbols.get(name)

class AstNode:
    def print_ast(self, indent="", is_last=True):
        pass

class ProgramNode(AstNode):
    def __init__(self, name, init_node):
        self.name = name
        self.init_node = init_node

    def print_ast(self, indent="", is_last=True):
        prefix = "└── " if is_last else "├── "
        res = f"{indent}{prefix}ProgramNode (name: {self.name})\n"
        child_indent = indent + ("    " if is_last else "│   ")
        if self.init_node:
            res += self.init_node.print_ast(child_indent, True)
        return res

class LambdaNode(AstNode):
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def print_ast(self, indent="", is_last=True):
        prefix = "└── " if is_last else "├── "
        res = f"{indent}{prefix}LambdaNode\n"
        child_indent = indent + ("    " if is_last else "│   ")
        
        for i, param in enumerate(self.params):
            is_last_param = (i == len(self.params) - 1) and (self.body is None)
            res += param.print_ast(child_indent, is_last_param)
            
        if self.body:
            res += self.body.print_ast(child_indent, True)
        return res

class ParamNode(AstNode):
    def __init__(self, param_type, name):
        self.param_type = param_type
        self.name = name

    def print_ast(self, indent="", is_last=True):
        prefix = "└── " if is_last else "├── "
        return f"{indent}{prefix}ParamNode (type: {self.param_type}, name: {self.name})\n"

class BinaryOpNode(AstNode):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def print_ast(self, indent="", is_last=True):
        prefix = "└── " if is_last else "├── "
        res = f"{indent}{prefix}BinaryOpNode (op: {self.op})\n"
        child_indent = indent + ("    " if is_last else "│   ")
        if self.left:
            res += self.left.print_ast(child_indent, False)
        if self.right:
            res += self.right.print_ast(child_indent, True)
        return res

class VariableNode(AstNode):
    def __init__(self, name):
        self.name = name

    def print_ast(self, indent="", is_last=True):
        prefix = "└── " if is_last else "├── "
        return f"{indent}{prefix}VariableNode (name: {self.name})\n"

class LiteralNode(AstNode):
    def __init__(self, value):
        self.value = value

    def print_ast(self, indent="", is_last=True):
        prefix = "└── " if is_last else "├── "
        return f"{indent}{prefix}LiteralNode (value: {self.value})\n"
