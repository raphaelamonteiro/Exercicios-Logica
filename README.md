# Exercícios de Lógica

1. Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. <br>
**IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;**

2. Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
**IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;**

3. Observe o trecho de código abaixo: <br>
``` python
int INDICE = 12, SOMA = 0, K = 1;
enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
```
Ao final do processamento, qual será o valor da variável SOMA? <br>

4. Descubra a lógica e complete o próximo elemento: <br>
a) 1, 3, 5, 7, ___ <br>
resp: 9, somente números ímpares <br>
b) 2, 4, 8, 16, 32, 64, ____  <br>
resp: 128, dobro dos números (2 * 2 = 4 * 2 = 8 * 2 = 16...) <br>
c) 0, 1, 4, 9, 16, 25, 36, ____ <br>
resp: 49, somando os números ímpares(0 + 1 = 1 + 3 = 4 + 5 = 9 + 7 = 16...) <br>
d) 4, 16, 36, 64, ____ <br>
resp: 100, somando os números á números que tem como diferença 8 (4 + 12 = 16 + 20 = 36... // 20 - 12 = 8) <br>
e) 1, 1, 2, 3, 5, 8, ____ <br>
resp: 13, somando os dois números anteriores da sequência (1 + 0 = 1, 1 + 1 = 2, 2 + 1 = 3, 3 + 2 = 5, 5 + 
f) 2,10, 12, 16, 17, 18, 19, ____ <br>
resp: 20, O padrão da sequência é um aumento alternado de 8, 2, 4 e 1 (2 + 8 = 10, 10 + 2 = 12, 12 + 4 = 16, 16 + 1 = 17, 17 + 1 = 18, 18 + 1 = 19)


6.  Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? <br>
Ligue o interruptor 1 por 5 minutos. Em seguida, desligue-o e ligue o interruptor 2 por 5 minutos. Desligue o interruptor 2 e ligue o interruptor 3 por 5 minutos. Desligue o interruptor 3. <br>

Vá até uma das salas das lâmpadas e observe as lâmpadas. <br>
- Uma lâmpada está acesa (quente)
- Uma lâmpada está morna (não acesa, mas quente)
- Uma lâmpada está fria (não acesa e não quente)
- As outras duas lâmpadas estão frias

Com base nisso, é possível deduzir as seguintes informações:
<br>
Se uma lâmpada estiver acesa, ela é controlada pelo interruptor 3.<br>
Se uma lâmpada estiver morna, ela é controlada pelo interruptor 2.<br>
Se uma lâmpada estiver fria, ela é controlada pelo interruptor 1.<br>

