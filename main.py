from front import *

def main(): 
    with open ('filename.txt','r') as myfile:       
        data = myfile.read()
        if(data == None):
            print("ERROR - cannot open file.txt \n")
        else:
            getChar()
            while True:
                lex()
                if (nextToken != EOF):
                    break
        
if __name__ == "__main__":
    main()