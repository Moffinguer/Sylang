grammar Test;


main: BEGIN
        instruction+
      END
      EOF;


instruction: assign;
assign: variable_type variableId ASSIGN expression END_OF_INSTRUCTION;
variableId: ID;
value_type: variable_type
            |
            VOID;

expression: digit;
variable_type: INTEGER | DOUBLE | BOOLEAN;
digit: NUMBER;


/*
 * Lexer Rules
 */

// Skipeable elements
WS
:
 [ \t\r\n]+ -> skip
;
COMMENTS: '#' -> skip;


// Operators
PLUS: 'add';
MINUS: 'sub';
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

// Symbols
ASSIGN: ':=';
OPEN_BLOCK: '{';
CLOSE_BLOCK: '}';
OPEN_ARGUMENTS: '(';
CLOSE_ARGUMENTS: ')';
END_OF_INSTRUCTION: ';';

// Keywords
VOID: 'void';
BEGIN: 'BEGIN';
END: 'END';
DEF_FUNC: 'function';
ST_OUTPUT: 'print';
IF: 'if';
RETURN: 'returns';
BREAK: 'stop';
CONTINUE: 'next';
WHILE: 'while';
THEN: 'then';

INTEGER: 'int'; // All natural and negative numbers
BOOLEAN: 'boolean';
DOUBLE: 'real'; // All floating point numbers

// Complex Expressions
ID: [a-zA-Z][0-9a-zA-Z]*;

NUMBER: DECIMAL_NUMBER | FLOATING_NUMBER | HEX_NUMBER | OCTAL_NUMBER;
fragment DECIMAL_NUMBER: [0-9]+;
fragment FLOATING_NUMBER: DECIMAL_NUMBER'.'DECIMAL_NUMBER
                 |
                 '.'DECIMAL_NUMBER
                 ;
fragment HEX_NUMBER: [0][xX][0-9a-fA-F]+;
fragment OCTAL_NUMBER: [0]DECIMAL_NUMBER;

BOOLEAN_VALUES: TRUE | FALSE;
TRUE: 'T' | 'TRUE';
FALSE: 'F' | 'FALSE';