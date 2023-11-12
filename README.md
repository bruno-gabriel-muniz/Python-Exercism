# Exercícios do site Execism

Este é o projeto em que eu vou realizar todos os  exercícios de python do site Exercism, assim como, avaliar os resultados obtidos neles, através deste mesmo arquivo readme.

# Versionamento

Além disso, o versionamento será guiado por versões, em que acada nova Major Version significa que um novo exercício foi iniciado. Dessa forma, mesmo que isso não esteja relacionado com a compatibilidade do programa, acredito ser um bom teste para me adaptar as tags.

# Exercícios

## currency-exchange -- 1.3

Exercício básico sobre a lógica e as operações básicas da matemática.

## meltdown-mitigation -- 2.2

Exercício sobre estruturas de decisão (`if`, `elif` e `else`), em que também pode-se usar os operadores lógicos `and` e `or` para melhorar a legibilidade do código.
<div>
Nele foquei em usar as estruturas de decisão elfi e else (como pode ser visto na segunda função) e os operadores lógicos and e or (na primeira função) além da estrutura de decisão if.
</div>

#### Primeira função:

```
return temperature < 800 and neutrons_emitted > 500 and temperature*neutrons_emitted < 500000
```

#### Segunda função:

```
    # calculando o valor da eficiencia
    eficiencia = (voltage * current)/theoretical_max_power
    # verificando se se enquadra na faixa da bandeira verde
    if eficiencia >= 0.8:
        flag = 'green'
    # verificando se se enquadra na faixa da bandeira laranja
    elif eficiencia >= 0.6:
        flag = 'orange'
    # verificando se se enquadra na faixa da bandeira vermelha
    elif eficiencia >= 0.3:
        flag = 'red'
    # e, caso não se encaixe em nenhuma, declarando que é bandeira preta
    else:
        flag = 'black' 
    # retornando o valor encontrado   
    return flag 
```