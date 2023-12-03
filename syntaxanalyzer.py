import csv
# from syntaxanalyzer import *
# from lexer import *

global numeric_data_types
numeric_data_types = ["fint", "str", "char"]

index=0
def f_start():
    global index
    # List of keywords and variable patterns
    keywords_and_patterns = ["static", "virtual", "void", "const", "class", "enum", "variable_pattern", "float", "string", "char", "bool", "int"]

    # Check if ts[index][cp] is in the list
    if ts[index][cp] in keywords_and_patterns:
        # Your code here

        if f_class():
            if f_defs():
                if ts[index][cp] == "int":
                    index+=1
                    if f_start1():
                        if ts[index][cp] == "main":
                            index+=1
                            if ts[index][cp] == "(":
                                index+=1
                                if ts[index][cp] == ")":
                                    index+=1
                                    if ts[index][cp] == "{":
                                        index+=1
                                        if f_MST():
                                            if f_ret():
                                                if ts[index][cp] == "}":
                                                    index+=1
                                                    if f_defs():
                                                        return True
    elif f_MST():
        return True
                           
    elif f_enum():
            if f_defs():
                if ts[index][cp] == "int":
                    index += 1
                    if f_start1():
                        if ts[index][cp] == "main":
                            index += 1
                            if ts[index][cp] == "(":
                                index += 1
                                if ts[index][cp] == ")":
                                    index += 1
                                    if ts[index][cp] == "{":
                                        index += 1
                                        if f_MST():
                                            if f_ret():
                                                if ts[index][cp] == "}":
                                                    index += 1
                                                    if f_defs():
                                                        return True
    elif ts[index][cp] == "static":
        index += 1
        if f_st():
            if f_defs():
                if ts[index][cp] == "int":
                    index += 1
                    if f_start1():
                        if ts[index][cp] == "main":
                            index += 1
                            if ts[index][cp] == "(":
                                index += 1
                                if ts[index][cp] == ")":
                                    index += 1
                                    if ts[index][cp] == "{":
                                        index += 1
                                        if f_MST():
                                            if f_ret():
                                                if ts[index][cp] == "}":
                                                    index += 1
                                                    if f_defs():
                                                        return True
    elif ts[index][cp] == "virtual":
        index += 1
        if f_vi():
            if f_defs():
                if ts[index][cp] == "int":
                    index += 1
                    if f_start1():
                        if ts[index][cp] == "main":
                            index += 1
                            if ts[index][cp] == "(":
                                index += 1
                                if ts[index][cp] == ")":
                                    index += 1
                                    if ts[index][cp] == "{":
                                        index += 1
                                        if f_MST():
                                            if f_ret():
                                                if ts[index][cp] == "}":
                                                    index += 1
                                                    if f_defs():
                                                        return True
    elif ts[index][cp] == "void":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if ts[index][cp] == "(":
                index += 1
                if ts[index][cp] == "argu":
                    index += 1
                    if ts[index][cp] == ")":
                        index += 1
                        if f_void_dec():
                            if f_defs():
                                if ts[index][cp] == "int":
                                    index += 1
                                    if f_start1():
                                        if ts[index][cp] == "main":
                                            index += 1
                                            if ts[index][cp] == "(":
                                                index += 1
                                                if ts[index][cp] == ")":
                                                    index += 1
                                                    if ts[index][cp] == "{":
                                                        index += 1
                                                        if f_MST():
                                                            if f_ret():
                                                                if ts[index][cp] == "}":
                                                                    index += 1
                                                                    if f_defs():
                                                                        return True
    elif ts[index][cp] == "const":
        index += 1
        if ts[index][cp] in numeric_data_types:
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_defs1():
                    if f_defs():
                        if ts[index][cp] == "int":
                            index += 1
                            if f_start1():
                                if ts[index][cp] == "main":
                                    index += 1
                                    if ts[index][cp] == "(":
                                        index += 1
                                        if ts[index][cp] == ")":
                                            index += 1
                                            if ts[index][cp] == "{":
                                                index += 1
                                                if f_MST():
                                                    if f_ret():
                                                        if ts[index][cp] == "}":
                                                            index += 1
                                                            if f_defs():
                                                                return True
    elif ts[index][cp] == "int":
        index += 1
        if f_start1():
            if ts[index][cp] == "main":
                index += 1
                if ts[index][cp] == "(":
                    index += 1
                    if ts[index][cp] == ")":
                        index += 1
                        if ts[index][cp] == "{":
                            index += 1
                            if f_MST():
                                if f_ret():
                                    if ts[index][cp] == "}":
                                        index += 1
                                        if f_defs():
                                            return True
    elif ts[index][cp_] == "variable_pattern":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_defs3():
                if f_defs():
                    if ts[index][cp] == "int":
                        index += 1
                        if f_start1():
                            if ts[index][cp] == "main":
                                index += 1
                                if ts[index][cp] == "(":
                                    index += 1
                                    if ts[index][cp] == ")":
                                        index += 1
                                        if ts[index][cp] == "{":
                                            index += 1
                                            if f_MST():
                                                if f_ret():
                                                    if ts[index][cp] == "}":
                                                        index += 1
                                                        if f_defs():
                                                            return True
    else:
        if f_DT_ot():
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_defs2():
                    if f_defs():
                        if ts[index][cp] == "int":
                            index += 1
                            if f_start1():
                                if ts[index][cp] == "main":
                                    index += 1
                                    if ts[index][cp] == "(":
                                        index += 1
                                        if ts[index][cp] == ")":
                                            index += 1
                                            if ts[index][cp] == "{":
                                                index += 1
                                                if f_MST():
                                                    if f_ret():
                                                        if ts[index][cp] == "}":
                                                            index += 1
                                                            if f_defs():
                                                                return True
    return False


def f_start1():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "main":
    # Your code here

    # Code to handle the "variable_pattern" or "main" token

        
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_defs2():
                if f_defs():
                    if f_start2():
                        return True
    return False


def f_start2():
    global index
    if ts[index][cp] == "int":
        index += 1
        if f_start1():
            return True
    return False


def f_defs():
    global index
    if ts[index][cp] == "static" or ts[index][cp] == "virtual" or ts[index][cp] == "void" or ts[index][cp] == "const" or ts[index][cp] == "class" or ts[index][cp] == "enum" or ts[index][cp_] == "variable_pattern" or ts[index][cp] == "float" or ts[index][cp] == "char" or ts[index][cp] == "string" or ts[index][cp] == "bool" or ts[index][cp] == "int" or  ts[index][cp] == "$": 
    # Your code here if the token matches one of the allowed values

        
        if f_class():
            if f_defs():
                return True
        elif f_enum():
            index += 1
            if f_defs():
                return True
        elif ts[index][cp] == "static":
            index += 1
            if f_st():
                if f_defs():
                    return True
        elif ts[index][cp] == "virtual":
            index += 1
            if f_vi():
                if f_defs():
                    return True
        elif ts[index][cp] == "void":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if ts[index][cp] == "(":
                    index += 1
                    if f_argu():
                        if ts[index][cp] == ")":
                            index += 1
                            if f_void_dec():
                                if f_defs():
                                    return True
        elif ts[index][cp] == "const":
            index += 1
            if ts[index][cp] in numeric_data_types:
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if f_defs1():
                        if f_defs():
                            return True
        elif f_DT_ot():
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_defs2():
                    if f_defs():
                        return True
        elif ts[index][cp_] == "variable_pattern":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_defs3():
                    if f_defs():
                        return True

    return False


def f_DT_ot():
    global index
    if ts[index][cp] == "float" or ts[index][cp] == "string" or ts[index][cp] == "char" or ts[index][cp] == "bool":

        if ts[index][cp] in ["float", "string", "char", "bool"]:
            index += 1
            return True
    return False

def f_MST():
    global index
    if ts[index][cp] in inc_decs or ts[index][cp] == "this" or ts[index][cp] == "const" or ts[index][cp] in DT or ts[index][cp_] == "variable_pattern" or ts[index][cp] == "while" or ts[index][cp] == "do" or ts[index][cp] == "if" or ts[index][cp] == "for" or ts[index][cp] == "enum" or ts[index][cp] == "return" or ts[index][cp] == "}" or ts[index][cp] == "break" or ts[index][cp] == "continue":
    # Do something when the condition is met for any of these values

        if f_SST():
            if f_MST():
                return True
        return False

def f_SST():
    global index
    if ts[index][cp] in inc_decs or ts[index][cp] == "this" or ts[index][cp] == "const" or ts[index][cp] in DT or ts[index][cp_] == "variable_pattern" or ts[index][cp] == "while" or ts[index][cp] == "do" or ts[index][cp] == "if" or ts[index][cp] == "for" or ts[index][cp] == "enum":

        if f_while() or f_if() or f_for() or f_do_while() or f_enum():
            return True
        elif ts[index][cp] in inc_decs:
            index += 1
            if f_t():
                
                
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if f_d1():
                        if f_I_A():
                            if f_other_inc_dec():
                                
                                return True
    elif ts[index][cp] == "this":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_d1():
                if f_I_A():
                    if f_SST_th():
                        return True
    elif ts[index][cp] == "const":
        index += 1
        if ts[index][cp] in numeric_data_types:
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_SST_Arr_Dec():
                    return True
    elif ts[index][cp] in numeric_data_types:
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_SST2():
                return True
    elif ts[index][cp_] == "variable_pattern":
        index += 1
        if f_SST3():
            return True

    return False

def f_SST2():
    global index
    if ts[index][cp] == "=" or ts[index][cp] == "[" or ts[index][cp] == "," or ts[index][cp] == ";":
    # This code block will be executed if the current token is one of '=', '[', ',', or ';'


        if ts[index][cp] == "[":
            index += 1
            if f_SIZE():
                return True
        else:
            if f_init():
                if f_List():
                    return True
    return False


def f_SST_th():
    global index
    if ts[index][cp] in inc_decs or ts[index][cp] == "=" or ts[index][cp] in PM and ts[index][cp] in MDM:
    # Your code for handling these values here


        if ts[index][cp] in inc_decs:
            index += 1
            if f_other_inc_dec():
                if ts[index][cp] == ";":
                    index += 1
                    return True
        elif f_AO():
            if f_OE():
                if ts[index][cp] == ";":
                    index += 1
                    return True
    return False


def f_SST_Arr_Dec():
    global index
    if ts[index][cp] == '=' or ts[index][cp] == '[':




        if ts[index][cp] == "=":
            index += 1
            if f_OE():
                if f_List():
                    return True


        else:
            if ts[index][cp] == "[":
                index += 1
                if f_A1():
                    if ts[index][cp] == "]":
                        index += 1
                        if f_Dim():
                            if ts[index][cp] == "=":
                                index += 1
                                if ts[index][cp] == "{":
                                    index += 1
                                    if f_OE():
                                        if f_A():
                                            if ts[index][cp] == "}":
                                                index += 1
                                                if f_A2():
                                                    return True

    # Use 'else' for the last condition check
    return False



def f_SST3():
    global index
    if ts[index][cp] == "." or ts[index][cp] == "[" or ts[index][cp_] == "variable_pattern" or ts[index][cp] == "(":

        if f_d1():            
            if f_SST4():
                return True
        else:
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_SST5():
                    return True
        return False

def f_SST4():

    global index
    if ts[index][cp] == "(":
        index += 1
        if f_param():
            if ts[index][cp] == ")":
                index += 1
                if f_SST4_alpha():
                    return True
    return False

def f_SST4_alpha():
    global index
    if ts[index][cp] == ";" or ts[index][cp] == ".":

        if ts[index][cp] == ";":
            index += 1
            return True
        else:
            if ts[index][cp] == ".":
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if f_I_A() and f_SST_th():
                        return True
        return False



def f_SST5():
    global index
    if ts[index][cp] == "[" or ts[index][cp] == "(" or ts[index][cp] in inc_decs | ts[index][cp] == "this" | ts[index][cp] == "const" | ts[index][cp] in DT | ts[index][cp_] == "variable_pattern" | ts[index][cp] == "while" | ts[index][cp] == "do" | ts[index][cp] == "if" | ts[index][cp] == "for" | ts[index][cp] == "enum" | ts[index][cp] == "return" | ts[index][cp] == "}" | ts[index][cp] == "break" | ts[index][cp] == "continue":



        if f_PC():
            if f_other_obj():
                return True
        elif ts[index][cp] == "[":
            index += 1
            if f_A1():
                if ts[index][cp] == "]":
                    index += 1
                    if f_Dim():
                        if f_A3():
                            return True
    else:
        # Handle the else condition here (if needed).
        return False

def f_defs1():
    
    # Code for handling the specific condition

    global index

    if ts[index][cp] == "=":
        index += 1
        if f_OE() and f_List():
            return True
    else:
        if ts[index][cp] == "[":
            index += 1
            if f_A1() and ts[index][cp] == "]":
                index += 1
                if f_Dim() and ts[index][cp] == "=" and ts[index+1][cp] == "{":
                    index += 2
                    if f_OE() and f_A() and ts[index][cp] == "}":
                        index += 1
                        if f_A2():
                            return True
    return False

def f_defs2():
    global index


    if ts[index][cp] == "[":
        index += 1
        if f_SIZE():
            if ts[index][cp] == "]":
                index += 1
                return True
    elif ts[index][cp] == "(":
        index += 1
        if f_argu():
            if ts[index][cp] == ")":
                index += 1
                if f_dec():
                    return True
    else:
        if f_init():
            if f_List():
                return True
    return False

def f_defs3():
    global index

    if ts[index][cp] == "(":
        index += 1
        if f_defs3_arg():
            if ts[index][cp] == ")":
                index += 1
                return True
    elif ts[index][cp] == "[":
        index += 1
        if f_A1() and ts[index][cp] == "]":
            index += 1
            if f_Dim() and f_A3():
                return True
    else:
        if f_other_obj() and ts[index][cp] == ";":
            index += 1
            return True
    return False





def f_defs3_arg():
    global index
    if ts[index][cp] == "const" or ts[index][cp] in DT or ts[index][cp_] == "variable_pattern" or ts[index][cp] == ")" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs:


        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_art():
                return True
        elif f_CT():
            if ts[index][cp] in numeric_data_types:
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if f_Arr() and f_argu1() and ts[index][cp] == ")":
                        index += 1
                        if f_dec():
                            return True
        elif ts[index][cp] == ")":
            index += 1
            if f_dec():
                return True
        elif f_const():
            if f_A() and ts[index][cp] == ")":
                index += 1
                if f_other_obj():
                    return True
        elif ts[index][cp] == "(":
            index += 1
            if f_OE() and ts[index][cp] == ")":
                index += 1
                if f_A() and ts[index][cp] == ")":
                    index += 1
                    if f_other_obj():
                        return True
        elif ts[index][cp] == "!":
            index += 1
            if f_F() and f_A() and ts[index][cp] == ")":
                index += 1
                if f_other_obj():
                    return True
        elif ts[index][cp] in inc_decs:
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_A() and ts[index][cp] == ")":
                    index += 1
                    if f_other_obj():
                        return True

    return False


def f_art():
    global index


    if ts[index][cp_] == "variable_pattern":
        index += 1
        if f_Arr() and f_argu1() and ts[index][cp] == ")":
            index += 1
            if f_dec():
                return True
    elif f_dot():
        if f_A() and ts[index][cp] == ")":
            index += 1
            if f_other_obj():
                return True
    return False

def f_dec():
    global index
    if ts[index][cp] == ";":
        index += 1
        return True
    else:
        if ts[index][cp] == "{":
            index += 1
            if f_MST():
                if f_ret():
                    if ts[index][cp] == "}":
                        index += 1
                        return True
    return False


def f_OE():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs:
    # Perform some action for the matching keywords


        if f_AE() and f_OE1():
            return True

    return False


def f_OE1():
    global index
    if ts[index][cp] == "||" or ts[index][cp] == "," or ts[index][cp] == ";" or ts[index][cp] == "}" or ts[index][cp] == ")":


        if f_AE() and f_OE1():
            return True

    return False

def f_AE():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs:



        if f_RE() and f_AE1():
            return True

    return False


def f_AE1():
    global index
    if ts[index][cp] == "&&" or ts[index][cp] == "||" or ts[index][cp] == "," or ts[index][cp] == ";" or ts[index][cp] == "}" or ts[index][cp] == ")":

        

        if ts[index][cp] == "&&":
            index += 1
            if f_RE() and f_AE1():
                return True

    return False  # This is for the case where <AE'> can be null


def f_RE():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs:
    # Perform actions when one of the specified options is found


        if f_E(): 
            if f_RE1():
                return True

    return False

def f_RE1():
    global index
    if ts[index][cp] in relational_operators or ts[index][cp] == "&&" or ts[index][cp] == "||" or ts[index][cp] == "," or ts[index][cp] == ";" or ts[index][cp] == "}" or ts[index][cp] == ")":
    
        if ts[index][cp] in relational_operators:
            index+=1
            if f_E():
                if f_RE1():
                    return True
    return False

def f_E():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs:
        if f_T():
            if f_E1():
                return True
    return False

def f_E1():
    global index
    
    if ts[index][cp] in PM or ts[index][cp] in relational_operators or ts[index][cp] == "&&" or ts[index][cp] == "||" or ts[index][cp] == "," or ts[index][cp] == ";" or ts[index][cp] == "}" or ts[index][cp] == "]":
    # Perform some action for newline values


        if ts[index][cp] in PM:
            index += 1
            if f_T():
                if f_E1():
                    return True
    return False

def f_T():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs:
        if f_F():
            if f_T1():
                return True
    return False

def f_T1():
    global index
    if ts[index][cp] in MDM or ts[index][cp] in PM or ts[index][cp] in relational_operators or ts[index][cp] == "&&" or ts[index][cp] == "||" or ts[index][cp] == "," or ts[index][cp] == ";" or ts[index][cp] == "}" or ts[index][cp] == ")":

        if ts[index][cp] in MDM:
            index += 1
            if f_F():
                if f_T1():
                    return True
    return False

def f_F():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs:

        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_dot():
                return True
        elif f_const():
            return True
        elif ts[index][cp] == "(":
            index += 1
            if f_OE():
                if ts[index][cp] == ")":
                    index += 1
                    return True
        elif ts[index][cp] == "!":
            index += 1
            if f_F():
                return True
        else:
            if ts[index][cp] in ["++", "--"]:
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    return True
    return False

def f_dot():
    global index
    if ts[index][cp] == "." or ts[index][cp] == "(" or ts[index][cp] == "[" or ts[index][cp] in inc_decs:

        if ts[index][cp] == ".":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_dot():
                    return True
        elif ts[index][cp] == "(":
            index += 1
            if f_param():
                if ts[index][cp] == ")":
                    index += 1
                    if ts[index][cp] == ".":
                        index += 1
                        if ts[index][cp_] == "variable_pattern":
                            index += 1
                            if f_dot():
                                return True
        elif ts[index][cp] == "[":
            index += 1
            if f_OE():
                if ts[index][cp] == "]":
                    index += 1
                    if f_Dim():
                        if ts[index][cp] == ".":
                            index += 1
                            if ts[index][cp_] == "variable_pattern":
                                index += 1
                                if f_dot():
                                    return True
        else:
            if ts[index][cp] in ["++", "--"]:
                index += 1
                return True

    return False


def f_Dim():
    global index
    if ts[index][cp] == "[" or ts[index][cp] == "." or ts[index][cp] == ";" or ts[index][cp] == "=":

        if ts[index][cp] == "[":
            index += 1
            if f_OE():
                if ts[index][cp] == "]":
                    index += 1
                    return True
    return False

def f_param():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs or ts[index][cp] == ")":
    
        if f_OE():
            if f_par():
                return True
    return False

def f_par():
    global index
    if ts[index][cp] == "," or  ts[index][cp] == ")":
        if ts[index][cp] == ",":
            index += 1
            if f_OE():
                if f_par():
                    return True
    return False

def f_Dec():
    global index
    if ts[index][cp] == "const" or ts[index][cp] in DT:

        
        if ts[index][cp] == "const":
            index += 1
            if ts[index][cp] in numeric_data_types:
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if ts[index][cp] == "=":
                        index += 1
                        if f_OE():
                            if f_List():
                                return True

        else:
            if ts[index][cp] in numeric_data_types:
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if f_init():
                        if f_List():
                            return True
    return False
                    
def f_init():
    global index
    if ts[index][cp] == "=" or ts[index][cp] == "," or ts[index][cp] == ";":
        

        if ts[index][cp] == "=":
            index += 1
            if f_OE():
                return True
    return False


def f_List():
    global index
    if ts[index][cp] == "," or ts[index][cp] == ";":

    

        if ts[index][cp] == ",":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_init():
                    if f_List():
                        return True
        
        else:
            if ts[index][cp] == ";":
                index += 1
                return True
    return False

def f_vi():
    global index
    if ts[index][cp] == "void" or ts[index][cp] in DT or ts[index][cp_] == "variable_pattern":

        if ts[index][cp] == "void":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if ts[index][cp] == "(":
                    index += 1
                    if f_argu():
                        if ts[index][cp] == ")":
                            index += 1
                            if f_vi1():
                                return True
        elif ts[index][cp_] == "variable_pattern":
            index += 1
            if ts[index][cp] == "(":
                index += 1
                if f_argu():
                    if ts[index][cp] == ")":
                        index += 1
                        if ts[index][cp] == "void":
                            if f_vi2():
                                return True
        else:
            if ts[index][cp] in numeric_data_types:
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if ts[index][cp] == "(":
                        index += 1
                        if f_argu():
                            if ts[index][cp] == ")":
                                index += 1
                                if f_vi2():
                                    return True
    return False

def f_argu():
    global index
    if ts[index][cp] == "const" or ts[index][cp] in DT or ts[index][cp_] == "variable_pattern" or ts[index][cp] == ")":

        if ts[index][cp] == "const":
            index += 1
            if ts[index][cp] in numeric_data_types:
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if f_Arr():
                        if f_argu1():
                            return True
        else: 
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if f_Arr():
                        if f_argu1():
                            return True
    return False

def f_vi1():
    global index, cp
    if ts[index][cp] == "=" or ts[index][cp] == ";" or ts[index][cp] == "{":
        if ts[index][cp] == "=":
            index += 1
            if ts[index][cp] == "0":
                index += 1
                if ts[index][cp] == ";":
                    index += 1
                    return True

        elif ts[index][cp] == ";":
            index += 1
            return True

        else:
            if ts[index][cp] == "{":

                index += 1
                if f_MST():
                    if ts[index][cp] == "}":
                        index += 1
                        return True

    return False

def f_vi2():
    global index, cp
    if ts[index][cp] == "=" or ts[index][cp] == ";" or ts[index][cp] == "{":
        if ts[index][cp] == "=":
            index += 1
            if ts[index][cp] == "0":
                index += 1
                if ts[index][cp] == ";":
                    index += 1
                    return True
        elif ts[index][cp] == ";":
            index += 1
            return True
        elif ts[index][cp] == "{":
            index += 1
            if f_MST():
                if f_ret():
                    if ts[index][cp] == "}":
                        index += 1
                        return True
    return False

def f_st():
    global index
    if ts[index][cp] == "void" or ts[index][cp] in DT or ts[index][cp_] == "variable_pattern":
        if ts[index][cp] == "void":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if ts[index][cp] == "(":
                    index += 1
                    if f_argu():
                        if ts[index][cp] == ")":
                            index += 1
                            if f_void_dec():
                                return True
        elif ts[index][cp] in numeric_data_types:
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if ts[index][cp] == "(":
                    index += 1
                    if f_argu():
                        if ts[index][cp] == ")":
                            index += 1
                            if f_dec():
                                return True
        else:
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if ts[index][cp] == "(":
                        index += 1
                        if f_argu():
                            if ts[index][cp] == ")":
                                index += 1
                                if f_dec():
                                    return True
    return False

def f_void_dec():
    global index, cp
    if ts[index][cp] == ";" or ts[index][cp] == "{":
    # Handle newline character

        if ts[index][cp] == ";":
            index += 1
            return True
        else:
            if ts[index][cp] == "{":
                index += 1
                if f_MST():
                    if ts[index][cp] == "}":
                        index += 1
                        return True
    return False

def f_ret():
    global index
    if ts[index][cp] == "return":
        
        if ts[index][cp] == "return":
            index += 1
            if f_OE():
                return True
    return False

def f_CT():
    global index
    if ts[index][cp] == "const" or ts[index][cp] in DT:
    # Your code for the combined condition goes here


        if ts[index][cp] == "const":
            index += 1
            return True
    return False


def f_argu1():
    global index, cp
    if ts[index][cp] == "," or ts[index][cp] == ")":

        
        if ts[index][cp] == ",":
            index += 1
            if f_argu2():
                return True
    return False

def f_argu2():
    global index, cp
    if ts[index][cp] in numeric_data_types:
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_Arr():
                if f_argu1():
                    return True
    else:
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_Arr():
                    if f_argu1():
                        return True
    return False


def f_Arr():
    global index

    if ts[index][cp] == "[":
        index += 1
        if f_A1():
            if ts[index][cp] == "]":
                index += 1
                if f_dim():
                    return True
    return False

def f_dim():
    global index

    if ts[index][cp] == "[":
        index += 1
        if f_A1():
            if ts[index][cp] == "]":
                index += 1
                return True
    return False

def f_A1():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs or ts[index][cp] == "]":
        if f_OE():
            return True
    return False

def f_jump():
    global index

    if ts[index][cp] in jump_statements:
        index += 1
        if ts[index][cp] == ";":
            index += 1
            return True
    return False

def f_while():
    global index

    if ts[index][cp] == "while":
        index += 1
        if ts[index][cp] == "(":
            index += 1
            if f_OE():
                if ts[index][cp] == ")":
                    index += 1
                    if f_Body_wh():
                        return True
    return False


def f_Body_wh():
    global index

    if ts[index][cp] == ";":
        index += 1
        return True
    elif ts[index][cp] == "{":
        index += 1
        if f_MST():
            if f_jump():
                if ts[index][cp] == "}":
                    index += 1
                    return True
    return False


def f_d1():
    global index
    if ts[index][cp] == ".":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_d1():
                return True
    elif ts[index][cp] == "[":
        index += 1
        if f_OE():
            if ts[index][cp] == "]":
                index += 1
                if f_Dim():
                    if ts[index][cp] == ".":
                        index += 1
                        if ts[index][cp_] == "variable_pattern":
                            index += 1
                            if f_d1():
                                return True
    return False




def f_con1():
    global index
    if ts[index][cp] == ";":
        index += 1
        return True
    elif ts[index][cp] == "{":
        index += 1
        if f_MST():
            if ts[index][cp] == "}":
                index += 1
                return True
    return False


def f_class():
    global index

    if ts[index][cp] == "class":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_seal():
                return True
    return False

def f_seal():
    global index

    if ts[index][cp] == "final":
        index += 1
        if ts[index][cp] == "{":
            index += 1
            if f_Body():
                if ts[index][cp] == "}":
                    index += 1
                    return True
    elif f_Access_Modifier():
        
        if ts[index][cp] == ":":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_class1():
                    if ts[index][cp] == "{":
                        index += 1
                        if f_Body():
                            if ts[index][cp] == "}":
                                index += 1
                                return True
    else:
        if ts[index][cp] == "{":
            index += 1
            if f_Body():
                if ts[index][cp] == "}":
                    index += 1
                    return True
    return False


def f_class1():
    global index

    if ts[index][cp] == ",":
        index += 1
        if f_Access_Modifier():
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_class1():
                    return True
    return False


def f_Body():
    global index, cp
    if f_Access_Modifier() or ts[index][cp] == "static" or ts[index][cp] == "virtual" or ts[index][cp] == "void" or ts[index][cp] == "const" or ts[index][cp] in DT or ts[index][cp_] == "variable_pattern" or ts[index][cp] == "class" or ts[index][cp] == "enum" or ts[index][cp] == "~" or ts[index][cp] == "}":

        if f_class():
            if f_Body():
                return True
        elif f_enum():
            if f_Body():
                return True
        elif ts[index][cp] == "static":
            index += 1
            if f_st():
                if f_Body():
                    return True
        elif ts[index][cp] == "virtual":
            index += 1
            if f_vi():
                if f_Body():
                    return True
        elif ts[index][cp] == "void":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if ts[index][cp] == "(":
                    index += 1
                    if f_argu():
                        if ts[index][cp] == ")":
                            index += 1
                            if f_void_dec():
                                if f_Body():
                                    return True
        elif ts[index][cp] == "const":
            index += 1
            if ts[index][cp] in numeric_data_types:
                index += 1
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if f_defs1():
                        if f_Body():
                            return True
        elif ts[index][cp] in numeric_data_types:
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                
                if ts[index][cp_] == "punctuators":
                    index+=1
                    if f_defs2():
                        if f_Body():
                            return True
        elif ts[index][cp_] == "variable_pattern":
            index += 1
            if f_Bd():
                if f_Body():
                    return True
        elif ts[index][cp] == "~":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if ts[index][cp] == "(":
                    index += 1
                    if ts[index][cp] == ")":
                        index += 1
                        if f_con1():
                            if f_Body():
                                return True
        else:
            if f_Access_Modifier():
                if ts[index][cp] == ":":
                    index += 1
                    if f_Body():
                        return True
    return False

def f_Bd():
    global index
    
    if ts[index][cp_] == "variable_pattern":
        index += 1
        if f_defs3():
            return True
    else:
        if ts[index][cp] == "(":
            index += 1
            if f_argu():
                if ts[index][cp] == ")":
                    index += 1
                    if f_con1():
                        return True
    return False

def f_PC():
    global index
    if ts[index][cp] == "(":
        index += 1
        if f_OE():
            if f_A():
                if ts[index][cp] == ")":
                    index += 1
                    return True
    return False


def f_other_obj():
    global index

    if ts[index][cp] == ";" or ts[index][cp] == ",":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_PC():
                if f_other_obj():
                    return True
    return False


def f_enum():
    global index

    if ts[index][cp] == "enum":
        index += 1
        if ts[index+1][cp_] == "variable_pattern":
            index += 1
            if ts[index][cp] == "{":
                index += 1
                if f_values():
                    if ts[index][cp] == "}":
                        index += 1
                        if ts[index][cp] == ";":
                            index += 1
                            return True
    return False


def f_values():
    global index
    
    if ts[index][cp_] == "variable_pattern":
        index += 1
        if f_val():
            return True
    return False

def f_val():
    global index

    if ts[index][cp] == ",":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_val():
                return True
    else:
        if ts[index][cp] == "=":
            index += 1
            if f_const():
                if f_val1():
                    return True
    return False

def f_val1():
    global index
    
    if ts[index][cp] == ",":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_val():
                return True
    return False

def f_t():
    global index
    if ts[index][cp] == "this" and ts[index + 1][cp] == ".":
        index += 2  # Advance the index by 2 to consume both "this" and "."
        return True
    return False

def f_inc_dec():

    global index, cp
    if ts[index][cp] == "this" or ts[index][cp_] == "variable_pattern" or ts[index][cp] in inc_decs:


        if f_t():
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_d1():
                    if f_I_A():
                        if ts[index][cp] in ["++", "--"]:
                            index += 1
                            if f_other_inc_dec():
                                index += 1
                                return True

        if ts[index][cp] in ["++", "--"]:
            index += 1
            if f_t():
                if ts[index][cp_] == "variable_pattern":
                    index += 1
                    if f_I_A():
                        if f_other_inc_dec():
                            index += 1
                            return True

    return False

def f_I_A():
    global index, cp
    if ts[index][cp] == "(":
        index += 1
        if f_param():
            if ts[index][cp] == ")":
                index += 1
                if ts[index][cp] == ".":
                    index += 1
                    if ts[index][cp_] == "variable_pattern":
                        index += 1
                        if f_I_A():
                            return True
    return False



def f_other_inc_dec():
    global index
    if ts[index][cp] == ",":
        index += 1
        if f_inc_dec():
            return True
    return False

def f_for():
    global index
    if ts[index][cp] == "for":
        index += 1
        if ts[index][cp] == "(":
            index += 1
            if f_F1():
                if f_F2():
                    if ts[index][cp] == ";":
                        index += 1
                        if f_F3():
                            if ts[index][cp] == ")":
                                index += 1
                                if f_for1():
                                    return True
    return False

def f_F1():
    global index
    if ts[index][cp] == "const" or ts[index][cp] in DT or ts[index][cp] == "this" or ts[index][cp_] == "variable_pattern":

        if f_Dec() or f_assignment():
            return True
    return False

def f_F2():
    global index
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs or ts[index][cp] == ";":
    # Your code for handling these conditions goes here

        if f_OE():
            return True
    return False

def f_F3():
    global index, cp
    if ts[index][cp] == "this":
        index += 1
        if ts[index][cp] == ".":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_d1():
                    if f_I_A():
                        if f_SST_th():
                            return True
    elif ts[index][cp_] == "variable_pattern":
        index += 1
        if f_d1():
            if f_I_A():
                if f_SST_th():
                    return True
    elif ts[index][cp] in ["++", "--"]:
        index += 1
        if f_t():
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_I_A():
                    if f_other_inc_dec():
                        return True
    return False


def f_for1():
    global index, cp
    if ts[index][cp] == ";":
        index += 1
        return True
    elif ts[index][cp] == "{":
        index += 1
        if f_MST() and f_jump():
            if ts[index][cp] == "}":
                index += 1
                return True
    return False

def f_do_while():
    global index, cp
    if ts[index][cp] == "do":
        index += 1
        if ts[index][cp] == "{":
            index += 1
            if f_MST():
                if f_jump():
                    if ts[index][cp] == "}":
                        index += 1
                        if ts[index][cp] == "while":
                            index += 1
                            if ts[index][cp] == "(":
                                index += 1
                                if f_OE():
                                    if ts[index][cp] == ")":
                                        index += 1
                                        if ts[index][cp] == ";":
                                            index += 1
                                            return True
    return False

def f_if():
    global index, cp
    if ts[index][cp] == "if":
        index += 1
        if ts[index][cp] == "(":
            index += 1
            if f_OE():
                if ts[index][cp] == ")":
                    index += 1
                    if f_if1():
                        if ts[index][cp] == "else":
                            index += 1
                            return True
    return False

def f_if1():
    global index, cp
    if ts[index][cp] == ";":
        index += 1
        return True
    else:
        if ts[index][cp] == "{":
            index += 1
            if f_MST():
                if f_jump():
                    if ts[index][cp] == "}":
                        index += 1
                        return True
    return False


def f_else():
    global index
    if ts[index][cp] == "else":
        index += 1
        if f_if1():
            return True
    return False

def f_A():
    global index
    if ts[index][cp] == ",":
        index += 1
        if f_OE():
            if f_A():
                return True
    return False

def f_SIZE():
    global index, cp
    if ts[index][cp_] == "variable_pattern" or ts[index][cp] == "int_const" or ts[index][cp] == "float_const" or ts[index][cp] == "string_const" or ts[index][cp] == "char_const" or ts[index][cp] == "bool_const" or ts[index][cp] == "(" or ts[index][cp] == "!" or ts[index][cp] in inc_decs or ts[index][cp] == "]":
        if f_OE():
            if ts[index][cp] == "]":
                index += 1
                if f_Dim():
                    if f_A7():
                        return True
        else:
            if ts[index][cp] == "]":
                index += 1
                if f_Dim():
                    if ts[index][cp] == "=":
                        index += 1
                        if ts[index][cp] == "{":
                            index += 1
                            if f_OE():
                                if f_A():
                                    if ts[index][cp] == "}":
                                        index += 1
                                        if f_A8():
                                            return True
    return False    

def f_A2():
    global index, cp
    if ts[index][cp] == ";":
        index += 1
        return True
    elif ts[index][cp] == ",":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if ts[index][cp] == "[":
                index += 1
                if f_A1():
                    if ts[index][cp] == "]":
                        index += 1
                        if ts[index][cp] == "=":
                            index += 1
                            if ts[index][cp] == "{":
                                index += 1
                                if f_OE():
                                    if f_A():
                                        if ts[index][cp] == "}":
                                            index += 1
                                            if f_A2():
                                                return True
    return False


def f_A3():
    global index, cp
    if ts[index][cp] == ";":
        index += 1
        return True
    elif ts[index][cp] == "=":
        index += 1
        if ts[index][cp] == "{":
            index += 1
            if f_A4():
                if ts[index][cp] == "}":
                    index += 1
                    return True
    return False


def f_A4():
    global index, cp
    if ts[index][cp_] == "variable_pattern":
        index += 1
        if f_A5() and f_A6():
            return True
    return False

def f_A5():
    global index, cp
    if ts[index][cp] == "(":
        index += 1
        if f_param():
            if ts[index][cp] == ")":
                index += 1
                return True
    else:
        if ts[index][cp] == "[":
            index += 1
            if f_OE():
                if ts[index][cp] == "]":
                    index += 1
                    return True
    return False

def f_A6():
    global index
    if ts[index][cp] == ",":
        index += 1
        if ts[index][cp_] == "variable_pattern":
            index += 1
            if f_A5():
                return True
    return False



def f_A7():
    global index
    if ts[index][cp] == ";":
        index += 1
        return True
    elif ts[index][cp] == "=":
        index += 1
        if ts[index][cp] == "{":
            index += 1
            if f_OE() and f_A() and ts[index][cp] == "}":
                index += 1
                if f_A2():
                    return True
    return False


def f_A8():
    global index
    if ts[index][cp] == ";":
        index += 1
        return True
    else:
        if ts[index][cp] == ",":
            index += 1
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if ts[index][cp] == "[":
                    index += 1
                    if f_SIZE():
                        return True
                    
def f_assignment():
    global index
    if ts[index][cp] == "this" or ts[index][cp_] == "variable_pattern":

        if f_t():
            if ts[index][cp_] == "variable_pattern":
                index += 1
                if f_d1():
                    if f_I_A():
                        if f_AO():
                            if f_OE():
                                if ts[index][cp] == ";":
                                    index += 1
                                    return True
    return False


def f_AO():
    global index, cp
    if ts[index][cp] == "=":
        index += 1
        return True
    elif ts[index][cp] in PM:
        index += 1
        if ts[index][cp] in MDM:
            index += 1
            return True

    
    return False

def f_const():
    global index
    if ts[index][cp_] in constants:
        index+=1
        return True
    return False

def f_Access_Modifier():
    global index
    if ts[index][cp] in access_modifiers:
        index+=1
        return True
    return False

cp_=0
cp=1
# from cfsgparsers import *
# Specify the CSV file path
csv_file_path = "tokens.csv"

# Create an empty list to store the data from the CSV file
ts = []

# Open and read the CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row if it exists
    next(csv_reader, None)  # This skips the first row (header) if it's present

    # Read each row of data from the CSV file
    for row in csv_reader:
        ts.append(row)

# print(ts)





if f_start():
    # print(ts[index][2])
    if ts[index][cp] == eof:
        print("No syntaxError")


else:
    print("SyntaxError at line:",ts[index][2])


