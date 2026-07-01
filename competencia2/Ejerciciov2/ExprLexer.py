# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,21,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,4,1,11,8,1,11,
        1,12,1,12,1,2,4,2,16,8,2,11,2,12,2,17,1,2,1,2,0,0,3,1,1,3,2,5,3,
        1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,22,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,1,7,1,0,0,0,3,10,1,0,0,0,5,15,1,0,0,0,7,8,5,45,0,0,8,
        2,1,0,0,0,9,11,7,0,0,0,10,9,1,0,0,0,11,12,1,0,0,0,12,10,1,0,0,0,
        12,13,1,0,0,0,13,4,1,0,0,0,14,16,7,1,0,0,15,14,1,0,0,0,16,17,1,0,
        0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,6,2,0,0,20,6,
        1,0,0,0,3,0,12,17,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MENOS = 1
    NUM = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'" ]

    symbolicNames = [ "<INVALID>",
            "MENOS", "NUM", "WS" ]

    ruleNames = [ "MENOS", "NUM", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


