import math;

def geraMatriz(linhas, colunas):
    matriz = [];
    for _ in range(linhas):
        matriz.append([0] * colunas);
    return matriz;

def ColetaCoordenadas(matrizOperada):
    while True:
        coleta = input();
        indexEOF = coleta.find('EOF');
        if indexEOF == -1:
            strColetada = coleta.split();
            try:
                matrizOperada[int(strColetada[0])-1][0] = float(strColetada[1]);
                matrizOperada[int(strColetada[0])-1][1] = float(strColetada[2]);
            except:
                raise Exception("String Error: ",strColetada," Index EOF: ",indexEOF);
        else:
            break;
    return matrizOperada;

def coletaDadosEntrada(dicionario):
    cont = 0;
    while cont < 6:
        entrada = input();
        cont = cont + 1;
        if entrada != "EOF":
            if entrada == "NODE_COORD_SECTION":
                chave = entrada;
                conteudo = [];
                dicionario[chave] = conteudo;
                break;
            else:
                index = entrada.find(":");
                chave = entrada[0:index];
                index = chave.find(' ');
                if index != -1:
                    chave = chave[:index];
                conteudo = entrada[index+1:];
                index = conteudo.find(' ');
                if index != -1:
                    conteudo = conteudo[index+1:];
                dicionario[chave] = conteudo;
        else:
            break;
    return(dicionario);

def knn(matriz,origem):
    distanciaTotal = 0;
    distancia = 0;
    melhorDestino = 0;
    numerosUsados = [];
    contador = 0;
    origemInicial = origem;
    while matriz[origem][2] == 0:
        contador = contador + 1;
        numerosUsados.append(origem);
        matriz[origem][2] = 1;
        distanciaInicial = 2147483647;
        iterado = 0;
        if contador == len(matriz):
            distancia = math.sqrt((matriz[origem][0] - matriz[origemInicial][0])**2 + (matriz[origem][1] - matriz[origemInicial][1])**2);
            distanciaTotal = distanciaTotal + distancia;
        else:
            for i in range(0, len(matriz)):
                if i != origem:
                    if matriz[i][2] == 0:
                        distancia = math.sqrt((matriz[origem][0] - matriz[i][0])**2 + (matriz[origem][1] - matriz[i][1])**2);
                        if distancia < distanciaInicial:
                            distanciaInicial = distancia;
                            melhorDestino = i;
                            iterado = 1;
            if iterado != 0:
                distanciaTotal = distanciaTotal + distanciaInicial;
                origem = melhorDestino;
    return distanciaTotal, numerosUsados;

def cost_change(matriz, n1, n2, n3, n4):
    dist13 = math.sqrt((matriz[n1][0] - matriz[n3][0])**2 + (matriz[n1][1] - matriz[n3][1])**2);
    dist24 = math.sqrt((matriz[n2][0] - matriz[n4][0])**2 + (matriz[n2][1] - matriz[n4][1])**2);
    dist12 = math.sqrt((matriz[n1][0] - matriz[n2][0])**2 + (matriz[n1][1] - matriz[n2][1])**2);
    dist34 = math.sqrt((matriz[n3][0] - matriz[n4][0])**2 + (matriz[n3][1] - matriz[n4][1])**2);
    if dist13 + dist24 < dist12 + dist34:
        return True;
    else:
        return False;

def two_opt(route,matriz):
    best = route;
    improved = True;
    while improved:
        improved = False;
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                if cost_change(matriz,best[i - 1], best[i], best[j - 1], best[j]):
                    best[i:j] = best[j - 1:i - 1:-1];
                    improved = True;
        route = best;
    return best;

def calcula_distancia(rota,matriz):
    distanciaTotal = 0;
    for i in range(0, len(rota)):
        if i == len(rota)-1:
            distancia = math.sqrt((matriz[rota[i]][0] - matriz[rota[0]][0])**2 + (matriz[rota[i]][1] - matriz[rota[0]][1])**2);
            distanciaTotal += distancia;
        else:
            distancia = math.sqrt((matriz[rota[i]][0] - matriz[rota[i+1]][0])**2 + (matriz[rota[i]][1] - matriz[rota[i+1]][1])**2);
            distanciaTotal += distancia;
    return distanciaTotal;

def main():
    colunas = 3;
    infos = {};
    infos = coletaDadosEntrada(infos);
    route = [];
    infos["DIMENSION"] = int(infos["DIMENSION"]);
    linhas = infos["DIMENSION"];
    vertices = geraMatriz(linhas, colunas);
    infos["NODE_COORD_SECTION"] = ColetaCoordenadas(vertices);
    distanciaPercorrida,route = knn(infos["NODE_COORD_SECTION"],0);
    best_route = two_opt(route,infos["NODE_COORD_SECTION"]);
    best_distance = calcula_distancia(best_route,infos["NODE_COORD_SECTION"]);
    if best_distance < distanciaPercorrida:
        print(round(best_distance,2));
    else:
        print(round(distanciaPercorrida,2));
    
if __name__ == "__main__":
    main();