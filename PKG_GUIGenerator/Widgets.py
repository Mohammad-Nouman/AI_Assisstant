from PKG_GUIGenerator.Connector import *


connection = Connector()
connection.connect()

class Widgets:
    def __init__(self):
        self.__col = None
        self.__row = None
        self.__x = None
        self.__y = None
        self.__fill = None
        self.__pad = None
        self.__ipad = None
        self.__side = None

    def setGrid(self, col, row):
        self.__col = col
        self.__row = row

    def setPlace(self, x, y):
        self.__x = x
        self.__y = y

    def setPack(self, side, fill, pad, ipad):
        self.__side = side
        self.__fill = fill
        self.__pad = pad
        self.__ipad = ipad

    def getGrid(self):
        return f'.grid(column={self.__col},row={self.__row})\n\n'

    def getPlace(self):
        return f'.place(x={self.__x},y={self.__y})\n\n'

    def getPack(self):
        if self.__fill == 'X':
            return f'.pack(side = {self.__side},fill=X,pady = {self.__pad},ipady ={self.__ipad})\n\n'
        else:
            return f'.pack(side = {self.__side},fill=Y,padx = {self.__pad},ipadx ={self.__ipad})\n\n'

    def setLayout(self, layout):
        if layout == 'grid':
            return self.getGrid()
        elif layout == 'place':
            return self.getPlace()
        elif layout == 'pack':
            return self.getPack()

    def getCol(self):
        return self.__col

    def getRow(self):
        return self.__row

    def removeAllLabelsData(self):
        # connection.removeTableData("label")
        pass


class Frame:
    def __init__(self, name, bg, boder, boderWidth):
        self.__backGround = bg
        self.__border = boder
        self.__BoderWidth = boderWidth
        self.__name = name

    def getFrame(self):
        return f'frame{self.__name} = Frame(' \
               f'border =  {self.__border},borderwidth={self.__BoderWidth})\n'

    def packFrame(self, side, fill, pad, ipad):
        if fill == 'X':
            return f'frame{self.__name}.pack(side = {side},fill=X,pady = {pad},ipady ={ipad})\n\n'
        else:
            return f'frame{self.__name}.pack(side = {side},fill=Y,padx = {pad},ipadx ={ipad})\n\n'

    def placeFrameInCenter(self):
        return f'frame{self.__name}.place(relx=.5,rely=.5,anchor= CENTER)\n\n'


class Screen():
    def __init__(self, title, height, width):
        self.__title = title
        self.__height = height
        self.__width = width

    def getString(self):
        return f'from tkinter import *\n' \
               f'from tkinter.ttk import *\n' \
               f'from tkinter import scrolledtext\n' \
               f'from tkinter import messagebox\n\n' \
               f'window = Tk()\n' \
               f'window.title("{self.__title}")\n\n' \
               f'window.geometry("{self.__height}x{self.__width}")\n\n'


class Label(Widgets):
    def __init__(self, frameName, name, text, layout):
        super().__init__()
        self.__name = name
        self.__text = text
        self.frameName = frameName
        self.layout = layout

    def getString(self):
        # self.storeLabel()
        command = f'label{self.__name} = Label({self.frameName},text="{self.__text}")\n' \
                  f'label{self.__name}' + self.setLayout(self.layout)
        return command

    def storeLabel(self):
        connection.insertLabel(self.__name, self.getRow(), self.getCol(), self.__text)


class Entry(Widgets):
    def __init__(self, frameName, name, width, layout):
        super().__init__()
        self.__width = width
        self.__frameName = frameName
        self.__name = name
        self.layout = layout

    def getString(self):
        return f'entry{self.__name} = Entry({self.__frameName},width={self.__width})\n' \
               f'entry{self.__name}' + self.setLayout(self.layout)


class MessageBox(Widgets):
    def __init__(self, name, title, text):
        super().__init__()
        self.__title = title
        self.__name = name
        self.__text = text

    def getString(self):
        return f'messageBox{self.__name}  = messagebox.showinfo("{self.__title}","{self.__text}")\n'



class ComboBox(Widgets):
    def __init__(self, frameName, name, values, layout):
        super().__init__()
        self.__values = values
        self.__frameName = frameName
        self.__name = name
        self.layout = layout

    def getString(self):
        return f'combobox{self.__name} = Combobox()\ncombobox{self.__name}["values"] = {self.__values}\n'\
               f'combobox{self.__name}' + self.setLayout(self.layout)


class CheckBox(Widgets):
    def __init__(self, frameName, name, text, layout):
        super().__init__()
        self.__name = name
        self.__text = text
        self.frameName = frameName
        self.layout = layout

    def getString(self):
        # self.storeLabel()
        command = f'checkBtn{self.__name} = Checkbutton({self.frameName},text="{self.__text}")\n' \
                  f'checkBtn{self.__name}' + self.setLayout(self.layout)
        return command


class RadioButton(Widgets):
    def __init__(self, frameName, name, text, value, layout):
        super().__init__()
        self.__name = name
        self.__text = text
        self.frameName = frameName
        self.layout = layout
        self.__value = value

    def getString(self):
        # self.storeLabel()
        command = f'radioBtn{self.__name} = Radiobutton({self.frameName},text="{self.__text}",value = {self.__value})\n' \
                  f'radioBtn{self.__name}' + self.setLayout(self.layout)
        return command


class ScrolledText(Widgets):
    def __init__(self, frameName, name, width, height, text, layout):
        super().__init__()
        self.__name = name
        self.__width = width
        self.__text = text
        self.frameName = frameName
        self.layout = layout
        self.__height = height

    def getString(self):
        # self.storeLabel()
        command = f'scrollTxt{self.__name} = scrolledtext.ScrolledText({self.frameName},width = {self.__width},height = {self.__height})\n' \
                  f'scrollTxt{self.__name}.insert(INSERT,"{self.__text}")\n' \
                  f'scrollTxt{self.__name}' + self.setLayout(self.layout)
        return command


class SpinBox(Widgets):
    def __init__(self, frameName, name, width, min, max, layout):
        super().__init__()
        self.__name = name
        self.__width = width
        self.__min = min
        self.frameName = frameName
        self.layout = layout
        self.__max = max

    def getString(self):
        # self.storeLabel()
        command = f'spinBox{self.__name} = Spinbox({self.frameName},from_={self.__min},to={self.__min},width ={self.__width})\n' \
                  f'spinBox{self.__name}' + self.setLayout(self.layout)
        return command

