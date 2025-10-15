from collections import Counter

enkriptatutako_testua = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE. """

# Gaztelaniazko letra maiztasunak
maiztasuna = {
    'e': 16.78, 'a': 11.96, 'o': 8.69, 'l': 8.37, 's': 7.88,
    'n': 7.01, 'd': 6.87, 'r': 4.94, 'u': 4.80, 'i': 4.15,
    't': 3.31, 'c': 2.92, 'p': 2.77, 'm': 2.12, 'y': 1.54,
    'q': 1.53, 'b': 0.92, 'h': 0.89, 'g': 0.73, 'f': 0.52,
    'v': 0.39, 'j': 0.30, 'ñ': 0.29, 'z': 0.15, 'x': 0.06,
    'k': 0.0,  'w': 0.0
}

# Emandako testuko letren maiztasunak
bakarrik_letrak = [c for c in enkriptatutako_testua.upper() if c.isalpha()]
letrak_guztira = len(bakarrik_letrak)
kont = Counter(bakarrik_letrak)

# Ehunekoa kalkulatu
testuaren_letra_maiztasunak = {letra: count * 100 / letrak_guztira for letra, count in kont.items()}

# Ordenatu testuko letrak eta gaztelaniazko alfabetoa
ordenatu_testu_letrak = sorted(testuaren_letra_maiztasunak.items(), key=lambda x: x[1], reverse=True)
ordenatu_gaztelaniako_alfabetoa= sorted(maiztasuna.items(), key=lambda x: x[1], reverse=True)

# Mapatu: testuko maiztasun handiena -> gaztelaniazko maiztasun handiena
ordezkapen_mapa= {enc: dec for (enc, _), (dec, _) in zip(ordenatu_testu_letrak, ordenatu_gaztelaniako_alfabetoa)}

# Dekodetze funtzioa
def dekodetu(testua, mapatzea):
    erantzuna = ""
    for karaktere in testua:
        if karaktere.upper() in mapatzea:
            dek_karaktere = mapatzea[karaktere.upper()]
            erantzuna += dek_karaktere.lower() if karaktere.islower() else dek_karaktere.upper()
        else:
            erantzuna += karaktere
    return erantzuna

print("\n DESZIFRATUTAKO TESTUA: \n")
print(dekodetu(enkriptatutako_testua, ordezkapen_mapa))
