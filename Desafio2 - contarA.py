#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código

print("Contar Letras 'A' ")
frase = input("Escreva uma frase: ")

#deixa frase toda em minusculo 
frase = frase.lower()

if 'a' in frase:
    quantidades_A = frase.count('a')
    print(f"Há letras A nessa string! Ela aparece {quantidades_A} vezes!")
else:
    print("Não há letras a nessa string!")