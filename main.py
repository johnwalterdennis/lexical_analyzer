from front import initialize_lexer, lex, nextToken, EOF_TOKEN, is_done

def main():
    if initialize_lexer('filename.txt'):
        print("Starting lexical analysis...")

        while not is_done():
            lex()
        print("Lexical analysis complete.")

if __name__ == "__main__":
    main()
    

    