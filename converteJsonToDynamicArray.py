from lib2to3.pytree import convert
from tkinter import *
import tkinter
from tkinter import font
from tkinter.scrolledtext import ScrolledText
     
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 50
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Converte JSON para TDynamicJSON")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # self.jsonLabel = Label(self.segundoContainer,text="Json", font=self.fontePadrao)
        # self.jsonLabel.pack()

        self.json = ScrolledText(self.segundoContainer, wrap=tkinter.WORD)
        self.json["width"] = 30
        self.json["font"] = self.fontePadrao
        self.json.pack(side=LEFT)

        # self.convertidoLabel = Label(self.segundoContainer, text="Convertido", font=self.fontePadrao)
        # self.convertidoLabel.pack()

        self.convertido = ScrolledText(self.segundoContainer, wrap=tkinter.WORD)
        self.convertido["width"] = 30
        self.convertido["font"] = self.fontePadrao
        self.convertido.pack(side=LEFT)

        self.converter = Button(self.terceiroContainer)
        self.converter["text"] = "Converter"
        self.converter["font"] = self.fontePadrao
        self.converter["width"] = 12
        self.converter["command"] = self.convertJson
        self.converter.pack()

        self.mensagem = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
    def convertJson(self):
        json = self.json.get('0.0', tkinter.END)
        isArray = False
        isObject = False
        convertedJson = "with vData do\nbegin\n"
        
        for line in json.splitlines():
            split = line.split(":")      
            # formattedText = split[0].replace(" ", "").replace(" ","").replace('"', "") 
            formattedText = split[0].strip().replace('"', "") 
                        
            if formattedText == '{':
                isObject = True
                continue
                    
            if formattedText == '],':
                isArray = False
                convertedJson += "   end;\n".format(formattedText)
                continue
            
            if formattedText == '},' or formattedText == '}':
                isObject = False
                continue
            
            if len(split) > 1:
                formattedValue = split[1].strip().replace('"', "")
                if formattedValue == '[':
                    isArray = True
                    convertedJson += "   with AddItem('{}') do\n   begin\n".format(formattedText)
                    continue
            
                if len(formattedText) > 1 and not formattedText.endswith(','): 
                    if isArray and isObject:
                        convertedJson += "      AddField('{}').value := nil; \n".format(formattedText)
                    else:
                        convertedJson += "   AddField('{}').value := nil; \n".format(formattedText)
          
        convertedJson += "end;\n"            
        self.convertido.delete('0.0', tkinter.END)
        self.convertido.insert('0.0', convertedJson)

root = Tk()
Application(root)
root.mainloop()