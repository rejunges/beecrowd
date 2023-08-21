num_a, num_b = map(int, input().split())
while num_a != 0 and num_b != 0:
    soma = num_a + num_b
    resultado = str(soma).replace("0","")
    print(resultado)
    num_a, num_b = map(int, input().split())