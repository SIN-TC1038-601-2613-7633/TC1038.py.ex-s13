
# Se asumen 30 días por mes y 365 días por año para simplificar el cálculo de la diferencia de días entre dos fechas.
def diferencia_dias(dia1, mes1, anio1, dia2, mes2, anio2):
    tdias1 = dia1 + mes1 * 30 + anio1 * 365
    tdias2 = dia2 + mes2 * 30 + anio2 * 365

    return abs(tdias1 - tdias2)

def main():
    #escribe tu código abajo de esta línea

    dia1 = int(input("Día: "))
    mes1 = int(input("Mes: "))
    anio1 = int(input("Año: "))

    dia2 = int(input("Día: "))
    mes2 = int(input("Mes: "))
    anio2 = int(input("Año: "))

    print(f"Hay {diferencia_dias(dia1, mes1, anio1, dia2, mes2, anio2)} día(s) de diferencia")

if __name__=='__main__':
    main()
