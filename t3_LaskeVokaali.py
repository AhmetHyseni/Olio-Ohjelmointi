def laske_vokaalit(tiedoston_nimi):
    """Palauttaa vokaalien määrän tekstitiedostossa"""
    vokaalit = 'aeiouyäöAEIOUYÄÖ'
    vokaalien_lkm = 0
    with open(tiedoston_nimi, 'r') as tiedosto:
        for rivi in tiedosto:
            for merkki in rivi:
                if merkki in vokaalit:
                    vokaalien_lkm += 1
    return vokaalien_lkm

# Esimerkkikäyttö
tiedoston_nimi = 'LaskeVokaalit.txt'
vokaalien_maara = laske_vokaalit(tiedoston_nimi)
print(f'Tekstitiedostossa {tiedoston_nimi} on {vokaalien_maara} vokaalia.')
