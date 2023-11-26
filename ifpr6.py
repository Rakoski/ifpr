# Chaves padrão do dicionário pessoas: nome, email, sal, nasc
import ifpr6_funcoes as ifpr

opcao_escolhida = ifpr.menu()
dictio = {"nome": "Márcia", "email": "marciastainer@gmail.com", "salario": 5000, "nascimento": "02/11/1972"}

if opcao_escolhida == 1:
    ifpr.inserir_dados("ifpr6", dictio)

