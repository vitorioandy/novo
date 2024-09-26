def analise_vendas(vendas):
  total_vendas = sum(vendas)
  media_vendas = total_vendas / len(vendas)
  return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas(opcao):
  entradas = {
    1: "120,150,170,130,200,250,180,220,210,160,140,190",
    2: "10,20,30,40,50,60,70,80,90,100,110,120",
    3: "5,10,15,20,25,30,35,40,45,50,55,60"
  }
  entrada = entradas.get(opcao)
  if entrada is not None:
    # Dividindo a string com split, mapeando para inteiros e convertendo para lista
    vendas = list(map(int, entrada.split(',')))
    return vendas
  else:
    print("Opção inválida")
    return []

vendas1 = obter_entrada_vendas(1)
vendas2 = obter_entrada_vendas(2)
vendas3 = obter_entrada_vendas(3)

print(analise_vendas(vendas1))
print(analise_vendas(vendas2))
print(analise_vendas(vendas3))
