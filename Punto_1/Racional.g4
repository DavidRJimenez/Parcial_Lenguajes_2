grammar Racional;

prog:   expr EOF;

expr:   expr ('+' | '-') term
    |   term
    ;

term:   term ('*' | '/') factor
    |   factor
    ;

factor: RACIONAL
    |   '(' expr ')'
    ;

RACIONAL: NUM '/' NUM;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;
