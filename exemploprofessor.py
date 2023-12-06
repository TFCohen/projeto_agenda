
turma = []

while True :
    print("Menu")
    print("1 Cadastro")
    print("2 Listar")
    print("3 Pesquisar")
    print("4 Alterar")
    print("5 Excluir")
    print("9 Sair")

    opcao = int(input("Informe a opção: "))

    if opcao == 1:
       aluno = {}
       aluno['nome'] = input("Informe o nome do aluno: ")
       aluno['disciplina'] = (input("Informe o nome da disciplina: "))
       aluno['nota1'] = float(input("Informe a primeira nota: "))
       aluno['nota2'] = float(input("Informe a segunda nota: "))
       aluno['nota3'] = float(input("Informe a terceira nota: "))
       aluno['nota4'] = float(input("Informe a quarta nota: "))
       turma.append(aluno)
    elif opcao == 2:    
        for m in turma:
            media = (m['nota1'] + m['nota2'] + m['nota3'] + m['nota4'])/4
            situacao = ''     
            if media >= 7:
                situacao = "Aprovado"
            else:
                situação = "Reprovado"    
            print(f"{m['nome']} - {m['disciplina']} - {m['nota1']} - {m['nota2']} - {m['nota3']} - {m['nota4']} {media:.2f} {situacao}")         
                  
    elif opcao == 3:  
        nomebusca = input("Informe nome: ")
        posicao = -1
        i = 0
        for m in turma:
            if m['nome'].lower() == nomebusca.lower():
                    posicao = i
                    break
            i = i + 1

            if posicao > -1:
                print(f"{turma[posicao]['nome']} - {turma[posicao]['disciplina']} - {turma[posicao]['nota1']} - {turma[posicao]['nota2']} - {turma[posicao]['nota3']} - {turma[posicao]['nota4']} {media:.2f} {situacao}")
            else:
                print("Não encontrado")
   
    elif opcao == 4:  
        nomebusca = input("Informe nome: ")
        posicao = -1
        i = 0
        for m in turma:
            if m['nome'].lower() == nomebusca.lower():
                    posicao = i
                    break
            i = i + 1

            if posicao > -1:
                turma[posicao]['nome'] = input("Informe o nome do aluno: ")
                turma[posicao]['disciplina'] = (input("Informe o nome da disciplina: "))
                turma[posicao]['nota1'] = float(input("Informe a primeira nota: "))
                turma[posicao]['nota2'] = float(input("Informe a segunda nota: "))
                turma[posicao]['nota3'] = float(input("Informe a terceira nota: "))
                turma[posicao]['nota4'] = float(input("Informe a quarta nota: "))
            else:
                print("Não encontrado")
    elif opcao == 5:  
        pass
    elif opcao == 9:  
        break
    else:
        print("Opção inválida")

