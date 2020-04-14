grammar Lang;


//parser - lowercased

var_type : INT_TYPE | STRING_TYPE | DOUBLE_TYPE | BOOLEAN_TYPE ;
type : INT_TYPE | STRING_TYPE | DOUBLE_TYPE | BOOLEAN_TYPE | VOID ;


operator : PLUS | MINUS | DIV | MUL ;
logical_operator : AND | OR ;
relation_operator : NOT_EQUAL | EQUAL | GREATER_EQ | GREATER | LESS | LESS_EQ ;



declaration : var_type NAME ; //Napis a;
definition : declaration assign_val ;
assign_val : ASSIGN value ;
assignment : NAME assign_val ; //b = "aa" / 1 / 1.1 / true | a | a+3 / -3 / 5-6 | fun(3)

value: STRING_VAL | var_or_num_value | math_operation | fun_call ;
var_or_num_value: NAME | INT_VAL | DOUBLE_VAL ;


math_operation : LEFT_PAREN math_operation RIGHT_PAREN | math_operation operator math_operation | (MINUS)? var_or_num_value ;


fun_call : NAME LEFT_PAREN (fun_args)? RIGHT_PAREN ;
fun_args : value (COMMA value)* ; //a(2,5,"a")

fun_params : var_type NAME (COMMA var_type NAME)* ;


print : PRINT LEFT_PAREN value RIGHT_PAREN ;
return_value : RETURN LEFT_PAREN value RIGHT_PAREN ;

line : (declaration | definition | assignment | return_value | print | fun_call) SEMI ;
body : LEFT_SQUARE_BR line+ RIGHT_SQUARE_BR ;



conditions: condition (logical_operator condition)* ;
condition: var_or_num_value relation_operator var_or_num_value ;

logical_stmt : BOOLEAN_VAL | conditions ;
brack_logical_stm : LEFT_PAREN logical_stmt RIGHT_PAREN ;


if_def : IF brack_logical_stm body
	(ELSE_IF brack_logical_stm body)*
    	(ELSE body)? ;






//lexer - uppercased

CLASS : 'klasa' ;
RETURN : 'zwroc' ;
FUNCTION : 'funkcja' ;


STRING_TYPE : 'Napis' ;
INT_TYPE : 'Calkowita' ;
DOUBLE_TYPE : 'Rzeczywista' ;
BOOLEAN_TYPE : 'TypLogiczny' ;
VOID : 'TypPusty' ;

STRING_VAL : QUOT ~["]* QUOT;
INT_VAL : DIGIT+ ;
DOUBLE_VAL : INT_VAL DOT INT_VAL ;
BOOLEAN_VAL : TRUE | FALSE ;




PRINT : 'pisz' ;

DOT : '.' ;
COMMA : ',' ;
SEMI : ';' ;
COLON : ':' ;
QUOT : '"' ;

LEFT_PAREN : '(' ;
RIGHT_PAREN : ')' ;

LEFT_SQUARE_BR : '[' ;
RIGHT_SQUARE_BR : ']' ;

AND : 'oraz' ;
OR : 'lub' ;

NOT_EQUAL : '!=?=' ;
EQUAL : '=?=' ;

GREATER : '>?' ;
LESS : '<?' ;
GREATER_EQ : '>=?' ;
LESS_EQ : '<=?' ;


ASSIGN : '<=' ;

PLUS : '+' ;
MINUS : '-' ;
MUL : '*' ;
DIV : '/';


IF : 'jezeli' ;
ELSE_IF : 'inaczejJezeli' ;
ELSE : 'inaczej' ;

FOR : 'dlaKazdego' ;
IN_RANGE : 'wZakresie' ;
DOT_DOT : '..' ;

WHILE : 'dopoki' ;

TRUE : 'prawda' ;
FALSE : 'falsz' ;



NAME : [a-zA-Z0-9]+ ;


fragment DIGIT : [0-9] ;
fragment CHAR : [a-z] ;       
fragment WORD : CHAR+ ;


WS: [ \t\n\r]+ -> skip ; //whitespace
COMMENT :  '***' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '#/#' .*? '#/#' -> skip ;

