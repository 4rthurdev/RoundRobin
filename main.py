from collections import deque

processos = {
    'Processo 1': 10,
    'Processo 2': 5,
    'Processo 3': 8
}

quantum = 2
fila = deque(processos.items())

# Armazena o tempo
tempo_total = 0

# Saida
execucao = []

print("Iniciando com Quantum =", quantum)
while fila:
    processo, tempo_restante = fila.popleft()

    if tempo_restante > quantum:
        tempo_total += quantum
        tempo_restante -= quantum
        fila.append((processo, tempo_restante))
        execucao.append(f"{processo} executou por {quantum} unidades de tempo (restam {tempo_restante})")
    else:
        tempo_total += tempo_restante
        execucao.append(f"{processo} executou por {tempo_restante} e terminou")

print("\n--- LOG DE EXECUÇÃO ---")
for linha in execucao:
    print(linha)

print("\nTempo total de execução:", tempo_total)
