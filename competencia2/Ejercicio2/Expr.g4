grammar Expr;


root : expr EOF;

// expr: expr MAS expr | NUM;
expr: EOF;
ID: [a-zA-Z]+;
IF: 'if';

MAYOR_QUE: '>';
NUM: [0-9]+;
MAS: '+';
WS : [ \t\r\n]+ -> skip ;
