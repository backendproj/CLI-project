# Humoyun va Ibrohim aka
import os 
import time
import termcolor

class Animation:
    def __init__(self) -> None:
        pass
    def loading(self):
        while True:
            frame = ["|", "/", "-", "\\"]
            for x in frame:
                os.system("cls")
                print(termcolor.colored(x,"green"))
                time.sleep(0.2)
    def number(self):
        numbers1 = "01234"
        numbers2 = "56789"
        for i in numbers1:
            print(termcolor.colored(i,"red"))
            time.sleep(0.5)
        for x in numbers2:
            print(termcolor.colored(x,"green"))
            time.sleep(0.5)
    def ravno1(self):
        frame1 = [
            " |=     |",
            " | =    |",
            " |  =   |",
            " |   =  |",
            " |    = |",
            " |     =|",
            " |    = |",
            " |   =  |",
            " |  =   |",
            " | =    |",
        ]
        while True:
            for i in frame1:
                print(i,end = "\r")
                time.sleep(0.2)
    def ravno2(swlf):
        frame2 = [
            " |        |",
            " |=       |",
            " |===     |",
            " |====    |",
            " |=====   |",
            " |======  |",
            " |======= |",
            " |========|",
            " | =======|",
            " |  ======|",
            " |   =====|",
            " |    ====|",
            " |     ===|",
            " |      ==|",
            " |       =|",
            " |        |",
            " |        |",
        ]
        while True:
            for i in frame2:
                print(i,end = "\r")
                time.sleep(0.2)
loading = Animation()
loading.loading()
loading.ravno1()
# loading.ravno2()
# loading.number()
