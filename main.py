import re
import sys

from Token import Token
def tokenize(code):
    keywords = {
        'agar', 'magar', 'then', 'for', 'return',
        'class', 'Do', 'struct', 'array', 'extends', 'dict', 'secret', 'sensitive', 'public','while'
    }
    data_types = ["fint", "str", "char"]

    token_specification = [
        ('PUNCTUATORS', r'[:,]'),
        # ('SCOPE_STARTING', r"{"),
        # ('SCOPE_ENDING', r"}"),
        ('CHAR', r"'(\\'|\\\"|\\\\|\\t|\\n|.)'"),
        ('FINT', r'\d+\.\d+|\d+\.\d*|\d*\.\d+|\d+'),  # Integer or decimal number
        ('TRIPLE_QUOTE_STRING_CONST', r"'''([^']|'{1,2}[^'])*'''"),
        ('UNARY_OPS', r'\+\+|--'),
        ('ASSIGN', r':='),  # Assignment operator
        ('COMPOUND_COMP_OPS', r'!=|==|<=|>=|\|\||&&'),
        ('COMP_OPS', r'[=><|&]'),
        ('OP_SCOPE',r'[{]'),
        ('CL_SCOPE',r'[}]'),
        ('OP_BRACE',r'[(]'),
        ('CL_BRACE', r'[)]'),
        ('COMP_OPS_N_ASSIGN', r'[!<>]=|==|&&|\|\||\+=|-=|\*=|/='),  # Compound assignment
        ('END', r';'),  # Statement terminator
        ('ID', r'[A-Za-z]+'),  # Identifiers
        ('OP', r'[+\-*/%]'),  # Arithmetic operators
        ('NEWLINE', r'\n'),  # Line endings
        ('SKIP', r'[ \t]+'),  # Skip over spaces and tabs
        ('DOT', r'\.'),  # Dot
        ('DOUBLE_QUOTE_STRING_CONST', r'"([^"]*)"'),  # Double-quoted string
        ('MISMATCH', r'.'),  # Any other character
    ]
    comment_pattern = r'/\*.*?\*/|#.*?(?=\n|$)'

    code = re.sub(comment_pattern, '', code, flags=re.DOTALL)

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'ID':
            if value in keywords:
                kind = value
            elif value in data_types:
                kind = 'DATA_TYPE'
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            kind = 'Invalid Lexem'
        yield Token(kind, value, line_num, column)


def syntax_analyzer(tokens):

    token_index = 0

    def match(*expected_class_part):
        nonlocal token_index
        try:
            if tokens[token_index].class_part in expected_class_part or tokens[token_index].value in expected_class_part:
                print("----------> {token} with {class_part}".format(token=tokens[token_index].value, class_part=tokens[token_index].class_part))
                token_index += 1
                return True
            else:
                # print("Error at {line}".format(line=tokens[token_index].line))
                return False
        except:
            print("Syntax errror")
            sys.exit()

    def Start():
        if len(tokens) <= token_index:
            return True
        if SST():
           if Start():
              return True
        return True

    def SST():
        if initialize():
            return True
        elif func_call():
            return True

    def func_call():
        if match("ID"):
            if match("OP_BRACE"):
                if args():
                    pass

    def args():
        if f_OE():
            if match(","):
                if args():
                    return True
            else:
                return True
        return False

#<<<<<<<<<<<<<<<<<<Expression>>>>>>>>>>>>>>>>>>>>>>>>>

    def f_OE():
        if match("ID","FINT", "DOUBLE_QUOTE_STRING_CONST", "CHAR", "BOOL", "(", "!", "UNARY_OPS"):
            if f_AE() and f_OE1():
                return True

        return False

    def f_OE1():
        if match("COMPOUND_COMP_OPS", ",", "END", "}", ")"):
            if f_AE() and f_OE1():
                return True

        return False

    def f_AE():
        if match("ID", "FINT", "DOUBLE_QUOTE_STRING_CONST", "BOOL", "CHAR", "(", "!", "UNARY_OPS"):
            if f_RE() and f_AE1():
                return True

        return False

    def f_AE1():
        if match("COMP_OPS_N_ASSIGN", ",","END", "}",")"):
            if match("&&"):
                if f_RE() and f_AE1():
                    return True

        return False  # This is for the case where <AE'> can be null

    def f_RE():
        if match("ID", "FINT", "DOUBLE_QUOTE_STRING_CONST", "BOOL", "CHAR", "(", "!", "UNARY_OPS"):
            if f_E():
                if f_RE1():
                    return True

        return False

    def f_RE1():
        if match("COMP_OPS_N_ASSIGN", "COMPOUND_COMP_OPS", ",", ";", "}", ")"):
            if match("COMP_OPS_N_ASSIGN", "COMPOUND_COMP_OPS"):
                if f_E():
                    if f_RE1():
                        return True
        return False

    def f_E():
        if match("ID", "FINT", "DOUBLE_QUOTE_STRING_CONST", "BOOL", "CHAR", "(", "!", "UNARY_OPS"):
            if f_T():
                if f_E1():
                    return True
        return False

    def f_E1():
        if match("+", "-", "COMP_OPS_N_ASSIGN", "COMPOUND_COMP_OPS", ",", ";", "}", "]"):
            if match("+", "-"):
                if f_T():
                    if f_E1():
                        return True
        return False

    def f_T():
        if match("ID", "FINT", "DOUBLE_QUOTE_STRING_CONST", "BOOL", "CHAR", "(", "!", "UNARY_OPS"):
            if f_F():
                if f_T1():
                    return True
        return False

    def f_T1():
        if match("OP", "COMP_OPS_N_ASSIGN", "COMPOUND_COMP_OPS", ",", ";", "}", ")"):
            if match("OP"):
                if f_F():
                    if f_T1():
                        return True
        return False

    def f_F():
        if match("ID", "FINT", "DOUBLE_QUOTE_STRING_CONST", "BOOL", "CHAR", "(", "!", "UNARY_OPS"):
            if match("ID"):
                if f_dot():
                    return True
            elif match("DOUBLE_QUOTE_STRING_CONST", "FINT", "CHAR", "BOOL"):
                return True
            elif match("("):
                if f_OE():
                    if match(")"):
                        return True
            elif match("!"):
                if f_F():
                    return True
            else:
                if match("UNARY_OPS"):
                    if match("ID"):
                        return True
        return False

    def f_dot():
        if match(".", "DOT", "(", "[", "UNARY_OPS"):
            if match("."):
                if match("ID"):
                    if f_dot():
                        return True
            elif match("("):
                if f_param():
                    if match(")"):
                        if match("."):
                            if match("ID"):
                                if f_dot():
                                    return True
            elif match("["):
                if f_OE():
                    if match("]"):
                        if f_Dim():
                            if match("."):
                                if match("ID"):
                                    if f_dot():
                                        return True
            else:
                if match("UNARY_OPS"):
                    return True

        return False

    def f_Dim():
        if match("[", ".", ";", "="):
            if match("["):
                if f_OE():
                    if match("]"):
                        return True
        return False

    def f_param():
        if match("ID", "FINT", "DOUBLE_QUOTE_STRING_CONST", "BOOL", "CHAR", "(", "!", "UNARY_OPS", ")"):
            if f_OE():
                if f_par():
                    return True
        return False

    def f_par():
        if match(",", ")"):
            if match(","):
                if f_OE():
                    if f_par():
                        return True
        return False


#<<<<<<<<<<<<<<<<<<Expression>>>>>>>>>>>>>>>>>>>>>>>>>


    def initialize():
        nonlocal token_index
        if match("DATA_TYPE"):
            if match("ID"):
                if list1() and list2():
                    return True
        else:
            print("Syntax Error at line {line} on phrase {value}".format(line=tokens[token_index].line, value=tokens[token_index].value))
            return False

    def list1():
        if match('COMP_OPS'):
            if match('DOUBLE_QUOTE_STRING_CONST', 'FINT', 'CHAR'):
                return True
            elif match('ID'):
                list1()
            else:
                return False
        return True

    def list2():
        if match('END'):
            return True
        elif match('PUNCTUATORS') and match('ID'):
            if list1() and list2():
                return True
        return True

    if Start():
        print("parsed")
        return True


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< OLD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # token_index = 0
    #
    # def interface():
    #     pass
    #
    # def classDef():
    #     pass
    #
    # def funcDec():
    #     pass
    #
    # def match(class_part, value=None):
    #     nonlocal token_index
    #     if token_index < len(tokens):
    #         if tokens[token_index].class_part == class_part and (value is None or tokens[token_index].value == value):
    #             token_index += 1
    #         else:
    #             print(f"Error: Expected {class_part}, but found {tokens[token_index].class_part} at line {tokens[token_index].line}")
    #             return False
    #     else:
    #         print(f"Error: Unexpected end of input")
    #         return False
    #     return True
    #
    # def progStart():
    #     nonlocal token_index
    #     for token in range(len(tokens) - 1 ):
    #     # while token_index < len(tokens):
    #         if Initialization():
    #             pass
    #
    #         ObjectReference()
    #         # SST()
    #         # classDef()
    #         # funcDec()
    #         # interface()
    #
    # def Initialization():
    #     Datatype()
    #     if match("ID"):
    #         List1()
    #         List2()
    #
    # def List1():
    #     if match("="):
    #         Const()
    #     elif match("ID"):
    #         List1()
    #
    # def List2():
    #     if match(";"):
    #         pass
    #     elif match(","):
    #         if match("ID"):
    #             List1()
    #             List2()
    #
    # def Datatype():
    #     nonlocal token_index
    #     if match("DATA_TYPE"):
    #         pass
    #     # if tokens[token_index].class_part in ["str", "fint", "char", "bool"]:
    #     else:
    #         print(f"Error: Expected Datatype, but found {tokens[token_index].class_part} at line {tokens[token_index].line}")
    #
    #
    #
    # def ObjectReference():
    #     if match("ID"):
    #         while match("."):
    #             if not match("ID"):
    #                 return False
    #     return True
    #
    # def MethodCall():
    #     nonlocal token_index
    #     if ObjectReference():
    #         if match("."):
    #             if match("ID") and match("(") and ArgumentList() and match(")"):
    #                 return True
    #     elif match("ID") and match("(") and ArgumentList() and match(")"):
    #         return True
    #     return False
    #
    # def SST():
    #     nonlocal token_index
    #     if tokens[token_index].class_part == "ID":
    #         if MethodCall():
    #             return True
    #         elif tokens[token_index].class_part == "agar":
    #             AgarMagar()
    #         # elif tokens[token_index].class_part == "while":
    #         #     WhileLoop()
    #         # elif tokens[token_index].class_part == "for":
    #         #     ForLoop()
    #         # elif tokens[token_index].class_part == "print":
    #         #     Print()
    #         # elif tokens[token_index].class_part == "struct":
    #         #     Struct()
    #         # elif tokens[token_index].class_part == "array":
    #         #     Array()
    #         # elif tokens[token_index].class_part == "dict":
    #         #     Dict()
    #         elif tokens[token_index].class_part in ("fint", "str", "char", "bool"):
    #             Initialization()
    #     elif tokens[token_index].class_part == "extends":
    #         InheritanceDeclaration()
    #     else:
    #         print(f"Error: Unexpected token {tokens[token_index].class_part} at line {tokens[token_index].line}")
    #         return False
    #
    #     # Ensure there's a semicolon at the end of the statement
    #     if not match(";"):
    #         return False
    #
    #     return True
    #
    # def AgarMagar():
    #     nonlocal token_index
    #     if match("agar"):
    #         if match("("):
    #             if condition():  # Check the condition inside the "agar" block
    #                 if match(")"):
    #                     if match("{"):
    #                         MST()  # Parse statements inside the "agar" block
    #                         if match("}"):
    #                             if magar():
    #                                 return True
    #     return False
    #
    # def ArgumentList():
    #     if expression():
    #         while match(","):
    #             if not expression():
    #                 return False
    #     return True
    #
    # def condition():
    #     return expression() and comparison() and expression()
    #
    # def comparison():
    #     return match("==") or match("!=") or match("<") or match(">") or match("<=") or match(">=")
    #
    # def expression():
    #     return logical_expression() and statement_prime()
    #
    # def statement_prime():
    #     while match("COMP_OPS_N_ASSIGN"):
    #         if not logical_expression():
    #             return False
    #     return True
    #
    # def logical_expression():
    #     return relational_expression() and logical_expression_prime()
    #
    # def logical_expression_prime():
    #     while match("COMP_OPS_N_ASSIGN"):
    #         if not relational_expression():
    #             return False
    #     return True
    #
    # def relational_expression():
    #     return sub_expression() and relational_expression_prime()
    #
    # def relational_expression_prime():
    #     while rop():
    #         if not sub_expression():
    #             return False
    #     return True
    #
    # def sub_expression():
    #     return term() and expression_prime()
    #
    # def expression_prime():
    #     while match("OP"):
    #         if not term():
    #             return False
    #     return True
    #
    # def term():
    #     return factor() and term_prime()
    #
    # def term_prime():
    #     while match("OP"):
    #         if not factor():
    #             return False
    #     return True
    #
    # def factor():
    #     return match("ID") or Const() or ObjectReference() or ArgumentList()
    #
    # def rop():
    #     return match("<") or match(">") or match("<=") or match(">=") or match("==") or match("!=")
    #
    # def magar():
    #     nonlocal token_index
    #     if match("magar"):
    #         if match("{"):
    #             MST()  # Parse statements inside the "magar" block
    #             if match("}"):
    #                 return True
    #     return True
    #
    # def MST():
    #     nonlocal token_index
    #     while token_index < len(tokens):
    #         if not SST():
    #             return False
    #     return True
    #
    # def InheritanceDeclaration():
    #     if match("EXTENDS"):
    #         if parentClass():
    #             return True
    #         else:
    #             return False  # Parsing error
    #     return True  # <inheritance> can be Null
    #
    # def parentClass():
    #     if match("ID"):
    #         if match("PUNCTUATORS"):
    #             return parentClass()  # Recursive call to handle multiple parent classes
    #         return True
    #     return False  # Parsing error, expected <className> or Null
    #
    # # def SST():
    # #     nonlocal token_index
    # #     if tokens[token_index].class_part in ["FunctionCall", "agar-magar", "whileloop", "forloop", "print", "struct", "array", "dict", "Initialization", "InheritanceDeclaration", "MultipleInheritance"]:
    # #         token_index += 1
    # #     else:
    # #         print(f"Error: Unexpected token {tokens[token_index].class_part} at line {tokens[token_index].line}")
    #
    # # def MST():
    # #     nonlocal token_index
    # #     while token_index < len(tokens):
    # #         SST()
    # #         MST()
    #
    # def Const():
    #     nonlocal token_index
    #     if tokens[token_index].class_part in ["const-str", "const-char", "const-fint", "const-bool"]:
    #         token_index += 1
    #     else:
    #         print(f"Error: Expected Const, but found {tokens[token_index].class_part} at line {tokens[token_index].line}")
    #
    #
    #
    # progStart()
    # return token_index == len(tokens)