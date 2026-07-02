grammar Expr;

root: expr EOF ;    

expr: NUM | IDF ;

NUM: [0-9]+ ;
IDF: [a-zA-Z]+ ;
WS: [ \t\r\n]+ -> skip ;