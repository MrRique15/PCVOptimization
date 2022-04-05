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
    shortestPath = [];
    contador = 0;
    origemInicial = origem;
    while matriz[origem][2] == 0:
        contador = contador + 1;
        shortestPath.append(origem);
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
    return distanciaTotal, shortestPath;

def farAway(matriz,origem):
    distanciaTotal = 0;
    distancia = 0;
    maiorDestino = 0;
    longestPath = [];
    contador = 0;
    origemInicial = origem;
    while matriz[origem][2] == 0:
        contador = contador + 1;
        longestPath.append(origem);
        matriz[origem][2] = 1;
        distanciaInicial = 0;
        iterado = 0;
        if contador == len(matriz):
            distancia = math.sqrt((matriz[origem][0] - matriz[origemInicial][0])**2 + (matriz[origem][1] - matriz[origemInicial][1])**2);
            distanciaTotal = distanciaTotal + distancia;
        else:
            for i in range(0, len(matriz)):
                if i != origem:
                    if matriz[i][2] == 0:
                        distancia = math.sqrt((matriz[origem][0] - matriz[i][0])**2 + (matriz[origem][1] - matriz[i][1])**2);
                        if distancia > distanciaInicial:
                            distanciaInicial = distancia;
                            maiorDestino = i;
                            iterado = 1;
            if iterado != 0:
                distanciaTotal = distanciaTotal + distanciaInicial;
                origem = maiorDestino;
    return distanciaTotal, longestPath;

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

def distance_nodes(matriz,n1,n2):
    if n1 == n2:
        return 0;
    return math.sqrt((matriz[n1][0] - matriz[n2][0])**2 + (matriz[n1][1] - matriz[n2][1])**2);

def exchange(path, execute, a, c, e, matriz):
    b, d, f = a + 1, c + 1, e + 1;

    p_a, p_b, p_c, p_d, p_e, p_f = [path[i] for i in (a, b, c, d, e, f)];

    base = distance_nodes(matriz, p_a, p_b) + distance_nodes(matriz, p_c, p_d) + distance_nodes(matriz, p_e, p_f);

    if execute == 0:
        # 2-opt (a, e) [d, c] (b, f)
        sol = path[:a + 1] + path[e:d - 1:-1] + path[c:b - 1:-1] + path[f:]
        gain = distance_nodes(matriz, p_a, p_e) + distance_nodes(matriz, p_c, p_d) + distance_nodes(matriz, p_b, p_f)
    elif execute == 1:
        # 2-opt [a, b] (c, e) (d, f)
        sol = path[:a + 1] + path[b:c + 1] + path[e:d - 1:-1] + path[f:]
        gain = distance_nodes(matriz, p_a, p_b) + distance_nodes(matriz, p_c, p_e) + distance_nodes(matriz, p_d, p_f)
    elif execute == 2:
        # 2-opt (a, c) (b, d) [e, f]
        sol = path[:a + 1] + path[c:b - 1:-1] + path[d:e + 1] + path[f:]
        gain = distance_nodes(matriz, p_a, p_c) + distance_nodes(matriz, p_b, p_d) + distance_nodes(matriz, p_e, p_f)
    elif execute == 3:
        # 3-opt (a, d) (e, c) (b, f)
        sol = path[:a + 1] + path[d:e + 1] + path[c:b - 1:-1] + path[f:]
        gain = distance_nodes(matriz, p_a, p_d) + distance_nodes(matriz, p_e, p_c) + distance_nodes(matriz, p_b, p_f)
    elif execute == 4:
        # 3-opt (a, d) (e, b) (c, f)
        sol = path[:a + 1] + path[d:e + 1] + path[b:c + 1] + path[f:]
        gain = distance_nodes(matriz, p_a, p_d) + distance_nodes(matriz, p_e, p_b) + distance_nodes(matriz, p_c, p_f)
    elif execute == 5:
        # 3-opt (a, e) (d, b) (c, f)
        sol = path[:a + 1] + path[e:d - 1:-1] + path[b:c + 1] + path[f:]
        gain = distance_nodes(matriz, p_a, p_e) + distance_nodes(matriz, p_d, p_b) + distance_nodes(matriz, p_c, p_f)
    elif execute == 6:
        # 3-opt (a, c) (b, e) (d, f)
        sol = path[:a + 1] + path[c:b - 1:-1] + path[e:d - 1:-1] + path[f:]
        gain = distance_nodes(matriz, p_a, p_c) + distance_nodes(matriz, p_b, p_e) + distance_nodes(matriz, p_d, p_f)

    return sol, base - gain

def three_optSwap(route,size,matriz):
    saved = None
    bestChange = 0
    for a in range(size - 5):
        for c in range(a + 2, size - 3):
            for e in range(c + 2, size - 1):
                change = 0
                for i in range(7):
                    path, change = exchange(route, i, a, c, e, matriz);
                    if change > bestChange:
                        saved = a, c, e, i
                        bestChange = change
                        return saved, bestChange
    return saved, bestChange

def three_opt(route,distancia,matriz):
    print("Iniciando 3-opt");
    bestPath = route;
    size = len(route);
    bestChange = 1;
    while bestChange > 0:
        print("Fazendo bestChange!");
        print("Distancia: ", distancia);
        saved, bestChange = three_optSwap(bestPath, size, matriz);
        if bestChange > 0:
            a, c, e, which = saved;
            bestPath, change = exchange(bestPath, which, a, c, e, matriz);
            distancia -= change;
    print(bestPath);
    print(distancia);
    return bestPath, distancia;                       

def calcula_distancia(rota,matriz):
    distanciaTotal = 0;
    for i in range(0, len(rota)):
        if i == len(rota)-1:
            distancia = distance_nodes(matriz, rota[i], rota[0]);
            distanciaTotal += distancia;
        else:
            distancia = distance_nodes(matriz, rota[i], rota[i+1]);
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
    
    #------------------ KNN + TWO-OPT ------------------#
    distanciaInicial_knn,rotaInicial_knn = knn(infos["NODE_COORD_SECTION"],0);
    best_route_two = two_opt(rotaInicial_knn,infos["NODE_COORD_SECTION"]);
    best_distance_knnTwo = calcula_distancia(best_route_two,infos["NODE_COORD_SECTION"]);

    # ------------------ Reset para os visitados ------------------#
    for i in range(0, len(infos["NODE_COORD_SECTION"])):
        infos["NODE_COORD_SECTION"][i][2] = 0;
        
    #------------------ FAR-AWAY + THREE-OPT ------------------#
    distanciaInicial_far,rotaInicial_far = farAway(infos["NODE_COORD_SECTION"],0);
    best_route_three, best_distance_farThree = three_opt(rotaInicial_far,distanciaInicial_far,infos["NODE_COORD_SECTION"]);

    # ------------------ Print Informações FInais ------------------#
    print("Distancia percorrida KNN + 2-OPT: ",best_distance_knnTwo);
    print("Distancia percorrida FarAway + 3-OPT: ",best_distance_farThree);
    
if __name__ == "__main__":
    main();