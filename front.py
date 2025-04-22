#character classes
LETTER  = 0
DIGIT = 1
UNKNOWN = 99 
EOF_CLASS = -1

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

EOF_TOKEN = -1


# Global
charClass  = 0
lexeme = []   
nextChar = " "
lexLen = 0 
token = 0
nextToken = 0 
input_text = ""
position = 0
done = False




def addChar():
    global lexeme, lexLen, nextChar
    if lexLen <= 98:
        lexeme.append(nextChar)
        lexLen += 1
    else:
        print("Error - lexeme is too long\n")
    
def getChar():
    global nextChar, charClass, position, input_text, done
    if position < len(input_text):
        nextChar = input_text[position]
        position += 1
        
        if nextChar.isalpha():
            charClass = LETTER
        elif nextChar.isdigit():
            charClass = DIGIT
        else:
            charClass = UNKNOWN
    else:
        nextChar = " "
        charClass = EOF_CLASS
        done = True

def getNonBlank():
    global nextChar
    while(nextChar.isspace() and charClass !=  EOF_CLASS):
        getChar()

def lex():
    global lexLen, nextToken, lexeme, charClass, nextChar

    if done:
        nextToken = EOF_TOKEN
        print(f"Next token is {nextToken}, Next lexeme is EOF")
        return nextToken
    lexLen = 0
    lexeme = []  # Reset lexeme
    
    getNonBlank()
    
    if charClass == LETTER:
        addChar()
        getChar()
        while charClass == LETTER or charClass == DIGIT:
            addChar()
            getChar()
        nextToken = IDENT
    
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    
    elif charClass == EOF_CLASS:
        nextToken = EOF_TOKEN
        lexeme = ["E", "O", "F"]
    
    print(f"Next token is {nextToken}, Next lexeme is {''.join(lexeme)}")
    return nextToken

def lookup(ch):
    global nextToken
    
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    elif ch == '=':
        addChar()
        nextToken = ASSIGN_OP
    else:
        addChar()
        nextToken = EOF_TOKEN
    return nextToken                

def initialize_lexer(file_path):
    global input_text, position, done
    try:
        with open(file_path, 'r') as file:
            input_text = file.read()
            position = 0
            done = False
        getChar()  # Initialize the first character
        return True
    except Exception as e:
        print(f"Error opening file: {e}")
        return False
    
def is_done():
    global done
    return done