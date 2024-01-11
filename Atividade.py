while True:
     try:
          NomeCompleto = (input("Nome Completo:"))
          DataNascimento = int(input("Data de Nascimento por favor: "))

          if (DataNascimento <= 1922) and (DataNascimento <= 2021):
                    idade = datetime.datetime.now().year - DataNascimento

                    print ("Seu nome: {NomeCompleto}")
                    print ("Sua idade:{DataNascimento}")

                    break

          else:
               print("Erro!!! não foi possivel, o ano tem que está ente 1922 e 2021. tente novamente")        
      
     except ValueError:

      print("Erro: Por favor, insira um valor numérico válido para o ano de nascimento.")

print("Programa encerrado.")
                  
              

