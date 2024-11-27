import json,os
from tabulate import tabulate

def validamascara(mascara): #Valida e verifica a mascara
    if not (0 <= mascara <= 32):
        raise ValueError("Máscara de rede inválida. Deve estar entre 0 e 32.")
    return mascara

def ip_binario(ip): # conversao ip para binario
    partes = map(int, ip.split("."))
    return ''.join(f"{parte:08b}" for parte in partes)

def binario_ip(binario): #Retornar o binário para endereço IP
    partes = [str(int(binario[i:i+8], 2)) for i in range(0, 32, 8)]
    return ".".join(partes)

def calcular_subrede(ip, mascara): #Calcular informações da sub-rede
    ip_bin = ip_binario(ip)
    net_bin = ip_bin[:mascara] + "0" * (32 - mascara)
    broadcast_bin = ip_bin[:mascara] + "1" * (32 - mascara)  
    rede = binario_ip(net_bin)
    broadcast = binario_ip(broadcast_bin)  
    primeiro_host = binario_ip(net_bin[:-1] + "1")
    ultimo_host = binario_ip(broadcast_bin[:-1] + "0")   
    num_hosts_validos = (2 ** (32 - mascara)) - 2    
    mascara_bin = "1" * mascara + "0" * (32 - mascara)
    mascara_decimal = binario_ip(mascara_bin)   
    return {
        "CIDR": f"/{mascara}",
        "Endereço de Rede": rede,
        "Primeiro Host": primeiro_host,
        "Último Host": ultimo_host,
        "Endereço de Broadcast": broadcast,
        "Máscara de Sub-Rede": mascara_decimal,
        "Máscara de Sub-Rede (Binário)": mascara_bin,
        "Hosts Válidos": num_hosts_validos   }

def salvar_resultado_json(resultado, nome_arquivo): #Salvar resultado sem sobrescrever arquivos existentes
    if os.path.exists(nome_arquivo):
        raise FileExistsError(f"O arquivo '{nome_arquivo}' já existe.")
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=4, ensure_ascii=False)

def calcular_intervalo_subredes(ip, mascara_inicial, mascara_final):
    resultado = []
    for mascara in range(mascara_inicial, mascara_final + 1):
        resultado.append(calcular_subrede(ip, mascara))
    return resultado

def exibir_tabela(resultados):       # mostra  o resultado em formato tabela
    tabela = []
    for info in resultados:
        tabela.append([
            info["CIDR"],
            info["Endereço de Rede"],
            info["Primeiro Host"],
            info["Último Host"],
            info["Endereço de Broadcast"],
            info["Máscara de Sub-Rede"],
            info["Máscara de Sub-Rede (Binário)"],
            info["Hosts Válidos"]
        ])
    
    colunas = ["CIDR", "Endereço de Rede", "Primeiro Host", "Último Host", "Endereço de Broadcast", 
               "Máscara de Sub-Rede", "Máscara de Sub-Rede (Binário)", "Hosts Válidos"]
    
    print(tabulate(tabela, headers=colunas, tablefmt="pipe"))

def validar_ip(ip):
    """Valida o endereço IP fornecido pelo usuário"""
    partes = ip.split(".")
    if len(partes) != 4:
        raise ValueError("Endereço IP inválido.")
    for parte in partes:
        if not parte.isdigit() or not (0 <= int(parte) <= 255):
            raise ValueError("Endereço IP inválido.")
    return ip

try:
    # Solicita e valida o endereço IP
    ip = input("Digite o endereço IP separado por . (ponto) : ")
    ip = validar_ip(ip)

    mascara_inicial = input("Digite a máscara de rede inicial em CIDR (0-32): ")
    if not mascara_inicial.isdigit():
        raise ValueError("A máscara inicial deve ser um número inteiro.")
    mascara_inicial = validamascara(int(mascara_inicial))
    
    mascara_final = input("Digite a máscara de rede final em CIDR (0-32): ")
    if not mascara_final.isdigit():
        raise ValueError("A máscara final deve ser um número inteiro.")
    mascara_final = validamascara(int(mascara_final))
    
    if mascara_inicial > mascara_final:
        raise ValueError("A máscara de rede inicial deve ser menor ou igual à máscara final.")
    
    resultado = calcular_intervalo_subredes(ip, mascara_inicial, mascara_final)
    
    nome_arquivo = input("Digite o nome do arquivo JSON para salvar (sem extensão): ") + ".json"
    salvar_resultado_json(resultado, nome_arquivo)
    print(f"Resultados salvos com sucesso em {nome_arquivo}.")
    
    exibir_tabela(resultado)

except ValueError as e:
    print(f"Erro de valor: {e}")

except FileExistsError as e:
    print(f"Erro de arquivo: {e}")

except OSError as e:
    print(f"Erro de sistema: {e.strerror} (código {e.errno})")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e.__class__.__name__} - {e}")