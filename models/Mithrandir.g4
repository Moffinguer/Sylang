grammar Mithrandir;

// ========================================
// expresions
ID: [a-zA-Z_$][0-9a-zA-Z_$]*;
DECIMAL_NUMBER: [0-9]+;
FLOATING_NUMBER: [0-9]*'.'[0-9]+;
//todo STRING: '"'[^]*'"';

// ignoring parts
WS: [ \t\n]+;
COMMENTS: '#' ~( '\r' | '\n' )*;
// ========================================

// ========================================
// keywords
FUNCTION: 'elesar';
RETURN: 'comeback';
INTEGER_VAR: 'int';
FLOATING_VAR: 'double';
BOOLEAN_VAR: 'bool';
/// instructions
PRINT: 'println';
// blocks
OPEN: '|{';
CLOSE: '|}';
END_LINE: ';';
// ========================================

// ========================================
// operators
/// asignation
ASSIGN: ':=';
ASSIGN_ADD: '+:=';
ASSIGN_SUB: '-:=';
ASSIGN_MULT: '*:=';
ASSIGN_DIV: '/:=';
=========================
/// arithmetic
ADD: '+';
SUB: '-';
MULT: '*';
DIV: '/';
//todo INT_DIV: '\';
MOD: 'mod';
========================
/// bitwise
BIT_AND: '&&';
BIT_OR: '||';
BIT_XOR: '^';
BIT_LEFT_SHIFT: '<<';
BIT_RIGHT_SHIGT: '>>';
BIT_NOT: '~';
=======================
/// logic
AND: 'and';
OR: 'or';
NOT: 'not';
XOR: 'xor';
NAND: 'nand';
NOR: 'nor';
XNOR: 'xnor';
======================
/// relational
GREATER_THAN: 'gt'; // >
LESS_THAN: 'lt'; // <
EQUALS: 'eq'; // ==
NOT_EQUALS: 'df'; // !=
GREATER_EQUAL: 'ge'; // >=
LESS_EQUAL: 'le'; // <=
======================
/// strings
//todo CONCAT: '.';
=====================
// ========================================
