for luku in range(1, 101):
    #Tarkistaa jos luku on jaollinen kolmella ja viidellä
    if luku % 3 == 0 and luku % 5 == 0:
        print(luku, "HuiHai")
    #Tarkistaa jos luku on jaollinen kolmella
    elif luku % 3 == 0:
        print(luku, "Hui")
    #Tarkistaa jos luku on jaollinen kolmella
    elif luku % 5 == 0:
        print(luku, "Hai")
    #Jos luku ei ole jaollinen kolmella viidellä tai molemilla, tulostaa vain luvun
    else:
        print(luku)