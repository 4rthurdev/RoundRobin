from collections import deque

processos = {
    'Processo 1': 10,
    'Processo 2': 5,
    'Processo 3': 8
}

quantum = 2
fila = deque(processos.items())

tempo_corrente = 0  # tempo total global
tempo_finalizacao = {}  # dicionário para armazenar o tempo em que cada processo terminou
tempo_inicio = {}  # para marcar quando o processo entra na CPU pela primeira vez

execucao = []

print("Iniciando execução com Quantum =", quantum)
while fila:
    processo, tempo_restante = fila.popleft()

    # Marca o primeiro tempo em que o processo entrou na CPU
    if processo not in tempo_inicio:
        tempo_inicio[processo] = tempo_corrente

    if tempo_restante > quantum:
        tempo_corrente += quantum
        tempo_restante -= quantum
        fila.append((processo, tempo_restante))
        execucao.append(f"T={tempo_corrente}: {processo} executou por {quantum} unidades de tempo (restam {tempo_restante})")
    else:
        tempo_corrente += tempo_restante
        execucao.append(f"T={tempo_corrente}: {processo} executou por {tempo_restante} e terminou")
        tempo_finalizacao[processo] = tempo_corrente

# Tempo de permanência total no sistema (turnaround time)
tempo_processos = {
    p: tempo_finalizacao[p] - tempo_inicio[p] for p in processos
}

# Impressão
print("\n--- LOG DE EXECUÇÃO ---")
for linha in execucao:
    print(linha)

print("\n--- TEMPOS DE EXECUÇÃO INDIVIDUAL ---")
for p in processos:
    print(f"{p} ficou no sistema por {tempo_processos[p]} unidades de tempo")

print("\nTempo total até todos os processos finalizarem:", tempo_corrente)
