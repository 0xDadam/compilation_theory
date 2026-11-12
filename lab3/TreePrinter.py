try:
    from . import AST
except ImportError:
    import AST


def addToClass(cls):
    def decorator(function):
        setattr(cls, function.__name__, function)
        return function
    return decorator


def _print_children(children, indent):
    if children is None:
        return
    for child in children:
        if child is not None:
            child.printTree(indent)


class TreePrinter:

    @addToClass(AST.AST)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.value))

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.value))

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.value))

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.name))

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.op))
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.op))
        self.expr.printTree(indent + 1)

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.op))
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.MatrixFunc)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.name))
        self.arg.printTree(indent + 1)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print("|  " * indent + "VECTOR")
        _print_children(self.elements, indent + 1)

    @addToClass(AST.Ref)
    def printTree(self, indent=0):
        print("|  " * indent + "REF")
        self.variable.printTree(indent + 1)
        _print_children(self.indices, indent + 1)

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        print("|  " * indent + "RANGE")
        if self.start is not None:
            self.start.printTree(indent + 1)
        if self.end is not None:
            self.end.printTree(indent + 1)

    @addToClass(AST.If)
    def printTree(self, indent=0):
        print("|  " * indent + "IF")
        if self.condition is not None:
            self.condition.printTree(indent + 1)
        print("|  " * indent + "THEN")
        if self.then_stmt is not None:
            self.then_stmt.printTree(indent + 1)
        if self.else_stmt is not None:
            print("|  " * indent + "ELSE")
            self.else_stmt.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        print("|  " * indent + "WHILE")
        if self.condition is not None:
            self.condition.printTree(indent + 1)
        if self.statement is not None:
            self.statement.printTree(indent + 1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print("|  " * indent + "FOR")
        self.variable.printTree(indent + 1)
        self.range.printTree(indent + 1)
        if self.statement is not None:
            self.statement.printTree(indent + 1)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print("|  " * indent + "PRINT")
        _print_children(self.expressions, indent + 1)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        print("|  " * indent + "BREAK")

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        print("|  " * indent + "CONTINUE")

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print("|  " * indent + "RETURN")
        if self.expression is not None:
            self.expression.printTree(indent + 1)

    @addToClass(AST.CompoundStmt)
    def printTree(self, indent=0):
        _print_children(self.instructions, indent)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass


def printTree(tree):
    _print_children(tree, 0) if isinstance(tree, list) else tree.printTree()