grammar Expr;


root : expr EOF;

// expr: expr MAS expr | NUM;
expr: EOF;

NUM: [0-9]+;
MAS: '+';
WS : [ \t\r\n]+ -> skip ;
