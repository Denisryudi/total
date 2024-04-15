vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}

def segundo_item(tupla):
    return tupla[1]
#list, transforma em tupla. lista ordena pelo primeiro valor. (necessita da func)
lista = list(vendas_produtos.items())
lista.sort(key=segundo_item)
print(lista)

segundo_item1 = lambda tupla: tupla[1]
lista1 = list(vendas_produtos.items())
lista1.sort(key=segundo_item1)
print(lista1)

minha_funcao = lambda num: num*2
print(minha_funcao(5))

imposto = 0.3

imposto_1 = lambda valor: valor * 1.3
