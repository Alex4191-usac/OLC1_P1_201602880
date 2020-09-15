from tkinter import Tk,Menu,scrolledtext,END,filedialog,INSERT,messagebox
from Html_Analyzer import Html_lex
from Js_Analyzer import Js_Lex
from Css_Analyzer import Css_Lex
from Rmt_Analyzer import Rmt_Lex
class Window_app:
     
    text_area=None
    text_console=None
    type_Analizer=None
    name_file=""
    file_open=None
    def __init__(self,gui_window):
        self.gui_window = gui_window
        self.gui_window.title('HTML, CSS & JS COMPILER')
        self.gui_window.geometry("1200x720")
        self.gui_window.configure(bg='#3d405b')
        self.text_area = scrolledtext.ScrolledText(gui_window, width=80, height=40,bg='#edf2f4')
        self.text_area.grid(column=0,row=0, pady=30,padx=20)
       
        self.text_console= scrolledtext.ScrolledText(gui_window, width=50, height=40,bg='#000000',foreground='#aacc00')
        self.text_console.grid(column=1,row=0, pady=20,padx=20)
        self.text_area.focus()
        menu_bar=Menu(gui_window)
        self.gui_window.config(menu=menu_bar)

        file_menu=Menu(menu_bar,tearoff=0)
        file_menu.add_command(label="New",command=self.New_Data)
        file_menu.add_command(label="Open",command=self.Open_Data)
        file_menu.add_command(label="Save",command=self.save_file)
        file_menu.add_command(label="Save As",command=self.save_As)
        tools_menu=Menu(menu_bar,tearoff=0)
        help_menu=Menu(menu_bar,tearoff=0)
        
        #Creating tag for Each Principal Element of the Menu

        tools_menu=Menu(menu_bar, tearoff=0)
        tools_menu.add_command(label="Analyze",command=self.Analyzer)

        menu_bar.add_cascade(label="File",menu=file_menu)
        menu_bar.add_cascade(label="Tools",menu=tools_menu)
        menu_bar.add_cascade(label="Help",menu=help_menu)

        global temp_htmlAnalyzer,temp_jsAnalizer,temp_CssAnalyzer,temp_RmtAnalyzer
        temp_htmlAnalyzer = Html_lex()
        temp_jsAnalizer = Js_Lex()
        temp_CssAnalyzer = Css_Lex()
        temp_RmtAnalyzer = Rmt_Lex()
        
        #class instance's
   

    def New_Data(self):
        self.text_area.delete(1.0,END)
        self.text_console.delete(1.0,END)

    
    def Open_Data(self):
        try:
            self.name_file=""
            self.file_open = filedialog.askopenfilename(title = "Open File", initialdir = "C:/",filetypes=[("JavaScript Files","*.js"),
            ("Html Files","*.html"),("Css Files","*.css"),("Rmt Files","*.rmt")])
            text_data = open(self.file_open, encoding='utf-8')
            data_extension=str(text_data.name)
            sub_name=text_data.name.split("/")
            self.name_file=sub_name[len(sub_name)-1]

            if(data_extension.endswith('.js')):
                self.type_Analizer="js"
                print("JAVASCRIPT ANALYZER ON")
            elif(data_extension.endswith('.html')):
                print("HTML ANALYZER ON")
                self.type_Analizer="html"
            elif(data_extension.endswith('.css')):
                print("CSS ANALYZER ON")
                self.type_Analizer="css"
            elif(data_extension.endswith('.rmt')):
                print("RMT ANALYZER ON")
                self.type_Analizer="rmt"    
            else:
                print("THERE'S NO EXTENSION")
                self.type_Analizer=""
        except FileNotFoundError:
            print("File not Found")
            data_extension=""
            text_data=""
            
        if(data_extension!=""):
            content = text_data.read()
            self.text_area.delete(1.0, END)
            self.text_area.insert(INSERT, content)
            text_data.close()
        else:
            self.text_area.delete(1.0, END)
            
           
                
            
#save file as data method
    def save_As(self):
        save_a=filedialog.asksaveasfilename(title="Save File", initialdir="C:/")
        open_buffer_save=open(save_a,"w+")
        open_buffer_save.write(self.text_area.get(1.0,END))
        open_buffer_save.close()
        self.file_open=save_a

#save file data method
    def save_file(self):
        if self.file_open is None:
            self.save_As()
        else:
            open_buffer=open(self.file_open,"w")
            open_buffer.write(self.text_area.get(1.0,END))
            open_buffer.close()

#FOREGROUND CHANGE COLOR:
    def Tokens_Color(self,Array_Tokens):
        print("VA A PINTAR TOKENS")
        for index,Token_List in enumerate(Array_Tokens): 
            if (Token_List.get_TypeT()=="Reserved Keyword"):
                self.text_area.tag_add(str(index)+Token_List.get_Token(),str(Token_List.get_Row())+"."+str(Token_List.get_Column()-len(Token_List.get_Token())),str(Token_List.get_Row())+"."+str(Token_List.get_Column()))
                self.text_area.tag_config(str(index)+Token_List.get_Token(), foreground="red")    
            elif(Token_List.get_TypeT()=="Double Quote comment" or Token_List.get_TypeT()=="Single Quote comment"):
                self.text_area.tag_add(str(index)+Token_List.get_Token(),str(Token_List.get_Row())+"."+str(Token_List.get_Column()-len(Token_List.get_Token())),str(Token_List.get_Row())+"."+str(Token_List.get_Column()))
                self.text_area.tag_config(str(index)+Token_List.get_Token(), foreground="yellow")
            elif(Token_List.get_TypeT()=="multiline comment"):
                self.text_area.tag_add(str(index)+Token_List.get_Token(),Token_List.get_Index(),str(Token_List.get_Row())+"."+str(Token_List.get_Column()))
                self.text_area.tag_config(str(index)+Token_List.get_Token(), foreground="gray")
            elif(Token_List.get_TypeT()=="single comment"):
                self.text_area.tag_add(str(index)+Token_List.get_Token(),str(Token_List.get_Row())+"."+str(Token_List.get_Column()-len(Token_List.get_Token())),str(Token_List.get_Row())+"."+str(Token_List.get_Column()))
                self.text_area.tag_config(str(index)+Token_List.get_Token(), foreground="gray")
            elif(Token_List.get_TypeT()=="forward-slash"or Token_List.get_TypeT()=="Equality sign" or Token_List.get_TypeT()=="Asterisk" or 
            Token_List.get_TypeT()=="Minus-sing" or Token_List.get_TypeT()=="Plus-sign" or Token_List.get_TypeT()=="Percent" or Token_List.get_TypeT()=="Right parentheses" or
            Token_List.get_TypeT()=="Left parentheses" or Token_List.get_TypeT()=="Less-than sign" or Token_List.get_TypeT()=="greater-than sign" or Token_List.get_TypeT()=="or" or
            Token_List.get_TypeT()=="not" or Token_List.get_TypeT()=="and"): 
                self.text_area.tag_add(str(index)+Token_List.get_Token(),str(Token_List.get_Row())+"."+str(Token_List.get_Column()-len(Token_List.get_Token())),str(Token_List.get_Row())+"."+str(Token_List.get_Column()))
                self.text_area.tag_config(str(index)+Token_List.get_Token(), foreground="orange")
            elif(Token_List.get_TypeT()=="Int" or Token_List.get_TypeT()=="Float"):
                self.text_area.tag_add(str(index)+Token_List.get_Token(),str(Token_List.get_Row())+"."+str(Token_List.get_Column()-len(Token_List.get_Token())),str(Token_List.get_Row())+"."+str(Token_List.get_Column()))
                self.text_area.tag_config(str(index)+Token_List.get_Token(), foreground="blue")
            elif(Token_List.get_TypeT()=="Identifier"):
                self.text_area.tag_add(str(index)+Token_List.get_Token(),str(Token_List.get_Row())+"."+str(Token_List.get_Column()-len(Token_List.get_Token())),str(Token_List.get_Row())+"."+str(Token_List.get_Column()))
                self.text_area.tag_config(str(index)+Token_List.get_Token(), foreground="green")
            else:
                pass

   #Analyzer call function 
    def Analyzer(self):

        #CLEANS ALL VARIABLES OF EACH CLASS
        temp_jsAnalizer.clear_method()
        temp_htmlAnalyzer.clear_method()
        temp_CssAnalyzer.clear_method()
        temp_RmtAnalyzer.clear_method()
    

    #test js
        temp_jsAnalizer.Analyze_text_Js(self.text_area.get(1.0,END),self.name_file)
        self.Tokens_Color(temp_jsAnalizer.Token_Array_Js)
        
        """if(self.type_Analizer=="js"):
            temp_jsAnalizer.Analyze_text_Js(self.text_area.get(1.0,END),self.name_file)
            self.Tokens_Color(temp_jsAnalizer.Token_Array_Js)
        elif(self.type_Analizer=="html"):
            temp_htmlAnalyzer.Analyze_text(self.text_area.get(1.0, END),self.name_file)
            self.Tokens_Color(temp_htmlAnalyzer.Token_Array)
        elif(self.type_Analizer=="css"):
            temp_CssAnalyzer.Analyze_text(self.text_area.get(1.0, END))
            self.Tokens_Color(temp_CssAnalyzer.Token_Array_Css)
            self.text_console.insert(INSERT, temp_CssAnalyzer.Log_Analyzer)
        elif(self.type_Analizer=="rmt"):
            temp_RmtAnalyzer.Analyze_text_Rmt(self.text_area.get(1.0, END))
            self.Tokens_Color(temp_RmtAnalyzer.Token_Array_Rmt)
            self.text_console.insert(INSERT, temp_RmtAnalyzer.result_board)
            
        else:
            messagebox.showerror(title="Warning", message="There's no File to Analyze")"""

if __name__ == "__main__":
    gui_window = Tk()
    app = Window_app(gui_window)
    gui_window.mainloop()
