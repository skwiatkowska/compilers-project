grammar Lang;


//parser - lowercased

type : INT | STRING | DOUBLE | BOOLEAN | VOID ;
operator : PLUS | MINUS | DIV | MUL ;

logic_operator : AND | OR ;
relation_operator: NOT_EQUAL | EQUAL | GREATER_EQ | GREATER | LESS | LESS_EQ ;








//lexer - uppercased

CLASS : 'klasa' ;
RETURN : 'zwroc' ;
FUNCTION : 'funkcja' ;


STRING : 'Napis' ;
INT : 'Calkowita' ;
DOUBLE : 'Rzeczywista' ;
BOOLEAN : 'TypLogiczny' ;
VOID : 'TypPusty' ;


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

WHILE : 'dopoki' ;


WS: [ \t\n\r]+ -> skip ; //whitespace
COMMENT :  '***' ~[\r\n]* -> skip;
BLOCK_COMMENT : '#/#' .*? '#/#' -> skip;