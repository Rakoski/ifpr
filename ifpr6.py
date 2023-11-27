# Chaves padrão do dicionário pessoas: nome, email, sal, nasc
import ifpr6_funcoes as ifpr

opcao_escolhida = ifpr.menu()
dictio = {"nome": "Mateus", "email": "msrakoski@gmail.com", "salario": 1000, "nascimento": "03/12/2004"}

if opcao_escolhida == 1:
    ifpr.inserir_dados("ifpr6", dictio)

elif opcao_escolhida == 2:
    print(ifpr.ler_arquivo("ifpr6"))

elif opcao_escolhida == 3:
    print(ifpr.acessar_onde_tem_n("ifpr6", "Márcia"))


