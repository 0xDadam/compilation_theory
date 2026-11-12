from sly import Parser
try:
    from lab1.scanner import Scanner
except ImportError:
    from scanner import Scanner

try:
    from . import AST
except ImportError:
    import AST


class Mparser(Parser):

    tokens = Scanner.tokens

    debugfile = 'parser.out'

    precedence = (
        ('nonassoc', IFX),
        ('nonassoc', ELSE),
        ('nonassoc', '<', '>', EQ, NEQ, LE, GE),
        ('left', '+', '-', DOTADD, DOTSUB),
        ('left', '*', '/', DOTMUL, DOTDIV),
        ('right', UMINUS),
        ('left', "'"),
    )

    def __init__(self):
        self.has_error = False

    @_('instructions_opt')
    def program(self, p):
        return p.instructions_opt

    @_('instructions',
       '')
    def instructions_opt(self, p):
        return p.instructions if p else []

    @_('instructions instruction',
       'instruction')
    def instructions(self, p):
        return p.instructions + [p.instruction] if len(p) == 2 else [p.instruction]

    @_('assignment ";"',
       'print_stmt ";"',
       'break_stmt ";"',
       'continue_stmt ";"',
       'return_stmt ";"',
       'if_stmt',
       'while_stmt',
       'for_stmt',
       'compound_stmt')
    def instruction(self, p):
        return p[0]

    @_('ID assignment_operator expr')
    def assignment(self, p):
        return AST.Assignment(p.assignment_operator, AST.Variable(p.ID), p.expr)

    @_('ID "[" expr "," expr "]" assignment_operator expr')
    def assignment(self, p):
        ref = AST.Ref(AST.Variable(p.ID), [p.expr0, p.expr1])
        return AST.Assignment(p.assignment_operator, ref, p.expr2)

    @_('"="',
       'ADDASSIGN',
       'SUBASSIGN',
       'MULASSIGN',
       'DIVASSIGN')
    def assignment_operator(self, p):
        return p[0]

    @_('PRINT expr_list')
    def print_stmt(self, p):
        return AST.Print(p.expr_list)

    @_('BREAK')
    def break_stmt(self, p):
        return AST.Break()

    @_('CONTINUE')
    def continue_stmt(self, p):
        return AST.Continue()

    @_('RETURN',
       'RETURN expr')
    def return_stmt(self, p):
        return AST.Return(p.expr if len(p) == 2 else None)

    @_('"{" instructions_opt "}"')
    def compound_stmt(self, p):
        return AST.CompoundStmt(p.instructions_opt)

    @_('IF expr instruction %prec IFX',
       'IF expr instruction ELSE instruction')
    def if_stmt(self, p):
        return AST.If(p.expr, p[2], p[4] if len(p) == 5 else None)

    @_('WHILE expr instruction')
    def while_stmt(self, p):
        return AST.While(p.expr, p.instruction)

    @_('FOR ID "=" expr ":" expr instruction')
    def for_stmt(self, p):
        return AST.For(
            AST.Variable(p.ID),
            AST.Range(p.expr0, p.expr1),
            p.instruction,
        )

    @_('ZEROS "(" expr ")"',
       'ONES "(" expr ")"',
       'EYE "(" expr ")"')
    def expr(self, p):
        return AST.MatrixFunc(p[0], p.expr)

    @_('"[" matrix_rows "]"')
    def expr(self, p):
        return AST.Vector(p.matrix_rows)

    @_('matrix_rows "," matrix_row',
       'matrix_row')
    def matrix_rows(self, p):
        return p.matrix_rows + [p.matrix_row] if len(p) == 3 else [p.matrix_row]

    @_('"[" expr_list "]"')
    def matrix_row(self, p):
        return AST.Vector(p.expr_list)

    @_('expr_list "," expr',
       'expr')
    def expr_list(self, p):
        return p.expr_list + [p.expr] if len(p) == 3 else [p.expr]

    @_('expr "+" expr',
       'expr "-" expr',
       'expr "*" expr',
       'expr "/" expr',
       'expr DOTADD expr',
       'expr DOTSUB expr',
       'expr DOTMUL expr',
       'expr DOTDIV expr',
       'expr "<" expr',
       'expr ">" expr',
       'expr EQ expr',
       'expr NEQ expr',
       'expr LE expr',
       'expr GE expr')
    def expr(self, p):
        return AST.BinExpr(p[1], p[0], p[2])

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return AST.UnaryExpr('-', p.expr)

    @_('expr "\'"')
    def expr(self, p):
        return AST.UnaryExpr('TRANSPOSE', p.expr)

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('ID')
    def expr(self, p):
        return AST.Variable(p.ID)

    @_('INTNUM')
    def expr(self, p):
        return AST.IntNum(p.INTNUM)

    @_('FLOATNUM')
    def expr(self, p):
        return AST.FloatNum(p.FLOATNUM)

    @_('STRING')
    def expr(self, p):
        return AST.String(p.STRING)

    @_('ID "[" expr "," expr "]"')
    def expr(self, p):
        return AST.Ref(AST.Variable(p.ID), [p.expr0, p.expr1])

    def error(self, p):
        self.has_error = True
        if p:
            print(f"({p.lineno}): blad skladniowy - niespodziewany token '{p.value}'")
        else:
            print("blad skladniowy: niespodziewany koniec pliku (EOF)")