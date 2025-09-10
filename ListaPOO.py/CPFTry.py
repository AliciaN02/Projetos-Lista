class CPF: 
  def validar(self):
    try: 
      cpf = (input("Informe o número do seu CPF: ")).strip()

      int(cpf)

      if len(cpf) == 11:
        print(f"O formato do CPF é válido: {cpf}")
      else: 
        print("Erro! CPF deve conter exatamente 11 dígitos.")
    except ValueError:
      print("Erro! Formato ínvalido, informe inteiros!")

c = CPF()
c.validar()
