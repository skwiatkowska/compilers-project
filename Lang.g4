//parser - lowercased











//lexer - uppercased

CLASS : 'klasa' ;
RETURN : 'zwroc' ;
FUNCTION : 'funkcja' ;


DOT : '.' ;
COMMA : ',' ;
SEMI : ';' ;
COLON : ':' ;


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

IF : 'jezeli' ;
ELSEIF : 'inaczejJezeli' ;
ELSE : 'inaczej' ;

WHILE : 'dopoki' ;


WS: [ \t\n\r]+ -> skip ; //whitespace