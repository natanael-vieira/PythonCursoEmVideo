def leiaDinheiro(msg):
    val = False

    while not val:
        ent = str(input(msg)).replace(',', '.').strip()
        if ent.isalpha() or ent == '':
            print(f'\033[0;31mERRO \"{ent}\" é um PREÇO INVÁLIDO!\033[m')
        else:
            val = True
            return float(ent)
