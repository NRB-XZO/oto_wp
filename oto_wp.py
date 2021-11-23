import pywhatkit as kit
import datetime
import random
import pyautogui
from time import sleep
nm = str()
while True:
    try:
        number_RETK_country = 90
        number_RETK2_one = [542, 530, 538, 546, 543, 534, 553]
        str_nmb = "+{}{}{}{}{}".format(number_RETK_country, number_RETK2_one[random.randint(0, 6)],
                                       random.randint(100, 999), random.randint(10, 99), random.randint(10, 99))
        print(str_nmb)
        kit.sendwhatmsg(str_nmb,"Merhaba, *22.11.2021* tarihinde *Bosch elektrikli ev aletleri* sponsorlugunda düzenledigimiz ay sonu cekilisimizde *Beyza Onder* adli kisinin etiketi sayesinde *Bosch Bbs61pet2 18 V Dikey Şarjlı Süpürge BBS61PET2*
kazandiniz. Siparis onayi icin asagidaki yonlendirmeyi kullaniniz. İlet: https://bit.ly/3r6RKlY", datetime.datetime.now().hour,
                        datetime.datetime.now().minute + 1)
        print("[+] {} successfully sent".format(nm))
        sleep(5)
        pyautogui.hotkey('ctrl', 'w')
    except:
        print("[!] {} Message could not be sent".format(nm))
