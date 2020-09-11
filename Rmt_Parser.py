import os
import platform
from Token import Token
class Parser_Rmt:
    
    def __init__(self):
        self.num_before_analsys=0
        self.post_analisys=None
        self.Token_List=[]
        self.correct_analysys=""
    
    def parser_Rmt(self,Lex_Rmt):
        self.Token_List=Lex_Rmt
        self.post_analisys=self.Token_List[0]
        self.E()
        return self.correct_analysys

    
    def E(self):
        self.T()
        self.EP()
     
    def EP(self):
        if (self.post_analisys.get_TypeT()=="Plus-Sign"):
            self.match("Plus-Sign")
            self.T()
            self.EP()
        elif(self.post_analisys.get_TypeT()=="Minus-Sign"):
            self.match("Minus-Sign")
            self.T()
            self.EP()
    
    def T(self):
        self.F()
        self.TP()

    def TP(self):
        if (self.post_analisys.get_TypeT()=="Asterisk"):
            self.match("Asterisk")
            self.F()
            self.TP()
        elif (self.post_analisys.get_TypeT()=="forward-slash"):
            self.match("forward-slash")
            self.F()
            self.TP()
    
    def F(self):
        if (self.post_analisys.get_TypeT()=="Left parentheses"):
            self.match("Left parentheses")
            self.E()
            self.match("Right parentheses")
       
        elif(self.post_analisys.get_TypeT()=="Int"):
            self.match("Int")
        elif(self.post_analisys.get_TypeT()=="Float"):
            self.match("Float")
        elif(self.post_analisys.get_TypeT()=="Identifier"):
            self.match("Identifier")
        else:
            print("vacio")

    def match(self,type_Token):
        if (type_Token!=self.post_analisys.get_TypeT()):
            self.correct_analysys="INCORRECTO"
            print("INCORRECTO")
        if(self.post_analisys.get_TypeT()!="Last-Token"):
            self.num_before_analsys+=1
            self.post_analisys=self.Token_List[self.num_before_analsys]
            
