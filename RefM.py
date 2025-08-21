class ContaBancaria:
  def __init__(self, titular, saldo) -> None:
     self.titular = titular
     self.saldo = saldo
 
  def exibir_saldo(self):
    print(f"{self.titular} tem R$ {self.saldo:.2f} na conta.")

# Objetos diferentes, com os mesmos dados
minhaConta = ContaBancaria('Paulo', 2000.00)
suaConta = ContaBancaria('João', 1500.00)

print(minhaConta is suaConta)

print(minhaConta.titular)
print(suaConta.titular)

minhaConta.exibir_saldo()
suaConta.exibir_saldo()
print()
minhaConta = suaConta # Agora os dois apontam para o mesmo objeto

minhaConta.saldo=4000

print(minhaConta is suaConta)# True
print(minhaConta.titular)
print(suaConta.titular)

minhaConta.exibir_saldo()
suaConta.exibir_saldo()
