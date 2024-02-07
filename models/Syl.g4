grammar Syl;

// Sintax analysis 
prog: instruction EOF;

instruction: var_declaration;
var_declaration: VAR ID SEMICOLON; 
// Sintax analysis 


// Skipeable elements

//saltar esto
WS
:
 [ \t\r\n]+ -> skip
;

// Skipeable elements

// Palabras clave
VAR: 'var';
SEMICOLON: ';'; // End of instruction line
// Palabras clave

// Expresiones completas
ID: [a-zA-Z][0-9a-zA-Z]*;