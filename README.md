# Instruções gerais

- Duração: 45 minutos
- Tela compartilhada
- Clonar este repositório
- Adicionar solução para os desafios neste repositório

# Desafios

## Verificar se um número é um número de Armstrong

Definição: Um número inteiro positivo x de n algarismos é um número de Armstrong de ordem n se x é igual a soma das n-ésimas potências de seus algarismos.

- Exemplo 1: x = 153; n = 3: x é um número de Armstrong de ordem 3, pois x = 1^3 + 5^3 + 3^3.
- Exemplo 2: x = 13; n = 2: x não é um número de Armstrong de ordem 2, pois x != 1^2 + 3^2.

Desafio: Escreva um programa que determine se um número é um número de Armstrong e determine sua ordem.

---

## Imprimir elementos da sequência de Fibonacci

Definição: A sequência de Fibonacci (s[n]) é uma sequência de números inteiros positivos definida da seguinte forma:

s[0] = 0; s[1] = 1; … ; s[n] = s[n-1] + s[n-2], n >= 2.

Os 7 primeiros termos da sequência de Fibonacci são 0, 1, 1, 2, 3, 5 e 8.

Desafio: Escreva um programa que receba como entrada um número inteiro n e imprima em uma linha os n primeiros termos da sequência de Fibonacci, separados por “; ”.

- Exemplo: Para n = 5, a saída esperada é: "0; 1; 1; 2; 3"

---

## Encontrar o maior número entre três números

Desafio: Escreva um programa que receba três números e encontre o maior dentre eles, sem utilizar rotinas builtin (por exemplo, rotina max do Python).

---

## Verificar se um ano é bissexto

Definição: Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos, exceto anos múltiplos de 100 que não são múltiplos de 400.

Desafio: Escreva um programa que receba um número inteiro positivo representando um ano e determine se esse é um ano bissexto.

---

## Vetores: Busca, Inserção e Remoção

Desafio: Escreva um programa que contenha as seguintes 3 funções:

- search(v, x): Caso o elemento x esteja no vetor v, retorna o índice correspondente à primeira ocorrência do elemento x no vetor v. Caso contrário, retorna -1.
- insert(v, x, k): Insere o elemento x na posição de índice k do vetor v. Caso k for superior ou igual ao comprimento do vetor v, preencher as posições até o índice k com o valor 0.
- remove(v, x): Remove a primeira ocorrência do valor x no vetor v. Retorna -1, caso não haja nenhuma ocorrência.

Escreva uma função principal para executar as seguintes instruções:

- v = [0, -1, -2, -2, -4, -5]
- rs = search(v, -2)
- imprime rs
- rs = search(v, 2)
- imprime rs
- insert(v, 2, 3)
- imprime v
- insert(v, 10, 10)
- imprime v
- rr = remove(v, -2)
- imprime rr
- imprime v 


