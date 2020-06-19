# compilers-project


Custom lang parser with ANTLR4 library

# Project basics:

We are constructing a language which uses polish keywords.

## Basic keywords:

 'klasa' -  class
 
 'zwroc'  - return 
 
 'funkcja'  - function
 
 'start'  - main function 
 
 'pisz' - print
 
 

## Types:

 'Napis' - string 
 
 'Calkowita' - integer 
 
 'Rzeczywista' - double 
 
 'TypLogiczny' - boolean
 


## Operators:


 'oraz' - and 
 
 'lub'  - or
 
 '!=?=' - not equal
 
 '=?='  - equal
 
 '>?'  - greater
 
 '<?'  - less
 
 '>=?'  - greater or equal
 
 '<=?'  - less or equal
 
 '<='  - assign value 
 


## Program control:

 'jezeli'  - if
 
 'inaczejJezeli'  - else if
 
 'inaczej'  - else
 
 'dlaKazdego'  - for
 
 'wZakresie'  - in range
 
 'dopoki'  - while
 
 'prawda'  - true
 
 'falsz'  - false
 

 '***' - comment
 
 '#/#' ...'#/#'  - multi-line comment
 
 
 '[' ... ']' - block of code
 
 
 ## Podział obowiązków podczas tworzenia projektu

Stworzenie gramatyki, wygenerowanie lexera, parsera i drzewa parsowania - Sylwia Kwiatkowska

Stworzenie listenera, za pomocą którego język jest tłumaczony na Pythona - Adrianna Kopeć, Anna Nagi

Napisanie dokumentacji - Adrianna Kopeć, Anna Nagi





