def analise_vendas(vendas):
  total_vendas = sum(obter_entrada_vendas)
  media_vendas = total_vendas / len(obter_entrada_vendas)
  return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas(opcao):
  entradas = {
   input("", "", "",)}
  vendas = list(map(vendas.split(",")))


