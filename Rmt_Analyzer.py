import os
import platform
from Token import Token
from Errors import Lexical_Errors
from Rmt_Parser import Parser_Rmt
class Rmt_Lex:

    def __init__(self):
        self.status=0
        self.Token_Array_Rmt = []
        self.Token_Array_Rmt_TEMP=[]
        self.Errors_Html_Rmt = []
        self.Data_text_temp=""
        self.file_name=""
        self.result_board=""
        self.row=1
        self.column=0

    def Analyze_text_Rmt(self,data_text):
        Lexical_Aux=""
        counter=0
        temp_status=0
        lenght_text = len(data_text)
        while counter<lenght_text:
            temp_character=data_text[counter]
            assci_code=ord(temp_character)
            self.status=temp_status
            counter+=1
            if (self.status==0):#STATE NUMBER 0
                if(assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122): #token LETTER
                    temp_status=1
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=Lexical_Aux
                    self.column+=1
                elif(assci_code>=48 and assci_code<=57):#TOKEN NUMBER 
                    temp_status=2
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=Lexical_Aux
                    self.column+=1
                elif(assci_code==43):#TOKEN +
                    temp_status=3
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=Lexical_Aux
                    self.column+=1
                elif(assci_code==45):#TOKEN -
                    temp_status=4
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=Lexical_Aux
                    self.column+=1
                elif(assci_code==42):#TOKEN *
                    temp_status=5
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=Lexical_Aux
                    self.column+=1
                elif(assci_code==47):#TOKEN  /
                    temp_status=6
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=Lexical_Aux
                    self.column+=1
                elif(assci_code==40):#TOKEN (
                    temp_status=7
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=Lexical_Aux
                    self.column+=1
                elif(assci_code==41):#TOKEN )
                    temp_status=8
                    Lexical_Aux+=temp_character
                    self.Data_text_temp+=Lexical_Aux
                    self.column+=1
                else:
                    if(assci_code>=00 and assci_code <=32 and assci_code!=10):
                        self.column+=1
                    elif(assci_code==10):#enter key
                        self.row+=1
                        self.column=0
                        if(self.Data_text_temp!=""):
                            self.Token_Array_Rmt_TEMP.append(Token(1,"#","Last-Token",self.row,self.column,""))
                            tmp_Rmt=Parser_Rmt()
                            self.result_board+="<tr>\n"+"<td>"+self.Data_text_temp+" Resultado: "+tmp_Rmt.parser_Rmt(self.Token_Array_Rmt_TEMP,self.Data_text_temp)+"</td>\n</tr>"
                            self.Token_Array_Rmt_TEMP.clear()
                            self.Data_text_temp=""
                    else: # means lexical Error founded
                        self.status=0
                        self.Errors_Html_Rmt.append(Lexical_Errors(self.row,self.column,temp_character,"The Symbol "+temp_character+"is not part of the Alphabet Language"))
                        self.column+=1
            elif(self.status==1):#STATE NUMBER 1
                if (assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122):# Letter
                    temp_status=1
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code>=48 and assci_code<=57):#number
                    temp_status=1
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code==95):# underScore or UnderLine
                    temp_status=1
                    Lexical_Aux+=temp_character
                    self.column+=1
                else:
                    self.Token_Array_Rmt.append(Token(1,Lexical_Aux,"Identifier",self.row,self.column,""))
                    self.Token_Array_Rmt_TEMP.append(Token(1,Lexical_Aux,"Identifier",self.row,self.column,""))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0 
            elif(self.status==2):#STATE NUMBER 2
                if(assci_code>=48 and assci_code<=57):#Token Number
                    temp_status=2
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif (assci_code==46):# Token .
                    temp_status=9
                    Lexical_Aux+=temp_character
                    self.column+=1
                else:
                    self.Token_Array_Rmt.append(Token(2,Lexical_Aux,"Int",self.row,self.column,""))
                    self.Token_Array_Rmt_TEMP.append(Token(2,Lexical_Aux,"Int",self.row,self.column,""))                    
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            elif(self.status==3):#STATE NUMBER 3
                self.Token_Array_Rmt.append(Token(3,Lexical_Aux,"Plus-Sign",self.row,self.column,""))
                self.Token_Array_Rmt_TEMP.append(Token(3,Lexical_Aux,"Plus-Sign",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==4):#STATE NUMBER 4
                self.Token_Array_Rmt.append(Token(4,Lexical_Aux,"Minus-Sign",self.row,self.column,""))
                self.Token_Array_Rmt_TEMP.append(Token(4,Lexical_Aux,"Minus-Sign",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==5):#STATE NUMBER 5
                self.Token_Array_Rmt.append(Token(5,Lexical_Aux,"Asterisk",self.row,self.column,""))
                self.Token_Array_Rmt_TEMP.append(Token(5,Lexical_Aux,"Asterisk",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==6):#STATE NUMBER 6
                self.Token_Array_Rmt.append(Token(6,Lexical_Aux,"forward-slash",self.row,self.column,""))
                self.Token_Array_Rmt_TEMP.append(Token(6,Lexical_Aux,"forward-slash",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==7):#STATE NUMBER 7
                self.Token_Array_Rmt.append(Token(7,Lexical_Aux,"Left parentheses",self.row,self.column,""))
                self.Token_Array_Rmt_TEMP.append(Token(7,Lexical_Aux,"Left parentheses",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==8):#STATE NUMBER 8
                self.Token_Array_Rmt.append(Token(8,Lexical_Aux,"Right parentheses",self.row,self.column,""))
                self.Token_Array_Rmt_TEMP.append(Token(8,Lexical_Aux,"Right parentheses",self.row,self.column,""))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==9):#STATE NUMBER 9
                if(assci_code>=48 and assci_code<=57):#Token Number
                    temp_status=10
                    Lexical_Aux+=temp_character
                    self.column+=1
                else:
                    self.status=0
                    self.Errors_Html_Rmt.append(Lexical_Errors(self.row,self.column,temp_character,"Need Numbre, Token Founded: "+temp_character+""))
                    self.column+=1
            elif(self.status==10):
                if(assci_code>=48 and assci_code<=57):#Token Number
                    temp_status=10
                    Lexical_Aux+=temp_character
                    self.column+=1
                else:
                    self.Token_Array_Rmt.append(Token(21,Lexical_Aux,"Float",self.row,self.column,""))
                    self.Token_Array_Rmt_TEMP.append(Token(21,Lexical_Aux,"Float",self.row,self.column,""))
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            else:
                print("ERROR ANALYZER")
        self.Report_Decision()    
            
        

    def clear_method(self):
        self.status=0
        self.Token_Array_Rmt.clear()
        self.Token_Array_Rmt_TEMP.clear()
        self.Errors_Html_Rmt.clear()
        self.Data_text_temp=""
        self.file_name=""
        self.result_board=""
        self.row=1
        self.column=0

     # ERRORS report snippet
    def print_SizeTokens_Errors(self):
        Error_string=""
        for index,erorrs_Values in enumerate(self.Errors_Html_Rmt):
            Error_string+="<tr>\n"+"<td>" + str(index)+"</td>\n<td>"+str(erorrs_Values.get_Row())+"</td>\n<td>"+str(erorrs_Values.get_Column()) +"</td>\n<td>" + erorrs_Values.get_Lex_Token()+"</td>\n<td>" + erorrs_Values.get_Details()+"</td>\n</tr>"
        return Error_string

    #Error Html Report
    def Errores_Report(self): 
        file_temp=open('Error_Rmt_Report.html','w')
        file_temp.write("<!doctype html>\n")
        file_temp.write("<html>\n")
        file_temp.write("<head>\n")
        file_temp.write("<meta charset="'"utf-8"'">\n")
        file_temp.write("<meta http-equiv="'"X-UA-Compatible"'" content="'"IE=edge"'">\n")
        file_temp.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"bootstrap.min.css\">\n")
        file_temp.write("<title>Errors Report</title>\n")
        file_temp.write("</head>\n")
        file_temp.write("<body>\n")
        file_temp.write("<h1 class="'"text-center"'"style="'"margin-top:20px;"'">Rmt Report (Errors) List</h1>\n")
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
        os.system('Error_Rmt_Report.html')



    def Rmt_Report_Parser(self): 
        file_temp=open('Rmt_Parser.html','w')
        file_temp.write("<!doctype html>\n")
        file_temp.write("<html>\n")
        file_temp.write("<head>\n")
        file_temp.write("<meta charset="'"utf-8"'">\n")
        file_temp.write("<meta http-equiv="'"X-UA-Compatible"'" content="'"IE=edge"'">\n")
        file_temp.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"bootstrap.min.css\">\n")
        file_temp.write("<title>Errors Report</title>\n")
        file_temp.write("</head>\n")
        file_temp.write("<body>\n")
        file_temp.write("<h1 class="'"text-center"'"style="'"margin-top:20px;"'">Rmt Report (Errors) List</h1>\n")
        file_temp.write("<div class="'"container"'" style="'"margin-top:20px;"'">\n")
        file_temp.write("<table class="'"table table-striped"'">\n")
        file_temp.write("<thead class="'"bg-dark"'" style="'"color:white;"'">\n")
        file_temp.write("<tr>\n")
        file_temp.write("<td><strong>Entrada</td>\n")
        file_temp.write("</tr>\n")
        file_temp.write("</thead>")
        file_temp.write("<tr>\n"+"</td>\n<td>"+self.result_board+"</td>\n</tr>")
        file_temp.write("</table>\n")
        file_temp.write("</div>")
        file_temp.write("</body>\n")
        file_temp.write("</html>\n")
        file_temp.close()
        os.system('Rmt_Parser.html')            


    def Report_Decision(self):
        if(len(self.Errors_Html_Rmt)==0):# clean Execution ( no errors founded !!!)
            self.Rmt_Report_Parser()
        else:
            self.Errores_Report()