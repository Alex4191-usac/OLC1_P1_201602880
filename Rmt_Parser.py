import os
import platform
from Token import Token
class Parser_Rmt:
    
    def __init__(self):
        self.post_analisys=None
        self.Data_tmp=""
        self.Token_List=[]
        self.correct_analysys="Correcto"
        self.open_list = ["("] 
        self.close_list = [")"] 
    
    def parser_Rmt(self,Lex_Rmt,Lex_temp):
        self.Data_tmp=Lex_temp
        self.Token_List=Lex_Rmt
        self.post_analisys=self.Token_List[0]
        self.num_before_analsys=0
        self.E()
        p_temp=self.check(self.Data_tmp)
        p_analysys=self.full_return(self.correct_analysys,p_temp)
        print("full analysys result:")
        print(p_analysys)
        

    
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
        else: 
            self.match("Identifier")

    def match(self,type_Token):
        if (type_Token!=self.post_analisys.get_TypeT()):
            self.correct_analysys="Incorrecto"
            print("se esperaba"+self.post_analisys.get_TypeT())
        if(self.post_analisys.get_TypeT()!="Last-Token"):
            self.num_before_analsys+=1
            self.post_analisys=self.Token_List[self.num_before_analsys]
            
    def check(self,myStr): 
        stack = [] 
        for i in myStr: 
            if i in self.open_list: 
                stack.append(i) 
            elif i in self.close_list: 
                pos = self.close_list.index(i) 
                if ((len(stack) > 0) and
                    (self.open_list[pos] == stack[len(stack)-1])): 
                    stack.pop() 
                else: 
                    return "Unbalanced"
        if len(stack) == 0: 
            return "Correcto"
        else: 
            return "Incorrecto"

    def full_return(self,parser,parentheses):
        if (parser==parentheses):
            return "Correcto"
        else:
           return "Incorrecto"