
import time , sys , os , pickle , colorama , random
from colorama import Fore, Back, Style
from colorama import init
init()
kol2 = random.randint(5,7)


def banner3():
  print(Fore.YELLOW)
  banner2 = """
┏━━━┓  ┏━━━┓  ┏━━┓      ┏━━┓       ┏━━━┳━━━┳━━━┓┃┏━┓┃  ┃┏━┓┃  ┃┏┓┃      ┃┏┓┃       ┃┏━┓┃┏━┓┃┏━┓┃
┃┗━━┳┓┏┫┗━━┓  ┃┗┛┗┳━━┳┓┏┫┗┛┗┳━━┳━┓ ┗┛┏┛┃┃┃┃┃┃┃┃┃
┗━━┓┃┗┛┣━━┓┣━━┫┏━┓┃┏┓┃┗┛┃┏━┓┃┃━┫┏┻━┳┓┗┓┃┃┃┃┃┃┃┃┃
┃┗━┛┃┃┃┃┗━┛┣━━┫┗━┛┃┗┛┃┃┃┃┗━┛┃┃━┫┣━━┫┗━┛┃┗━┛┃┗━
┗━━━┻┻┻┻━━━┛  ┗━━━┻━━┻┻┻┻━━━┻━━┻┛  ┗━━━┻━━━┻━━━┛
                \033[32mv.10.1\033[33m (Разработчик: \033[31mАлексей Макаров\033[33m)
                    Ваша система - Linux/Android   
                            Сервисы - \033[32m320 
                                                        """
  for char in banner2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.002)



def banner4():
  print(Fore.YELLOW)
  banner = """
  
     ██████╗███╗   ███╗ ██████╗
    ██╔════╝████╗ ████║██╔════╝   
    ╚█████╗ ██╔████╔██║╚█████╗
     ╚═══██╗██║╚██╔╝██║ ╚═══██╗
    ██████╔╝██║ ╚═╝ ██║██████╔╝     
    ╚═════╝ ╚═╝     ╚═╝╚═════╝    
        
                                                                        \033[32mv.10.1\033[33m (Разработчик: \033[31mАлексей Макаров\033[33m)   
                                                                            Ваша система - Windows/Другая
      _________________________________________________________________________________________  
      |                                                                                       |
      | \033[34mVK\033[33m - https://vk.com/alexey_makarov1122                               |
      |                                                                                       |
      |                                                                                       |        
      |_______________________________________________________________________________________|                                                                                         

                           +|| На Да\033[31mНН\033[33mый мОме\033[34mН\033[33mт сеРвИсоВ -- \033[32m320 \033[33m||+

    """
  for char in banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.001)




def banner1an():
    start_time = time.time()
    CLOSE_AFTER = kol2
    banner1 = """
                         (                    (
     )                  ) )                    )   
     ((            ( ((( (())  ))))     (  ( /(( /
    (_))  ) `  )   ))   /(_)) (╲    (     ))  ) ()) 
    ()/( /(/(  /((_) (_))   )   )  '/((_|_))((_)()
    ┏━━━┓  ┏━━━┓
    ┃┏━┓┃  ┃┏━┓┃  
    ┃┗━━┳┓┏┫┗━━┓ 
    ┗━━┓┃┗┛┣━━┓┃
    ┃┗━┛┃┃┃┃┗━┛┃
    ┗━━━┻┻┻┻━━━┛  
                  v.10.1 (Разработчик: Алексей Макаров)
                       Ваша система - Linux/Android
                              Сервисы - 320
"""
    r=0
    while True:
        if time.time() > start_time + float(CLOSE_AFTER):
            break
            
        if r == 0:
            print(banner1.replace(")", "(").replace("/", "╲"))
            time.sleep(0.1)
            os.system("clear")
            r+=1
        elif r == 1:
            print(banner1.replace("(", ")").replace("╲", "/"))
            time.sleep(0.1)
            os.system("clear")
            r-=1





def banner2an():
    start_time = time.time()
    CLOSE_AFTER = kol2
    banner2 = """        )                        ) )
     )                  )  )                    )   )  )                     )   )          ()    )       )   )
    /((            (   (()/(        )     (  ( /(( /((        (  ( (   (()/(    )    )     (  ( /(( /((        (  (
    _))  ) `  )   ))    /(_)) (    (     ))╲ )╲())╲())╲  (    )╲))( ( )(_))  )   )   ))    /(_)) (    (     ))╲ )╲(╲
    ()|()/( /(/(  /((_) (_))   )╲   )╲  '/((_|_))((_)((_) )╲ )((_))╲ (_(_()|()/( /(/(  /((_) (_))   )╲   )╲  '/((_|_)
    _|)(_)|(_)_ (_))   / __| ((_)_((_))(_)) | |_| |(_|_)_(_/( (()(_) _()|()/(  )____()|()/( _()|()/( )))|_| |(_|_)_
     ██████╗███╗   ███╗ ██████╗
    ██╔════╝████╗ ████║██╔════╝  
    ╚█████╗ ██╔████╔██║╚█████╗
     ╚═══██╗██║╚██╔╝██║ ╚═══██╗
    ██████╔╝██║ ╚═╝ ██║██████╔╝ 
    ╚═════╝ ╚═╝     ╚═╝╚═════╝      
                                                                       v.10.1 (Разработчик: Алексей Макаров)
                                                                            Ваша система - Windows/Другая
      _________________________________________________________________________________________
      |                                                                                       |
      | VK - https://vk.com/alexey_makarov1122                                                |
      |                                                                                       |
      |                                                                                       |
      |_______________________________________________________________________________________|

                           +|| На ДаНый мОмеНт сеРвИсоВ -- 320 ||+
     """
    i=0
    while True:
       if time.time() > start_time + float(CLOSE_AFTER):
           break
       if i == 0:
            print(banner2.replace(")", "(").replace("/", "╲"))
            time.sleep(0.1)
            os.system("cls")


            i+=1
       elif i == 1:
            print(banner2.replace("(", ")").replace("╲", "/"))
            time.sleep(0.1)
            os.system("cls")
            i-=1





def banner_atack():
  print(Fore.YELLOW)
  print("""        _       _             _      ____  _             _   _             
       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                                     |___/ ......""")
  print ("[                    ] \033[94m5%\033[0m")
  time.sleep(0.1)
  print ("[=====               ] \033[94m35%\033[0m")
  time.sleep(1)
  print ("[==========          ] \033[94m52%\033[0m")
  time.sleep(1)
  print ("[====================] \033[94m100%\033[0m")
  time.sleep(2)
  print(Fore.RED)
  print("Атака началась на ||" + str(_phone)+ "||\033[94mDDos-SMS-Attack\033[0m")

message = "\033[94m \n -|| Проверка запуска ||- \033[0m"
message2 = " Нажми  Пуц для продолжения ..."



def start(): 
  os.system("title SMS-Bomber-300-Free")
  print(Fore.YELLOW)
  os.system("clear")
  os.system("CLS")
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

  print(Fore.RED)
  time.sleep(3)
  print (" \033[31m-[                    ]-\033[33m \033[94m2%\033[0m ")
  time.sleep(1)
  print (" \033[31m-[=====               ]-\033[33m \033[94m25%\033[0m")
  time.sleep(0.1)
  print (" \033[31m-[==========          ]-\033[33m \033[94m50%\033[0m")
  time.sleep(1)
  print (" \033[31m-[===============     ]-\033[33m \033[94m75%\033[0m")
  time.sleep(1)
  print (" \033[31m-[====================]-\033[33m \033[94m100%\033[0m")
  time.sleep(0.1)
  print(Fore.YELLOW)
  print (" --|| Запуск Успешный  ||--")
  for char in message2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)





def banner_atack2():
  print(Fore.GREEN)
  baner = """
			┏━━━┓┏┓     ┏┓
			┃┏━┓┣┛┗┓   ┏┛┗┓
			┃┗━━╋┓┏╋━━┳┻┓┏┛
			┗━━┓┃┃┃┃┏┓┃┏┫┃
			┃┗━┛┃┃┗┫┏┓┃┃┃┗┓
			┗━━━┛┗━┻┛┗┻┛┗━┛....."""
  print(baner)
  print ("[                    ] \033[94m5%\033[0m")
  time.sleep(0.1)
  print ("[=====               ] \033[94m35%\033[0m")
  time.sleep(1)
  print ("[==========          ] \033[94m52%\033[0m")
  time.sleep(1)
  print ("[====================] \033[94m100%\033[0m")
  time.sleep(2)
  print(Fore.RED)
  print("Атака началась на ||" + str(_phone)+ "||\033[94mDDos-SMS-Attack\033[0m")


