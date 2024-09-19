def verificar_letra_a(string):
    """
    Verifica a existência da letra 'a' (maiúscula ou minúscula) em uma string
    e informa a quantidade de vezes em que ela ocorre.

    Args:
        string (str): A string a ser verificada.

    Returns:
        tuple: Uma tupla contendo um booleano indicando a existência da letra 'a'
               e a quantidade de vezes em que ela ocorre.
    """
    # Convertendo a string para minúscula para facilitar a verificação
    string_min = string.lower()
    
    # Verificando a existência da letra 'a'
    existe_a = 'a' in string_min
    
    # Contando a quantidade de vezes em que a letra 'a' ocorre
    contagem_a = string_min.count('a')
    
    return existe_a, contagem_a

# Exemplo de uso
string = "Olá, mundo! A letra 'a' é muito comum."
existe_a, contagem_a = verificar_letra_a(string)

print(f"A letra 'a' existe na string: {existe_a}")
print(f"A letra 'a' ocorre {contagem_a} vezes na string.")
