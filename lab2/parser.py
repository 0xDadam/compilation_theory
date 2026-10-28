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
    def program(p):
        pass

    @_('instructions')
    def instructions_opt(p):
        pass

    @_('')
    def instructions_opt(p):
        pass

    @_('instructions instruction')
    def instructions(p):
        pass

    @_('instruction')
    def instructions(p):
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

