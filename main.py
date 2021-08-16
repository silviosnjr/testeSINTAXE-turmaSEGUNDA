def escreve_idade():
    nome = input("Qual é o seu nome ?")
    nascimento = int(input("Em que ano você nasceu ?"))
    idade = 2021 - nascimento

    print("Olá ", nome, ", você tem ", idade, "anos")

    if (idade >= 18):
        print("Já pode tirar CNH")
    elif(idade >= 16):
        print("Já pode votar")
    elif(idade >=15 ):
        print("Já debutou!")
    else :
        print("Você tem menor que 15 anos é uma criança!")

escreve_idade()



