def calcula_grado(score):
    if score < 0 or score > 1:
        return "Score incorrecto"

    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

def main():
    score = float(input())
    print(calcula_grado(score))

if __name__=='__main__':
    main()
