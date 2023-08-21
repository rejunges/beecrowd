def is_primo(num):
    if num <= 1:
        return False
    
    num_divisiveis = 0
    for i in range(1, num+1):
        if num%i == 0:
            num_divisiveis += 1
        if num_divisiveis > 2:
            return False
    return True

while True:
    try:
        num_moedas = int(input())
        if not num_moedas:
            break
        valor_moedas = []
        for _ in range(num_moedas):
            valor_moedas.append(int(input()))
        num_saltos = int(input())

        soma_moeda = sum(valor_moedas[::-num_saltos])

        if is_primo(soma_moeda):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")
    except EOFError:
        break
