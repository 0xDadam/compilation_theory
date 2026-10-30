from sly import Parser
from lab1.scanner import Scanner


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

    @_('instructions_opt')
    def program(self, p):
        pass

    @_('instructions',
       '')
    def instructions_opt(self, p):
        pass
    
    @_('instructions instruction',
       'instruction')
    def instructions(self, p):
        pass

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
        pass


    @_('ID assignment_operator expr',
       'ID "[" expr "," expr "]" assignment_operator expr')
    def assignment(self, p):
        pass

    @_('"="',
       'ADDASSIGN',
       'SUBASSIGN',
       'MULASSIGN',
       'DIVASSIGN')
    def assignment_operator(self, p):
        pass

    @_('PRINT expr_list')
    def print_stmt(self, p):
        pass

    @_('BREAK')
    def break_stmt(self, p):
        pass

    @_('CONTINUE')
    def continue_stmt(self, p):
        pass

    @_('RETURN',
       'RETURN expr')
    def return_stmt(self, p):
        pass

    @_('"{" instructions_opt "}"')
    def compound_stmt(self, p):
        pass

    @_('IF expr instruction %prec IFX',
       'IF expr instruction ELSE instruction',)
    def if_stmt(self, p):
        pass

    @_('WHILE expr instruction',)
    def while_stmt(self, p):
        pass

    @_('FOR ID "=" expr ":" expr instruction')
    def for_stmt(self, p):
        pass

    @_('ZEROS "(" expr ")"',
       'ONES "(" expr ")"',
       'EYE "(" expr ")"')
    def expr(self, p):
        pass

    @_('"[" matrix_rows "]"')
    def expr(self, p):
        pass

    @_('matrix_rows "," matrix_row',
       'matrix_row')
    def matrix_rows(self, p):
        pass

    @_('"[" expr_list "]"')
    def matrix_row(self, p):
        pass

    @_('expr_list "," expr',
       'expr')
    def expr_list(self, p):
        pass

    @_('expr "+" expr',
       'expr "-" expr',
       'expr "*" expr',
       'expr "/" expr',
       'expr DOTADD expr',
       'expr DOTSUB expr',
       'expr DOTMUL expr',
       'expr DOTDIV expr')
    def expr(self, p):
        pass

    @_('expr "<" expr',
       'expr ">" expr',
       'expr EQ expr',
       'expr NEQ expr',
       'expr LE expr',
       'expr GE expr')
    def expr(self, p):
        pass

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        pass

    @_('expr "\'"')
    def expr(self, p):
        pass

    @_('"(" expr ")"')
    def expr(self, p):
        pass

    @_('ID', 
       'INTNUM', 
       'FLOATNUM', 
       'STRING')
    def expr(self, p):
        pass

    @_('ID "[" expr "," expr "]"')
    def expr(self, p):
        pass

    def error(self, p):
        if p:
            print(f"({p.lineno}): blad skladniowy - niespodziewany token '{p.value}'")
        else:
            print("blad skladniowy: niespodziewany koniec pliku (EOF)")
