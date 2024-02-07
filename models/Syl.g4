grammar Syl;


// SORTING AND CLEARING FILE, SPLIT INTO OTHER FILES

// Sintax analysis 
prog: functions*
      main
      functions*
      EOF;

functions: DEF_FUNC value_type ID OPEN_BLOCK
           instruction+
           RETURN expression
           CLOSE_BLOCK;
instruction: var_declaration | var_assign;
var_declaration: value_type ID END_OF_INSTRUCTION 
                |
                 value_type var_assign; // requires modification in the future
main: BEGIN
       instruction+
      END;
var_assign: ID ASSIGN expression END_OF_INSTRUCTION;
// Sintax analysis 

// Agrupaciones
value_type: INTEGER |
            DOUBLE |
            STRING |
            BOOLEAN
            |
            VOID;
//


// Skipeable elements

//saltar esto
WS
:
 [ \t\r\n]+ -> skip
;
// Skipeable elements

// Palabras clave
VOID: 'void';
INTEGER: 'int'; // All natural and negative numbers
BEGIN: 'BEGIN';
END: 'END';
DEF_FUNC: 'function';
ST_OUTPUT: 'print';
STRING: 'string';
BOOLEAN: 'boolean';
DOUBLE: 'real'; // All floating point numbers
TRUE: 'T';
FALSE: 'F';
IF: 'if';
RETURN: 'returns';
BREAK: 'stop';
CONTINUE: 'next';
WHILE: 'while';
THEN: 'then';
PLUS: 'add';
MINUS: 'sub';
NEGATIVE: 'neg';
MULTIPLY: 'mul';
DIVIDE: 'div';
MODULE: 'mod';
EQUALS: 'eq';
NOT_EQUALS: 'ne';
GREATER_THAN: 'gt';
LESS_THAN: 'lt';
GREATER_EQUAL: 'ge';
LESS_EQUAL: 'le';
AND: 'and';
OR: 'or';
NOT: 'not';
XOR: 'xor';
ASSIGN: ':=';
OPEN_BLOCK: '{';
CLOSE_BLOCK: '}';
OPEN_ARGUMENTS: '(';
CLOSE_ARGUMENTS: ')';
END_OF_INSTRUCTION: ';'; // End of instruction line

// Palabras clave

// Expresiones completas
ID: [a-zA-Z][0-9a-zA-Z]*;
DECIMAL_NUMBER: [0-9]+;
FLOATING_NUMBER: [0-9]+'.'[0-9]+
                 |
                 '.'[0-9]+
                 ;