import os
import sys

def main(): #Verificação de argumentos
    if len(sys.argv) != 4:
        print("para fazer o uso : python programa.py <arquivo_origem> <palavra_passe> <arquivo_destino>")
        return
   
    arquivo_origem = sys.argv[1]
    palavra_passe = sys.argv[2]        # parametros  de comando
    arquivo_destino = sys.argv[3]
    
    xor_encrypt(arquivo_origem, palavra_passe, arquivo_destino) #Chamar a função de criptografia

def xor_encrypt(input_file, password, output_file):
    """
    criptografar os bytes de um arquivo usando a operação XOR com  uma palavra-passe
    :para input_file: Nome do arquivo de origem.
    :para password: Palavra-passe para a operação XOR.+
    :para output_file: Nome do arquivo de destino.
    """
    
    if not os.path.isfile(input_file): # Verifica a existência do arquivo de origem
        print(f"Erro: O arquivo de origem '{input_file}' não existe.")
        return
    
    if os.path.isfile(output_file): #Verifica o arquivo de destino já existe 
        print(f"Erro: O arquivo de destino '{output_file}' já existe. Escolha outro nome para evitar sobrescrita.")
        return
 
    if not password: # Verifica se a palavra-passe  está vazia
        print("Erro: A palavra-passe não pode estar vazia.")
        return

    try:
        with open(input_file, 'rb') as f_in: #Abre o arquivo de origem para leitura em modo binário
            data = f_in.read()
           
        encrypted_data = bytearray() #Prepara a lista para armazenar os bytes criptografados
        
        password_length = len(password) #Criptografar os bytes usando XOR e a palavra-passe
        for i, byte in enumerate(data):      
            encrypted_byte = byte ^ ord(password[i % password_length]) #Realiza a operação XOR entre o byte atual e o byte correspondente da palavra-passe
            encrypted_data.append(encrypted_byte) #Adiciona o byte criptografado à lista
             
        with open(output_file, 'wb') as f_out: #Salva os dados criptografados no arquivo de destino
            f_out.write(encrypted_data)

        print(f"Criptografia concluída com sucesso! O arquivo foi salvo como '{output_file}'.")
    
    except Exception as e:
        print(f"Erro durante a criptografia: {e}")

if __name__ == "__main__":
    main()