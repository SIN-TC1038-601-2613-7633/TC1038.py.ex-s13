def perimetro_triangulo(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return "Error"
    return a + b + c

def area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        return "Error"
    return (base * altura) / 2

def main():
    opcion = int(input())
    if opcion == 1:
        a = float(input())
        b = float(input())
        c = float(input())
        print(f"Perímetro={perimetro_triangulo(a, b, c)}")
    elif opcion == 2:
        base = float(input())
        altura = float(input())
        print(f"Área={area_triangulo(base, altura)}")
    else:
        print("Error")

if __name__=='__main__':
    main()
