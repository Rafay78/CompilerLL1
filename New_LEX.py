import re

class Token :
    def __init__(self,Token_Class , Token_Value,Line_No):
            self.Token_Class = Token_Class
            self.Token_Value = Token_Value 
            self.Line_No = Line_No
            pass




identifier_re = "^[A-Za-z]+[A-Za-z0-9]*[A-Za-z0-9]*$"
string_re = "^\"[A-Za-z0-9 .+=\",#\\\:\']+\"$"
integ_re = "[+,-]?[0-9]+$|[0-9]+$"
fpoint_re = "[+,-]?[0-9]+(.)[0-9]+$|[0-9]+(.)[0-9]*$|[0-9]+(.)[0-9]+$"
prev = ""
multi_line = 0
line_number = 1
inside_string = False
compound_checker = False
multiline_checker= False
comment_check = False
special_check =False
float_check=False
multi_comment_check = False
temp_checker =  False
signed = False
Token_List=[]
temp = ""
skip = 0

def Lexical_Analyzer():
    global special_check
    global compound_checker
    global multi_comment_check
    global multi_line
    global multiline_checker
    global comment_check
    global inside_string
    global temp
    global float_check
    global line_number
    global temp_checker
    global signed
    global skip




    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False


    def check_conditions():
            global line_number
            global multi_line
            global temp
            if temp in keywords:
                token_class = keywords[temp]
                # print(f"[{token_class},{temp},Line {line_number}]")
                output_file.write(f"[{token_class},{temp},Line {line_number}]\n")
                new_token = Token(token_class,temp,line_number)
                Token_List.append(new_token)

            elif re.match(identifier_re, temp):
                # print(f"[Line {line_number}, ID, {temp}]")
                # print(f"[Line {line_number}, {token_class}, {temp}]")
                output_file.write(f"[ID,{temp},Line {line_number}]\n")
                new_token = Token("ID",temp,line_number)
                Token_List.append(new_token)

            elif re.match(integ_re, temp):
                # print(f"[Line {line_number}, .integ, {temp}]")
                # print(f"[Line {line_number}, {token_class}, {temp}]")
                output_file.write(f"[int_const, {temp},Line {line_number}]\n")
                new_token = Token("int_const",temp,line_number)
                Token_List.append(new_token)
            
            elif re.match(fpoint_re, temp):

                # print(f"[Line {line_number}, .fpoint, {temp}]")
                # print(f"[Line {line_number}, {token_class}, {temp}]")
                output_file.write(f"[fpoint_const, {temp},Line {line_number}]\n")
                new_token = Token("fpoint_const",temp,line_number)
                Token_List.append(new_token)
            
            

            

            elif temp in operators:
                token_class = operators[temp]
                # print(f"[{token_class},{temp},Line {line_number}]")
                output_file.write(f"[{token_class},{temp},Line {line_number}]\n")
                new_token = Token(token_class,temp,line_number)
                Token_List.append(new_token)
            elif temp in punctuators:
                token_class = punctuators[temp]
                # print(f"[{token_class},{temp},Line {line_number}]")
                output_file.write(f"[{token_class},{temp},Line {line_number}]\n")
                new_token = Token(token_class,temp,line_number)
                Token_List.append(new_token)
            elif re.match(string_re,temp):

                # print(f"[str_lit, {temp},Line {line_number}]")
                temp = temp[1:-1]
                output_file.write(f"[str_const, {temp},Line {line_number}]\n")
                new_token = Token("str_const",temp,line_number)
                Token_List.append(new_token)
                line_number+=multi_line
                multi_line=0
            else:
                # print(f"[Invalid, {temp},Line {line_number}]")
                output_file.write(f"[Invalid, {temp},Line {line_number}]\n")
                # Token_List.append(f"[Invalid, {temp},Line {line_number}]\n")
                new_token = Token("Invalid",temp,line_number)
                Token_List.append(new_token)
            temp = ""



    with open("input.txt", "r") as f:
        input_str = f.read() + "\0"

    output_file = open("output.txt","w")

    special_chars = ['n', 'r','t']
    break_chars = [" ", '\n']

    keywords = {
        "construct":"construct",
        "integ": "dtype",
        "fpoint": "dtype",
        "str": "dtype",
        "public": "acc_mod",
        "private": "acc_mod",
        "class": "class",
        "inherits":"inherits",
        "make":"make",
        "remove":"remove",
        "this->":"this->",
        "super.":"super.",
        "virtual":"virtual",
        "override":"override",
        "static":"static",
        "return":"return",
        "provide":"provide",
        "except provide":"except provide",
        "except":"except",
        "struct":"struct",
        "break" : "flow_control",
        "continue":"flow_control",
        "while":"while",
        "for":"for",
        "abstract":"abstract",
        "sealed":"sealed",
        "def":"def",
        "friend":"friend",
        "operator":"operator",
        "construct":"construct",
        "inherit":"inherit",
        "new":"new"
    }

    operators = {
        "*": "MDM",
        "%": "MDM",
        "/": "MDM",
        "+": "PM",
        "-": "PM",
        "<":"ROP",
        "<=":"ROP",
        ">":"ROP",
        ">=":"ROP",
        "==":"ROP",
        "!=":"ROP",
        "=":"AOP",
        "+=":"CMP_OP",
        "-=":"CMP_OP",
        "*=":"CMP_OP",
        "++":"inc_dec",
        "--":"inc_dec",
        "&&":"LOP",
        "||":"LOP",
        "!":"!"
    }

    punctuators = {
        "(": "(",
        ")": ")",
        ";": ";",
        ",": ",",
        ":":":",
        "[":"[",
        "]":"]",
        "{":"{",
        "}":"}",
        ".":"."
    }




    for index,char in enumerate(input_str):
        

        if temp_checker ==True:
            temp_checker = False
            continue



        if char == "." and float_check == True and not inside_string:
            float_check=not float_check
            check_conditions()



        if signed == True and  not inside_string:
            signed = not signed
            continue

        if special_check == True:
            special_check = not special_check
            prev =""
            continue

        if compound_checker==True:
            compound_checker= not compound_checker
            continue
        
        if multiline_checker==True:
            multiline_checker= not multiline_checker
            if char == '\n' and inside_string:
                temp+='\\n'
                multi_line+=1
                multiline_checker = not multiline_checker
                continue
        
        if char == "." and input_str[index + 1 ].isdigit() and not inside_string and float_check ==False:
            prev = temp+char+input_str[index+1]
            
            if isfloat(prev):
                float_check = not float_check
                temp+="."
                prev=""
                continue
            else:
                check_conditions()
                temp+=char
                continue
        if char =="." and temp.isdigit():
            temp+=char
            check_conditions()
            continue

        if char == "#" and input_str[index+1]=='*' and not inside_string and multi_comment_check == False:
            multi_comment_check = not multi_comment_check
            continue    


        if char == "#" and not inside_string and comment_check == False:
            comment_check = not comment_check
            continue

        if multi_comment_check == True:
            if char=="\n":
                line_number+=1
                continue
            if char == "*" and input_str[index+1]=="#":
                multi_comment_check=not multi_comment_check
                continue
            else:
                continue

        if comment_check == True:
            if char =="\n":
                line_number+=1
                comment_check=not comment_check
                continue
            else:
                continue
        
        
        if char == "." and temp == "super" and not inside_string:
            temp=temp+char
            check_conditions()
            continue

        if char  ==  "-" and temp == "this" and input_str[index+1]==">" and not inside_string:
            temp = temp + char + input_str[index + 1]
            check_conditions()
            temp_checker = True
            skip = 1
            continue
        

        if char == '\n' and inside_string:
            temp+='\\n'
            multi_line+=1
            multiline_checker = not multiline_checker
            continue
        
        
        
        if char == '\\' and inside_string:
            if char == '\\' and prev == '\\':
                temp+='\\'
                prev = ""
                continue
            else:    
                prev=char
                continue

        if char =='"' and prev == "\\" and inside_string:
            temp+='"'
            prev=""
            continue

        if char == '"' or inside_string: #Checking If character is '"' or we are already in string
            if inside_string:#if inside string just join the previous chars
                
                temp+=prev+char
                prev=""
            else: #if char == '"' old temp updated with new temp 
                temp=temp
        
            

        # if char == "+" or char  == "-"  and input_str[index+1].isdigit() and not inside_string :

            
            

        


        
    
        elif char not in break_chars and char not in punctuators and char not in operators and char != "\\":
            temp+=char
                
        if char in break_chars and not inside_string:
                if temp:
                    check_conditions()
                
                else:
                    temp = ""

        if char in punctuators and not inside_string:
            if temp:
                check_conditions()
                temp=char
                check_conditions()

            else:
                temp=char
                check_conditions()

        if char in operators and not inside_string:
            if temp:
                
                check_conditions()
                prev=char + input_str[index +1]
                if prev in operators:
                    temp = prev
                    check_conditions()
                    prev = ""
                    compound_checker=not compound_checker
                else:
                    prev=""
                    temp = char
                    check_conditions()




            else:
                prev=char + input_str[index +1]
                if prev in operators:
                    temp = prev
                    check_conditions()
                    prev = ""
                    compound_checker=not compound_checker
                else:
                    prev=""
                    temp=char
                    check_conditions()
                    
        
        

        if char == '\n' and not inside_string:
            line_number += 1
            float_check=False

        if char == "\\" and input_str[index+1] in special_chars and not inside_string:
            if input_str[index+1] == 'n':
                special_check = True
                if temp:
                    check_conditions()
                line_number+=1
                prev=temp
            if input_str[index +1]=='t':
                special_check = True
                temp+=" "
                prev=temp
        
        if char == "\\" and input_str[index+1] not in special_chars and not inside_string:
            temp +=char
        
        
        elif char == '"':
            if inside_string == False:
                if temp:
                    check_conditions()       
                temp=temp + char
                inside_string = not inside_string
            else:
                if temp:
                    check_conditions()
                inside_string = not inside_string
                
        if char == "\0" and temp =="\0":
                return Token_List
        if char =="\0" and temp != "\0":
            temp = temp[0:-1]
            check_conditions()
            return Token_List

List=Lexical_Analyzer()
new_obj = Token("$","$",line_number)

# List.append(new_obj)
# for i in List:
#     print(List)
# List.append(["$","$",line_number])
# print(List[0].Token_Value)