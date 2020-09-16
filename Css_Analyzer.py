import os
import platform
import subprocess
from tkinter import messagebox
from Token import Token
from Errors import Lexical_Errors
class Css_Lex:

    def __init__(self):
        self.Log_Analyzer="Css Log States"+"\n"
        self.status=0
        self.path_file=""
        self.file_Name=""
        self.multi_flag=False
        self.row=1
        self.column=0
        self.Token_Array_Css = []
        self.Errors_Html_Css = []
        self.Data_text_temp=""
        self.index=""

    def Analyze_text_Css(self,data_text,file_N):
        self.file_Name=file_N
        Lexical_Aux=""
        counter=0
        temp_status=0
        lenght_text = len(data_text)
        while counter<lenght_text:
            temp_character=data_text[counter]
            assci_code=ord(temp_character)
            self.status=temp_status
            if(self.status==0): # STATE NUMBER 0
                if(assci_code==42): #Token *
                    temp_status=1
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==59):# Token ;
                    temp_status=2
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==58):# Token :
                    temp_status=3
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==40):# Token (
                    temp_status=4
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==41): #Token )
                    temp_status=5
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==123): #Token {
                    temp_status=6
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==125): #Token }
                    temp_status=7
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==46): #Token .
                    temp_status=8
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==44): #Token ,
                    temp_status=9
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==45): #Token -
                    temp_status=10
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==37): #Token %
                    temp_status=11
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==34): #Token "
                    temp_status=12
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code>=48 and assci_code<=57):#Token Number
                    temp_status=14
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==35): #Token #
                    temp_status=17
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif((assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122)): #Token L
                    temp_status=19
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                elif(assci_code==47): #Token /
                    temp_status=20
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S0"+"\n"
                    self.index=str(self.row)+"."+str(self.column)
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
                        self.Errors_Html_Css.append(Lexical_Errors(self.row,self.column,temp_character,"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                        self.column+=1
            elif(self.status==1): #STATE NUMBER 1
                self.Log_Analyzer+="Actual Character  "+ temp_character+ " In to S1"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Type: Asterisk" +" Acepted in S1"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(1,Lexical_Aux,"asterisk",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==2): #STATE NUMBER 2
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S2"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S2"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(2,Lexical_Aux,"semi-colon",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==3): #STATE NUMBER 3
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S3"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S3"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(3,Lexical_Aux,"Double dot token",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==4): #STATE NUMBER 4
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S4"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S4"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(4,Lexical_Aux,"right Paranthesis",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==5): #STATE NUMBER 5
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S5"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S5"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(5,Lexical_Aux,"left parenthesis",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==6):#STATE NUMBER 6
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S6"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S6"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(6,Lexical_Aux,"left curly bracket",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==7):#STATE NUMBER 7
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S7"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S7"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(7,Lexical_Aux,"right curly bracket",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==8):#STATE NUMBER 8
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S8"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S8"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(8,Lexical_Aux,"dot",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==9):#STATE NUMBER 9
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S9"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S9"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(9,Lexical_Aux,"comma",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==10):#STATE NUMBER 10
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S10"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S10"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(10,Lexical_Aux,"minus sign",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==11):#STATE NUMBER 11
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S11"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S11"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(11,Lexical_Aux,"Percent",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==12):#STATE NUMBER 12
                if (assci_code==34):#Token "
                    temp_status=13
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                else:
                    temp_status=12
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S12"+"\n"
            elif(self.status==13):#STATE NUMBER 13
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S13"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S13"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(13,Lexical_Aux,"Double Quote comment",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==14):#STATE NUMBER 14
                if (assci_code>=48 and assci_code<=57):#TOKEN NUMBER 
                    temp_status=14
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S14"+"\n"
                elif(assci_code==46):#TOKEN DOT .
                    temp_status=15
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S14"+"\n"
                else:
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S14"+"\n"
                    self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S14"+"\n"
                    self.Log_Analyzer+="\n"
                    self.Token_Array_Css.append(Token(13,Lexical_Aux,"Int",self.row,self.column,""))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            elif(self.status==15):#STATE NUMBER 15
                if (assci_code>=48 and assci_code<=57):
                    temp_status=16
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S15"+"\n"
                else:
                    temp_status=0
                    self.Errors_Html_Css.append(Lexical_Errors(self.row,self.column,temp_character,"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                    self.column+=1
            elif(self.status==16):#STATE NUMBER 16
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S16"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S16"+"\n"
                self.Log_Analyzer+="\n"
                self.Token_Array_Css.append(Token(16,Lexical_Aux,"Float",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0 
            elif(self.status==17):#STATE NUMBER 17
                if (assci_code>=48 and assci_code<=57):#TOKEN NUMBER 
                    temp_status=18
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S17"+"\n"
                elif(assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122): #Token L
                    temp_status=18
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S17"+"\n"
                else:
                    temp_status=0
                    self.Errors_Html_Css.append(Lexical_Errors(self.row,self.column,temp_character,"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                    self.column+=1
            elif(self.status==18):#STATE NUMBER 18
                if (assci_code>=48 and assci_code<=57):#TOKEN NUMBER 
                    temp_status=18
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S18"+"\n"
                elif(assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122): #Token L
                    temp_status=18
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S18"+"\n"
                elif(assci_code==45):#TOKEN -
                    temp_status=18
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S18"+"\n"
                elif(assci_code==95):#TOKEN _
                    temp_status=18
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S18"+"\n"
                else:
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S18"+"\n"
                    self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S18"+"\n"
                    self.Log_Analyzer+="\n"
                    self.Token_Array_Css.append(Token(16,Lexical_Aux,"Call Id",self.row,self.column,""))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            elif(self.status==19):#STATUS NUMBER 19
                if (assci_code>=48 and assci_code<=57):#TOKEN NUMBER 
                    temp_status=19
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S19"+"\n"
                elif((assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122)): #Token L
                    temp_status=19
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S19"+"\n"
                elif(assci_code==45):#TOKEN -
                    temp_status=19
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S19"+"\n"
                elif(assci_code==95):#TOKEN _
                    temp_status=19
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S19"+"\n"
                else:
                    type_Id=self.Vef_Id(Lexical_Aux)
                    self.Token_Array_Css.append(Token(16,Lexical_Aux,type_Id,self.row,self.column,""))
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S18"+"\n"
                    self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S18"+"\n"
                    self.Log_Analyzer+="\n"
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            elif(self.status==20):# STATE NUMBER 20
                if (assci_code==42): #Token *
                    temp_status=21
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S20"+"\n"
                else:
                    temp_status=0
                    self.Errors_Html_Css.append(Lexical_Errors(self.row,self.column,temp_character,"The Symbol "+temp_character+"is not part of the Alphabet Language")) 
                    self.column+=1
            elif(self.status==21):#STATE NUMBER 20
                if(assci_code==42):# Token *
                    self.multi_flag=True
                    temp_status=21
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S21"+"\n"
                elif(assci_code==47 and self.multi_flag==True):
                    temp_status=22
                    #capture path before /
                    path_t=(Lexical_Aux.lower().find("pathw:"))
                    if(path_t!=-1):
                        self.path_file=Lexical_Aux
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S21"+"\n"
                else:
                    if(assci_code==10):
                        self.multi_flag=False
                        temp_status=21
                        Lexical_Aux+=temp_character
                        self.Data_text_temp+=temp_character
                        self.row+=1
                        self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S21"+"\n"
                    else:
                        self.multi_flag=False
                        temp_status=21
                        Lexical_Aux+=temp_character
                        self.Data_text_temp+=temp_character
                        self.column+=1
                        self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S21"+"\n"
            elif(self.status==22):#STATE NUMBER 22
                self.Log_Analyzer+="Actual Character "+ temp_character+ " In to S18"+"\n"
                self.Log_Analyzer+="Success: Token-> "+ Lexical_Aux+ " Acepted in S18"+"\n"
                self.Log_Analyzer+="\n"
                self.multi_flag=False
                self.Token_Array_Css.append(Token(21,Lexical_Aux,"multiline comment",self.row,self.column,self.index))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            else:
                print("NON STATE")
            counter+=1
        self.Report_Decision()
        
        

    def clear_method(self):
        self.Token_Array_Css.clear()
        self.Errors_Html_Css.clear()
        self.Log_Analyzer="Css Log States"+"\n"
        self.row=1
        self.multi_flag=False
        self.column=0
        self.status=0
        self.path_file=""
        self.file_Name=""
        self.Data_text_temp=""
        self.index=""

    def replaceMultiple(self,mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
        for elem in toBeReplaces :
            # Check if string is in the main string
            if elem in mainString :
            # Replace the string
                mainString = mainString.replace(elem, newString)
        
        return  mainString

    def create_path_Css(self,temp_path_W):
        temp_path=temp_path_W
        if(temp_path_W!=""):
            temp_path=""
            temp_path=temp_path_W.lower().split("output",1)
            temp_path=temp_path[1]
            otherStr = self.replaceMultiple(temp_path, ['!', '*', '?','<','>'] , "")
            temp_path="C:/Users/bryan/Desktop/P1/Output"+otherStr.strip()
            if(temp_path[len(temp_path)-1]=="/"):
                #we slice the string
                temp_path=temp_path[:len(temp_path)-1]
                temp_path=temp_path.replace("/","//")
            else:
                temp_path=temp_path.replace("/","//")
            if(os.path.exists(temp_path)==False):
                try:
                    os.makedirs(temp_path,mode=0o777)
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


    #verifying if is Identifier or not 
    def Vef_Id(self,Token_type):
        for temp_Token in Token.Special_Tokens_CSs:
            if(Token_type.lower()==Token.Special_Tokens_CSs[temp_Token]):
                return "Reserved Keyword"
        #the token isn't a Reserved Keyword so that will return a Identifier       
        return "Identifier"

      # ERRORS report snippet
    def print_SizeTokens_Errors(self):
        Error_string=""
        for index,erorrs_Values in enumerate(self.Errors_Html_Css):
            Error_string+="<tr>\n"+"<td>" + str(index)+"</td>\n<td>"+str(erorrs_Values.get_Row())+"</td>\n<td>"+str(erorrs_Values.get_Column()) +"</td>\n<td>" + erorrs_Values.get_Lex_Token()+"</td>\n<td>" + erorrs_Values.get_Details()+"</td>\n</tr>"
        return Error_string

    #Error Html Report
    def Errores_Report(self): 
        file_temp=open('Error_Css_Report.html','w',encoding='utf-8')
        file_temp.write("<!doctype html>\n")
        file_temp.write("<html>\n")
        file_temp.write("<head>\n")
        file_temp.write("<meta charset="'"utf-8"'">\n")
        file_temp.write("<meta http-equiv="'"X-UA-Compatible"'" content="'"IE=edge"'">\n")
        file_temp.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"bootstrap.min.css\">\n")
        file_temp.write("<title>Errors Report</title>\n")
        file_temp.write("</head>\n")
        file_temp.write("<body>\n")
        file_temp.write("<h1 class="'"text-center"'"style="'"margin-top:20px;"'">Css Report (Errors) List</h1>\n")
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
        os.system('Error_Css_Report.html')

    def Report_Decision(self):
        if(len(self.Errors_Html_Css)==0):# clean Execution ( no errors founded !!!)
            #self.Tokens_Report()
            pass        
        else:
            print("TIENE eRORORES")
            #self.Tokens_Report()
            self.Errores_Report()

        path_token=self.create_path_Css(self.path_file)
        completeName=None
        if(path_token==""):
            messagebox.showwarning(title="File", message="Alternative Path was created")
            pt=r'C:/Users/bryan/Desktop/P1/Output/css'
            if(os.path.exists(pt)==True):
                completeName = os.path.join(pt, self.file_Name)
            else:
                os.makedirs(pt,mode=0o444)
                completeName = os.path.join(pt, self.file_Name)
            if(os.path.exists(completeName)):
                    os.remove(completeName)
                    file1 = open(completeName, "w")
                    file1.write(self.Data_text_temp)
                    file1.close()
            else:         
                file1 = open(completeName, "w")
                file1.write(self.Data_text_temp)
                file1.close()           
        else:
            complete_path=path_token+"//"+self.file_Name
            if(os.path.isfile(complete_path)==True):
                os.remove(complete_path)
                file1 = open(complete_path, "w")
                file1.write(self.Data_text_temp)
                file1.close() 
            else:
                print("css")
                print(self.file_Name)
                print(complete_path)
                file1 = open(complete_path, "w")
                file1.write(self.Data_text_temp)
                file1.close()  
            