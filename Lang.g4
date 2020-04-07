grammar Lang;


//parser - lowercased











//lexer - uppercased

CLASS : 'klasa' ;
RETURN : 'zwroc' ;
FUNCTION : 'funkcja' ;


PRINT : 'pisz' ;

DOT : '.' ;
COMMA : ',' ;
SEMI : ';' ;
COLON : ':' ;
QUOTE : '"' ;

LEFT_PAREN : '(' ;
RIGHT_PAREN : ')' ;

LEFT_SQUARE_BR : '[' ;
RIGHT_SQUARE_BR : ']' ;

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

WHILE : 'dopoki' ;


WS: [ \t\n\r]+ -> skip ; //whitespace
COMMENT :  '***' ~[\r\n]* -> skip;
BLOCK_COMMENT : '#/#' .*? '#/#' -> skip;