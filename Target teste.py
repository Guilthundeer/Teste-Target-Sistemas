import json

# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

int Indice = 13, Soma = 0, K = 0;

while (K < Indice) {
    K = K + 1;
    Soma = Soma+ K;
}

System.out.println(Soma);

#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a 
# soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na 
# linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o
# número informado pertence ou não a sequência.


def pertence_fibonacci(num):
    fib_1, fib_2 = 0, 1
    while fib_1 <= num:
        if fib_1 == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return f"O número {num} NÃO pertence à sequência de Fibonacci."

num = int(input("Informe um número: "))
print(pertence_fibonacci(num))




# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal


faturamento_json = '''
[
    {"dia": 1, "valor": 200.0},
    {"dia": 2, "valor": 0.0},
    {"dia": 3, "valor": 350.0},
    {"dia": 4, "valor": 400.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 100.0},
    {"dia": 7, "valor": 0.0}
]
'''

faturamento = json.loads(faturamento_json)

def calcular_faturamento(faturamento):
    valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

menor, maior, dias_acima_media = calcular_faturamento(faturamento)
print(f"Menor faturamento: R${menor}")
print(f"Maior faturamento: R${maior}")
print(f"Dias acima da média: {dias_acima_media}")


# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  




faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_estados.values())

def calcular_percentuais(faturamento_estados, total):
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}
    return percentuais

percentuais = calcular_percentuais(faturamento_estados, total)

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")




#5) Escreva um programa que inverta os caracteres de um string.

def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Exemplo de uso:
string = input("Digite uma string: ")
print("String invertida:", inverter_string(string))

