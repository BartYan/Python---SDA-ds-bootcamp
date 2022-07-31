"""
    Napisz prosta funkcje "szyfrujaca". Jej zadaniem jest zamiana
    co trzeciego znaku w hasle na znak gwiazdki (*).
    Przyklad:
    >> x = hide_password("moje_super_tajne_haslo123")
    >> print(x)
    "mo*e_*up*r_*aj*e_*as*o1*3"
    Pamietaj, ze dlugosc napisu nie musi byc podzielna przez 3.
"""
def hide_password(password):

    signs = list(password)

    for i, sign in enumerate(signs):
        if i > 1 and (i+1) % 3 == 0:
            signs[i] = "*"

    return "".join(signs)
