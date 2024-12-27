import hashlib
import time

def funcao_nonce(dados_para_hash: bytes, bits_para_zero: int):
    """
    Função que encontra  o nonce que gera um hash SHA-256 
    com os primeiros bits iguais a zero.

    Args:
        dados_para_hash (bytes): Os dados  combinados com o nonce.
        bits_para_zero (int): Quantidade de bits iniciais que devem ser zero no hash.

    Returns:
        tuple: Um par contendo o nonce encontrado e o tempo decorrido para encontrá-lo.
    """
    nonce = 0
    tempo_inicio = time.time()
    while True:
        # Combine o nonce com os dados de entrada
        bytes_nonce = nonce.to_bytes(4, byteorder='little')
        combinado = bytes_nonce + dados_para_hash
        
        # Calcular o hash 
        resultado_hash = hashlib.sha256(combinado).digest()
        
        # Converter o hash para uma sequência de bits
        bits_hash = ''.join(f'{byte:08b}' for byte in resultado_hash)
        
        # Verificar se os primeiros bits são zeros
        if bits_hash.startswith('0' * bits_para_zero):
            tempo_fim = time.time()
            tempo_decorrido = tempo_fim - tempo_inicio
            return nonce, tempo_decorrido
        
        # Incrementar o nonce
        nonce += 1