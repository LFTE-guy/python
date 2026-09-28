x = input()

for char in x:
    Bx = ord(char)
    Hx = hex(Bx)
    BIx = bin(Bx)
    print(f"{char} | DEC:{Bx} | Hex:{Hx} | BIN:{BIx} ")

