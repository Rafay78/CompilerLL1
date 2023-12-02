from main import tokenize, syntax_analyzer
from Token import Token
import os

bash_command = f"echo >> "

file = open("SampleCode", 'r')
code = file.read()
tokens = []
for token in tokenize(code):
    tokens.append(token)
# tokens.append(Token(class_part="EOF",column=None,line=None,value="$"))
for token in tokens:
    print(token)

if syntax_analyzer(tokens):
    print("Syntax is correct.")
else:
    print("Syntax contains errors.")


