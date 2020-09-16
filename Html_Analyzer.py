import os
import platform
from Token import Token
from tkinter import messagebox
from Errors import Lexical_Errors
class Html_lex:
    
    def __init__(self):
        self.status=0
        self.path_file=""
        self.file_Name=""
        self.row=1
        self.column=0
        self.Token_Array = []
        self.Errors_Html = []
        self.Data_text_temp=""
        self.Text_Flag=False
        self.multi_flag=False
        self.index=""



    def Analyze_text(self,data_text,file_N):
        self.file_Name=file_N
        Lexical_Aux=""
        counter=0
        temp_status=0
        lenght_text = len(data_text)
        while counter<lenght_text:
            temp_character=data_text[counter]
            assci_code=ord(temp_character)
            self.status=temp_status
            if(self.status==0):# STATE NUMBER 0:
                if(assci_code==60):# token <
                    self.Text_Flag=False
                    temp_status=1
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                    self.index=str(self.row)+"."+str(self.column)
                elif(assci_code==62):# token >
                    self.Text_Flag=True
                    temp_status=2
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character 
                    self.column+=1
                elif (assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122):# token Letter
                    temp_status=3
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                elif(assci_code==47):# token /
                    temp_status=4
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                elif(assci_code==61):# token =
                    temp_status=6
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                elif(assci_code==34): # token "
                    temp_status=7
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                else:
                    if(assci_code>=00 and assci_code <=32 and assci_code!=10):
                        print("space")
                        self.Data_text_temp+=temp_character #
                        self.column+=1
                    elif(assci_code==10):#enter key
                        self.row+=1
                        self.column=0
                        self.Data_text_temp+=temp_character #
                        print("enter space")
                    else: # means lexical Error founded
                        if(self.Text_Flag==False):
                            self.status=0
                            self.Errors_Html.append(Lexical_Errors(self.row,self.column,temp_character,"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                        else:#menas that we still text between the close and open Html Tags
                            temp_status=9
                            Lexical_Aux+=temp_character
                            self.Data_text_temp+=temp_character
                        self.column+=1
            elif (self.status==1):# STATE NUMBER 1
                if(assci_code==33): #Token !
                    temp_status=10
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1
                else:
                    self.Token_Array.append(Token(1,Lexical_Aux,"Less-than sign",self.row,self.column,""))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
                    #self.column+=1
            elif(self.status==2):# STATE NUMBER 2
                self.Token_Array.append(Token(2,Lexical_Aux,"greater-than sign",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==3):# STATE NUMBER 3
                if(self.Text_Flag==False):
                    if (assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122):# Letter
                        temp_status=3
                        Lexical_Aux+=temp_character
                        self.Data_text_temp+=temp_character #
                        self.column+=1
                    elif(assci_code>=48 and assci_code<=57):#number
                        temp_status=3
                        Lexical_Aux+=temp_character
                        self.Data_text_temp+=temp_character #
                        self.column+=1
                    elif(assci_code==95):# underScore or UnderLine
                        temp_status=3
                        Lexical_Aux+=temp_character
                        self.Data_text_temp+=temp_character #
                        self.column+=1
                    else:
                        self.Token_Array.append(Token(3,Lexical_Aux,self.Vef_Id(Lexical_Aux),self.row,self.column,""))
                        Lexical_Aux=""
                        counter-=1
                        temp_status=0
                else: # this means that we found text (example: <p>dummy text</p>)
                    temp_status=9
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                    self.column+=1 
            elif(self.status==4):# STATE NUMBER 4
                    self.Token_Array.append(Token(4,Lexical_Aux,"forward-slash",self.row,self.column,""))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            elif(self.status==6): # STATE NUMBER 6
                self.Token_Array.append(Token(6,Lexical_Aux,"Equality sign",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==7): # STATE NUMBER 7
                if(assci_code==34):
                    temp_status=8
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                else:
                    temp_status=7
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                self.column+=1
            elif(self.status==8): # STATE NUMBER 8
                self.Token_Array.append(Token(8,Lexical_Aux,"Double Quote comment",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            elif(self.status==9):
                if(assci_code==60):
                    self.Token_Array.append(Token(8,Lexical_Aux,"Text",self.row,self.column,""))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0 
                    self.Text_Flag=False
                else:
                    temp_status=9
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #  
                    self.column+=1
            elif(self.status==10):#STATE NUMBER 10
                if(assci_code==45): #TOKEN -
                    temp_status=11
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                else:
                    self.status=0
                    self.Errors_Html.append(Lexical_Errors(self.row,self.column,temp_character,"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                self.column+=1
            elif (self.status==11):#STATE NUMBER 11
                if(assci_code==45): #TOKEN -
                    temp_status=13
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character #
                else:
                    self.status=0
                    self.Errors_Html.append(Lexical_Errors(self.row,self.column,temp_character,"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                self.column+=1
            elif(self.status==13):#STATE NUMBER 13
                if(assci_code==45): #TOKEN -
                    temp_status=14
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1    
                else:
                    if(assci_code==10):
                        self.multi_flag=False
                        temp_status=13
                        Lexical_Aux+=temp_character
                        self.Data_text_temp+=temp_character
                        self.column=0
                        self.row+=1
                    else:
                        self.multi_flag=False
                        temp_status=13
                        Lexical_Aux+=temp_character
                        self.Data_text_temp+=temp_character
                        self.column+=1
            elif (self.status==14):#STATE NUMBER 14
                if(assci_code==45):#TOKEN -
                    self.multi_flag=True
                    temp_status=14
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                elif(assci_code==62 and self.multi_flag==True):#TOKEN >
                    path_t=(Lexical_Aux.lower().find("pathw:"))
                    if(path_t!=-1):
                        self.path_file=Lexical_Aux
                    temp_status=15
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=temp_character
                    self.column+=1
                else:
                    if(assci_code==10):
                        self.multi_flag=False
                        temp_status=13
                        Lexical_Aux+=temp_character
                        self.Data_text_temp+=temp_character
                        self.column=0
                        self.row+=1
                    else:
                        self.multi_flag=False
                        temp_status=13
                        Lexical_Aux+=temp_character
                        self.Data_text_temp+=temp_character
                        self.column+=1
            elif(self.status==15):#STATE NUMBER 15
                self.Token_Array.append(Token(8,Lexical_Aux,"multiline comment",self.row,self.column,self.index))
                Lexical_Aux=""
                counter-=1
                temp_status=0
                #self.column+=1
            else:
                print("ANALYZER ERROR")
       
            counter+=1
        self.Report_Decision()


   #overwrite variables to set empty
    def clear_method(self):
        self.Token_Array.clear()
        self.Errors_Html.clear()
        self.row=1
        self.column=0
        self.status=0
        self.path_file=""
        self.file_Name=""
        self.Data_text_temp=""
        self.Text_Flag=False
        self.multi_flag=False
        self.index=""


    def replaceMultiple(self,mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
        for elem in toBeReplaces :
            # Check if string is in the main string
            if elem in mainString :
            # Replace the string
                mainString = mainString.replace(elem, newString)
        
        return  mainString

    #File's output dir
    def create_path_Js(self,temp_path_W):
        temp_path=temp_path_W
        if(temp_path_W!=""):
            temp_path=""
            temp_path=temp_path_W.lower().split("output",1)
            temp_path=temp_path[1]
            otherStr = self.replaceMultiple(temp_path, ['!','@','#','$', '*', '?','<','>'] , "")
            otherStr=otherStr.strip()
            new_p=temp_path[0:len(temp_path)-2]
            temp_path="C:/Users/bryan/Desktop/P1/Output"+new_p
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
        for temp_Token in Token.Special_Tokens:
            if(Token_type.lower()==Token.Special_Tokens[temp_Token]):
                return "Reserved Keyword"
        #the token isn't a Reserved Keyword so that will return a Identifier       
        return "Identifier"

    #Html report snippet
    def print_SizeTokens(self):
        Token_string=""
        for token_values in self.Token_Array:
            if token_values.get_Token=="<":
                Token_string+="<tr>\n"+"<td>" + str(token_values.get_Id())+"</td>\n<td>" +"&lt"+"</td>\n<td>"+token_values.get_TypeT() +"</td>\n<td>" + str(token_values.get_Row())+"</td>\n<td>" + str(token_values.get_Column())+"</td>\n</tr>"
            elif token_values.get_Token==">":
                Token_string+="<tr>\n"+"<td>" + str(token_values.get_Id())+"</td>\n<td>" +"&gt"+"</td>\n<td>"+token_values.get_TypeT() +"</td>\n<td>" + str(token_values.get_Row())+"</td>\n<td>" + str(token_values.get_Column())+"</td>\n</tr>"
            else: 
                Token_string+="<tr>\n"+"<td>" + str(token_values.get_Id())+"</td>\n<td>" + token_values.get_Token()+"</td>\n<td>"+token_values.get_TypeT() +"</td>\n<td>" + str(token_values.get_Row())+"</td>\n<td>" + str(token_values.get_Column())+"</td>\n</tr>"
        return Token_string

    #Html File Method
    def Tokens_Report(self): 
        file_temp=open('Html_Report.html','w',encoding='utf-8')
        file_temp.write("<!doctype html>\n")
        file_temp.write("<html>\n")
        file_temp.write("<head>\n")
        file_temp.write("<meta charset="'"utf-8"'">\n")
        file_temp.write("<meta http-equiv="'"X-UA-Compatible"'" content="'"IE=edge"'">\n")
        file_temp.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"bootstrap.min.css\">\n")
        file_temp.write("<title>Tokens Report</title>\n")
        file_temp.write("</head>\n")
        file_temp.write("<body>\n")
        file_temp.write("<h1 class="'"text-center"'"style="'"margin-top:20px;"'">Token's List</h1>\n")
        file_temp.write("<div class="'"container"'" style="'"margin-top:20px;"'">\n")
        file_temp.write("<table class="'"table table-striped"'">\n")
        file_temp.write("<thead class="'"bg-dark"'" style="'"color:white;"'">\n")
        file_temp.write("<tr>\n")
        file_temp.write("<td><strong>Id Token</td>\n")
        file_temp.write("<td><strong>Token Value</td>\n")
        file_temp.write("<td><strong>Token Type</td>\n")
        file_temp.write("<td><strong>Row</td>\n")
        file_temp.write("<td><strong>Column</td>\n")
        file_temp.write("</tr>\n")
        file_temp.write("</thead>")
        file_temp.write(self.print_SizeTokens())
        file_temp.write("</table>\n")
        file_temp.write("</div>")
        file_temp.write("</body>\n")
        file_temp.write("</html>\n")
        file_temp.close()
        os.system('Html_Report.html')

    # ERRORS report snippet
    def print_SizeTokens_Errors(self):
        Error_string=""
        for index,erorrs_Values in enumerate(self.Errors_Html):
            Error_string+="<tr>\n"+"<td>" + str(index)+"</td>\n<td>"+str(erorrs_Values.get_Row())+"</td>\n<td>"+str(erorrs_Values.get_Column()) +"</td>\n<td>" + erorrs_Values.get_Lex_Token()+"</td>\n<td>" + erorrs_Values.get_Details()+"</td>\n</tr>"
        return Error_string

    #Error Html Report
    def Errores_Report(self): 
        file_temp=open('Error_Html_Report.html','w')
        file_temp.write("<!doctype html>\n")
        file_temp.write("<html>\n")
        file_temp.write("<head>\n")
        file_temp.write("<meta charset="'"utf-8"'">\n")
        file_temp.write("<meta http-equiv="'"X-UA-Compatible"'" content="'"IE=edge"'">\n")
        file_temp.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"bootstrap.min.css\">\n")
        file_temp.write("<title>Errors Report</title>\n")
        file_temp.write("</head>\n")
        file_temp.write("<body>\n")
        file_temp.write("<h1 class="'"text-center"'"style="'"margin-top:20px;"'">Html's Report (Errors) List</h1>\n")
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
        os.system('Error_Html_Report.html')


    #this method will decid wich if we want to show our Error Report ( if Error's exists)
    
    def Report_Decision(self):
        if(len(self.Errors_Html)==0):# clean Execution ( no errors founded !!!)
            pass
        else:
            self.Tokens_Report()
            self.Errores_Report()
        print(self.path_file)
        path_token=self.create_path_Js(self.path_file)
        completeName=None
        if(path_token==""):
            messagebox.showwarning(title="File", message="Alternative Path was created")
            pt=r'C:/Users/bryan/Desktop/P1/Output'
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
                print("js")
                print(complete_path)
                file1 = open(complete_path, "w")
                file1.write(self.Data_text_temp)
                file1.close()  
    
    
    
    
    

            
