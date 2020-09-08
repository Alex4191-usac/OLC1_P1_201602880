import os
import platform
from Token import Token
from Errors import Lexical_Errors

class Js_Lex:

    def __init__(self):
        self.status=0
        self.multi_flag=False
        self.Token_Array_Js = []
        self.Errors_Html_Js = []
        self.Data_text_temp=""
        self.file_name=""
        self.path_file=""
        self.Data_text_temp=""
        self.row=1
        self.column=0

    def Analyze_text_Js(self,data_text,self_name):
        self.file_name=self_name
        Lexical_Aux=""
        counter=0
        temp_status=0
        #data_text=data_text+"#"
        lenght_text = len(data_text)
        while counter<lenght_text:
            temp_character=data_text[counter]
            assci_code=ord(temp_character)
            self.status=temp_status
            if(self.status==0): #INITIAL STATE S0
                if(assci_code==47): #Token /
                    temp_status=1
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==61): #Token =
                    temp_status=2
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==42): #Token *
                    temp_status=3
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==43):#Token +
                    temp_status=4
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==45):#Token -
                    temp_status=5
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==59):# Token ;
                    temp_status=6
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==40):# Token (
                    temp_status=7
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==41): #Token )
                    temp_status=8
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==123): #Token {
                    temp_status=9
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==125): #Token }
                    temp_status=10
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==46): #Token .
                    temp_status=11
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==44): #Token ,
                    temp_status=12
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==60): #Token <
                    temp_status=13
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==62): #Token >
                    temp_status=14
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==33): #Token !
                    temp_status=15
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==38): #Token &
                    temp_status=16
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code==124): #Token |
                    temp_status=18
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code>=48 and assci_code<=57):#Token Number
                    temp_status=24
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif (assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122):# token Letter
                    temp_status=27
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                elif(assci_code==34): # Token "
                    temp_status=28
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                elif(assci_code==39): # Token '
                    temp_status=30
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                elif(assci_code==58):# Token :
                    temp_status=32
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                else:
                    if(assci_code>=00 and assci_code <=32 and assci_code!=10):
                        self.Data_text_temp+=temp_character #
                        self.column+=1
                    elif(assci_code==10):#enter key
                        self.row+=1
                        self.column=0
                        self.Data_text_temp+=temp_character
                    else: # means lexical Error founded
                        self.status=0
                        self.Errors_Html_Js.append(Lexical_Errors(self.row,self.column,temp_character,"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                        self.column+=1
            elif(self.status==1):# STATE NUMBER 1
                if (assci_code==42): #Token *
                    temp_status=20
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==47): #Token /
                    temp_status=21
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                else:
                    self.Token_Array_Js.append(Token(1,Lexical_Aux,"forward-slash",self.row,self.column))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
                    #self.column+=1
            elif(self.status==2):#STATE NUMBER 2
                self.Token_Array_Js.append(Token(2,Lexical_Aux,"equality sign",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==3):#STATE NUMBER 3
                self.Token_Array_Js.append(Token(3,Lexical_Aux,"Asterisk",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==4):#STATE NUMBER 4
                self.Token_Array_Js.append(Token(4,Lexical_Aux,"Plus-Sign",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==5):#STATE NUMBER 5
                self.Token_Array_Js.append(Token(5,Lexical_Aux,"Minus-Sign",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==6):#STATE NUMBER 6
                self.Token_Array_Js.append(Token(6,Lexical_Aux,"semi-colon",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==7):#STATE NUMBER 7
                self.Token_Array_Js.append(Token(7,Lexical_Aux,"Left parentheses",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==8):#STATE NUMBER 8
                self.Token_Array_Js.append(Token(8,Lexical_Aux,"Right parentheses",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==9):#STATE NUMBER 9
                self.Token_Array_Js.append(Token(9,Lexical_Aux,"Left curly bracket",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==10):#STATE NUMBER 10
                self.Token_Array_Js.append(Token(10,Lexical_Aux,"Right curly bracket",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==11):#STATE NUMBER 11
                self.Token_Array_Js.append(Token(11,Lexical_Aux,"Dot",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==12):#STATE NUMBER 12
                self.Token_Array_Js.append(Token(12,Lexical_Aux,"comma",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==13):#STATE NUMBER 13
                self.Token_Array_Js.append(Token(13,Lexical_Aux,"Less-than sign",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==14):#STATE NUMBER 14
                self.Token_Array_Js.append(Token(14,Lexical_Aux,"greater-than symbol",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==15):#STATE NUMBER 15
                self.Token_Array_Js.append(Token(15,Lexical_Aux,"not",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==16):#STATE NUMBER 16
                if(assci_code==38): # Token &
                    temp_status=17
                    Lexical_Aux+=temp_character

                    #grabs the lex before the validations
                    sub_temp=data_text[counter-1]
                    self.Data_text_temp+=sub_temp
                    self.Data_text_temp+=temp_character
                    self.column+=1
                else:
                    temp_status=0
                    self.Errors_Html_Js.append(Lexical_Errors(self.row,self.column,data_text[counter-1],"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                    self.column+=1
            elif(self.status==17):#STATE NUMBER 17
                self.Token_Array_Js.append(Token(18,Lexical_Aux,"and",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==18):#STATE NUMBER 18
                if(assci_code==124): # Token |
                    temp_status=19
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                else:
                    temp_status=0
                    self.Errors_Html_Js.append(Lexical_Errors(self.row,self.column,data_text[counter-1],"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                self.column+=1
            elif(self.status==19):#STATE NUMBER 19
                self.Token_Array_Js.append(Token(19,Lexical_Aux,"or",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0   
            elif(self.status==20):#STATE NUMBER 20
                if(assci_code==42):# Token *
                    self.multi_flag=True
                    temp_status=20
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==47 and self.multi_flag==True):
                    temp_status=22
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                else:
                    self.multi_flag=False
                    temp_status=20
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
            elif(self.status==21):#STATE NUMBER 20
                if(assci_code==10):# Token enter
                    path_t=(Lexical_Aux.find("PATHW") or Lexical_Aux.find("PATHL"))
                    if(path_t!=-1): # its a file path
                        self.path_file=Lexical_Aux
                        self.Token_Array_Js.append(Token(21,Lexical_Aux,"path",self.row,self.column))
                        Lexical_Aux=""
                        counter-=1
                        temp_status=0
                    else: # isn't a file path
                        self.Token_Array_Js.append(Token(21,Lexical_Aux,"single comment",self.row,self.column))
                        Lexical_Aux=""
                        counter-=1
                        temp_status=0
                else:
                    temp_status=21
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1  
            elif(self.status==22):#STATE NUMBER 22 
                self.multi_flag=False
                self.Token_Array_Js.append(Token(21,Lexical_Aux,"multiline comment",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==24): #STATE NUMBER 24
                if(assci_code>=48 and assci_code<=57):#Token Number
                    temp_status=24
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif (assci_code==46):# Token .
                    temp_status=25
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                else:
                    self.Token_Array_Js.append(Token(21,Lexical_Aux,"Integer",self.row,self.column))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0 
            elif (self.status==25):#STATE NUMBER 25
                if(assci_code>=48 and assci_code<=57):# Token Number 
                    temp_status=26
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                else:
                    temp_status=0
                    self.Errors_Html_Js.append(Lexical_Errors(self.row,self.column,data_text[counter-1],"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                    self.column+=1
            elif(self.status==26):#STATE NUMBER 26
                if(assci_code>=48 and assci_code<=57):# Token Number 
                    temp_status=26
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                else:
                    self.Token_Array_Js.append(Token(21,Lexical_Aux,"Float",self.row,self.column))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
                    self.column+=1 
            elif(self.status==27):# STATE NUMBER 27
                if (assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122):# Letter
                    temp_status=27
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                elif(assci_code>=48 and assci_code<=57):#number
                    temp_status=27
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                elif(assci_code==95):# underScore or UnderLine
                    temp_status=27
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                else:
                    self.Token_Array_Js.append(Token(27,Lexical_Aux,self.Vef_Id(Lexical_Aux),self.row,self.column))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0    
            elif(self.status==28): # STATE NUMBER 28
                if(assci_code==34):
                    temp_status=29
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                else:
                    temp_status=28
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
            elif(self.status==29):#STATE NUMBER 29
                    self.Token_Array_Js.append(Token(29,Lexical_Aux,"Double Quote comment",self.row,self.column))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            elif(self.status==30):#STATE NUMBER 30
                if(assci_code==39):
                    temp_status=31
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                else:
                    temp_status=30
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
            elif(self.status==31):#STATE NUMBER 31
                    self.Token_Array_Js.append(Token(31,Lexical_Aux,"Single Quote comment",self.row,self.column))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            elif(self.status==32):#STATE NUMBER 32
                    self.Token_Array_Js.append(Token(32,Lexical_Aux,"Double dot token",self.row,self.column))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            else:
                print("LEXICAL ERRROS")      
            
            counter+=1
        self.Report_Decision()

    def clear_method(self):
        self.Token_Array_Js.clear()
        self.Errors_Html_Js.clear()
        self.row=1
        self.multi_flag=False
        self.column=0
        self.status=0
        self.path_file=""
        self.file_name=""
        self.Data_text_temp=""
    
    def Vef_Id(self,Token_type):
        for temp_Token in Token.Special_Tokens:
            if(Token_type.lower()==Token.Special_Tokens[temp_Token]):
                return "Reserved Keyword"
        #the token isn't a Reserved Keyword so that will return a Identifier       
        return "Identifier"


    def create_path_Js(self,temp_path_W):
        temp_path=temp_path_W
        if(temp_path_W!=""):
            system_temp=platform.system()
            temp_path=""

            if(system_temp=='Linux'):
                temp_path=temp_path_W.split('PATHL:',1)
                temp_path=temp_path[1]
            else:
                temp_path=temp_path_W.split('PATHW:',1)
                temp_path=temp_path[1]

            temp_path=temp_path.replace("/","//")
            if(os.path.exists(temp_path)==False):
                try:
                    os.makedirs(temp_path,mode=0o444)
                except OSError:
                    print("Creation of the directory %s failed" % temp_path)
                    return ""
                else:
                    print("Successfully created the directory %s" % temp_path)
                    return temp_path
            else:
                print("PATH ALREADY EXISTS")
                return temp_path 
        else:
            print("path is not in File")
            return ""

    # ERRORS report snippet
    def print_SizeTokens_Errors(self):
        Error_string=""
        for index,erorrs_Values in enumerate(self.Errors_Html_Js):
            Error_string+="<tr>\n"+"<td>" + str(index)+"</td>\n<td>"+str(erorrs_Values.get_Row())+"</td>\n<td>"+str(erorrs_Values.get_Column()) +"</td>\n<td>" + erorrs_Values.get_Lex_Token()+"</td>\n<td>" + erorrs_Values.get_Details()+"</td>\n</tr>"
        return Error_string

    #Error Html Report
    def Errores_Report(self): 
        file_temp=open('Error_Js_Report.html','w')
        file_temp.write("<!doctype html>\n")
        file_temp.write("<html>\n")
        file_temp.write("<head>\n")
        file_temp.write("<meta charset="'"utf-8"'">\n")
        file_temp.write("<meta http-equiv="'"X-UA-Compatible"'" content="'"IE=edge"'">\n")
        file_temp.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"bootstrap.min.css\">\n")
        file_temp.write("<title>Errors Report</title>\n")
        file_temp.write("</head>\n")
        file_temp.write("<body>\n")
        file_temp.write("<h1 class="'"text-center"'"style="'"margin-top:20px;"'">jS Report (Errors) List</h1>\n")
        file_temp.write("<div class="'"container"'" style="'"margin-top:20px;"'">\n")
        file_temp.write("<table class="'"table table-striped"'">\n")
        file_temp.write("<thead class="'"bg-dark"'" style="'"color:white;"'">\n")
        file_temp.write("<tr>\n")
        file_temp.write("<td><strong>No</td>\n")
        file_temp.write("<td><strong>Row</td>\n")
        file_temp.write("<td><strong>Column</td>\n")
        file_temp.write("<td><strong>Error</td>\n")
        file_temp.write("<td><strong>Description</td>\n")
        file_temp.write("</tr>\n")
        file_temp.write("</thead>")
        file_temp.write(self.print_SizeTokens_Errors())
        file_temp.write("</table>\n")
        file_temp.write("</div>")
        file_temp.write("</body>\n")
        file_temp.write("</html>\n")
        file_temp.close()
        os.system('Error_Js_Report.html')

    def Report_Decision(self):
        if(len(self.Errors_Html_Js)==0):# clean Execution ( no errors founded !!!)
            #self.Tokens_Report()
            print("grafo")        
        else:
            print("TIENE eRORORES")
            #self.Tokens_Report()
            self.Errores_Report()

        path_token=self.create_path_Js(self.path_file)
        if(path_token==""):
            pt=r'C:\Users\Bryan\Desktop\Output_temporal'
            os.makedirs(pt,mode=0o444)
            completeName = os.path.join(pt, self.file_name)         
            file1 = open(completeName, "w")
            file1.write(self.Data_text_temp)
            file1.close()
        else:
            completeName = os.path.join(path_token, self.file_name)  
            file1 = open(completeName, "w")
            file1.write(self.Data_text_temp)
            file1.close()