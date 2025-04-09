from collections import deque

processos = {
    'Processo 1': 10,
    'Processo 2': 5,
    'Processo 3': 8
}

quantum = 2
fila = deque(processos.items())

tempo_corrente = 0  # tempo global
tempo_inicio = {}  # primeira vez que o processo roda
tempo_finalizacao = {}  # quando o processo termina
tempo_executado = {p: 0 for p in processos}  # quanto tempo cada processo rodou (soma dos quantums)

execucao = []

print("Iniciando execução com Quantum =", quantum)
while fila:
    processo, tempo_restante = fila.popleft()

    # Marca quando o processo começou a rodar pela primeira vez
    if processo not in tempo_inicio:
        tempo_inicio[processo] = tempo_corrente

    # Executa o processo
    tempo_a_executar = min(quantum, tempo_restante)
    tempo_corrente += tempo_a_executar
    tempo_executado[processo] += tempo_a_executar

    if tempo_restante > quantum:
        tempo_restante -= quantum
        fila.append((processo, tempo_restante))
        execucao.append(f"T={tempo_corrente}: {processo} executou por {tempo_a_executar} (restam {tempo_restante})")
    else:
        tempo_finalizacao[processo] = tempo_corrente
        execucao.append(f"T={tempo_corrente}: {processo} executou por {tempo_a_executar} e terminou")

# Cálculo dos tempos
turnaround_time = {p: tempo_finalizacao[p] for p in processos}  # todos chegaram no tempo 0
waiting_time = {p: turnaround_time[p] - tempo_executado[p] for p in processos}

# Impressão
print("\n--- LOG DE EXECUÇÃO ---")
for linha in execucao:
    print(linha)

print("\n--- TEMPOS POR PROCESSO ---")
for p in processos:
    print(f"{p}:")
    print(f"  - Tempo total no sistema (turnaround): {turnaround_time[p]}")
    print(f"  - Tempo total executando (CPU): {tempo_executado[p]}")
    print(f"  - Tempo total esperando na fila: {waiting_time[p]}")

print("\nTempo total até todos os processos finalizarem:", tempo_corrente)
