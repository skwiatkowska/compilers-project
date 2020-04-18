grammar Lang;


//parser - lowercased

var_type : INT_TYPE | STRING_TYPE | DOUBLE_TYPE | BOOLEAN_TYPE ;


operator : PLUS | MINUS | DIV | MUL ;
logical_operator : AND | OR ;
relation_operator : NOT_EQUAL | EQUAL | GREATER_EQ | GREATER | LESS | LESS_EQ ;



declaration : var_type NAME ; //Napis a;
definition : declaration assign_val ;
assign_val : ASSIGN value ;
assignment : NAME assign_val ; 


value: STRING_VAL | var_or_num_value | math_operation | fun_call ;
var_or_num_value: NAME | INT_VAL | DOUBLE_VAL ;

math_operation : LEFT_PAREN math_operation RIGHT_PAREN 
	| math_operation operator math_operation 
	| (MINUS)? var_or_num_value ;



fun_call : NAME LEFT_PAREN (fun_args)? RIGHT_PAREN ;
fun_args : value (COMMA value)* ; // fun(2,5,"a")
fun_params : var_type NAME (COMMA var_type NAME)* ; // fun(Napis a, Calkowita b, Calkowita c)

fun_declaration : FUNCTION NAME LEFT_PAREN (fun_params)? RIGHT_PAREN (RETURN var_type)? ;

fun_def : fun_declaration body ;


class_def : CLASS NAME LEFT_SQUARE_BR code* main? RIGHT_SQUARE_BR ;


print : PRINT LEFT_PAREN value RIGHT_PAREN ;
return_value : RETURN LEFT_PAREN value RIGHT_PAREN ;

line : if_def | for_def | while_def | line_semi ;
line_semi : (declaration | definition | assignment | return_value | print | fun_call | increment | decrement ) SEMI ;
body : LEFT_SQUARE_BR line+ RIGHT_SQUARE_BR ;
code : ((declaration | definition | fun_declaration) SEMI) | fun_def ;
main : MAIN body ;



conditions: condition (logical_operator condition)* ;
condition: var_or_num_value relation_operator var_or_num_value ;

logical_stmt : BOOLEAN_VAL | conditions ;
brack_logical_stm : LEFT_PAREN logical_stmt RIGHT_PAREN ;


if_def : IF brack_logical_stm body
	(ELSE_IF brack_logical_stm body)*
    	(ELSE body)? ;


for_def : FOR LEFT_PAREN NAME IN_RANGE INT_VAL DOT_DOT INT_VAL RIGHT_PAREN body ; 

while_def : WHILE brack_logical_stm body ;


increment : NAME PLUS PLUS ;
decrement : NAME MINUS MINUS ;




//lexer - uppercased

CLASS : 'klasa' ;
RETURN : 'zwroc' ;
FUNCTION : 'funkcja' ;
MAIN : 'start' ;
PRINT : 'pisz' ;


STRING_TYPE : 'Napis' ;
INT_TYPE : 'Calkowita' ;
DOUBLE_TYPE : 'Rzeczywista' ;
BOOLEAN_TYPE : 'TypLogiczny' ;

STRING_VAL : QUOT ~["]* QUOT;
INT_VAL : DIGIT+ ;
DOUBLE_VAL : INT_VAL DOT INT_VAL ;
BOOLEAN_VAL : TRUE | FALSE ;



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

