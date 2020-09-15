class Token:

       
    def __init__(self,id_Token, lex_Token, type_Token, row_Token, column_Token, index):
        self.id_Token=id_Token
        self.lex_Token=lex_Token
        self.type_Token=type_Token
        self.row_Token=row_Token
        self.column_Token=column_Token
        self.index=index
    
    def get_Id(self):
        return self.id_Token

    def get_Token(self):
        return self.lex_Token
    
    def get_TypeT(self):
        return self.type_Token
    
    def get_Row(self):
        return self.row_Token
    
    def get_Column(self):
        return self.column_Token

    def get_Index(self):
        return self.index
        
    Special_Tokens={
                0:'html',
                1:'head',
                2:'title',
                3:'body',
                4:'h1',
                5:'h2',
                6:'h3',
                7:'h4',
                8:'h5',
                9:'h6',
                10:'p',
                11:'img',
                12:'src',
                13:'a',
                14:'href',
                15:'ul',
                16:'li',
                17:'ol',
                18:'ul',
                19:'style',
                20:'table',
                21:'th',
                22:'tr',
                23:'caption',
                24:'section',
                25:'td',
                26:'colgroup',
                27:'col',
                28:'tbody',
                29:'tfoot',
                30:'footer',
                31:'script',
                32:'div',
                33:'class'
        }
    
    Special_Tokens_CSs={
        
        0:'color',
        1:'border',
        2:'text-align',
        3:'font-weight',
        4:'padding',
        5:'padding-left',
        6:'padding-right',
        7:'padding-top',
        8:'padding-bottom',
        9:'line-height',
        10:'margin-top',
        11:'margin-left',
        12:'display',
        13:'top',
        14:'float',
        15:'min-width',
        16:'background-color',
        17:'Opacity',
        18:'font-family',
        19:'font-size',
        20:'padding-right',
        21:'padding',
        22:'width',
        23:'margin-right',
        24:'margin',
        25:'position',
        26:'right',
        27:'clear',
        28:'max-height',
        29:'background-image',
        30:'background',
        31:'font-style',
        32:'font',
        33:'padding-bottom',
        34:'display',
        35:'height',
        36:'margint-bottom',
        37:'border-style',
        38:'bottom',
        39:'left',
        40:'max-width',
        41:'min-width'
        
        
    }

    Special_Tokens_Js={
        0:'if',
        1:'else',
        2:'for',
        3:'while',
        4:'do',
        5:'continue',
        6:'break',
        7:'return',
        8:'class',
        9:'constructor',
        10:'function'

    } 


    