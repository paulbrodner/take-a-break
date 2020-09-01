import tkinter as tk
from time import sleep


class TakeABreak(object):
    __main = tk.Tk()

    def __init__(self):
        self.__main.bind('<Escape>', self.hide)
        self.__main.title("Take a Break!")
        self.focus()

    def show(self):
        self.__main.mainloop()

    def quit(self, event=None):
        self.__main.destroy()

    def focus(self):
        self.__main.attributes("-alpha", 1)
        self.__main.state('zoomed')

    def hide(self, event=None):
        alpha = self.__main.attributes("-alpha")
        if alpha > 0:
            alpha -= .1
            print(alpha)
            self.__main.attributes("-alpha", alpha)
            sleep(0.1)
            self.hide()
        else:
            self.__main.iconify()


if __name__ == '__main__':
    print("It's working...")
    TakeABreak().show()
