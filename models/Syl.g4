grammar Syl;


/*
 * Parser Rules
 */
 
prog: functions*
      main
      functions*
      EOF;

functions: DEF_FUNC value_type ID OPEN_BLOCK
           instruction+
           (RETURN expression END_OF_INSTRUCTION)?
           CLOSE_BLOCK;
instruction: var_declaration | var_assign;
var_declaration: variable_type ID END_OF_INSTRUCTION
                |
                 variable_type var_assign; // requires modification in the future
main: BEGIN
       instruction+
      END;
var_assign: ID ASSIGN expression END_OF_INSTRUCTION;

// Groups
value_type: variable_type
            |
            VOID;
variable_type: INTEGER |
            DOUBLE |
            STRING |
            BOOLEAN;
number: DECIMAL_NUMBER | FLOATING_NUMBER | HEX_NUMBER;
boolean_variable: TRUE | FALSE;

//
expression: OPEN_ARGUMENTS+ expression CLOSE_ARGUMENTS+
            |
            ID
            |
            number
            |
            boolean_variable |
            expression PLUS expression |
            expression MINUS expression | MINUS expression |
            expression MULTIPLY expression |
               expression DIVIDE expression |
                expression MODULE expression |
                 expression AND expression |
                 expression OR expression |
                  NOT expression |
                   expression EQUALS expression |
                    expression NOT_EQUALS expression |
                     expression GREATER_THAN expression |
                      expression LESS_THAN expression |
                       expression LESS_EQUAL expression |
                     expression GREATER_EQUAL expression;



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
INTEGER: 'int'; // All natural and negative numbers
BEGIN: 'BEGIN';
END: 'END';
DEF_FUNC: 'function';
ST_OUTPUT: 'print';
STRING: 'string';
BOOLEAN: 'boolean';
DOUBLE: 'real'; // All floating point numbers
IF: 'if';
RETURN: 'returns';
BREAK: 'stop';
CONTINUE: 'next';
WHILE: 'while';
THEN: 'then';

// Complex Expressions
ID: [a-zA-Z][0-9a-zA-Z]*;
DECIMAL_NUMBER: [0-9]+;
FLOATING_NUMBER: DECIMAL_NUMBER'.'DECIMAL_NUMBER
                 |
                 '.'DECIMAL_NUMBER
                 ;
HEX_NUMBER: [0][xX][0-9a-fA-F]+;
OCTAL_NUMBER: [0]DECIMAL_NUMBER;
TRUE: 'T' | 'TRUE';
FALSE: 'F' | 'FALSE';