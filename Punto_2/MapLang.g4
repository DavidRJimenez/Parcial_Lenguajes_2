grammar MapLang;

program: mapExpression EOF;

mapExpression: 'MAP' '(' function ',' iterable ')';
function: IDENTIFIER;
iterable: list | tuple;
list: '[' (expression (',' expression)*)? ']';
tuple: '(' (expression (',' expression)*)? ')';
expression: IDENTIFIER | NUMBER;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
WS: [ \t\n\r]+ -> skip;
