#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


def calcularNum():
    num = 0
    try:
        num = int(input("Informe um número: "))
    except:
        print("Digite apenas número!")
        calcularNum()
        return
        
    a, b = 0, 1
    
    if num == a or num == b:
        print(f"O número {num}, pertence a sequencia de fibonacci!")
    
    proximo = a + b
    
    while proximo <= num:
        if proximo == num:
            print(f"O número {num}, pertence a sequencia de fibonacci!")
            return
        
        a = b
        b = proximo
        proximo = a + b
    
    print(f"O número {num}, não pertence a sequencia de fibonacci!")

calcularNum()