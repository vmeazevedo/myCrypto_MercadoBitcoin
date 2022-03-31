
def calc_porc(anterior, nova):
    anterior = anterior
    nova = nova

    if anterior < nova:
        x = (nova*100.00) / anterior
        x = 100.00 - x
        x = str(x)
        x = x.replace('-', '')
        x = float(x)
        x = round(x, 2)
        x = ("+" + str(x))
        return x

    elif anterior > nova:
        x = (nova*100.00) / anterior
        x = 100.00 - x
        x = str(x)
        x = float(x)
        x = round(x, 2)
        x = ("-" + str(x))
        return x

    else:
        x = ("-%")
        return x
