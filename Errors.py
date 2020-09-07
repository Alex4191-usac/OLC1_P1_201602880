class Lexical_Errors:

    def __init__(self,row_Token, column_Token, lex_Token,details):
        self.row_Token=row_Token
        self.column_Token=column_Token
        self.lex_Token=lex_Token
        self.details=details

    def get_Row(self):
        return self.row_Token
    
    def get_Column(self):
        return self.column_Token
    
    def get_Lex_Token(self):
        return self.lex_Token
    
    def get_Details(self):
        return self.details