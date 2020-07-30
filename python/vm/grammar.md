# 关键字：



| int    | bool     | True     | False   | void    | **while** |
| ------ | :------- | :------- | ------- | ------- | --------- |
| **if** | **elif** | **else** | **+**   | **-**   | *****     |
| **/**  | **%**    | **=**    | **==**  | **!=**  | **>**     |
| **<**  | **>=**   | **<=**   | **&**   | **\|**  | **!**     |
| **^**  | **;**    | **0-9**  | **a-w** | **A-W** | **_**     |
| **,**  | **{**    | **}**    | **(**   | **)**   |           |
|        |          |          |         |         |           |





标识符：以字母或下划线开头，其它可以是字母、数字、下划线。

数字：个位数字 0-9；多位数必须以1-9开头，其它可以是0-9

https://github.com/antlr/grammars-v4/blob/master/c/C.g4

LeftParen : '(';
RightParen : ')';
LeftBrace : '{';
RightBrace : '}';
While : 'while';
Void : 'void';
Int : 'int';
Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';
Plus : '+';
Minus : '-';
Star : '*';
Div : '/';
Mod : '%';
And : '&';
Or : '|';
Caret : '^';
Not : '!';
Assign : '=';
Equal : '==';
NotEqual : '!=';
Identifier:   Nondigit  ( Nondigit|   Digit )*
Nondigit:   [a-zA-Z_];



Constant :  NonzeroDigit  Digit * ;
NonzeroDigit :  '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;
Digit : '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;
















