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
        self.row=1
        self.column=0

    def Analyze_text_Rmt(self,data_text):
        Lexical_Aux=""
        counter=0
        temp_status=0
        print("DATA TEXT IS")
        print(data_text)
        lenght_text = len(data_text)
        while counter<lenght_text:
            temp_character=data_text[counter]
            print(temp_character)
            assci_code=ord(temp_character)
            self.status=temp_status
            print(assci_code)
            counter+=1
            if (self.status==0):#STATE NUMBER 0
                if(assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122): #token LETTER
                    temp_status=1
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code>=48 and assci_code<=57):#TOKEN NUMBER 
                    temp_status=2
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code==43):#TOKEN +
                    temp_status=3
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code==45):#TOKEN -
                    temp_status=4
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code==42):#TOKEN *
                    temp_status=5
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code==47):#TOKEN  /
                    temp_status=6
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code==40):#TOKEN (
                    temp_status=7
                    Lexical_Aux+=temp_character
                    self.column+=1
                elif(assci_code==41):#TOKEN )
                    temp_status=8
                    Lexical_Aux+=temp_character
                    self.column+=1
                else:
                    if(assci_code>=00 and assci_code <=32 and assci_code!=10):
                        self.column+=1
                    elif(assci_code==10):#enter key
                        self.Token_Array_Rmt_TEMP.append(Token(1,Lexical_Aux,"Last-Token",self.row,self.column))
                        self.row+=1
                        self.column=0
                        tmp_Rmt=Parser_Rmt()
                        self.Data_text_temp+=tmp_Rmt.parser_Rmt(self.Token_Array_Rmt_TEMP)+"\n"
                        self.Token_Array_Rmt_TEMP.clear()
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
                    self.Token_Array_Rmt.append(Token(1,Lexical_Aux,"Identifier",self.row,self.column))
                    self.Token_Array_Rmt_TEMP.append(Token(1,Lexical_Aux,"Identifier",self.row,self.column))
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
                    self.Token_Array_Rmt.append(Token(2,Lexical_Aux,"Int",self.row,self.column))
                    self.Token_Array_Rmt_TEMP.append(Token(2,Lexical_Aux,"Int",self.row,self.column))                    
                    Lexical_Aux=""
                    counter-=1
                    temp_status=0
            elif(self.status==3):#STATE NUMBER 3
                self.Token_Array_Rmt.append(Token(3,Lexical_Aux,"Plus-Sign",self.row,self.column))
                self.Token_Array_Rmt_TEMP.append(Token(3,Lexical_Aux,"Plus-Sign",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==4):#STATE NUMBER 4
                self.Token_Array_Rmt.append(Token(4,Lexical_Aux,"Minus-Sign",self.row,self.column))
                self.Token_Array_Rmt_TEMP.append(Token(4,Lexical_Aux,"Minus-Sign",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==5):#STATE NUMBER 5
                self.Token_Array_Rmt.append(Token(5,Lexical_Aux,"Asterisk",self.row,self.column))
                self.Token_Array_Rmt_TEMP.append(Token(5,Lexical_Aux,"Asterisk",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==6):#STATE NUMBER 6
                self.Token_Array_Rmt.append(Token(6,Lexical_Aux,"forward-slash",self.row,self.column))
                self.Token_Array_Rmt_TEMP.append(Token(6,Lexical_Aux,"forward-slash",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==7):#STATE NUMBER 7
                self.Token_Array_Rmt.append(Token(7,Lexical_Aux,"Left parentheses",self.row,self.column))
                self.Token_Array_Rmt_TEMP.append(Token(7,Lexical_Aux,"Left parentheses",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==8):#STATE NUMBER 8
                self.Token_Array_Rmt.append(Token(8,Lexical_Aux,"Right parentheses",self.row,self.column))
                self.Token_Array_Rmt_TEMP.append(Token(8,Lexical_Aux,"Right parentheses",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            elif(self.status==9):#STATE NUMBER 9
                self.Token_Array_Rmt.append(Token(21,Lexical_Aux,"Float",self.row,self.column))
                self.Token_Array_Rmt_TEMP.append(Token(21,Lexical_Aux,"Float",self.row,self.column))
                Lexical_Aux=""
                counter-=1
                temp_status=0
            else:
                print("ERROR ANALYZER")
            
            
        

    def clear_method(self):
        self.status=0
        self.Token_Array_Rmt.clear()
        self.Token_Array_Rmt_TEMP.clear()
        self.Errors_Html_Rmt.clear()
        self.Data_text_temp=""
        self.file_name=""
        self.row=1
        self.column=0