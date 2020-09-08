import os
import platform
from Token import Token
from Errors import Lexical_Errors

class Rmt_Lex:

    def __init__(self):
        self.status=0
        self.Token_Array_Rmt = []
        self.Errors_Html_Rmt = []
        self.Data_text_temp=""
        self.file_name=""
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
            if (assci_code==0):#STATE NUMBER 0
                if(assci_code>=48 and assci_code<=57):#TOKEN NUMBER 
                        print("NUMBER")
                elif(assci_code>= 65 and assci_code<=90) or (assci_code>= 97 and assci_code<=122): #token LETTER
                        print("LETTER")
                elif(assci_code==43):#TOKEN +
                    print("PLUS")
                elif(assci_code==45):#TOKEN -
                    print("Minus")
                elif(assci_code==42):#TOKEN *
                    print("Asterisc")
                elif(assci_code==47):#TOKEN  /
                    print("forward-slash")
                elif(assci_code==40):#TOKEN (
                    print("PA")
                elif(assci_code==41):#TOKEN )
                    print("PC")
                else:
                    print("error") 
            else:
                print("ERROR ANALYZER")
            counter+=1