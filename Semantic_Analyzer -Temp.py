from tabulate import tabulate
ScopeTable=[]
DefTable=[]
FriendTable=[]
Stack=[0]
currentScope=0
body_type=""
return_type = ""
AccessModefier = "public"
def_type=""
func_type=""
arr_dt=""



CCN=""
CCR=[]
scope = 0


class ScopeTableInstance:
    def __init__(self,Name,Type,Scope):
        self.Name = Name
        self.Type = Type
        self.Scope = Scope

class DefTableInstance:
    def __init__(self,Name,Type,Acc_Mod,Parent,Type_Mod):
        self.Name = Name
        self.Type = Type
        self.Acc_Mod = Acc_Mod
        self.Parent = Parent
        self.Type_Mod = Type_Mod
        self.MemTable = []


        

class MemTableInstance:
    def __init__(self,Name,Type,Acc_Mod,Type_Mod,Const,Class_Name):
        self.Name = Name
        self.Type = Type
        self.Acc_Mod = Acc_Mod
        self.Type_Mod = Type_Mod
        self.Const = Const
        self.Class_Name = Class_Name

class FriendInstance:
    def __init__(self,Name,Operator):
        self.Name = Name
        self.Operator = Operator



def main():
    print(CCN)
    print()
    print()
    print("Scope Table")
    Scope_table_data = []
    for i in range (len(ScopeTable)):
        Scope_table_data.append([ScopeTable[i].Name, ScopeTable[i].Type, ScopeTable[i].Scope])

    # Specify the table format
    table_format = "grid"

    # Generate the table using tabulate
    table = tabulate(Scope_table_data, headers=["Name", "Type", "Scope"], tablefmt=table_format)

    # Print the table
    print(table)

    print()
    print()
    print("Defination Table")
    Def_table_data = []
    for i in range (len(DefTable)):
        Def_table_data.append([DefTable[i].Name, DefTable[i].Type, DefTable[i].Acc_Mod,DefTable[i].Parent,DefTable[i].Type_Mod])

    # Specify the table format
    table_format = "grid"

    # Generate the table using tabulate
    table = tabulate(Def_table_data, headers=["Name", "Type", "Access Modifier","Type Modifier","Class_Name"], tablefmt=table_format)

    # Print the table
    print(table)

    print()
    print()
    print("Member Table")
    for i in range (len(DefTable)):
        Mem_table_data = []
        print()
        print()
        print(f"Member Table of {DefTable[i].Type} {DefTable[i].Name}")
    
        for j in range (len(DefTable[i].MemTable)):
            Mem_table_data.append([DefTable[i].MemTable[j].Name, DefTable[i].MemTable[j].Type, DefTable[i].MemTable[j].Acc_Mod,DefTable[i].MemTable[j].Type_Mod,DefTable[i].MemTable[j].Class_Name])

        # Specify the table format
        table_format = "grid"

        # Generate the table using tabulate
        table = tabulate(Mem_table_data, headers=["Name", "Type", "Access Modifier","Parent","Type Modifier"], tablefmt=table_format)

        # Print the table
        print(table)
        
    

    print("--------------------------------------------------------------------------")
    print()
    print(f"{FriendTable[0].Name}|{FriendTable[0].Operator}")
def lookUpScopeTable(Name):
    for i in range(len(ScopeTable)):
        if ScopeTable[i].Name == Name :
            if "->" in ScopeTable[i].Type:
                continue
            if "[]" in ScopeTable[i].Type:
                stripped = ScopeTable[i].Type.strip('[]')
                return stripped
            if ScopeTable[i].Scope == currentScope:
                return ScopeTable[i].Type
    return True
            
def lookUpDefTable(Name,Type):
    global CCN
    for i in range(len(DefTable)):
        if (DefTable[i].Name == Name):
            # if (DefTable[i].Type==Type):
                return DefTable[i]
    if (len(DefTable)==0):
        return False
    else:
        # print(f"Can't Find The Structure {Name}")
        return False

def lookUpMemTable(Name,Class_Name):
    global CCN,CCR
    global def_type
    CCN =Class_Name
    CCR = lookUpDefTable(CCN,def_type)
    if (CCR):
        for j in range(len(CCR.MemTable)):
            if (CCR.MemTable[j].Name == Name):
                if (CCR.MemTable[j].Acc_Mod == 'private'):
                    return 'private'
                else:
                    return CCR.MemTable[j].Type
            

        return True
            
            


def lookUpFuncST(Name,Plist):
    print(Name,Plist,'ION')
    if '->' in Plist:
        dt,rtype =Plist.split('->')
        print(dt)

        for j in range(len(Stack)):
            check_scope = Stack[j]
            for i in range(len(ScopeTable)):
                if (ScopeTable[i].Name == Name):
                    edt,ertype=ScopeTable[i].Type.split('->') 
                    if edt == dt:
                        if ScopeTable[i].Scope == check_scope:
                            print(check_scope)
                            print(ertype,"JOBOKKO")
                            return ertype
        
        return True
    else:
        for j in range(len(Stack)):
            check_scope = Stack[j]
            for i in range(len(ScopeTable)):
                if (ScopeTable[i].Name == Name):
                    edt,ertype=ScopeTable[i].Type.split('->') 
                    if edt == Plist:
                        if ScopeTable[i].Scope == check_scope:
                            print(check_scope)
                            print(ertype,"JOBOKKO")
                            return ertype
        
        return True




def lookUpFuncMT(Name,Plist,Class_Name):
    global func_type
    print(Name,Plist,Class_Name,"INSIDE  MT")
    global CCN,CCR
    CCN =Class_Name
    CCR = lookUpDefTable(CCN,"class")
    if '->' in Plist:
        if (CCR):
            for j in range(len(CCR.MemTable)):
                if (CCR.MemTable[j].Name == Name): 
                    if(CCR.MemTable[j].Type== Plist):
                        func_type=CCR.MemTable[j].Type_Mod
                        if (CCR.MemTable[j].Acc_Mod== 'private'):
                            return 'private'
                        else:
                            return CCR.MemTable[j]
            
            return True
    else:
        if (CCR) :
            for j in range(len(CCR.MemTable)):
                if (CCR.MemTable[j].Name == Name):
                    edt,ertype=CCR.MemTable[j].Type.split('->') 
                    if(edt == Plist):
                        func_type=CCR.MemTable[j].Type_Mod
                        
                        if (CCR.MemTable[j].Acc_Mod== 'private'):
                            return 'private'
                        else:
                            return ertype
            
            
            return True
                

        else:
            print(f"NO CLASS FOUND {CCN}")
            sys.exit()
    

def lookUpFriendTable(Name,Operator):
    for i in range (len(FriendTable)):
        if FriendTable[i].Name == Name and FriendTable[i].Operator == Operator:
            return FriendTable[i].Name
    
    return True

                
def compatibiltyCheck(LeftOp,RightOp,Operator):
    print ("Inside Compatibility Check")

    if LeftOp == RightOp and LeftOp not in ['integ', 'int_const', 'fpoint', 'fpoint_const', 'str', 'str_const'] and RightOp not in ['integ', 'int_const', 'fpoint', 'fpoint_const', 'str', 'str_const']:
        
        dt = lookUpFriendTable(LeftOp,Operator)
        print(dt)
        if dt!=True:
            return dt
        if dt==True:
            return False

    
    else:
        if (LeftOp == 'integ' or LeftOp=='int_const') and (RightOp == 'integ' or RightOp == 'int_const') and Operator in ['+','-','*','/','%','>','<','<=','>=','!=','=','==']:
            return 'integ'
        
        elif (LeftOp == 'fpoint' or LeftOp== 'fpoint_const') and (RightOp == 'fpoint' or RightOp == 'fpoint_const') and Operator in ['+','-','*','/','%','>','<','<=','>=','!=','=','==']:
            return 'fpoint'

        elif (LeftOp=='fpoint' or LeftOp=='fpoint_const') and (RightOp == 'integ' or RightOp =='integ_const') and Operator in ['+','-','*','/','%','>','<','<=','>=','!=','==']:
            
            return 'fpoint'

        elif (LeftOp=='integ' or LeftOp=='integ_const') and (RightOp == 'fpoint' or RightOp =='fpoint_const') and Operator in ['+','-','*','/','%','>','<','<=','>=','!=','==']:
            
            return 'fpoint'
        
        elif (LeftOp=='integ' or LeftOp=='integ_const') and (RightOp == 'fpoint' or RightOp =='fpoint_const') and Operator == "=":
            
            return 'integ'
        
        elif (LeftOp=='fpoint' or LeftOp=='fpoint_const') and (RightOp == 'integ' or RightOp =='integ_const') and Operator =='=':
            
            return 'fpoint'
        
        elif (LeftOp=='str' or LeftOp=='str_const') and (RightOp == 'str' or RightOp =='str_const') and Operator in ['+','=']:
            return 'str'

        else:
            return False


    
def CompatibilityTest(Optype,Operator):
    if Operator in ['!','++','--']:
        if Optype == 'integ':
            return 'integ'
        elif Optype == 'fpoint':
            return 'fpoint'    
    else:
        return False
        

        
    

def insertFriendTable(Name,Operator):
    DT = lookUpFriendTable(Name,Operator)
    if DT!=True:
        print(f"Error at Line No {List[i].Line_No}: {Operator} Overloading already exists in class {Name}")
        sys.exit()
        
    else:
        obj = FriendInstance(Name,Operator)
        FriendTable.append(obj)
        print(f"{Operator} Overloaded for class {Name}")
        
def insertScopeTable(Name,Type,Scope):
    global i
    print(Name,Type,Scope,"INSIDE JHOOT")
    if ("str" not in Type) and ("integ" not in Type) and ("fpoint" not in Type):
        srtr=lookUpDefTable(Type,'class')
        if(srtr):
                if srtr.Type!="abstract":
                    obj = ScopeTableInstance(Name,Type,Scope)
                    print(f"Object {Name} is added")
                else:
                    print("Error: Cannot declare an object of abstract class.")
                    sys.exit()
        else:
            print(f'Error in Line No {List[i].Line_No} : Class {Type} does not exist')
            sys.exit()

    if "->" in Type:

        if (lookUpFuncST(Name,Type)==True):
            obj = ScopeTableInstance(Name,Type,Scope)
            ScopeTable.append(obj)
            print(f"Function {Name} is added")
        else:
            print("Function Redeclaration Error")
            sys.exit()
    else:
        for j in range(len(ScopeTable)):
            if ScopeTable[j].Name == Name: 
                if ScopeTable[j].Scope ==Scope:
                    print(f"Error in Line No {List[i].Line_No}:{Name} is already declared ")
                    sys.exit()
                
        obj=ScopeTableInstance(Name,Type,Scope)
        ScopeTable.append(obj)
        print(f"Variable {Name} is added")
            
            



def insertDefTable(Name,Type,Acc_Mod,Parent,Type_Mod):
    global CCN,CCR
    if(lookUpDefTable(Name,Type)):
        print("Error !  Redefinition of "+Name+".")
        sys.exit()
        
    else:

        CCN = Name
        obj=DefTableInstance(Name,Type,Acc_Mod,Parent,Type_Mod)
        CCR = obj.MemTable
        DefTable.append(obj)
        print(f"{CCN} is added as {Type}")



def insertMemTable(Name,Type,Acc_Mod,Type_Mod,Const,Class_Name):
    global CCR ,CCN
    print(Name,Type,Acc_Mod,Type_Mod,Const,Class_Name,"INSIDE")
    if "->" in Type:
        a = lookUpFuncMT(Name,Type,Class_Name)

        if (a=='private'):
            print(f"Error in Line No {List[i].Line_No}: Redefinition of member function '"+str(Name)+"'")
            sys.exit()



        if(a!=True):
            print(f"Error in Line No {List[i].Line_No}: Redefinition of member function '"+str(Name)+"'")
            sys.exit()



        if(a==True):
            obj=MemTableInstance(Name,Type,Acc_Mod,Type_Mod,Const,Class_Name)
            CCR.MemTable.append(obj)
            print(f"{Name} function is added in {Class_Name} as member")

    else:
        a = lookUpMemTable(Name,Class_Name)
        
        if (a=='private'):
            print(f"Error in Line No {List[i].Line_No}: Redefinition of member function '"+str(Name)+"'")
            sys.exit()

        if(a!=True):
            print(f"Error in Line No {List[i].Line_No}: Redefinition of member variable '"+str(Name)+"'")
            sys.exit()


        if(a==True):
            obj=MemTableInstance(Name,Type,Acc_Mod,Type_Mod,Const,Class_Name)
            CCR.MemTable.append(obj)
            print(f"{Name} is added in {Class_Name} as member")


def createScope():
    global Stack
    global scope
    global currentScope
    scope+=1
    currentScope = scope
    Stack.insert(0,scope)



def destroyScope():
    global currentScope
    global Stack
    Stack.pop(0)
    currentScope = Stack[0]


from New_LEX import List
import sys
i=0
List[i].Token_Class=List[i].Token_Class
# print(List[-1].Token_Class)

def Start():
    
    global i
    print("Start")
    print(i)
    if(i>=len(List)):
        sys.exit(1)
    if(List[i].Token_Class == "$"):
        print("Valid Syntax")
        main()
        sys.exit()
    
    if List[i].Token_Class in ['class','acc_mod','abstract','sealed','public','private']:
        if(Class_Stat()==True):
            print("Class Stat")
            Start()          
    elif(Struct_Stat()==True):
        print("Struct_Stat")
        Start()
    elif(Single_State(body_type)==True):
        print("Recall Start")
        Start()
    
    
    
    
    else:
        print(f"Error in Line No {List[i-1].Line_No}: Invalid Syntax")
   


def Class_Stat():
    global i
    global def_type
    def_type = 'class'
    TM = Type_Modifier()
    if(TM):
        AM = Acc_Modifier()
        print(AM,"LOCKEY")
        if(AM):
            if(List[i].Token_Class=="class"):
                Type ='class'
                i=i+1

                if(ID()==True):

                    Name = List[i-1].Token_Value
                    Parent = Inherit()
                    if(Parent):
                        if Parent == "-":
                            insertDefTable(Name,Type,AM,Parent,TM)
                        else:
                            info=lookUpDefTable(Parent,Type)
                            if(info):
                                if info.Type_Mod == 'sealed':
                                    print("sealed class can't be inherited")
                                    sys.exit()
                                else:
                                    insertDefTable(Name,Type,AM,Parent,TM)
                            else:
                                print("No Declearation of Parent Class",Parent)
                                sys.exit()

                        if(Class_Main_Body()==True):
                            if(List[i].Token_Class==";"):
                                i=i+1
                                def_type = ""
                                return True

                    else:
                        print("Expecting 'inherit' keyword or { but getting",f"{List[i].Token_Value}")



        else:
            print(f"Error in Line {List[i].Line_No} : Expecting Access Modifier Or 'class' keyword but getting {List[i].Token_Value}")
            
    
    
    else:
        print(f"Error in Line {List[i].Line_No} : Expecting Type Modifier Or Access Modifier but getting {List[i].Token_Value}")
        sys.exit()



def Struct_Stat():
    global i
    global def_type
    def_type='struct'
    if(List[i].Token_Class=="struct"):
        i=i+1
        Type = 'struct'
        if(ID()==True):
            name = List[i-1].Token_Value
            insertDefTable(name,Type,'public','-','general')
            if(List[i].Token_Class=="{"):
                i=i+1
                if(Struct_Body()==True):
                    if(List[i].Token_Class=="}"):
                        print("}")
                        i=i+1
                        if(List[i].Token_Class==";"):
                            i=i+1
                            def_type=""
                            return True
    else:
        return False


def Single_State(body_type):
    global i
    global func_type
    print("Single State")
    if(While_Stat()==True):
        if List[i].Token_Class ==";":
            i+=1
            return True
        else:
                return False        

    elif(For_Stat()==True):
            if List[i].Token_Class ==";":
                i+=1
                return True
            else:
                return False
    
                
    elif(Func_Stat()==True):
        if List[i].Token_Class ==";":
            i+=1
            return True
        else:
                 return False        

    elif (List[i].Token_Value=='return'):
        dt=Return_Stat()
        if (dt):
            print(body_type,"TYPE")
            if body_type == "Function":
                if List[i].Token_Class ==";":
                    print(List[i].Token_Value)
                    i+=1
                    print(List[i].Token_Value)

                    print("RETURNONG TRUE")
                    return True
                else:
                    return False
            else:
                print(f"You Can Only Use Return Statement in Function")
                sys.exit()        

    elif(Flow_Control()==True):
        if body_type == "loop":
            if List[i].Token_Class ==";":
                i+=1
                return True
            else:
                print(f"Missing ; at Line No {List[i-1].Line_No}")
                sys.exit()
                
        else:
            print(f"{List[i-1].Token_Value} in Line no {List[i-1].Line_No} is not allowed here")
            sys.exit()

    elif(If_Else_State()==True):   
         if List[i].Token_Class ==";":
            i+=1
            return True
         else:
                 return False        
 
    elif(Inc_Dec_Op()==True):
         operator = List[i-1].Token_Value
         if(ID()==True):
            name = List[i-1].Token_Value
            dt = lookUpScopeTable(name)
            if(CompatibilityTest(dt,operator)):
                final_dt = A1(dt)
                if (final_dt):
                    if List[i].Token_Class ==";":
                        i+=1
                        return True 
                    else:
                        return False
            else:
                print(f"Error In Line No {List[i].Line_No}: {dt} can't be increment or decrement")
                sys.exit()
                   
    elif(DT()==True):
         dt=List[i-1].Token_Value
         print(List[i-1].Token_Value)
         if(ID()==True):

            if (List[i].Token_Value == '['):
                name=List[i-1].Token_Value
                print(name,"first")
                #insert(name)
                con_type = A1(dt)
                print(con_type,"BOLOGU")
                if(con_type):
                    insertScopeTable(name,con_type,currentScope)
                    if List[i].Token_Class ==";":
                        print(List[i].Token_Class,"n")
                        i+=1
                        return True 
                    else:
                        return False
                
                if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'): 
                    print(f"you can't assign {con_type} in {name}({dt})")
                    sys.exit()
                else:
                    return False

            else:
                name=List[i-1].Token_Value
                print(name,"first")
                insertScopeTable(name,dt,currentScope)
                #insert(name)
                con_type = A1(dt)
                final_dt = str(dt)+str(con_type)
                print(final_dt,"FONAL")
                if(con_type==True):
                    #   insertScopeTable(name,dt+con_type,currentScope)
                    print(dt,name)
                    print(name,"zero")
                    print(List[i].Token_Class)
                    if List[i].Token_Class ==";":
                        print(List[i].Token_Class,"n")
                        i+=1
                        return True 
                    else:
                        return False
                
                if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'): 
                    print(f"you can't assign {con_type} in {name}({dt})")
                    sys.exit()
                else:
                    return False    
         else:
             return False
                  
    elif(ID()==True):
        if (List[i].Token_Value=="("):
            con_type = A2('func')
            if(con_type==True):
                    print("Ahsaan")
                    if List[i].Token_Class ==";":
                        i+=1
                        return True
            
        else:            
            name = List[i-1].Token_Value
            print(List[i-1].Token_Value)

    
            if List[i].Token_Class =='ID':
                if List[i+1].Token_Class == "(":
                    name = List[i].Token_Value
                    i=i+1
                    class_name=List[i-2].Token_Value
                    if List[i+1].Token_Value==")":
                        plist = 'void'
                        i=i+1
                        check=lookUpFuncMT(name,plist,class_name)
                        if (check):
                            if func_type == 'static':
                                i=i+1
                                if List[i].Token_Value == ';':
                                    i=i+1
                                    return True
                            else:
                                print(f"Error in Line No {List[i].Line_No}: You can only call static function like this")
                                sys.exit()




                    else:
                        if (List[i].Token_Value=="("):

                            i=i+1

                            final_dt = Make_Dt("")
                            print("GERE")
                            print(final_dt)

                            if (final_dt):
                                Dtype=lookUpFuncMT(name,final_dt,class_name)
                                if (Dtype):
                                    if func_type == 'static':
                                        i=i+1
                                        if List[i].Token_Value == ';':
                                            i=i+1
                                            return True
                                    
                                    else:
                                        print(f"Error in Line No {List[i].Line_No}: You can only call static function like this")
                                        sys.exit()


                        

                    

                else:
                    name = List[i].Token_Value
                    class_type = List[i-1].Token_Value
                    i=i+1
                    check = lookUpDefTable(class_type,'class')
                    if(check==False):
                        print(f"Error In Line No {List[i].Line_No}: class/structure {class_type} is not defined")
                        sys.exit()

                    else:
                        type_mod = check.Type_Mod
                        if type_mod == 'abstract':
                            print(f"Error in Line No {List[i].Line_No}:can't create object of abstract class {class_type}")
                            sys.exit()
                        else:
                            insertScopeTable(name,class_type,currentScope)
                            con_type = A2(class_type)
                            if(con_type==True):
                                print("Ahsaan")
                                if List[i].Token_Class ==";":
                                    i+=1
                                    return True

            else:
                var_type=lookUpScopeTable(name)
                print(var_type,"MAMA")
                if (var_type==True):
                    print(f"Undefined variable '{name}'")
                    sys.exit()
                
                else:
                    con_type = A2(var_type)
                    print(con_type,"HOLA")
                    if(con_type==True):
                        print("Ahsaan")
                        if List[i].Token_Class ==";":
                            i+=1
                            return True
                
                    if((con_type == 'str_const' or con_type == 'str') or (con_type=='int_const' or con_type=='integ') or (con_type=='fpoint_const' or con_type=='fpoint')):
                        print(f"you can't assign {con_type} in {name}({var_type})")
                        sys.exit()
                    else:
                        return False
        
    else:
        return False 
    
    
def While_Stat():
    global i
    global body_type
    if body_type == "loop":
        if(List[i].Token_Class=="while"):
            print("While")
            i=i+1
            if(List[i].Token_Class=="("):
                i=i+1
                dt =Expr()
                if(dt):
                    if(List[i].Token_Class==")"):
                        i=i+1
                        createScope()
                        body_type = 'loop'
                        if(Body()==True):
                            body_type='loop'
                            destroyScope()
                            return True
                        else:
                            return  False
                            
                else:
                    return False
        else:
            return False

    else:    
        if(List[i].Token_Class=="while"):
            print("While")
            i=i+1
            if(List[i].Token_Class=="("):
                i=i+1
                dt =Expr()
                if(dt):
                    if(List[i].Token_Class==")"):
                        i=i+1
                        createScope()
                        body_type = 'loop'
                        if(Body()==True):
                            body_type=''
                            destroyScope()
                            return True
                        else:
                            return  False
                            
                else:
                    return False
        else:
            return False
def For_Stat():
    global i
    global body_type
    if body_type == 'loop':
        if(List[i].Token_Class=="for"):
            i=i+1
            body_type = 'loop'
            createScope()
            if(List[i].Token_Class=="("):
                i=i+1
                if(Init()==True):
                    if(List[i].Token_Class==";"):
                        i=i+1
                        if(Condition()==True):
                            if(List[i].Token_Class==";"):
                                i=i+1
                                if(Inc_Dec_Stat()==True):
                                    if(List[i].Token_Class==")"):
                                        i=i+1
                                        if(Body()==True):
                                            print(Stack[0],"BEFORE")
                                            body_type='loop'
                                            destroyScope()
                                            print(Stack[0],"AFTER")
                                            return True
        else:
            return False
        

    else:    
        if(List[i].Token_Class=="for"):
            i=i+1
            body_type = 'loop'
            createScope()
            if(List[i].Token_Class=="("):
                i=i+1
                if(Init()==True):
                    if(List[i].Token_Class==";"):
                        i=i+1
                        if(Condition()==True):
                            if(List[i].Token_Class==";"):

                                i=i+1
                                if(Inc_Dec_Stat()==True):
                                    if(List[i].Token_Class==")"):
                                        i=i+1
                                        if(Body()==True):
                                            print(Stack[0],"BEFORE")
                                            body_type=''
                                            destroyScope()
                                            print(Stack[0],"AFTER")
                                            return True
        else:
            return False
        
def Func_Stat():
    global i
    global body_type
    global return_type
    if(List[i].Token_Class=="def"):
        i=i+1
        if(DT()==True):
            rtype = List[i-1].Token_Value
            if(ID()==True):
                name = List[i-1].Token_Value
                createScope()
                if(List[i].Token_Class=="("):
                    i=i+1
                    T = Para_Init()
                    if(T):
                        T=T+'->'+rtype
                        insertScopeTable(name,T,Stack[1])
                        if(List[i].Token_Class==")"):
                            i=i+1
                            if(Func_Body()==True):
                                if return_type=="":
                                    if (List[i].Token_Class==";"):
                                        body_type=""
                                        destroyScope()
                                        return True
                                elif return_type==rtype:
                                    if (List[i].Token_Class==";"):
                                        body_type=""
                                        destroyScope()
                                        return True

                                else:
                                    print (f"Expecting return type {rtype}, Having {return_type}")
                                    sys.exit()
                    else:
                        print("Error in function declaration")
                        sys.exit()
            
            else:
                print(f"Error in Line No {List[i].Line_No}: Expecting ID After 'Datatype' but getting {List[i].Token_Value}")
                sys.exit()

        else:
            print(f"Error in Line No {List[i].Line_No}: Expecting Datatype After 'def' but getting {List[i].Token_Value}")
            sys.exit()
    else:
        return False
    
def Return_Stat():
    global i
    if(List[i].Token_Class=="return"):
        i=i+1
        dt = Return_Body()
        if(dt):
            return dt  
    else:
        return False              
def Flow_Control():
    global i
    if(List[i].Token_Class=="flow_control"):
       i=i+1
       return True
    else:
        return False
 
def If_Else_State():
    global i
    if(List[i].Token_Class=="provide"):
        i=i+1
        if(List[i].Token_Class=="("):
            i=i+1
            dt = Expr()
            if(dt):
                if(List[i].Token_Class==")"):
                    i=i+1
                    createScope()
                    if(Body()==True):
                        print("body")
                        if(Else_Stat()==True):
                            destroyScope()
                            return True
    else:
        return False


def Inc_Dec_Op():
    global i
    if(List[i].Token_Class=="inc_dec"):
        i=i+1
        return True
    else:
        return False

def A1(dt):
    
    global i
    print("Inside A1")

    
    if(List[i].Token_Class==","):
        i=i+1
        if(ID()==True):
            name = List[i-1].Token_Value
            insertScopeTable(name,dt,currentScope)
            con_type= A1(dt)
            if(con_type==True):
                return True
            if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'):
                print(f"you can't assign {con_type} in {name}({dt})")
                sys.exit()
            else:
                return False
        else:
            print(f"Error in Line No {List[i].Line_No}: Expected ID after ',' ")
            sys.exit()
    elif(List[i].Token_Class=="["):

        DT =""
        DT = dt+'['
        i=i+1
        T = Expr()
        if(T == 'integ' or T=='int_const'):
            if(List[i].Token_Class=="]"):
                DT = DT +"]"                
                i=i+1
                if List[i].Token_Class=="[":
                    final_dt=Arr_Assign(DT) 
                    print(final_dt,"NEXT TO ME")
                    if(final_dt):
                        print(final_dt)
                        return final_dt
                if List[i].Token_Class==";":
                    print("GOJO",DT)
                    return DT
            else:
                print(f"Error in Line No {List[i].Line_No}: Missing ']'")
                sys.exit()
        else:
            print("invalid array index type")
            sys.exit()
    elif(List[i].Token_Class=="("):
        i=i+1
        if(Arg_List("")==True):
            if(List[i].Token_Class==")"):
                i=i+1
                return True
    elif(List[i].Token_Class=="."):
        i=i+1
        if(ID()==True):
            if(A1()==True):
                return True
    elif(Assign_OP()==True):
        operator = List[i-1].Token_Value
        value = List[i].Token_Value
        con_type=Expr()
        if(con_type):
            print("HEre")
            # result = compatibiltyCheck(dt,con_type,operator)
            if(compatibiltyCheck(dt,con_type,operator)):
                if(A4(dt)==True):
                    return True
            else:
                return con_type
        else:
            return False
        
    elif(Inc_Dec_Op()==True):
        if(A4(dt="ido")==True):
            return True
    
    elif(List[i].Token_Class in[")",";"]):
        print("NULL parha")
        return True
    else:
        print("error")
        return False

def DT(): 
     global i
     if(List[i].Token_Class=="dtype"):
         print("data Type")
         i=i+1
         return True
     else:
        return False
     

def ID():
   global i
   if(List[i].Token_Class=="ID"):
       i=i+1
       print("ID")
       return True
   else:
        return False
def A2(dt):
    global CCN
    print(dt)
    print("A2")

    global i

    if(List[i].Token_Class==","):
        i=i+1
        if(ID()==True):
            if(A2()==True):
                return True
        
    elif(List[i].Token_Class=="["):
        i=i+1
        if(Expr()==True):
            if(List[i].Token_Class=="]"):
                i=i+1
                if(C()==True):
                    return True
            else:
                print(f"Error in Line No {List[i].Line_No}: Missing ']'")
                sys.exit()

                
    elif(List[i].Token_Class=="("):
        name = List[i-1].Token_Value
        if(List[i-2].Token_Value=="."):
                i=i+1
                TT = Arg_List("")
                if(TT):
                    if(List[i].Token_Class==")"):
                        i=i+1
                        DT=lookUpFuncMT(name,TT,CCN)

                        if (DT==True):
                            print(f"function \"{name}\" is not declared in {CCN}")
                            sys.exit()
                        
                        else:
                            if(B(DT)==True):
                                return True
            
        else:
            i=i+1
            if List[i].Token_Value == ")":
                i=i+1
                DT=lookUpFuncST(name,'void')
                if (DT==True):
                    print(f"function \"{name}\" is not declared")
                    sys.exit()
                    
                else:
                    if(B(dt)==True):
                        return True
        
                
            else:
                TT = Arg_List("")

                if(TT):
                    if(List[i].Token_Class==")"):
                        i=i+1
                        DT=lookUpFuncST(name,TT)
                        if (DT==True):
                            print(f"function \"{name}\" is not declared")
                            sys.exit()
                            
                        else:
                            final_dt = B(dt)
                            if(final_dt):
                                return final_dt
                
                    
    elif(List[i].Token_Class=="."):
        i=i+1
        if(ID()==True):
            name=List[i-1].Token_Value
            if(dt == 'integ') or (dt == 'str') or (dt == 'fpoint'):
                print(f"Error in Line No {List[i].Line_No}: Expecting a class name for {name} but getting {dt}")
                sys.exit()

                # name = List[i-1].Token_Value

                # check=lookUpMemTable(name,dt)
                # if check==True:
                #     print(f"Error in Line No {List[i].Line_No}: Can't find member({name}) in {CCN}")
                #     sys.exit()
                # else:
                #     con_type = A2(check)
                #     if(con_type):
                #         return con_type
                #     else:
                #         print(f"Error in Line No {List[i].Line_No} : Type mismatch for member access operator")
            
            
            else:
                if (List[i].Token_Value=="("):
                    con_type  = A2(dt)
                    if(con_type==True):
                        if List[i].Token_Class ==";":
                            return True
                        
                else:
                    name = List[i-1].Token_Value
                    print(name,"LOOP")
                    check=lookUpMemTable(name,dt)
                    print(check,"Andhayy")
                    if (check == 'private'):
                        print(f"Error in Line No {List[i].Line_No}:You Can't Call private member({name}) ")
                        sys.exit()

                    if check==True:
                        print(f"Error in Line No {List[i].Line_No}: Can't find member({name}) in {CCN}")
                        sys.exit()
                    else:

                        con_type = A2(check)
                        if(con_type):
                            return con_type
                        else:
                            print(f"Error in Line No {List[i].Line_No} : Type mismatch for member access operator")
    elif(Assign_OP()==True):
        operator = List[i-1].Token_Value
        con_type = Expr()
        print(con_type,"OOLLA")
        print(dt,"OOLLA")

        if(con_type):
            if(compatibiltyCheck(dt,con_type,operator)):
                if(A4(dt)==True):
                    return True
            else:
                print(con_type,'JOKER')
                return con_type
        else:
            False
    elif(Comp_OP()==True):
        if(Expr()==True):
            return True

    
    elif(Inc_Dec_Op()==True):
        operator = List[i-1].Token_Value
        if(CompatibilityTest(dt,operator)):
            if(A4(dt)==True):
                return True
        else:
            print(f"{dt} can't be incremented in line no {List[i-1].Line_No}")
            sys.exit()
    elif(ID()==True):
        if(Obj_List()==True):
            return True
    
    elif(List[i].Token_Value == ":"):
        i+=1
        if(ID()==True):
            name = List[i].Token_Value
            class_name = List[i-1].Token_Value
            if List[i].Token_Class == "(":
                    if List[i+1].Token_Value==")":
                        plist = 'void'
                        i=i+1
                        if class_name == dt:
                            check=lookUpFuncMT(class_name,plist,class_name)
                            print(check,"UMBRELLA")

                            if (check==True):
                                print(f"Error in Line No {List[i].Line_No}: Can't Find Constructor")
                                sys.exit()
                                
                                
                            else:   
                                if func_type == 'static':
                                    i=i+1
                                    if List[i].Token_Value == ';':
                                        return True
                                    
                                else:
                                    print(f"Error in Line No {List[i].Line_No}: You can only call static function like this")
                                    sys.exit()
                        else:
                            
                            class_info = lookUpDefTable(dt,'class')
                            parent = class_info.Parent
                            if parent == class_name:
                                check=lookUpFuncMT(name,plist,class_name)
                                print(check,"UMBRELLA")

                                if (check==True):
                                    print(f"Error in Line No {List[i].Line_No}: Can't Find Constructor")
                                    sys.exit()
                                else:
                                    if func_type == 'static':
                                        i=i+1
                                        if List[i].Token_Value == ';':
                                            return True
                                    else:
                                        print(f"Error in Line No {List[i].Line_No}: You can only call static function like this")
                                        sys.exit()
                            else:
                                print(f"Error in Line No {List[i].Line_No}: Can't Call Constructor Of Class Which Is Not Inherited")
                                sys.exit()
                    
                    else:
                        print(List[i].Token_Value,"SHER")
                        i+=1
                        plist =Make_Dt("")
                        if (plist):
                            print(plist,"HIRAN")
                            if class_name == dt:
                                check=lookUpFuncMT(dt,plist,class_name)
                                print(check,"UMBRELLA")
                                if (check):
                                    if func_type == 'static':
                                        i=i+1
                                        if List[i].Token_Value == ';':
                                            return True
                                    else:
                                        print(f"Error in Line No {List[i].Line_No}: You can only call static function like this")
                                        sys.exit()
                                else:
                                    print(f"Error in Line No {List[i].Line_No}: Constructor of the base class is not defined")
                                    sys.exit()

                            else:
                                
                                class_info = lookUpDefTable(dt,'class')
                                parent = class_info.Parent
                                if parent == class_name:
                                    check=lookUpFuncMT(name,plist,class_name)
                                    if (check):
                                        if func_type == 'static':
                                            i=i+1
                                            if List[i].Token_Value == ';':
                                                return True
                                        else:
                                            print(f"Error in Line No {List[i].Line_No}: You can only call static function like this")
                                            sys.exit()
                                    else:
                                        print(f"Error in Line No {List[i].Line_No}: Constructor of the base class is not defined")
                                        sys.exit()
                                else:
                                    print(f"Error in Line No {List[i].Line_No}: Can't Call Constructor Of Class Which Is Not Inherited")
                                    sys.exit()
                        
                        else:
                            print(f"Error in Line No {List[i].Line_No}: Invalid Parameters Of Constructor")
                            sys.exit()
                            














        
    elif(List[i].Token_Class==";"):
          return True

    else:
        
        return False



def Expr():
    global i
    final_dt,final_name=OR_Expr()
    print(final_dt,"MARCOPOLO")
    if (final_dt):
        return final_dt
    else:
        return False


def Arr_List(DT):
    global i
    if(List[i].Token_Class=="["):
        i=i+1
        DT=DT+'['
        T = Expr()

        if(T=='integ' or T=='int_const'):
            if(List[i].Token_Class=="]"):
                i=i+1
                DT=DT+']'
                final_dt=Arr_List(DT)
                if(final_dt):
                    return final_dt
            else:
                print(f"Error in Line No {List[i].Line_No}: Missing ']'")
                sys.exit()
    elif(List[i].Token_Class in[".","MDM","PM","ROP","LOP","]",")",";",","]):
        return DT
    
    else:
        return False
def Arg_List(TT):
        global i
        dt =Expr()
        T = TT+dt
        if(dt):
            FT =A(T)
            if(FT):
                return FT
            else:
                 return False
        elif(List[i].Token_Class==")"):
              return True
        else:
           return False 
def B(dt):
       global i
       global def_type
       print(dt,"Inside BT")
       if(List[i].Token_Class=="."):
           i=i+1
           if(ID()==True):
                name = List[i-1].Token_Value
                check = lookUpMemTable(name,dt)
                print(check,"Andhayy1")
                if (check == 'private'):
                    print(f"Error in Line No {List[i].Line_No}:You Can't Call private member({name}) ")
                    sys.exit()


                if(check == True):
                   print(f"Error in Line No {List[i].Line_No}: Can't find member({name}) in {CCN}")
                   sys.exit()
                else:
                    con_type = A2(check)
                    if(con_type):
                        return con_type
                    else:
                        print(f"Error in Line No {List[i].Line_No} : Type mismatch for member access operator")


       elif(List[i].Token_Class in ["MDM","PM","ROP","LOP","]",")",";",","]):
              return True
       else:
            return False  
def C():
    global i
    if(List[i].Token_Class=="."):
           i=i+1
           if(ID()==True):
               if(A2()==True):
                   return True
    elif(Assign_OP()==True):
        if(Expr()==True):
            return True
    elif(List[i].Token_Class in[";"]):
        i=i+1
        return True
    else:
            return False  
def Assign_OP():
        global i
        if(List[i].Token_Class=="AOP"):
            i=i+1
            return True 
        else:
           return False    
def A4(dt):
    global i

    if(List[i].Token_Class==","):        
        i=i+1

        if(ID()==True):
            if dt == 'ido':
                name=List[i-1].Token_Value
                type=lookUpScopeTable(name)
                if (type == True):
                    print(f"{name} in not initialized")
                    sys.exit()
                else:
                    if dt == 'str':
                        print(f"{name} ({dt}) can't be increment")
                        sys.exit()
                    if (dt!=True):
                        con_type = A1(dt)
                        if(con_type==True):
                            return True
                    
                
            else:
                name=List[i-1].Token_Value
                insertScopeTable(name,dt,currentScope)
                print(name)
                con_type = A1(dt)
                if(con_type==True):
                    return True
                if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'): 
                    print(f"Error in Line No {List[i].Line_No}: you can't assign {con_type} in {name}({dt})")
                    sys.exit()
                else:
                    return False
        else:
            print(f"Error in Line No {List[i].Line_No}: Expected ID after ',' ")
            sys.exit()
    elif(List[i].Token_Class==";" or List[i].Token_Class==")"):
        print("Null Parha")
        return True

    else:
        return False 
    #return True
def Obj_List():
        global i
        if(List[i].Token_Class==","):
            i=i+1
            if(ID()==True):
                if(Obj_List()==True):
                    return True
        elif(List[i].Token_Class=="("):
            i=i+1
            if(Expr()==True):
                if(Obj_List2()==True):
                    if(List[i].Token_Class==")"):
                         i=i+1
                         if(Obj_List1()==True):
                              return True
        elif(Assign_OP()==True):
            print("=")
            if(List[i].Token_Class=="new"):
                i=i+1
                print(List[i].Token_Class)
                if(Expr()==True):
                        return True
        elif(List[i].Token_Class==";" or List[i].Token_Class==")"):
              return True
      
        else:
           return False 
def Obj_List2():
    global i
    if(List[i].Token_Class==","):
        i=i+1
        if(Expr()==True):
            if(Obj_List2()==True):
                return True
    elif(List[i].Token_Class==")"):
        i=i+1
        return True
    else:
           return False 
   # return True#for NULL
def Arr_Assign(DT):
    global i
    if(List[i].Token_Class=="["):
        DT=DT+'['
        i=i+1
        T = Expr()
        if(T=='integ' or T == 'int_const'):
            if(List[i].Token_Class=="]"):
                DT=DT+']'
                print(DT,"LOCAL")
                i=i+1
                DT=Arr_Assign(DT)
                print(DT,"GHOST")
                if(DT):
                    return DT
            else:
                print(f"Error in Line No {List[i].Line_No}: Missing ']'")
                sys.exit()
        else:
            print(f"Error in Line No {List[i].Line_No}: invalid array index type")
            sys.exit()
    elif(List[i].Token_Class=="AOP"):
        print("AOP")
        i=i+1
        print(List[i].Token_Class)
        dt = Array_List1(DT)
        print(dt,"LOL")
        if(dt):
            return dt
    elif(List[i].Token_Class in[";"]):
         return DT
    else:
        return False 
        
def A3(dt):
    global i
    if(Inc_Dec_Op()==True):
        return dt
    elif(List[i].Token_Class == "("):
        i=i+1
        DT = Arg_List("")
        if(DT):
            if(List[i].Token_Class==")"):
                i=i+1
                if(B(DT)==True):
                    return DT
                
    elif(Arr_List("")==True):
        if(B()==True):
            return True
        else:
            return False
    
    if List[i].Token_Class =='.':
        i=i+1
        if List[i].Token_Class =='ID':
                    if List[i+1].Token_Class == "(":
                        name = List[i].Token_Value
                        i=i+1
                        class_name=dt
                        if List[i+1].Token_Value==")":
                            plist = 'void'
                            i=i+1
                            check=lookUpFuncMT(name,plist,class_name)

                            if (check):
                                print(f"Error in Line No {List[i].Line_No}: Undeclared Function {name}")
                                sys.exit()

                            else:
                                i=i+1
                                DT = A3(check)
                                if(DT):
                                    return DT
                        
                        else:
                            if (List[i].Token_Value=="("):
                                i=i+1
                                final_dt = Make_Dt("")
                                print("GERE")
                                print(final_dt)

                                if (final_dt):
                                    Dtype=lookUpFuncMT(name,final_dt,class_name)

                                    if (Dtype==True):
                                        print(f"Error in Line No {List[i].Line_No}: Undeclared Function {name} with parametes {final_dt}")
                                        sys.exit()

                                    else:
                                        i=i+1
                                        DT = A3(Dtype)
                                        if(DT):
                                            return DT
 
            

                            
                        

                        

        
    

    elif(List[i].Token_Class in["MDM","PM","ROP","LOP","]",")",";",","]):
        return dt
    else:
        print(f"Expecting , or ; in Line No {List[i-1].Line_No}") 
        sys.exit()
    
def Obj_List1():
     global i
     if(List[i].Token_Class==","):
         i=i+1
         if(ID()==True):
             if(Obj_List()==True):
                return True
    #Fir NULL
     #return True
     elif(List[i].Token_Class==";" or List[i].Token_Class==")"):
        i=i+1
        return True
     else:
           return False 

def Array_List1(DT):
    global i
    if(List[i].Token_Class=="["):
        i=i+1
        final_dt=Array(DT)
        print(final_dt,"SOMEBODY")
        if(final_dt):
            final_dt = Array_Cont(final_dt)
            if((final_dt)):
                if(List[i].Token_Class=="]"):
                    i=i+1
                    return final_dt
                else:
                    print(f"Error in Line No {List[i].Line_No}: Missing ']'")
                    sys.exit()
    elif(Expr()==True):
        return True
    else:
           return False 

def Array(DT):
    global i
    if List[i].Token_Class in ['ID','int_const','str_const','fpoint_const']:
        stripped = DT.strip('[]')
        T =Expr()
        print("SATURO",DT)
        if(T):
            if(compatibiltyCheck(stripped,T,'=')):
                return DT
            
            else:
                print(f"Error In Line No {List[i].Line_No}:You can't assign {T} in {DT} array")
                sys.exit()


    elif(List[i].Token_Class=="["):
        print("Second Bracket")
        i=i+1
        dt = Elements(DT)
        if(dt):
            if(List[i].Token_Class=="]"):
                i=i+1
                print(dt,"SHOOTING STAR")
                return dt
            else:
                print(f"Error in Line No {List[i].Line_No}: Missing ']'")
                sys.exit()
    else:
        return False 
def Array_Cont1(DT):
    global i
    if(List[i].Token_Class=="["):
        i=i+1
        dt = Elements(DT)
        if(dt):
            if(List[i].Token_Class=="]"):
                i=i+1
                dt = Array_Cont(DT)
                if (dt):
                    return DT
            else:
                print(f"Error in Line No {List[i].Line_No}: Missing ']'")
                sys.exit()
    elif List[i].Token_Class in ['ID','int_const','str_const','fpoint_const']:
        stripped = DT.strip('[]')
        T =Expr()
        print("SATURO",DT)
        if(T):
            if (compatibiltyCheck(stripped,T,'=')):
                final_dt=Array_Cont(DT)
                return final_dt
            
            else:
                print(f"Error In Line No {List[i].Line_No}:You can't assign {T} in {DT} array")
                sys.exit()
    else:
        return False
def Array_Cont(DT):
    global i
    if(List[i].Token_Class==","):
        i=i+1
        print(List[i].Token_Class)
        final_dt = Array_Cont1(DT)
        if(final_dt):
            return final_dt    
    elif(List[i].Token_Class=="]"):
         return DT
    else:
           return False

def Elements(DT):
    global i
    print(List[i].Token_Class,"sdsadsd")
    dt = Array(DT)
    if(dt):
        dt = Elements1(DT)
        if(dt):
            return DT
    else:
        return False 


def Elements1(DT):
    global i
    if(List[i].Token_Class==","):
        i=i+1
        dt = Elements(DT)
        if(dt):
            return DT
    elif(List[i].Token_Class=="]"):
        return DT
    else:
        return False 

def A(TT):
    global i
    if(List[i].Token_Class==","):
        i=i+1
        TT = TT+","
        FT = Arg_List(TT)
        if(FT):
            PT = A(FT)
            if (PT):
                return PT
    elif(List[i].Token_Class==")"):
        return TT
    else:
           return False 


def Body():
    global i
    if(List[i].Token_Class=="{"):

        i=i+1

        # print(List[i].Token_Class)
        if(Multiple_Stat()==True):
            if(List[i].Token_Class=="}") and (List[i-1].Token_Class==";" ):
                i=i+1
                if List[i].Token_Class==";":
                    return True
                else:
                    print(f"Error in Line No {List[i-1].Line_No} : Expecting ;")
                    sys.exit()
            elif (List[i-1].Token_Class=="{") and (List[i].Token_Class == "}"):
                i=i+1
                if List[i].Token_Value == ";":
                    return True
                else:
                    print(f"Error in Line No {List[i-1].Line_No} : Expecting ;")
                    sys.exit()

            else:
                return False
        else:
            print(f"Error in Line No {List[i].Line_No}: Error in Body Syntax")

            sys.exit()
        
    else:

        print(f"Error in Line No {List[i].Line_No}:" ,"Missing '{' ")

        sys.exit()
        
            
def Multiple_Stat():
    global i

    if(Single_State(body_type)==True):
        if(Multiple_Stat()==True):
            return True
    elif(List[i].Token_Class=="}"):
        return True

    else:
        print(List[i].Token_Class)
        return False 

    
def Init():
    global i
    if(DT()==True):
        dt= List[i-1].Token_Value
        if(ID()==True):
            name = List[i-1].Token_Value
            insertScopeTable(name,dt,currentScope)
            con_type = A1(dt)
            if(con_type==True):
                    return True 
            if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'):
                print(f"you can't assign {con_type} in {name}({dt})")
                sys.exit()
            else:
                return False
            
    elif(ID()==True):
        name = List[i-1].Token_Value
        dt=lookUpScopeTable(name)
        if dt == True:
            print(f"{name} is not initialized")
            sys.exit()
        else:
            con_type = A1(dt)
            if(con_type==True):
                return True
            else:
                print(f"{name}({dt}) is not compatible with {con_type}")
                sys.exit()
    elif(List[i].Token_Class==";"):
        return True
    else:
        return False 
def Condition():
    global i
    if(List[i].Token_Class==";"):
        return True
    elif(Expr()):
        return True
    
    else:
           return False 
def Inc_Dec_Stat():
    global i
    if(ID()==True):
        name = List[i-1].Token_Value
        dt=lookUpScopeTable(name)
        if dt == 'str':
            print(f"{name} ({dt}) can't be increment")
            sys.exit()
        if (dt!=True):
            con_type = A1(dt)
            if(con_type==True):
                    return True 
            
        else:
            print(f"{name} is not initilized")
            sys.exit()
            
    if(Inc_Dec_Op()==True):
        if(ID()==True):
            return True
    elif(List[i].Token_Class==")"):
        return True
    else:
           return False 


def OR_Expr():
    global i
    dt,dt_name =AND_Expr() 
    if(dt):
        final_dt,final_name =OR_Expr1(dt,dt_name)
        if (final_dt):
            return final_dt,final_name
    else:
           return False 
def AND_Expr():
    global i
    dt,dt_name =RO_Expr()
    if (dt):
        final_dt,final_name=AND_Expr1(dt,dt_name)
        if(final_dt):
            return final_dt,final_name
    else:
        return False

    
def OR_Expr1(dt,name):
    
    global i 
    if(List[i].Token_Class=="LOP"):
        i=i+1
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No
        dt2,dt_name = AND_Expr()
        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = OR_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
            else:
                print(f"{name} ({dt})  can't {operator} with {dt_name} ({dt2}) in line no {line_no}")
                sys.exit()
    elif(List[i].Token_Class in ["ROP","LOP","]",")",";",","]):
        return dt,name
    else:
        return False 
def RO_Expr():
    global i
    dt,dt_name = PM_Expr()
    if (dt):
        final_dt,final_name = RO_Expr1(dt,dt_name)
        if (final_dt):
            return final_dt,final_name
    else:
        return False

     
def AND_Expr1(dt,name):
    
    global i 
    if(List[i].Token_Class == "LOP"):
        i = i + 1
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No

        dt2,dt_name = RO_Expr()
        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = AND_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
            else:
                print(f"{name} ({dt})  can't {operator} with {dt_name} ({dt2}) in line no {line_no}")
                sys.exit()
    elif(List[i].Token_Class in ["ROP","LOP","]",")",";",","]):
        return dt,name
    else:
        return False   
def RO_Expr1(dt,name):
    global i 
    if(RO()==True):
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No

        dt2,dt_name = PM_Expr()
        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = RO_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
            else:
                print(f"{name} ({dt})  can't {operator} with {dt_name} ({dt2}) in line no {line_no}")
                sys.exit()
    elif(List[i].Token_Class in ["ROP","LOP","]",")",";",","]):
        return dt,name
    else:
        return False  
def PM_Expr():
    dt,dt_name =MDM_Expr()
    if(dt):
        final_dt,final_name=PM_Expr1(dt,dt_name)
        if(final_dt):
            return final_dt,final_name
    else:
        return False 
def RO():
    global i
    if(List[i].Token_Class=="ROP"):
        print("ROP_RO")
        i=i+1
        return True
    else:
           return False 
def MDM_Expr():
    global i
    dt,dt_name =I_C_B()
    if(dt):
        final_dt,final_name=MDM_Expr1(dt,dt_name)
        if(final_dt):
            return final_dt,final_name
    else:
        return False    
def PM_Expr1(dt,name):
    global i 
    if(PM()==True):
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No
        dt2,dt_name = MDM_Expr()
        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = PM_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
            else:
                print(f"{name} ({dt})  can't {operator} with {dt_name} ({dt2}) in line no {line_no}")
                sys.exit()
    elif(List[i].Token_Class in ["ROP","LOP","]",")",";",","]):
        return dt,name
    else:
        return False 
def PM():
    global i
    if(List[i].Token_Class=="PM"):
        i=i+1
        return True
    else:
           return False 

def MDM_Expr1(dt,name):
     
     global i
     if(MDM()==True):
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No
        dt2,dt_name = I_C_B()
        print(dt2)
        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = MDM_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
            else:
                print(f"{name} ({dt})  can't {operator} with {dt_name} ({dt2}) in line no {line_no}")
                sys.exit()
     elif(List[i].Token_Class in["PM","ROP","LOP","]",")",";","," ] ):
        return dt,name
     else:
        print(f"Expecting Operator or ']' or ')' or ';' or ',' but get {List[i].Token_Value} in Line no {List[i-1].Line_No}")
        sys.exit()
def MDM(): 
    global i  
    if(List[i].Token_Class =="MDM"):
        i=i+1
        return True 
    else:
           return False 
def I_C_B():  
    global i 
    if(ID()==True):
        if List[i].Token_Value=="(":
            name = List[i-1].Token_Value
            con_type = A3('func')
            check=lookUpFuncST(name,con_type)
            print(check)
            if(check==True):
                    print(f"Error In Line No {List[i].Line_No}: Function {name} is not defined")
                    sys.exit()
                    
            else:
                print("Ahsaan")
                if List[i].Token_Class ==";":
                    return check,name
            

        else:    
            name = List[i-1].Token_Value
            dt = lookUpScopeTable(name)
            if (dt==True):
                print(f"{name} is not declared in line no {List[i].Line_No}")
                sys.exit()
            else:
                print("Exp ID",name)
                print(dt)
                final_dt=A3(dt)
                print(final_dt,"LOOK AT ME")
                if(final_dt):
                    return final_dt ,name
    elif(Constant()==True):
        con_type = List[i-1].Token_Class
        con_name = List[i-1].Token_Value
        return con_type,con_name
    
    elif (List[i].Token_Class == "("):
        i=i+1
        dt = Expr()
        print(dt)
        if (dt):
            if (List[i].Token_Class == ")") :
                i=i+1
                return dt,'umer'
            else:
                print ("Expected ) but found ",List[i].Token_Class)
                sys.exit()
        else:
            print ("Error in expression")
            sys.exit()
    else:
        print(f"Expecting Operator or ']' or ')' or ';' or ',' but get {List[i].Token_Value} in Line no {List[i-1].Line_No}")
        sys.exit()
def Constant(): 
    global i
    if(List[i].Token_Class=="int_const" or List[i].Token_Class=="fpoint_const" or List[i].Token_Class=="str_const"):
        i=i+1
        print(List[i].Token_Class,"HIS")
        return True
    else:
        return False 
    
def Else_Stat():
    global i   
    if(List[i].Token_Class=="except"):
        i=i+1
        if(Body()==True):
            return True
    elif(List[i].Token_Class==";"):
        return True
    else:
        return False 
    
def Para_Init():
    print("Here") 
    global i  
    if(DT()==True):
        dt = List[i-1].Token_Value
        if(ID()==True):
            name = List[i-1].Token_Value
            insertScopeTable(name,dt,currentScope)
            T=dt
            TT=(Para_Init_List(T))
            if (TT):
                print(TT,"PARA_INIT()")
                return TT
            else:
                print (f"Expected , or ; but found {List[i].Token_Value}({List[i].Token_Class}) in Line no {List[i].Line_No}")
                sys.exit()
    elif(List[i].Token_Class==")"):
        return 'void'
    else:
           return False  

def Func_Body():
    global i
    global body_type
    body_type= "Function" 
    if(Body()==True):
        return True
    elif(List[i].Token_Class==";"):
        return True
    else:
           return False

def Para_Init_List(T):  
    global i 
    if(List[i].Token_Class==","):
        T = T+","
        i=i+1
        if(DT()==True):
            dt = List[i-1].Token_Value
            if(ID()==True):
                name = List[i-1].Token_Value
                insertScopeTable(name,dt,currentScope)
                T=T+dt
                final_dt  = Para_Init_List(T)
                if(final_dt):
                    print(final_dt,"PARA_INIT_LIST")
                    return final_dt
    elif(List[i].Token_Class=="AOP"):
        i=i+1
        if(Para_Init_Value()==True):
            return True
    elif(List[i].Token_Class==")"):
        return T
    else:
           return False
def Para_Init_Value():
    global i   
    if(Constant()==True):
        if(Para_Init_List2()==True):
            return True
    else:
           return False
    
def Para_Init_List2():   
    global i
    if(List[i].Token_Class==","):
        i=i+1
        if(DT()==True):
            if(ID()==True):
                if(Para_Init_List()==True):
                    return True
    elif(List[i].Token_Class==")"):
        return True
    
    else:
           return False
    
def Operators(): 
    global i  
    if(List[i].Token_Class=="PM"):
        i=i+1
        return True
    if(List[i].Token_Class=="MDM"):
        i=i+1
        return True
    if(List[i].Token_Class=="ROP"):
        i=i+1
        return True
    if(List[i].Token_Class=="AOP"):
        i=i+1
        return True
    
    else:
        return False
def Return_Body():
    global i
    global return_type
    dt = Expr()
    return_type = dt 
    if(dt):
        final_dt=Return_Body1(dt)
        if (final_dt):
            return dt
    else:
        return False # For Null
def Return_Body1(dt):  
    global i
    if(List[i].Token_Class=="("):
        i=i+1
        if(Arg_List()==True):
            if(List[i].Token_Class==")"):
                return True
    elif(List[i].Token_Class=="["):
        i=i+1
        if(Expr()==True):
            if(List[i].Token_Class=="]"):
                i=i+1
                if(Return_Body2()==True):
                    return True
            else:
                print(f"Error in Line No {List[i].Line_No}: Missing ']'")
                sys.exit()
    elif(List[i].Token_Class==";"):
        return dt
    else:
        return False
def Return_Body2():
    global i
    if(List[i].Token_Class=="["):
        i=i+1
        if(Expr()==True):
            if(List[i].Token_Class=="]"):
                i=i+1

                if(Return_Body2()==True):
                    return True
            
            else:
                print(f"Error in Line No {List[i].Line_No}: Missing ']'")
                sys.exit()
    elif(List[i].Token_Class==";"):
        i=i+1
        return True
    else:
           return False
    
    
def Struct_Stat1(): 
    global i  
    if(List[i].Token_Class=="{"):
        i=i+1
        if(Struct_Body()==True):
            if(List[i].Token_Class=="}"):
                i=i+1
                return True
    elif(ID()==True):
        if(Struct_List()==True):
            return True
    else:
           return False
def Struct_Body():
    global i
    global CCN
    if(DT()==True):
        dt=List[i-1].Token_Value
        
        if(ID()==True):
            name=List[i-1].Token_Value
            insertMemTable(name,dt,'public','-',0,CCN)
            con_type = Struct_Body_List(dt)
            if(con_type):
                if(Struct_Body()==True):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif(List[i].Token_Class=="}"):
        return True
    else:
           return False
  
def Struct_List(): 
    global i  
    if(List[i].Token_Class==";"):
        i=i+1
        return True
    elif(List[i].Token_Class=="AOP"):
        i=i+1
        if(List[i].Token_Class=="{"):
            i=i+1
            if(Arg_List()==True):
                if(List[i].Token_Class=="}"):
                    i=i+1
                    if(List[i].Token_Class==";"):
                        i=i+1
                        return True
    else:
           return False
def Struct_Body_List(DT):   
    global i
    if(List[i].Token_Class=="AOP"):
        operator = List[i].Token_Value
        i=i+1

        if(Constant()==True):
            con_type = List[i-1].Token_Class
            if(compatibiltyCheck(DT,con_type,operator)):
                if(List[i].Token_Class==";"):
                    i=i+1
                    return True
            else:
                print(f"Error in Line No {List[i].Line_No}: {DT} is not compatible with {con_type}")
                sys.exit()
        else:
            return False
    elif(List[i].Token_Class==","):
        i=i+1
        if(ID()==True):
            name = List[i-1].Token_Value
            insertMemTable(name,DT,'public','-',0,CCN)
            con_type = Struct_Body_List(DT)
            if(con_type==True):
                return True
            if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'):
                print(f"you can't assign {con_type} in {name}({DT})")
                sys.exit()
            
    elif(List[i].Token_Class==";"):
        i=i+1
        return True
    else:
           return False
        
            
                       
def Type_Modifier(): 
    global i  
    if(List[i].Token_Class=="abstract"):
        i=i+1
        return 'abstract'
    elif(List[i].Token_Class=="sealed"):
        i=i+1
        return 'sealed'
    elif(List[i].Token_Class in ["class",'acc_mod']) :
        return 'general'
    else:
        return False

       
def Inherit():
    global i
    if(List[i].Token_Class=="inherit"):
        i=i+1
        if(ID()==True):
            return List[i-1].Token_Value
    elif(List[i].Token_Class=="{"):
        return "-"
    else:
        return False   
 
def Class_Main_Body(): 
    global i
    global AccessModefier
    if(List[i].Token_Class=="{"):
        print("{")
        i=i+1
        if(Class_Main_Multiple_Stat()==True):
            if(List[i].Token_Class=="}") and (List[i-1].Token_Class==";" ):
                i=i+1
                if List[i].Token_Class==";":
                    return True
                else:
                    print(f"Error in Line No {List[i-1].Line_No} : Expecting ;")
                    sys.exit()
            elif (List[i-1].Token_Class=="{") and (List[i].Token_Class == "}"):
                i=i+1
                if List[i].Token_Value == ";":
                    return True
                else:
                    print(f"Error in Line No {List[i-1].Line_No} : Expecting ;")
                    sys.exit()
            else:
                return False
        
        else:
            print(f"Error in Line No {List[i].Line_No}: Error in Body Syntax")
            sys.exit()
        
    else:

        print(f"Error in Line No {List[i].Line_No}:" ,"Missing '{' ")

        sys.exit()
        
            

             
             
             
def Acc_Modifier():  
    global i 
    if(List[i].Token_Class=="acc_mod"):
        i=i+1
        return List[i-1].Token_Value
    if (List[i].Token_Value == "class"):
        return 'public'
    else:
        return False 
#def Inherit_Modifier1():   
 #   print("") 
def Class_Body(): 
    global i
    if(List[i].Token_Class=="{"):
        print("Class{")
        i=i+1
        if(Class_Multiple_Stat()==True):
            if(List[i].Token_Class=="}") and (List[i-1].Token_Class==";" ):
                i=i+1
                print("HERE;")

                if List[i].Token_Class==";":
                    return True
                else:
                    print(f"Error in Line No {List[i-1].Line_No} : Expecting ;")
                    sys.exit()
            elif (List[i-1].Token_Class=="{") and (List[i].Token_Class == "}"):
                i=i+1
                if List[i].Token_Value == ";":
                    return True
                else:
                    print(f"Error in Line No {List[i-1].Line_No} : Expecting ;")
                    sys.exit()


            else:
                return False
        else:
            print(f"Error in Line No {List[i].Line_No}: Error in Body Syntax")

            sys.exit()
        
    else:

        print(f"Error in Line No {List[i].Line_No}:" ,"Missing '{' ")

        sys.exit()
        
def Class_Single_Stat(body_type): 
    global i  


    if(Class_While_Stat()==True):
        if List[i].Token_Class ==";":
            i+=1
            return True
        else:
                return False        

    elif(Class_For_Stat()==True):
        if List[i].Token_Class ==";":
            i+=1
            return True
        else:
                return False        

    elif(Class_Func_Stat()==True):
        if List[i].Token_Class ==";":
            i+=1
            return True
        else:
                return False        
    elif (List[i].Token_Value=='return'):
        dt = Class_Return_Stat()

        if(dt):
            if body_type == "Function":
                if List[i].Token_Class ==";":
                    i+=1
                    return True
                else:
                    return False     
            else:
                print(f"You Can Only Use Return Statement in Function")
                sys.exit()


    elif(Class_If_Else_Stat()==True):
        if List[i].Token_Class ==";":
            i+=1
            return True
        else:
                return False        

    if List[i].Token_Class in ['class','acc_mod','abstract','sealed']:
        if(Class_Stat()==True):
            if List[i].Token_Class ==";":
                i+=1
                return True
            else:
                return False        

     
    elif(Inc_Dec_Op()==True):
        if(Ts()==True):
            if(ID()==True):
                if(Class_A1()==True):
                    if(List[i].Token_Class==";"):
                        i=i+1
                        return True
                    else:
                        print(f"Error in Line No {List[i].Token_Value}:Expecting  ';'")
                        sys.exit()
    elif(DT()==True):
        dt=List[i-1].Token_Value
        print(List[i-1].Token_Value)
        if(ID()==True):
            if (List[i].Token_Value == '['):
                name=List[i-1].Token_Value
                print(name,"first")
                #insert(name)
                con_type = Class_A1(dt)
                final_dt = str(dt)+str(con_type)
                if(con_type):
                    insertScopeTable(name,final_dt,currentScope)
                    if List[i].Token_Class ==";":
                        print(List[i].Token_Class,"n")
                        i+=1
                        return True 
                    else:
                        return False
                
                if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'): 
                    print(f"you can't assign {con_type} in {name}({dt})")
                    sys.exit()
                else:
                    return False

            else:
                name=List[i-1].Token_Value
                print(name,"first")
                insertScopeTable(name,dt,currentScope)
                #insert(name)
                con_type = Class_A1(dt)
                if(con_type==True):
                    #   insertScopeTable(name,dt+con_type,currentScope)
                    print(dt,name)
                    print(name,"zero")
                    print(List[i].Token_Class)
                    if List[i].Token_Class ==";":
                        print(List[i].Token_Class,"n")
                        i+=1
                        return True 
                    else:
                        return False
                
                if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'): 
                    print(f"you can't assign {con_type} in {name}({dt})")
                    sys.exit()
                else:
                    return False    
        else:
             return False
         
    
    elif(ID()==True):
        if (List[i].Token_Value=="("):
            con_type = Class_A2('func')
            if(con_type==True):
                    print("Ahsaan")
                    if List[i].Token_Class ==";":
                        i+=1
                        return True
        else:            
            name=List[i-1].Token_Value
            if List[i].Token_Class =='ID':
                name = List[i].Token_Value
                class_type = List[i-1].Token_Value
                check = lookUpDefTable(class_type,'class')
                if(check==True):
                    print(f"Error In Line No {List[i].Line_No}: {class_type} is not defined")
                    sys.exit()

                else:
                    insertScopeTable(name,check,currentScope)
                    con_type = Class_A2(class_type)
                    if(con_type==True):
                        print("Ahsaan")
                        if List[i].Token_Class ==";":
                            i+=1
                            return True

            else:    
                var_type=lookUpScopeTable(name)
                if (var_type==True):
                    print(f"Error in Line No {List[i].Line_No}: Undefined variable '{name}'")
                    sys.exit()
                
                else:
                    con_type = Class_A2(var_type)
                    print(con_type,"HOLA")
                    if(con_type==True):
                        print("Ahsaan")
                        if List[i].Token_Class ==";":
                            i+=1
                            return True
                
                    if((con_type == 'str_const' or con_type == 'str') or (con_type=='int_const' or con_type=='integ') or (con_type=='fpoint_const' or con_type=='fpoint')):
                        print(f"you can't assign {con_type} in {name}({var_type})")
                        sys.exit()
                    else:
                        return False
                    
    if List[i].Token_Value=="this->" or List[i].Token_Value=="super.":
        dt = Ts()
        if (dt):
            print(dt,'AM')
            if(Class_Ts_List(dt)==True):
                print("TS List Done")
                if(List[i].Token_Class==";"):
                    i=i+1
                    return True
                else:
                    print(f"Error in Line No {List[i].Line_No} : Expecting ;")
                    sys.exit()
            else:
                print(f"Error in Line No {List[i-1].Line_No} : Invalid Syntax")
                sys.exit()




        
            
        
    else:
           return False   
              

def Class_Multiple_Stat():   
    global i
    print("Class_Multiple_State")
    if(Class_Single_Stat(body_type)==True):
        if(Class_Multiple_Stat()==True):
            return True 
    elif(List[i].Token_Class=="}"):
        return True
    else:
           return False  
def Class_A2(dt):
    global i
    global AccessModefier
    global CCN
    if(List[i].Token_Class==","):
        i=i+1
        if(ID()==True):
            if(Class_A2(dt)==True):
                return True   
    elif(List[i].Token_Class=="["):
        i=i+1
        if(Class_Expr()==True):
            if(List[i].Token_Class=="]"):
                i=i+1
                if(Class_C()==True):
                    return True
    elif(List[i].Token_Class=="("):
        i=i+1
        if(Class_Arg_List()==True):
            if(List[i].Token_Class==")"):
                i=i+1
                if(Class_B()==True):
                    return True
    elif(List[i].Token_Class=="."):
        i=i+1
        if(ID()==True):
            if(Class_A2()==True):
                return True
    elif(Assign_OP()==True):
        operator = List[i-1].Token_Value
        con_type = Class_Expr()
        if(con_type):
            if(compatibiltyCheck(dt,con_type,operator)):
                if(Class_A4(dt)==True):
                    return True
            else:
                print(con_type,'JOKER')
                return con_type
        else:
            False

    elif(Inc_Dec_Op()==True):
        operator = List[i-1].Token_Value
        if(CompatibilityTest(dt,operator)):
            if(Class_A4(dt)==True):
                return True
        else:
            print(f"{dt} can't be incremented in line no {List[i-1].Line_No}")
            sys.exit()
    elif(ID()==True):
        if(Obj_List()==True):
            return True
    elif(List[i].Token_Class==";"):
        return True
    else:
           return False
    
def Ts():   
    global i
    global CCN
    print()
    if(List[i].Token_Class=="this->"):
            i=i+1
            if(ID()==True):
                name = List[i-1].Token_Value

                dt = lookUpMemTable(name,CCN)
                print(dt)
                if(dt == True):
                    print(f"member ({name}) is not defined")
                    sys.exit()
                if(dt!=True):
                    print(dt,"INSIDE TS()")
                    return dt

            else:
                return False
    elif(List[i].Token_Class=="super."):
        i=i+1
        if(ID()==True):
            if (List[i].Token_Value=="("):
                if(List[i+1].Token_Value==")"):
                    curr_class=CCN
                    name = List[i-1].Token_Value
                    parent = CCR.Parent
                    i=i+1

                    if (parent!='-'):
                        dt=lookUpFuncMT(name,'void',parent)
                        if(dt==True):
                                print(f"Error in Line No {List[i].Line_No}: Member ({name}) not found")
                                sys.exit()
                        else:
                            if (dt=='constructor'):
                                print(f"Error in Line No {List[i].Line_No}: Constructor cannot be called using super.")
                                sys.exit()
                            else:    
                                i=i+1
                                CCN=curr_class
                                return True
                    else:
                        print(f"Error in Line No {List[i].Line_No}: Class ({name}) not found")
                        sys.exit()
                    

                    
                else:
                    curr_class=CCN
                    name = List[i-1].Token_Value
                    parent = CCR.Parent
                    if (parent!='-'):
                        i=i+1
                        DT = Make_Dt("")
                        if (DT):
                            dt=lookUpFuncMT(name,DT,parent)
                            if(dt==True):
                                print(f"Error in Line No {List[i].Line_No}: Member ({name}) not found")
                                sys.exit()
                            else:
                                if (dt=='constructor'):
                                    print(f"Error in Line No {List[i].Line_No}: Constructor cannot be called using super.")
                                    sys.exit()
                                else:    
                                    i=i+1
                                    CCN=curr_class
                                    return True
                    else:
                        print(f"Error in Line No {List[i].Line_No}: Class ({name}) not found")
                        sys.exit()
                    


            else:    
                curr_class=CCN
                name = List[i-1].Token_Value
                parent = CCR.Parent
                if (parent!='-'):
                    dt =lookUpMemTable(name,parent)
                    if(dt==True):
                        print(f"Error in Line No {List[i].Line_No}: Member ({name}) not found")
                        sys.exit()

                        
                    else:
                        CCN=curr_class
                        return True
                else:
                    print(f"Error in Line No {List[i].Line_No}: Class ({name}) not found")
                    sys.exit()
                    

        else:
            return False
        
    else:
        return False
    

def Class_Ts_List(DT):
    global i
    if(List[i].Token_Class==","):
        i=i+1
        if(ID()==True):
            if(Class_A2(DT)==True):
               return True
    elif(List[i].Token_Class=="["):
        i=i+1
        if(Class_Expr()==True):
            if(List[i].Token_Class=="]"):
                i=i+1
                if(Class_Arr_List()==True):
                    return True
    elif(List[i].Token_Class=="("):
        i=i+1
        if(Class_Arg_List()==True):
            if(List[i].Token_Class==")"):
                 i=i+1
                 return True
    elif(Assign_OP()==True):
        Operator = "="
        dt = DT
        final_dt = Class_Expr()

        check = compatibiltyCheck(dt,final_dt,Operator)
        if(check):
            if(Class_A4(DT)==True):
                return True
        else:
            print(f"Error in Line No {List[i].Line_No}: {dt} and {final_dt} are not compatible for assignment operation.")
            sys.exit()
    elif(Inc_Dec_Op()==True):
        dt = DT
        operator = List[i-1].Token_Value
        if(CompatibilityTest(dt,operator)):
            if(Class_A4(DT)==True):
                return True
        else:
            print(f"Error in Line No {List[i].Line_No}: {dt} is not compatible with {operator}")
            sys.exit()

    elif(List[i].Token_Class==";"):
        return True
    else:
        return False

def Class_While_Stat():
    global i
    global body_type
    if body_type == "loop":
        if(List[i].Token_Class=="while"):
            i=i+1
            if(List[i].Token_Class=="("):
                i=i+1
                dt = Class_Expr()
                if(dt):
                    if(List[i].Token_Class==")"):
                        i=i+1
                        createScope()
                        if(Class_Body()==True):
                            body_type='loop'
                            destroyScope()
                            return True
        else:
           return False
    else:
        if(List[i].Token_Class=="while"):
            i=i+1
            if(List[i].Token_Class=="("):
                i=i+1
                dt = Class_Expr()
                if(dt):
                    if(List[i].Token_Class==")"):
                        i=i+1
                        createScope()
                        body_type = 'loop'
                        if(Class_Body()==True):
                            body_type=''
                            destroyScope()
                            return True


def Class_For_Stat():  
    global i 
    global body_type
    if body_type == 'loop':

        if(List[i].Token_Class=="for"):
            i=i+1
            body_type = 'loop'
            createScope()
            if(List[i].Token_Class=="("):
                i=i+1
                if(Class_Init()==True):
                    if(List[i].Token_Class==";"):
                        i=i+1
                        if(Class_Condition()==True):
                            if(List[i].Token_Class==";"):
                                i=i+1
                                if(Class_Inc_Dec_Stat()==True):
                                    if(List[i].Token_Class==")"):
                                        i=i+1
                                        if(Class_Body()==True):
                                            body_type='loop'
                                            destroyScope()
                                            return True
        else:
            return False
    else:
        if(List[i].Token_Class=="for"):
            i=i+1
            body_type = 'loop'
            createScope()
            if(List[i].Token_Class=="("):
                i=i+1
                if(Class_Init()==True):

                    if(List[i].Token_Class==";"):
                        i=i+1
                        if(Class_Condition()==True):
                            if(List[i].Token_Class==";"):

                                i=i+1
                                if(Class_Inc_Dec_Stat()==True):
                                    print(List[i].Token_Value,"JADOOO")
                                    if(List[i].Token_Class==")"):
                                        i=i+1
                                        if(Class_Body()==True):
                                            print("IGI")    
                                            print(Stack[0],"BEFORE")
                                            body_type=''
                                            destroyScope()
                                            print(Stack[0],"AFTER")
                                            return True
        else:
            return False
        

def Class_Func_Stat():  
    global i
    if(List[i].Token_Class=="def"):

        i=i+1
        if(Class_Func_Stat1()==True):
            return True 
        else:
            
            return False
    else:
         return False


  

def Class_Return_Stat():
    global i   
    if(List[i].Token_Class=="return"):
        i=i+1
        dt = Class_Return_Body()
        if(dt):
            return dt
        else:
           return False
        




    
def Class_Main_Multiple_Stat():   
    global i
    if(Class_Main_Single_Stat()==True):
        if(Class_Main_Multiple_Stat()==True):
            return True
    elif(List[i].Token_Class=="}"):
        return True
    else:
        return False
def Class_A1(dt):  
    global i 
    if(List[i].Token_Class==","):
        i=i+1
        if(ID()==True):
            name = List[i-1].Token_Value
            insertMemTable(name,dt,AccessModefier,'-',0,CCN)
            con_type= Class_A1(dt)
            if(con_type==True):
                return True
            if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'):
                print(f"you can't assign {con_type} in {name}({dt})")
                sys.exit()
            else:
                return False
        else:
            print(f"Expecting ID But Getting {List[i].Token_Value}")
            sys.exit()
            
    elif(List[i].Token_Class=="["):
        DT =""
        DT = dt+'['
        i=i+1
        T = Class_Expr()
        if(T == 'integ' or T=='int_const'):
            if(List[i].Token_Class=="]"):
                DT = DT +"]"                
                i=i+1
                if List[i].Token_Class=="[":
                    final_dt=Class_Arr_Assign(DT) 
                    if(final_dt):
                        print(final_dt)
                        return final_dt
                if List[i].Token_Class==";":
                    print("GOJO",DT)
                    return DT
        else:
            print("invalid array index type")
            sys.exit()
                    
    elif(List[i].Token_Class=="("):
        i=i+1
        if(Class_Arg_List()==True):
            if(List[i].Token_Class==")"):
                i=i+1
                return True
    elif(List[i].Token_Class=="."):
        i=i+1
        if(ID()==True):
            if(Class_A1()==True):
                return True
            
    elif(Assign_OP()==True):
        operator = List[i-1].Token_Value
        value = List[i].Token_Value
        con_type=Class_Expr()
        print(con_type,"OPERAitOIN")
        if(con_type):
            print("HEre")
            # result = compatibiltyCheck(dt,con_type,operator)
            if(compatibiltyCheck(dt,con_type,operator)):
                if(Class_A4(dt)==True):
                    return True
            else:
                return con_type
        else:
            return False
        
            
    elif(Inc_Dec_Op()==True):
        if(Class_A4(dt='ido')==True):
            return True
    elif(List[i].Token_Class in [")",";"]):
        return True
    else:
        print(f"Error in Line No {List[i].Line_No}: Expecting ';' or ')' but getting '{List[i].Token_Value}' ")
        sys.exit()
def Class_Main_Single_Stat(): 

    global i
    global AccessModefier
    global CCN  
    global def_type
    print("Class_Main_Single_State")

    if(Constructor()==True):
        if(List[i].Token_Class==";"):
             i=i+1
             return True
    elif(Access_Modifier()==True):
        return True
    elif(Class_Func_Stat()==True):
        if(List[i].Token_Class==";"):
             i=i+1
             return True
    
    elif(Class_While_Stat()==True):
        if List[i].Token_Class ==";":
            i+=1
            return True
        else:
            return False        

    elif(Class_For_Stat()==True):
        if List[i].Token_Class ==";":
            i+=1
            return True
        else:
             return False          

    elif(Class_If_Else_Stat()==True):
        if List[i].Token_Class ==";":
            i+=1
            return True
        else:
             return False          


    elif(DT()==True):
        dt=List[i-1].Token_Value
        print(List[i-1].Token_Value)
        if(ID()==True):
            if (List[i].Token_Value == '['):
                name=List[i-1].Token_Value
                print(name,"first")
                #insert(name)
                con_type = Class_A1(dt)
                final_dt = str(dt)+str(con_type)
                if(con_type):
                    insertMemTable(name,final_dt,AccessModefier,'-',0,CCN)
                    if List[i].Token_Class ==";":
                        print(List[i].Token_Class,"n")
                        i+=1
                        return True 
                    else:
                        return False
                
                if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'): 
                    print(f"you can't assign {con_type} in {name}({dt})")
                    sys.exit()
                else:
                    return False

            else:
                name=List[i-1].Token_Value
                print(name,"first")
                insertMemTable(name,dt,AccessModefier,'-',0,CCN)

                #insert(name)
                con_type = Class_A1(dt)
                if(con_type==True):
                    #   insertScopeTable(name,dt+con_type,currentScope)
                    print(dt,name)
                    print(name,"zero")
                    print(List[i].Token_Class)
                    if List[i].Token_Class ==";":
                        print(List[i].Token_Class,"n")
                        i+=1
                        return True 
                    else:
                        return False
                
                if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'): 
                    print(f"you can't assign {con_type} in {name}({dt})")
                    sys.exit()
                else:
                    return False    
        else:
             return False
         
    elif(ID()==True):
        name = List[i-1].Token_Value
        if List[i].Token_Class =='ID':
                name = List[i].Token_Value
                class_type = List[i-1].Token_Value
                curr_clss= lookUpDefTable(CCN,def_type)
                check = lookUpDefTable(class_type,def_type)
                if(check==False):
                    print(f"Error In Line No {List[i].Line_No}: class/structure {class_type} is not defined")
                    sys.exit()

                else:
                    type_mod = check.Type_Mod
                    parent = curr_clss.Parent
                    print(parent,"PARENT")
                    print(CCN,"CHILD")
                    if type_mod == 'abstract':
                        print(f"Error in Line No {List[i].Line_No}:can't create object of abstract class {class_type}")
                        
                        sys.exit()
                    else:
                        if parent ==check.Name:
                
                            insertMemTable(name,class_type,AccessModefier,type_mod,0,CCN)
                            con_type = A2(class_type)
                            if(con_type==True):
                                print("Ahsaan")
                                if List[i].Token_Class ==";":
                                    i+=1
                                    return True
                        print(f"Error in Line No {List[i].Line_No}: Can't Make Object of class {class_type} because {class_type} is not inherited by {curr_clss.Name}")
                        sys.exit()

        else:
            dt=lookUpMemTable(name,CCN)
            if (dt):
                if(Class_Ts_List(dt)==True):
                    if(List[i].Token_Class==";"):
                        i=i+1
                        return True



    if List[i].Token_Class in ['class','acc_mod','abstract','sealed']:
            
        if(Class_Stat()):
            if(List[i].Token_Class==";"):
                i=i+1
            return True
        
    elif(Access_Modifier()==True):
        return True
    else:
           return False


def Constructor():   
    global i
    if(List[i].Token_Class=="construct"):
        t1 = 'constructor'
        i=i+1
        if(ID()==True):
            name = List[i-1].Token_Value
            if CCN==name:
                createScope()
                if(List[i].Token_Class=="("):
                    i=i+1
                    T=Class_Para_Init()
                    if(T):
                        if(List[i].Token_Class==")"):
                            para_type = str(T) + "->"+ str(t1)
                            print(para_type,"UIIOERP")
                            i=i+1
                            insertMemTable(name,para_type,'public','static',0,CCN)
                            if(Class_Body()==True):
                                print("CLASSS BODYYY")
                                destroyScope()
                                return True
                            else: 
                                print(f"Constructor Body Not Found")
                                sys.exit()
                    else:
                        print("You can't make constructor of different class name")
                else:
                    print(f"Error in Line No{List[i].Line_No}:Expecting '(' but getting {List[i].Token_Value}")
                    sys.exit()
            else:
                print(f"{name} is not a valid Class Name")
                sys.exit()
                    
    else:
        return False
def Access_Modifier(): 
    global i
    global AccessModefier
    Acc= Acc_Modifier()
    print(Acc,"LANGrAYY")  
    if(Acc):
        if(List[i].Token_Class==":"):
            i=i+1
            AccessModefier = Acc
            return True
    else:
           print("Access Modifier False")
           return False
   
def Class_Func_Stat1():   
    global i
    global body_type
    global return_type
    global AccessModefier
    global CCN
    global CCR
    print("Class_func")
    print("HOOOLA",List[i-1].Token_Value)

    
    
    if(List[i].Token_Class=="virtual"):
        i=i+1
        TM = "virtual" 
        if(List[i].Token_Class == "dtype" or List[i].Token_Class=="ID"):
            rtype = List[i].Token_Value
            i=i+1
        
            if(ID()==True):
                name = List[i-1].Token_Value
                createScope()
                if(List[i].Token_Class=="("):
                    i=i+1
                    T=Class_Para_Init()
                    if(T):
                        T=T+'->'+rtype
                        print(T,name,CCN,"KING")
                        insertMemTable(name,T,AccessModefier,TM,0,CCN)
                        if(List[i].Token_Class==")"):
                            print(")")
                            i=i+1
                            if(Class_Func_Body()==True):
                                if return_type=="":
                                    if(List[i].Token_Class==";"):
                                        body_type=""
                                        destroyScope()
                                        return True
                                elif (return_type==rtype):
                                    if (List[i].Token_Class==";"):
                                        body_type=""
                                        destroyScope()
                                        return True
                                else:
                                    print (f"Expecting return type {rtype}, Having {return_type}")
                                    sys.exit()

                                    
                    else:
                        print("Error in function declaration")
                        sys.exit()
                        
                                    
                                
                            
        
    elif(List[i].Token_Value=="static"):
        i=i+1
        TM = "static" 
        if(List[i].Token_Class == "dtype" or List[i].Token_Class=="ID"):
            rtype = List[i].Token_Value
            i=i+1
            if(ID()==True):
                name = List[i-1].Token_Value
                print(name,"KILL")
                createScope()
                if(List[i].Token_Class=="("):
                    i=i+1
                    T=Class_Para_Init()
                    if(T):
                        T=T+'->'+rtype
                        print(T,"YEH RAHA T")
                        insertMemTable(name,T,AccessModefier,TM,0,CCN)
                        if(List[i].Token_Class==")"):
                            print(")")
                            i=i+1
                            if(Class_Func_Body()==True):
                                if return_type=="":
                                    if(List[i].Token_Class==";"):
                                        body_type=""
                                        destroyScope()
                                        return True
                                elif (return_type==rtype):
                                    if (List[i].Token_Class==";"):
                                        body_type=""
                                        destroyScope()
                                        return True
                                else:
                                    print (f"Expecting return type {rtype}, Having {return_type}")
                                    sys.exit()

                                    
                    else:
                        print("Error in function declaration")
                        sys.exit()
                            
                               
    elif(List[i].Token_Class=="friend"):
        i=i+1
        if(ID()==True):
            name= List[i-1].Token_Value
            if name == CCN:
                if(List[i].Token_Class=="operator"):
                    i=i+1
                    if(Operators()==True):
                        operator=List[i-1].Token_Value 
                        print(List[i].Token_Class)
                        insertFriendTable(name,operator)
                        createScope()
                        if(List[i].Token_Class=="("):

                            i=i+1
                            T = Class_Para_Init()
                            if(T):
                                print(List[i].Token_Value,"THERE")

                                if(List[i].Token_Class==")"):
                                    i=i+1
                                    if(Class_Func_Body()==True):
                                        destroyScope
                                        return True
        
    elif(List[i].Token_Class == "dtype" or List[i].Token_Class=="ID"):
            rtype=List[i].Token_Value
            i=i+1
            if(ID()==True):
                
                name = List[i-1].Token_Value
                createScope()
                if(List[i].Token_Class=="("):
                    i=i+1
                    T=Class_Para_Init()
                    if(T):
                        T=T+'->'+rtype
                        if(List[i].Token_Class==")"):
                            i=i+1
                            TM = Class_Func_Stat2()
                            if TM == 'override':

                                curr_class=lookUpDefTable(CCN,'class')

                                parent =curr_class.Parent
                                print(T,name,CCN,TM,parent,"QUEEN")

            
                                mem=lookUpFuncMT(name,T,parent)
                                if(mem!=True):
                                    CCN=curr_class.Name

                                    print("DEKHOOO")
                                    if (mem.Type_Mod == 'virtual'):
                                        insertMemTable(name,T,AccessModefier,TM,0,CCN)
                                        if(TM):
                                            if(Class_Func_Body()==True):
                                                if return_type=="":
                                                    if(List[i].Token_Class==";"):
                                                        body_type=""
                                                        destroyScope()
                                                        return True
                                                elif (return_type==rtype):
                                                    if (List[i].Token_Class==";"):
                                                        body_type=""
                                                        destroyScope()
                                                        return True
                                                else:
                                                    print (f"Expecting return type {rtype}, Having {return_type}")                    
                                                    sys.exit()
                                        else:
                                            print("INSIDE OVERIDE")
                                            return False
                                        
                                    else:
                                        print(f"Error in Line No {List[i].Line_No}:Cannot use override ")
                                        sys.exit()
                            if TM == '-':
                                        print(name,T,AccessModefier,TM,0,CCN,"FUNCTION")
                                        insertMemTable(name,T,AccessModefier,TM,0,CCN)
                                        if(TM):
                                            if(Class_Func_Body()==True):
                                                if return_type=="":
                                                    if(List[i].Token_Class==";"):
                                                        body_type=""
                                                        destroyScope()
                                                        return True
                                                elif (return_type==rtype):
                                                    if (List[i].Token_Class==";"):
                                                        body_type=""
                                                        destroyScope()
                                                        return True
                                                else:
                                                    print (f"Expecting return type {rtype}, Having {return_type}")                    
                                                    sys.exit()
                                            else:
                                                print("INSIDE OVERIDE")
                                                return False





                    
                    
                    else:
                        print("Error in function declaration")
                        sys.exit()
    else:
           return False
def Class_Para_Init_Obj_List():
    if(List[i].Token_Class==","):
        i=i+1
        if(ID()==True):
            if(ID()==True):
                if(Class_Para_Init_Obj_List()==True):
                    return True
    elif(List[i].Token_Class==")"):
        return True
    else:
        return False                                       
def Class_Para_Init():  
     global i 
     if(DT()==True):
        dt = List[i-1].Token_Value
        if(ID()==True):
            name = List[i-1].Token_Value
            insertScopeTable(name,dt,currentScope)
            T=dt
            TT = Class_Para_Init_List(T)

            if(TT):
                return TT
            else:
                print (f"Expected , or ; but found {List[i].Token_Value}({List[i].Token_Class}) in Line no {List[i].Line_No}")
                sys.exit()
     elif(ID()==True):
         if(ID()==True):
             if(Class_Para_Init_Obj_List()==True):
                 return True  
     elif(List[i].Token_Class==")"):
        return 'void'
     else:
           return False

def Class_Func_Body():
    global i
    global body_type
    body_type = "Function"   
    print(List[i].Token_Class,"Class_Func_body")
    if(Class_Body()==True):
        return True
    elif(List[i].Token_Class==";"):
        return True
    else:
           return False
def Class_Func_Stat2():   
    global i
    if(List[i].Token_Class=="override"):
        i=i+1
        return 'override'
    
    elif(List[i].Token_Class==";" or List[i].Token_Class == "{"):
        return "-"
    
    else:
        return False

def Class_Para_Init_List(T): 
    global i 
    if(List[i].Token_Class==","):
        T = T + ","
        i=i+1 
        if(DT()==True):
            dt = List[i-1].Token_Value
            if(ID()==True):
                name = List[i-1].Token_Value
                insertScopeTable(name,dt,currentScope)
                T = T + dt
                final_dt = Class_Para_Init_List(T)
                if(final_dt):
                    return final_dt
    elif(List[i].Token_Class==")"):
        return T
    else:
        return False
def Class_Para_Init_Value(): 
    global i
    if(Constant()==True):
        if(Class_Para_Init_List2()==True):
            return True  
    else:
           return False
def Class_Para_Init_List2():  
    global i 
    if(List[i].Token_Class==","):
        i=i+1
        if(DT()==True):
            if(ID()==True):
                if(Para_Init_List()==True):
                    return True
    elif(List[i].Token_Class==")"):
        return True
    else:
           return False


    
def Class_Return_Body():   
    global i
    global return_type
    dt = Class_Expr()
    return_type = dt
    if(dt):
        final_dt = Class_Return_Body1(dt)
        if(final_dt):
            return dt
    else:
           return False
def Class_Return_Body1(dt):
    global i   
    if(List[i].Token_Class=="("):
        i=i+1
        if(Class_Arg_List()==True):
            if(List[i].Token_Class==")"):
                i=i+1
                return True
    elif(List[i].Token_Class=="["):
        i=i+1
        if(Class_Expr()==True):
            if(List[i].Token_Class=="]"):
                i=i+1
                if(Class_Return_Body2()==True):
                    return True
    elif(List[i].Token_Class==";"):
        return dt
    
    else:
           return False
def Class_Return_Body2():
    global i
    if(List[i].Token_Class=="["):
        i=i+1
        if(Class_Expr()==True):
            if(List[i].Token_Class=="]"):
                i=i+1
                if(Class_Return_Body2()==True):
                    return True
    elif(List[i].Token_Class==";"):
        i=i+1
        return True
    else:
           return False
    

def Class_Expr(): 
    global i
    final_dt,final_name=Class_OR_Expr()  
    if(final_dt):
    
        return final_dt
    else:
        return False
    
def Class_Init():   
    global i
    if(DT()==True):
        dt= List[i-1].Token_Value
        
        if(ID()==True):
            name = List[i-1].Token_Value
            insertScopeTable(name,dt,currentScope)
            con_type = Class_A2(dt)
            if(con_type==True):
                return True
            if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'):
                print(f"you can't assign {con_type} in {name}({dt})")
                sys.exit()
    elif (List[i].Token_Class == "ID") or (List[i].Token_Class == "this->"):
            if (List[i].Token_Class == "this->"):
                name = List[i+1].Token_Value
                dt = lookUpMemTable(name,CCN)
                if dt == True:
                    print(f"{name} is not initialized")
                    sys.exit()
                else:
                    con_type = Class_A1(dt)
                    if(con_type==True):
                        return True
                    else:
                        print(f"{name}({dt}) is not compatible with {con_type}")
                        sys.exit()

            else:
                name = List[i-1].Token_Value
                dt=lookUpScopeTable(name)
                if dt == True:
                    print(f"{name} is not initialized")
                    sys.exit()
                else:
                    con_type = Class_A1(dt)
                    if(con_type==True):
                        return True
                    else:
                        print(f"{name}({dt}) is not compatible with {con_type}")
                        sys.exit()

    elif(List[i].Token_Class==";"):
        return True
    else:
           return False
def Class_Condition():  
    global i 

    if(List[i].Token_Class==";"):
        return True

    elif(Class_Expr()==False):
        return True
    
    else:
        return False 

def Class_Inc_Dec_Stat(): 
    global i
    if ((List[i].Token_Class=='ID') or (List[i].Token_Class=='this->')) :
        if List[i].Token_Class=='this->':
            name = List[i+1].Token_Value
            dt = lookUpMemTable(name,CCN)
            if dt == 'str':
                print(f"{name} ({dt}) can't be increment")
                sys.exit()
            if (dt!=True):
                con_type = Class_A1(dt)
                if(con_type==True):
                    return True
            else:
                print(f"{name} is not initilized")
                sys.exit() 
        
        else:
            name = List[i].Token_Value
            dt = lookUpScopeTable(name)

        if dt == 'str':
            print(f"{name} ({dt}) can't be increment")
            sys.exit()
        if (dt!=True):
            con_type = Class_A1(dt)
            if(con_type==True):
                    return True 
            
        else:
            print(f"{name} is not initilized")
            sys.exit()
        

    elif(Inc_Dec_Op()==True):
        if(Ts()==True):
            if(ID()==True):
                return True
    elif(List[i].Token_Class==")"):
        return True
    else:
           return False
            
def Class_C(): 
    global i 
    if(List[i].Token_Class=="."):
        i=i+1
        if(ID()==True):
            if(Class_A1()==True):
                return True
    elif(List[i].Token_Class=="AOP"):
        i=i+1
        if(Class_Expr()==True):
            return True
    elif(List[i].Token_Class==";"):
        return True
    else:
           return False 
def Class_Arr_List():  
    global i 
    if(List[i].Token_Class=="["):
        i=i+1
        if(Class_Expr()==True):
            if(List[i].Token_Class=="]"):
                i=i+1
                if(Class_Arr_List()==True):
                    return True
    elif(List[i].Token_Class in["this->","super.","MDM","PM","ROP","LOP","]",")",";",","]):
        return True
    else:
           return False
def Class_B():   
    global i
    if(List[i].Token_Class=="."):
           i=i+1
           if(ID()==True):
               if(Class_A2()==True):
                   return True
    elif(List[i].Token_Class in["this->","super.","MDM","PM","ROP","LOP","]",")",";",","]):
          return True
    else:
        return False
    
def Class_Arg_List(): 
    global i  
    if(Class_Expr()==True):
            if(Class_A()==True):
                return True
            else:
                return False
    elif(List[i].Token_Class in[")"]):
        i=i+1
        return True
    else:
           return False 
def Class_Arr_Assign(DT):
    global i   

    if(List[i].Token_Class=="["):
        DT=DT+'['
        i=i+1
        T = Class_Expr()

        if(T=='integ' or T == 'int_const'):
            if(List[i].Token_Class=="]"):
                DT=DT+']'
                i=i+1
                final_dt=Class_Arr_Assign(DT)
                if(final_dt):
                    return final_dt
        else:
            print("invalid array index type")
            sys.exit()
    elif(List[i].Token_Class=="AOP"):
        i=i+1
        if(Class_Array_List1(DT)==True):
            return True 
    elif(List[i].Token_Class in[";"]):
        return True
    else:
           return False
def Class_A3():   
    global i
    if(Inc_Dec_Op()==True):
            return True
    elif(List[i].Token_Class == "("):
        i=i+1
        dt=Class_Arg_List("")
        if(dt):
            if(List[i].Token_Class==")"):
                i=i+1
                if(Class_B()==True):
                    return dt

        
    elif(Class_Arr_List()==True):
        if(Class_B()==True):
            return True
    elif(List[i].Token_Class in["this->","super.","MDM","PM","ROP","LOP","]",")",";",","]):
        return True
    else:
           return False
def Obj_Arg():
    if(Expr()==True):
        if(Class_Obj_List2()==True):
            return True
    elif(List[i].Token_Class==")"):
        return True
    
def Class_Obj_List(): 
    global i  
    if(List[i].Token_Class==","):
            i=i+1
            if(ID()==True):
                if(Class_Obj_List()==True):
                    return True
                else:
                    return False
            else:
                return False
    elif(List[i].Token_Class=="("):
        i=i+1
        if(Obj_Arg()==True):
            if(List[i].Token_Class==")"):
                i=i+1
                if(Class_Obj_List1()==True):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif(List[i].Token_Class in[")",";"]):
        return True

    else:
        return False
def Class_Obj_List1(): 
    global i  
    if(List[i].Token_Class==","):
        i=i+1
        if(ID()==True):
            if(Class_Obj_List()==True):
                return True
            else:
                return False
        else:
            return False
    elif(List[i].Token_Class in[")",";"]):
        return True
    else:
           return False
def Class_Obj_List2():   
    if(List[i].Token_Class==","):
        i=i+1
        if(Class_Expr()==True):
            if(Class_Obj_List2()==True):
                return True
            else:
                return False
        else:
            return False
    elif(List[i].Token_Class in[")"]):
        return True
    else:
           return False

def Class_A4(dt):
    global i
    if(List[i].Token_Class==","):
        i=i+1
        if(ID()==True):
            if dt == 'ido':
                name=List[i-1].Token_Value
                type=lookUpScopeTable(name)
                if (type == True):
                    print(f"{name} in not initialized")
                    sys.exit()
                else:
                    if dt == 'str':
                        print(f"{name} ({dt}) can't be increment")
                        sys.exit()
                    if (dt!=True):
                        con_type = A1(dt)
                        if(con_type==True):
                            return True
            
            else:
                name=List[i-1].Token_Value
                insertScopeTable(name,dt,currentScope)
                print(name)
                con_type = A1(dt)
                if(con_type==True):
                    return True
                if(con_type == 'str_const' or con_type=='int_const' or con_type=='fpoint_const'): 
                    print(f"you can't assign {con_type} in {name}({dt})")
                    sys.exit()
                else:
                    return False
    elif(List[i].Token_Class in[")",";"]):
        return True
    else:
        return False
def Class_Array_List1(DT):  
    global i  

    if(List[i].Token_Class=="["):
        i=i+1
        print(DT,"so true")

        final_dt=Class_Array(DT)

        if(final_dt):
            final_dt = Class_Array_Cont(final_dt)
            if((final_dt)):
                if(List[i].Token_Class=="]"):
                    i=i+1
                    return final_dt
    elif(Class_Expr()==True):
        return True
    else:
           return False
def Class_Array(DT): 
    global i
    print(DT,"BANANANA")
    if List[i].Token_Class in ['ID','int_const','str_const','fpoint_const']:
        stripped = DT.strip('[]')
        T =Class_Expr()
        print("SATURO",DT)
        if(T):
            if (compatibiltyCheck(stripped,T,'=')):
                return DT
            
            else:
                print(f"Error In Line No {List[i].Line_No}:You can't assign {T} in {DT} array")
                sys.exit()


    elif(List[i].Token_Class=="["):
        i=i+1
        dt = Class_Elements(DT)
        if(dt):
            if(List[i].Token_Class=="]"):
                i=i+1
                return dt
    else:
           return False
def Class_Array_Cont(DT):
     global i   
     if(List[i].Token_Class==","):
        i=i+1
        print(List[i].Token_Class)
        final_dt = Class_Array_Cont1(DT)
        if(final_dt):
            return final_dt
        
     elif(List[i].Token_Class in["]"]):
           return DT
     else:
           return False
     

def Class_Array_Cont1(DT):
    global i
    if(List[i].Token_Class=="["):
        i=i+1
        dt = Class_Elements(DT)
        if(dt):
            if(List[i].Token_Class=="]"):
                i=i+1
                dt =Class_Array_Cont(DT) 
                if (dt):
                    return DT
    elif List[i].Token_Class in ['ID','int_const','str_const','fpoint_const']:
        stripped = DT.strip('[]')
        T =Class_Expr()
        print("SATURO",DT)
        if(T):
            if (compatibiltyCheck(stripped,T,'=')):
                final_dt=Class_Array_Cont(DT)
                return final_dt
            
            else:
                print(f"Error In Line No {List[i].Line_No}:You can't assign {T} in {DT} array")
                sys.exit()
    else:
        return False
def Class_Elements(DT):
    global i   
    dt = Class_Array(DT)
    if(dt):
        dt=(Class_Elements1(DT))
        if(dt):
            return DT
    else:
           return False


def Class_Elements1(DT):   
    global i
    if(List[i].Token_Class==","):
        i=i+1
        dt = Class_Elements(DT)
        if(dt):
            return DT
    elif(List[i].Token_Class in["]"]):
        return True
    else:
           return False  

def Class_A():   
    global i
    if(List[i].Token_Class==","):
        i=i+1
        if(Class_Arg_List()==True):
            return True
        else:
            return False
    elif(List[i].Token_Class in[")"]):
        return True
    else:
           return False
def Class_If_Else_Stat():   
     global i
     if(List[i].Token_Class=="provide"):
        i=i+1
        if(List[i].Token_Class=="("):
            i=i+1
            dt = Class_Expr()
            if(dt):
                if(List[i].Token_Class==")"):
                    i=i+1
                    createScope()
                    if(Class_Body()==True):
                        if(Class_Else_Stat()==True):
                            destroyScope()
                            return True
     else:
           return False


def Class_Else_Stat(): 
    global i  
    if(List[i].Token_Class=="except"):
        i=i+1
        if(Class_Body()==True):
            return True
    elif(List[i].Token_Class in[";"]):
        return True
    else:
           return False#for NULL
    
     
def Class_OR_Expr():
    global i  
    dt,dt_name = Class_AND_Expr() 
    if(dt):
        final_dt,final_name = Class_OR_Expr1(dt,dt_name)
        if(final_dt):
            return final_dt,final_name
    else:
           return False
def Class_AND_Expr():   
    global i
    dt,dt_name =Class_RO_Expr()
    if (dt):
        final_dt,final_name=Class_AND_Expr1(dt,dt_name)
        if (final_dt):
            return final_dt,final_name
        
    else:
           return False
def Class_OR_Expr1(dt,name):
    global i   
    if(List[i].Token_Class=="LOP"):
        i=i+1
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No
        dt2,dt_name = Class_AND_Expr()

        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = Class_OR_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
                else:
                    print(f"{name} ({dt})  can't {operator} with {dt_name} ({dt2}) in line no {line_no}")
                    sys.exit()
                
    elif(List[i].Token_Class in["ROP","LOP","]",")",";",","]):
        return dt,name
    else:
           return False 
def Class_RO_Expr():
    global i   
    dt,dt_name = Class_PM_Expr()
    if (dt):
        final_dt,final_name = Class_RO_Expr1(dt,dt_name)
        if (final_dt):
            return final_dt,final_name
    else:
        return False

def Class_AND_Expr1(dt,name):  
    global i 
    if(List[i].Token_Class=="LOP"):
        i=i+1
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No

        dt2,dt_name = Class_RO_Expr()
        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = Class_AND_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
    elif(List[i].Token_Class in["ROP","LOP","]",")",";",","]):
        return dt,name
    else:
           return False
def Class_PM_Expr(): 
    global i     
    dt,dt_name =Class_MDM_Expr()
    if(dt):
        final_dt,final_name=Class_PM_Expr1(dt,dt_name)
        if(final_dt):
            return final_dt,final_name
    else:
        return False
def Class_RO_Expr1(dt,name):
    global i   
    if(RO()==True):
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No

        dt2,dt_name = Class_PM_Expr()
        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = Class_RO_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
            else:
                print(f"{name} ({dt})  can't {operator} with {dt_name} ({dt2}) in line no {line_no}")
                sys.exit()
                
    elif(List[i].Token_Class in ["ROP","LOP","]",")",";",","]):
        return dt,name
    else:
           return False
def Class_MDM_Expr(): 
    global i
    dt,dt_name =Class_I_C_B()
    if(dt):
        final_dt,final_name=Class_MDM_Expr1(dt,dt_name)
        if(final_dt):
            return final_dt,final_name
    else:
        return False
def Class_PM_Expr1(dt,name): 
    global i     
    if(PM()==True):
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No
        dt2,dt_name = Class_MDM_Expr()
        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = Class_PM_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
            else:
                print(f"{name} ({dt})  can't {operator} with {dt_name} ({dt2}) in line no {line_no}")
                sys.exit()
    elif(List[i].Token_Class in["ROP","LOP","]",")",";",","]):
        return dt,name
    else:
           return False
def Class_I_C_B(): 
    global i
    if List[i].Token_Class == 'this->':
        dt_name = List[i+1].Token_Value      
        dt =Ts()
        if List[i].Token_Value=="(":
            con_type = Class_A3()
            check=lookUpFuncMT(dt_name,con_type,CCN)
            print(check)
            if(check==True):
                    print(f"Function {dt_name} is not defined")
                    sys.exit()
        
            else:
                print("Ahsaan")
                if List[i].Token_Class ==";":
                    return check,dt_name
        else:
            if (dt==True):
                print(f"{name} is not declared in line no {List[i].Line_No} ")
                sys.exit()
            else:
                print("Exp ID",dt_name)
                if(Class_A3()==True):
                    return dt ,dt_name
                
    elif(ID()==True):
        if List[i].Token_Value=="(":
                name = List[i-1].Token_Value
                con_type = Class_A3()
                check=lookUpFuncST(name,con_type)
                print(check)
                if(check==True):
                        print(f"Function {name} is not defined")
                        sys.exit()
            
                else:
                    print("Ahsaan")
                    if List[i].Token_Class ==";":
                        return check,name
        else:
            name = List[i-1].Token_Value
            dt = lookUpScopeTable(name)
            if (dt==True):
                print(f"{name} is not declared in line no {List[i].Line_No} ")
                sys.exit()
            else:
                print("Exp ID",name)
                if(Class_A3()==True):
                    return dt ,name
        
    
    elif(Constant()==True):
        con_type = List[i-1].Token_Class
        con_name = List[i-1].Token_Value
        return con_type,con_name
    
    elif(List[i].Token_Class == "("):
        i=i+1
        dt = Class_Expr()
        if (dt):
            if (List[i].Token_Class == ")") :
                i=i+1
                return dt,'umer'
            else:
                print ("Expected ) but found ",List[i].Token_Class)
                sys.exit()
        else:
            print ("Error in expression")
            sys.exit()

    elif(List[i].Token_Class == "!"):
        i=i+1
        if(Class_I_C_B()==True):
            return True
    else:
        print(f"Expecting Operator or ']' or ')' or ';' or ',' but get {List[i].Token_Value} in Line no {List[i-1].Line_No}")
        sys.exit()
            
        
    
def Class_MDM_Expr1(dt,name): 
    global i  
    if(MDM()==True):
        operator = List[i-1].Token_Value
        line_no = List[i-1].Line_No
        dt2,dt_name = Class_I_C_B()
        print(dt2)
        if(dt2):
            check = compatibiltyCheck(dt,dt2,operator)
            if (check):
                final_dt,final_name = Class_MDM_Expr1(check,dt_name)
                if(final_dt):
                    return final_dt,final_name
            else:
                print(f"{name} ({dt})  can't {operator} with {dt_name} ({dt2}) in line no {line_no}")
                sys.exit()

    elif(List[i].Token_Class in["PM","ROP","LOP","]",")",";","," ] ):
        return dt,name
    else:
         print(f"Error in Line No {List[i-1].Line_No}:Expecting Operator ,',',')' or ';' but get {List[i].Token_Value}")
         sys.exit()
        
    
def Comp_OP():
    global i 
    if (List[i].Token_Class == "CMP_OP"):
        i=i+1
        return True
    else:
        return False
    
def Make_Dt(dt):
    global i
    if(ID()==True):
        name = List[i-1].Token_Value
        dtype=lookUpScopeTable(name)
        if (dtype==True):
            print(f"Error in Line No {List[i-1].Line_No}: Undeclared variable '{List[i-1].Token_Value}'")
            sys.exit()
        else:
            DT=dt+dtype
            final_dt=Make_Dt(DT)
            if Make_Dt(final_dt):
                return final_dt

    elif (List[i].Token_Value==","):
        dt=dt+','
        print(dt,"Juice")
        i=i+1
        if(ID()==True):
            name = List[i-1].Token_Value
            dtype=lookUpScopeTable(name)
            if (dtype):
                DT=dt+dtype
                final_dt=Make_Dt(DT)
                if Make_Dt(final_dt):
                    return final_dt

                
    elif (List[i].Token_Value==")"):
        return dt

    else:
        return False


# insertDefTable('CBA','class','public','-','general')

Start()

