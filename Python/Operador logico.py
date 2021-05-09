"""
Operadores logicos

and (e)
or (ou)
not (negacao)
is (e)
is not (nao e)
in (esta contido)
not in (nao esta contido)
"""
if not(2 < 4 and 2==4):
    print("True One")

if (2 < 4 or 2==4):
    print("True Two")
    
if 2 is not str:
    print("Nao e float")