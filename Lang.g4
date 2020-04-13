grammar Lang;


//parser - lowercased

var_type : INT_TYPE | STRING_TYPE | DOUBLE_TYPE | BOOLEAN_TYPE;
type : INT_TYPE | STRING_TYPE | DOUBLE_TYPE | BOOLEAN_TYPE | VOID ;

math_operator : PLUS | MINUS | DIV | MUL ;
logical_operator : AND | OR ;
relation_operator : NOT_EQUAL | EQUAL | GREATER_EQ | GREATER | LESS | LESS_EQ ;



declaration : var_type VAR_NAME SEMI ; //Napis a;







//lexer - uppercased

CLASS : 'klasa' ;
RETURN : 'zwroc' ;
FUNCTION : 'funkcja' ;


STRING_TYPE : 'Napis' ;
INT_TYPE : 'Calkowita' ;
DOUBLE_TYPE : 'Rzeczywista' ;
BOOLEAN_TYPE : 'TypLogiczny' ;
VOID : 'TypPusty' ;

STRING : QUOT WORD QUOT ;
INT : DIGIT+ ;
DOUBLE: INT DOT INT ;
BOOLEAN : TRUE | FALSE ;



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
DOT_DOR : '..' ;

WHILE : 'dopoki' ;

TRUE : 'prawda' ;
FALSE : 'falsz' ;


VAR_NAME : CHAR (CHAR | DIGIT)* ;


fragment DIGIT : [0-9] ;
fragment CHAR : [a-z] ;       
fragment WORD : CHAR+ ;


WS: [ \t\n\r]+ -> skip ; //whitespace
COMMENT :  '***' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '#/#' .*? '#/#' -> skip ;

