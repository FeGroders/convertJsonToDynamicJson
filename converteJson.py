from tkinter import *
import tkinter
from tkinter import font
from tkinter.scrolledtext import ScrolledText

def convertJson(json):
    texto = ''
    isArray = False
    for line in json.splitlines():
        split = line.split(":")      
        textoFormatado = split[0].replace(" ", "").replace('"', "")
        if len(split) > 1:
            valorFormatado = split[1].replace(" ", "")
            if valorFormatado == '[' or valorFormatado == '{':
                isArray = True
                texto += "with vData.AddField('{}') do\nbegin\n".format(textoFormatado)
                continue
                
        if textoFormatado == '],' or textoFormatado == '},':
            isArray = False
            texto += "end;\n".format(textoFormatado)
            continue
        
        if len(textoFormatado) > 1 and not textoFormatado.endswith(','): 
            if isArray:
                texto += "   AddField('{}').value := nil; \n".format(textoFormatado)
            else:
                texto += "vData.AddField('{}').value := nil; \n".format(textoFormatado)
    return texto       

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
        self.converter["command"] = self.converteJson
        self.converter.pack()

        self.mensagem = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def converteJson(self):
        json = self.json.get('0.0', tkinter.END)
        jsonConvertido = convertJson(json)
        self.convertido.delete('0.0', tkinter.END)
        self.convertido.insert('0.0', jsonConvertido)

root = Tk()
Application(root)
root.mainloop()