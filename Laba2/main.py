from classes import *


publisher = Publisher("Good Publisher")
publisher.json_save("pFirst.json")
publisher.json_load("ex.json")
publisher.json_save("p.json")

magazine = Magazine("PlayBoy")
magazine.json_save("mFirst.json")
magazine.json_load("ex2.json")
magazine.json_save("m.json")
