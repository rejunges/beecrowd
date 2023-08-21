while True:
    try:
        texto = input().split()
        palavras = []
        comprimento_medio = 0

        for palavra in texto:
            if palavra.isalpha():
                palavras.append(palavra)
            elif palavra[:-1].isalpha() and palavra[-1] == '.':
                palavras.append(palavra[:-1])
        
        tamanho = [len(palavra) for palavra in palavras]
        
        if len(palavras):
            comprimento_medio = sum(tamanho) // len(palavras)

        if comprimento_medio <= 3:
            print("250")
        elif comprimento_medio <=5:
            print("500")
        else:
            print("1000")
    except EOFError:
        break