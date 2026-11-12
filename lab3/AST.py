class AST:
    def printTree(self, indent=0):
        raise NotImplementedError


class Variable(AST):
    def __init__(self, name):
        self.name = name


class Range(AST):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class If(AST):
    def __init__(self, condition, then_stmt, else_stmt=None):
        self.condition = condition
        self.then_stmt = then_stmt
        self.else_stmt = else_stmt


class While(AST):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement


class For(AST):
    def __init__(self, variable, range_, statement):
        self.variable = variable
        self.range = range_
        self.statement = statement


class Print(AST):
    def __init__(self, expressions):
        self.expressions = expressions


class Break(AST):
    pass


class Continue(AST):
    pass


class Return(AST):
    def __init__(self, expression=None):
        self.expression = expression


class CompoundStmt(AST):
    def __init__(self, instructions):
        self.instructions = instructions
