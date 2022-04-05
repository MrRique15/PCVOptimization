def calculaGap(ms, sol):
    return round(((sol-ms) / ms) * 100, 2);

def main():
    ms = round(float(input("Insira o valor da melhor solução conhecida: ")),2);
    sol1 = round(float(input("Insira o valor da primeira solução: ")),2);
    sol2 = round(float(input("Insira o valor da segunda solução: ")),2);
    # Calcula o gap
    gap1 = calculaGap(ms, sol1);
    gap2 = calculaGap(ms, sol2);

    print("O gap da primeira solução é: ", gap1,"%");
    print("O gap da segunda solução é: ", gap2,"%");

if __name__ == "__main__":
    main();