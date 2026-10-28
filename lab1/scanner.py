import sys
from sly import Lexer

class Scanner(Lexer):

     tokens = {
          ID, INTNUM, FLOATNUM, STRING,
          DOTADD, DOTSUB, DOTMUL, DOTDIV,
          ADDASSIGN, SUBASSIGN, MULASSIGN, DIVASSIGN,
          EQ, NEQ, LE, GE,
          IF, ELSE, FOR, WHILE, BREAK, CONTINUE, RETURN,
          EYE, ZEROS, ONES, PRINT
     }

     literals = { '+', '-', '*', '/', '=', '<', '>', '(', ')', '[', ']', '{', '}', ':', "'", ',', ';' }

     ignore = ' \t'
     ignore_comment = r'\#.*'

     DOTADD = r'\.\+'
     DOTSUB = r'\.-'
     DOTMUL = r'\.\*'
     DOTDIV = r'\./'
     
     ADDASSIGN = r'\+='
     SUBASSIGN = r'-='
     MULASSIGN = r'\*='
     DIVASSIGN = r'/='
     
     EQ = r'=='
     NEQ = r'!='
     LE = r'<='
     GE = r'>='


     FLOATNUM = r'((\d+\.\d*)|(\.\d+))([eE][+-]?\d+)?|\d+[eE][+-]?\d+'
     INTNUM = r'\d+'
     STRING = r'\"([^\\\n]|(\\.))*?\"'


     ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
     ID['if'] = IF
     ID['else'] = ELSE
     ID['for'] = FOR
     ID['while'] = WHILE
     ID['break'] = BREAK
     ID['continue'] = CONTINUE
     ID['return'] = RETURN
     ID['eye'] = EYE
     ID['zeros'] = ZEROS
     ID['ones'] = ONES
     ID['print'] = PRINT


     @_(r'\n+')
     def ignore_newline(self, t):
         self.lineno += t.value.count('\n')


     def error(self, t):
         print('Linia %d: nierozpoznany znak %r' % (self.lineno, t.value[0]))
         self.index += 1

if __name__ == '__main__':
     lexer = Scanner()
    
     if len(sys.argv) > 1:
          with open(sys.argv[1], "r") as f:
               text = f.read()
     else:
          text = sys.stdin.read()

     for tok in lexer.tokenize(text):
          print(f"({tok.lineno}): {tok.type}({tok.value})")