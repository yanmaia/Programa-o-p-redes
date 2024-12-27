# Programa principal para preencher a tabela
from funcao_nonce import funcao_nonce

textos = [
    "Esse é fácil", "Esse é fácil", "Esse é fácil", "Texto maior muda o tempo?", 
    "Texto maior muda o tempo?", "Texto maior muda o tempo?", 
    "É possível calcular esse?", "É possivel calcular esse?", "É possível calcular esse?"
]
bits_para_zero_lista = [8, 10, 15, 8, 10, 15, 18, 19, 20]

resultados = []

for texto, bits in zip(textos, bits_para_zero_lista):
    dados = texto.encode('utf-8')
    nonce_encontrado, tempo_decorrido = funcao_nonce(dados, bits)
    resultados.append((texto, bits, nonce_encontrado, tempo_decorrido))

# Salva a tabela de resultados
with open("resultado_tabela.txt", "w") as arquivo:
    arquivo.write(f"{'Texto':<30} {'Bits em zero':<12} {'Nonce':<10} {'Tempo (s)':<10}\n")
    for resultado in resultados:
        arquivo.write(f"{resultado[0]:<30} {resultado[1]:<12} {resultado[2]:<10} {resultado[3]:<10.4f}\n")

# Exibi a tabela no console
print(f"{'Texto':<30} {'Bits em zero':<12} {'Nonce':<10} {'Tempo (s)':<10}")
for resultado in resultados:
    print(f"{resultado[0]:<30} {resultado[1]:<12} {resultado[2]:<10} {resultado[3]:<10.4f}")
