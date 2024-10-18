grammar LaplaceTransform;

program: statement* EOF;

statement: laplaceExpression;

laplaceExpression: 'Laplace' '(' expression ')';

expression: term ((PLUS | MINUS) term)*;

term: factor ((MUL | DIV) factor)*;

factor: base (POW exponent)?;

base: specificFunction | NUMBER | IDENTIFIER | '(' expression ')';

exponent: specificFunction | NUMBER | IDENTIFIER | '(' expression ')';

specificFunction: 'exp' '(' expression ')' 
                | 'sin' '(' expression ')' 
                | 'cos' '(' expression ')' 
                | 'sinh' '(' expression ')' 
                | 'cosh' '(' expression ')' 
                | 'unit_step' '(' expression ')' 
                | 'delta_t_tau' 
                | 'delta_t' 
                | 't_n_exp' 
                | 'unit_step_tau' 
                | 't_n' 
                | 't_q' 
                | 'log' 
                | 'bessel_first' 
                | 'bessel_mod';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
POW: '**';

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
WS: [ \t\n\r]+ -> skip;
