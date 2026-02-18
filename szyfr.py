def szyfruj(str, key):
    out = ""
    for char in str:
        start = ord('A') if litera.isupper() else ord('a')
        out += chr((ord(char) - start + key) % 26 + start)
    return out

def odszyfruj(str, key):
    return szyfr_cezara(str, -key)
