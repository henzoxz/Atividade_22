# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
soma = 0

while True:
     
    num  = int(input("Digite o Número:"))
    if num == 0:
      break


    soma += num
   
print(f"{soma}")