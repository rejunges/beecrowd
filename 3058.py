num_supermercados = int(input())
valor_grama = []
for i in range(num_supermercados):
    preco, gramas = map(float, input().split())
    valor_grama.append(preco/gramas)

print("{:.2f}".format(min(valor_grama)*1000))
