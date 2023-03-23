def etsi_suurin_nelio(max_luku):
    suurin_nelio = 0
    i = 1
    while i*i <= max_luku:
        suurin_nelio = i*i
        i += 1
    return suurin_nelio

max_luku = int(input("Anna luku: "))
suurin_nelio = etsi_suurin_nelio(max_luku)
print("Suurin neliö, joka on korkeintaan yhtä suuri kuin annettu luku on", suurin_nelio)