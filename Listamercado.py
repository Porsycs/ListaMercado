carrinho = []
produto = ''

print('Adicione produtos ao carrinho ou digite sair: ')
while produto != 'sair':
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
carrinho.sort()
print('')
print('Produtos no carrinho: ')
for produto in carrinho:
    print(produto.title())
