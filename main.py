import re
import ast

# Regular expression for integers
INTEGER_REGEX = r"\b\d+\b"
# Regular expression for float
FLOAT_REGEX = r"\b\d*\.\d+\b"
# Regular expression for operator or any non alphanumeric data type
OPERATOR_REGEX = r"\W"
# Regular expression for alphabets
ID_REGEX = r"\b[a-zA-Z]\w*\b"
# Regular expression for special characters
SPECIAL_CHAR_REGEX = r"\b[!@#$%&]\b"

# Module-1
def lexical_analyzer(input_string):
    tokens = []
    search=re.finditer(f"{INTEGER_REGEX}|{FLOAT_REGEX}|{ID_REGEX}|{OPERATOR_REGEX}|{SPECIAL_CHAR_REGEX}", input_string)
    for match in search:
        if match.group(0).isdigit():
            token_type = "INTEGER"
        elif "." in match.group(0):
            token_type = "FLOAT"
        elif match.group(0).isalpha():
            token_type = "ID"
        elif "+" in match.group(0) or "-" in match.group(0) or "*" in match.group(0) or "/" in match.group(0) or "^" in match.group(0) or "=" in match.group(0):
            token_type = "Operator"
        elif " " in match.group(0):
            continue
        elif "!" in match.group(0) or "@" in match.group(0) or "#" in match.group(0) or "$" in match.group(0)or "%" in match.group(0) or "&" in match.group(0):
            token_type="Special Character"
        elif "(" in match.group(0) or ")" in match.group(0) or "{" in match.group(0) or "}" in match.group(0) or "[" in match.group(0) or"]" in match.group(0):
            token_type = "BRACKETS"
        tokens.append((token_type, match.group(0)))
    return tokens

def display(tokens):
    token1 = []
    for token in tokens:
        x = token[1]
        token1.append(x)

    print("--------Tokens--------")
    print(token1)
    print("\n--------Lexical Table--------")
    print("-" * 30)
    print("Variable".ljust(15), "Token".ljust(15))
    print("-" * 30)
    for token in tokens:
        print(token[1].ljust(15), token[0].ljust(15))

    return 0

def Syntax_tree(input_String):
    print("\n--------Syntax Tree--------\n")
    try:
        Syntax_tree1 = ast.parse(input_string)
        print(ast.dump(Syntax_tree1))
    except:
        print("Syntac Error try again")

    return 0

if __name__ == "__main__":
    input_string = input("Enter any expression: ")
    tokens = lexical_analyzer(input_string)
    display(tokens)
    Syntax_tree(input_string)
