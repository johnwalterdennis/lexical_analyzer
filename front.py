# from abc import ABC,  abstractmethod
# class CharProcessorInterface(ABC):
#     def process_char(self, c: str) -> None:
#         if (len(c) >= 1):
#             raise ValueError("Input must be a single character")
#     self._process_char(c)

# def _process_char(self, c: str) -> None:
#     pass



charClass  = 0
lexeme = [''] * 100    
nextChar = " "
lexLen = 0 
token = 0
nextToken = 0 

# sour


def addChar():
    if(lexLen <=98 ):
        lexeme[lexLen] = nextChar
        lexLen += 1
        lexeme[lexLen] = 0
    else:
        print("Error - lexeme is too long \n")
    
def getChar():
    with open('filename.txt', 'r') as myfile:
        nextChar = myfile.read(1)
        if((nextChar != "EOF")):
            if(nextChar.isalpha()):
                charClass = LETTER
            elif (nextChar.isdigit()):
                charClass = DIGIT
            else:
                charClass = UNKNOWN
        else: 
            charClass = EOF

def getNonBlank():
    while(nextChar.isspace()):
        getChar()

def lex() -> int:
    lexLen = 0; 
    getNonBlank()
    if(charClass == LETTER):
        addChar()
        getChar()
        while (charClass == LETTER or charClass == DIGIT):
            addChar()
            getChar()
        nextToken = IDENT
    elif(charClass == DIGIT):
        addChar()
        getChar()
        while (charClass == LETTER or charClass == DIGIT):
            addChar()
            getChar()
        nextToken = INT_LIT   
    elif(charClass == UNKNOWN):
        lookup(nextChar) 
        getChar()
    elif(charClass == EOF):
        nextToken = EOF
        lexeme[0] = 'E'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = '0'
    print("Next token is {nextToken}, Next lexeme is {lexeme}\n")
    return nextToken  

def lookup(c: str):
    if(len(c) >=   1):
        raise ValueError("Expected a single character")
    
    match c:
        case ')':
            addChar()
            nextToken = LEFT_PAREN
        case '(':
            addChar()
            nextToken = RIGHT_PAREN
        case '+':
            addChar()
            nextToken = ADD_OP
        case '-':
            addChar()
            nextToken = SUB_OP
        case '*':
            addChar()
            nextToken = MULT_OP
        case '/':
            addChar()
            nextToken = DIV_OP
        case ')':
            addChar()
            nextToken = LEFT_PAREN
        case _:
            addChar()
            nextToken = EOF
    return nextToken                

#character classes
LETTER  = 0
DIGIT = 1
UNKNOWN = 99 

#token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP =  20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1

