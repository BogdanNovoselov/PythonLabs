from classes import *


printing = Printing("Winnie Pooh")
printing.json_save("pFirst.json")
printing.json_load("ex.json")
printing.json_save("p.json")

magazine = Magazine("Forbes")
magazine.json_save("mFirst.json")
magazine.json_load("ex2.json")
magazine.json_save("m.json")
