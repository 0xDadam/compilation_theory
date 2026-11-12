class AST:
    def printTree(self, indent=0):
        raise NotImplementedError("printTree not defined in class " + self.__class__.__name__)


class IntNum(AST):
    def __init__(self, value):
        self.value = value


class FloatNum(AST):
    def __init__(self, value):
        self.value = value


class String(AST):
    def __init__(self, value):
        self.value = value


class Variable(AST):
    def __init__(self, name):
        self.name = name


class BinExpr(AST):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class UnaryExpr(AST):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr


class Assignment(AST):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class MatrixFunc(AST):
    def __init__(self, name, arg):
        self.name = name
        self.arg = arg


class Vector(AST):
    def __init__(self, elements):
        self.elements = elements


class Ref(AST):
    def __init__(self, variable, indices):
        self.variable = variable
        self.indices = indices


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


class Error(AST):
    pass