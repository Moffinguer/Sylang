grammar Syl;


main: 
      functions*
      BEGIN
        (instruction|standard_output|functionCall END_OF_INSTRUCTION)*
      END
      EOF;

functions: DEF_FUNC VOID functionId OPEN_ARGUMENTS (variable_type variableId )? CLOSE_ARGUMENTS OPEN_BLOCK
           (instruction|standard_output|functionCall END_OF_INSTRUCTION)+
           CLOSE_BLOCK |
            DEF_FUNC VOID functionId OPEN_ARGUMENTS variable_type variableId ( SEPARATOR variable_type variableId)* CLOSE_ARGUMENTS OPEN_BLOCK
           (instruction|standard_output|functionCall END_OF_INSTRUCTION)+
           CLOSE_BLOCK |
           DEF_FUNC variable_type functionId OPEN_ARGUMENTS (variable_type variableId)? CLOSE_ARGUMENTS OPEN_BLOCK
           (instruction|standard_output|functionCall END_OF_INSTRUCTION)*
           RETURN expression END_OF_INSTRUCTION
           CLOSE_BLOCK |
           DEF_FUNC variable_type functionId OPEN_ARGUMENTS variable_type variableId ( SEPARATOR variable_type variableId)* CLOSE_ARGUMENTS OPEN_BLOCK
           (instruction|standard_output|functionCall END_OF_INSTRUCTION)
           RETURN expression END_OF_INSTRUCTION
           CLOSE_BLOCK
           ;


instruction: assign | if_block | while_block;
assign: variable_type variableId ASSIGN expression END_OF_INSTRUCTION | 
        variableId ASSIGN expression END_OF_INSTRUCTION;
variableId: ID;
functionId: ID;
functionCall: functionId OPEN_ARGUMENTS CLOSE_ARGUMENTS | 
              functionId OPEN_ARGUMENTS expression ( SEPARATOR expression)* CLOSE_ARGUMENTS;
value_type: variable_type;
function_type: INTEGER | BOOLEAN | DOUBLE;

if_block: IF expression THEN
          (instruction|standard_output|functionCall END_OF_INSTRUCTION)+
          END_FI |
          IF expression THEN
          (instruction|standard_output|functionCall END_OF_INSTRUCTION)+
          ELSE
          (instruction|standard_output|functionCall END_OF_INSTRUCTION)+
          END_FI;
while_block: WHILE expression THEN
            (instruction|standard_output|functionCall)+
            END_WHILE_FOR;

standard_output: //ST_OUTPUT OPEN_ARGUMENTS expression CLOSE_ARGUMENTS END_OF_INSTRUCTION|
            ST_OUTPUT OPEN_ARGUMENTS STRING CLOSE_ARGUMENTS END_OF_INSTRUCTION;

expression: digit |
            variableId |
            boolean_values |
            functionCall |
            OPEN_ARGUMENTS expression CLOSE_ARGUMENTS |
            expression GREATER_EQUAL expression |
            expression GREATER_THAN expression |
            expression LESS_EQUAL expression |
            expression LESS_THAN expression |
            expression EQUALS expression |
            expression NOT_EQUALS expression | 
            expression PLUS expression |
            expression MINUS expression | 
            expression MULTIPLY expression |
            expression DIVIDE expression |
            expression MODULE expression |
            expression AND expression |
            expression OR expression |
            NOT expression | MINUS expression;
                     

variable_type: INTEGER | DOUBLE | BOOLEAN;
digit: NUMBER;
boolean_values: BOOLEAN_VALUES;


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
SEPARATOR: ',';

// Keywords
VOID: 'void';
BEGIN: 'BEGIN';
END: 'END';
DEF_FUNC: 'function';
ST_OUTPUT: 'print';
IF: 'if';
RETURN: 'returns';
WHILE: 'while';
THEN: 'then';
ELSE: 'else';
END_FI: 'fi';
END_WHILE_FOR: 'end';


INTEGER: 'int'; // All natural and negative numbers
BOOLEAN: 'boolean';
DOUBLE: 'real'; // All floating point numbers

STRING: '"' ( '\\n' | '\\t' | '\\v' | '\\a' | '\\b' | '\\f' | '\\r' | '\\\\' | '\\"' | '\\?' | ~["\\] )* '"';
BOOLEAN_VALUES: TRUE | FALSE;
TRUE: 'T' | 'TRUE';
FALSE: 'F' | 'FALSE';

// Complex Expressions
ID: [a-zA-Z][0-9a-zA-Z]*;

NUMBER: DECIMAL_NUMBER | FLOATING_NUMBER | HEX_NUMBER | OCTAL_NUMBER;
DECIMAL_NUMBER: [0-9]+;
FLOATING_NUMBER: DECIMAL_NUMBER'.'DECIMAL_NUMBER
                 |
                 '.'DECIMAL_NUMBER
                 ;
HEX_NUMBER: [0][xX][0-9a-fA-F]+;
OCTAL_NUMBER: [0]DECIMAL_NUMBER;