def de_pies_a_centimetros(pies):
    if pies > 0:
        centimetros = pies * 30.48
        return centimetros
    else:
        return "Error"
    
def de_pulgadas_a_centimetros(pulgadas):
    if pulgadas > 0:
        centimetros = pulgadas * 2.54
        return centimetros
    else:
        return "Error"

def de_yardas_a_centimetros(yardas):
    if yardas > 0:
        centimetros = yardas * 91.44
        return centimetros
    else:
        return "Error"

def main():
    opcion = int(input())
    distancia = int(input())
    match opcion:
        case 1:
            print(de_pies_a_centimetros(distancia))
        case 2:
            print(de_pulgadas_a_centimetros(distancia))
        case 3:
            print(de_yardas_a_centimetros(distancia))
        case _:
            print("Error")

if __name__=='__main__':
    main()
