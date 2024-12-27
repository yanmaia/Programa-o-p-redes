import random
import os

def main():  # Função para  ler o arquivo
    arquivo_palavras = os.path.join(os.path.dirname(__file__), "testepalavras.txt")
    
    if not os.path.exists(arquivo_palavras):
        print(f"Arquivo '{arquivo_palavras}' não encontrado.")
        return
    
    palavras = ler_palavras(arquivo_palavras)
    
    if not palavras:
        print("Nenhuma palavra válida encontrada no arquivo.")
        return
    
    palavra_sorteada = sortear_palavra(palavras)  # Sorteio da palavra
    jogar(palavra_sorteada)  # Iniciar o jogo

def ler_palavras(arquivo):  # Ler e retorna as palavras validas
    with open(arquivo, 'r') as file:
        palavras = [linha.strip() for linha in file if 5 <= len(linha.strip()) <= 8]  # Retornar uma lista com palavras de 5 a 8 letras
    return palavras

def sortear_palavra(palavras):  # sorteio de palavras
    palavra_sorteada = random.choice(palavras)
    print(f"A palavra sorteada tem {len(palavra_sorteada)} letras.")
    return palavra_sorteada

def fornecer_feedback(palavra_sorteada, tentativa):  # Resultado das tentativas 
    resultado = []
    for i, letra in enumerate(tentativa):
        if letra == palavra_sorteada[i]:
            resultado.append(f"\033[92m{letra}\033[0m")  # Verde
        elif letra in palavra_sorteada:
            resultado.append(f"\033[93m{letra}\033[0m")  # Amarelo
        else:
            resultado.append(f"\033[90m{letra}\033[0m")  # Cinza
    return " ".join(resultado)

def jogar(palavra_sorteada):  # Função principal do jogo
    tentativas_restantes = 6
    while tentativas_restantes > 0:
        print(f"Tentativa ({tentativas_restantes} restantes):")
        tentativa = input("Digite sua tentativa: ").strip().lower()
        
        if len(tentativa) != len(palavra_sorteada):
            print(f"A palavra deve ter {len(palavra_sorteada)} letras.")
            continue
        
        if tentativa == palavra_sorteada:
            print(f"\033[92mParabéns! Você acertou a palavra '{palavra_sorteada}' em {6 - tentativas_restantes + 1} tentativas.\033[0m")
            return
        
        print(f"Resultado: {fornecer_feedback(palavra_sorteada, tentativa)}")
        tentativas_restantes -= 1  # Reduzi caso tenha os criterios
    
    print(f"\033[91mVocê perdeu! A palavra era '{palavra_sorteada}'.\033[0m")

if __name__ == "__main__":
    main()