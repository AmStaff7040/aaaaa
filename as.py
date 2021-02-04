import time
import keyboard
import pyautogui
from PIL import Image, ImageGrab
import random
import os
def spawn():
    print("Début dans 5 secondes...")
    time.sleep(5)
    fish = False
    pause = round(random.uniform(150, 350))
    ps = 0
    cas = 0
    fuite = 0
    while True:
        E = False
        A = False
        B = False
        time.sleep(0.3)
        s = pyautogui.screenshot(region=(650,550, 500, 500))
        s.save(r"C:\aa\entree.png")
        im1 = Image.open(r"C:\aa\entree.png")
        color = (200, 80, 64)
        color2 = (198, 79, 63)
        color3 = (197, 79, 63)
        color4 = (196, 79, 63)
        color5 = (195, 79, 63)
        for x in range(s.width):
            for y in range(s.height):
                if E == False:
                    if im1.getpixel((x,y)) == color or im1.getpixel((x,y)) == color2 or im1.getpixel((x,y)) == color3 or im1.getpixel((x,y)) == color4 or im1.getpixel((x,y)) == color5:
                        keyboard.press("a")
                        time.sleep(2)
                        keyboard.release("a")
                        fish = False
                        print("ENTREE DU SAFARI DETECTE")
                        Paths = [1, 2, 3]
                        rdm = random.choice(Paths)
                        print ("EN CHEMIN...")
                        if rdm == 1:
                            print("CHEMIN 1 CHOISI")
                            time.sleep(3)
                            keyboard.press("z")
                            time.sleep(0.2)
                            keyboard.release("z")
                            time.sleep(random.uniform(0.3, 6))
                            keyboard.press("d")
                            time.sleep(0.6)
                            keyboard.release("d")
                            time.sleep(0.3)
                            keyboard.press("a")
                            time.sleep(3)
                            keyboard.release("a")
                            time.sleep(random.uniform(3, 4))
                            #path1
                            keyboard.press("z")
                            time.sleep(2.3)
                            keyboard.release("z")
                            time.sleep(0.3)
                            keyboard.press("d")
                            time.sleep(1.6)
                            keyboard.release("d")
                            keyboard.press("z")
                            time.sleep(0.6)
                            keyboard.release("z")
                            time.sleep(2)
                            fish = True
                        elif rdm == 2:
                            print("CHEMIN 2 CHOISI")
                            time.sleep(3)
                            keyboard.press("z")
                            time.sleep(0.2)
                            keyboard.release("z")
                            time.sleep(random.uniform(0.3, 6))
                            keyboard.press("d")
                            time.sleep(0.6)
                            keyboard.release("d")
                            time.sleep(0.3)
                            keyboard.press("a")
                            time.sleep(3)
                            keyboard.release("a")
                            time.sleep(random.uniform(3, 4))
                            #path2
                            keyboard.press("z")
                            time.sleep(0.7)
                            keyboard.release("z")
                            time.sleep(random.uniform(0.3, 0.8))
                            keyboard.press("d")
                            time.sleep(1.5)
                            keyboard.release("d")
                            time.sleep(random.uniform(0.3, 0.8))
                            keyboard.press("z")
                            time.sleep(0.3)
                            keyboard.release("z")
                            time.sleep(random.uniform(0.3, 0.8))
                            keyboard.press("d")
                            time.sleep(0.3)
                            keyboard.release("d")
                            time.sleep(random.uniform(0.3, 0.8))
                            keyboard.press("z")
                            time.sleep(1.4)
                            keyboard.release("z")
                            time.sleep(random.uniform(0.3, 0.8))
                            keyboard.press("q")
                            time.sleep(0.3)
                            keyboard.release("q")
                            time.sleep(random.uniform(0.3, 0.8))
                            keyboard.press("z")
                            time.sleep(0.6)
                            keyboard.release("z")
                            time.sleep(2)
                            fish = True
                        elif rdm == 3:
                            print("CHEMIN 3 CHOISI")
                            time.sleep(3)
                            keyboard.press("z")
                            time.sleep(0.2)
                            keyboard.release("z")
                            time.sleep(random.uniform(0.3, 6))
                            keyboard.press("d")
                            time.sleep(0.6)
                            keyboard.release("d")
                            time.sleep(0.3)
                            keyboard.press("a")
                            time.sleep(5)
                            keyboard.release("a")
                            time.sleep(random.uniform(3, 4))
                            #path3
                            keyboard.press("d")
                            time.sleep(0.3)
                            keyboard.release("d")
                            time.sleep(random.uniform(0.3, 0.8))  
                            keyboard.press("z")
                            time.sleep(2)
                            keyboard.release("z")
                            time.sleep(random.uniform(0.3, 0.8))
                            keyboard.press("d")
                            time.sleep(1.2)
                            keyboard.release("d")
                            time.sleep(random.uniform(0.3, 0.8))
                            keyboard.press("z")
                            time.sleep(0.9)
                            keyboard.release("z")
                            time.sleep(2)
                            fish = True
                        E = True
        fish = True
        ca2 = pyautogui.screenshot(region=(1000,200, 30, 30))
        ca2.save(r"C:\aa\ca2.png")
        im6 = Image.open(r"C:\aa\ca2.png")
        colorcaca = (0, 0, 0)
        for x in range(ca2.width):
            for y in range(ca2.height):
                    if B == False:
                        if fish == True:
                            if im6.getpixel((x,y)) == colorcaca:
                                    fuite = fuite + 1
                                    print(fuite)
                                    H = random.uniform(30, 45)
                                    if fuite >= H:
                                            print("PLUS DE POKEBALLS, SORTIE DU SAFARI!")
                                            keyboard.press("d")
                                            keyboard.release("d")
                                            time.sleep(0.2)
                                            keyboard.press("s")
                                            keyboard.release("s")
                                            B = True
                                    B = True
                            else:
                                    fuite = 0
                                

        ca = pyautogui.screenshot(region=(700,180, 500, 500))
        ca.save(r"C:\aa\ca.png")
        im5 = Image.open(r"C:\aa\ca.png")
        colorca = (103, 109, 111)
        colorca2 = (105, 110, 112)
        colorca3 = (54,58,62)
        colorca4 = (52,56,60)
        colorca5 = (40,47,51)
        for x in range(ca.width):
            for y in range(ca.height):
                if A == False:
                    if im5.getpixel((x,y)) == colorca or im5.getpixel((x,y)) == colorca2 or im5.getpixel((x,y)) == colorca3 or im5.getpixel((x,y)) == colorca4 or im5.getpixel((x,y)) == colorca5:
                        keyboard.press("x")
                        keyboard.release("x")
                        keyboard.press("x")
                        keyboard.release("x")
                        keyboard.press("x")
                        keyboard.release("x")
                        cas = cas + 1
                        A = True
        if ps >= pause:
            print("EN PAUSE... VEUILLEZ PATIENTER")
            ps = 0
            time.sleep(random.uniform(60, 360))
        if fish == True:
            ps = ps + 1
            os.system('cls')
            print("EN TRAIN DE PÊCHER!")
            print ("[", str(cas), " MAGICARPES", "]", "CAPTURES!", sep='')
            print ("[", str(ps), "/", str(pause), "]", "AVANT LA PAUSE!", sep='')
            keyboard.press("f")
            keyboard.release("f")
            keyboard.press("a") 
            keyboard.release("a")
            time.sleep(random.uniform(1, 3))
spawn()

        
#9z
#6d
#2z
