# Aula 22 — Oficina: o que extrair primeiro

## Objetivo e competências

Ao fechar a oficina, conseguimos:

- montar uma proposta de extração priorizada, em que cada item tem a força que o justifica, o preço que cobra e a evidência (ou a marca "não medido") que o sustenta;
- fixar um **critério de parada** observável: o ponto a partir do qual o grupo recomenda não extrair mais nada;
- defender a alternativa **"não extrair nada"** como opção real, com contexto, custo e condição de falseamento;
- registrar a ordem da extração em um ADR com consequências negativas e uma condição que o desmentiria;
- sustentar a proposta diante de perguntas que oferecem uma alternativa legítima que o grupo não escolheu.

## O pedido da diretoria

A diretoria aprovou, na reunião de planejamento, a frase "extrair com critério". Ela deixa de lado o "plano de migração para microsserviços" que abriu o Módulo 2 e pede algo diferente: **um plano**. O que sai primeiro? O que fica onde está? Em que ponto o time para e diz que o resto do sistema não compensa a rede?

O pedido é o oposto do de um catálogo de boas práticas. A diretoria quer uma ordem, um prazo e uma justificativa. E, por trás, quer saber uma coisa que a frase "extrair com critério" deixa implícita: se a resposta honesta, para este momento do Orion, é *não extrair nada*, o time tem coragem de dizê-lo com evidência?

Não há conceito novo nesta aula. O que se exercita é a competência central do módulo: **decidir sob restrição**, com tudo o que as Aulas 16 a 21 mediram à vista.

## O que cada aula deixou na mesa

A oficina não reconstrói nada. Os artefatos abaixo já existem, e o trabalho do grupo é combiná-los sobre o seu recorte.

| Aula | O que deixou | Para que serve na oficina |
|---|---|---|
| 16 | Arestas do recorte que atravessam a rede, com a falácia de cada uma | contagem de custo de rede por candidato |
| 17 | Formas do *deployable* e a conta de disponibilidade | comparar "manter", "cortar pouco" e "dividir mais" |
| 18 | Matriz de forças, ordem dos candidatos e regra de evolução do contrato | justificar por que um candidato vem antes de outro |
| 19 | Tabela de dados: dono, quem lê, como lê depois do corte | nomear o que o *join* perdido custa |
| 20 | Escolha de consistência, janela tolerada e saga da operação crítica | dizer o que acontece entre dois passos |
| 21 | Balanço de ganho e custo, com número ou "não medido" | mostrar quais itens da conta ainda não se sustentam |

No Mini-Orion, a mesma cadeia está resolvida e executável: `06-microkernel` (17 testes, 4 contratos) deu a fronteira lógica com o microkernel de `Promocoes`; `07-remoto` (57 testes, 6 contratos) pôs `Pagamentos` atrás da rede e escreveu o acordo entre os lados; `08-dados` (66 testes, 8 contratos) deu ao serviço o dado próprio; e `09-saga` (82 testes, 9 contratos) pôs o fechamento como saga, com reconciliação e rastro. A cadeia é referência para ler, não exercício para refazer.

## Aquecimento

Esta aula não tem resposta comentada. A oficina inteira é o exercício, e o que se avalia é a defesa.

Antes de começar, cinco minutos sozinho com o recorte do grupo. Anote:

- o candidato à extração que você escolheria **hoje**, com a razão em uma frase;
- o item da conta de que você menos tem evidência;
- o argumento mais forte **contra** o seu candidato;
- o que você diria à diretoria se a resposta fosse "não extrair nada".

Guarde a primeira anotação. Ao final, compare com a decisão do grupo. Se forem iguais, verifique se o grupo discutiu ou convergiu cedo demais para a primeira opinião dita em voz alta.

## A oficina

Dois encontros. O mapa, as métricas, a matriz de forças e o balanço já existem das aulas anteriores, e reconstruí-los ocuparia a oficina inteira sem exercitar nada novo. O que se exercita aqui é **ordenar e justificar sob restrição**.

A conta do tempo foi feita antes de definir a divisão. Ler os artefatos (5 min), preencher a matriz de forças de três candidatos com evidência (20), completar o balanço de um deles (15), ordenar os candidatos (10), fechar o critério de parada e a defesa de "não extrair" (10) e escrever um ADR completo (25 a 30) somam de 85 a 90 minutos. Os dois encontros têm 100. Sobram de 10 a 15 minutos, que cabem uma defesa de 10 minutos, e por isso a defesa de cada grupo é curta.

### Encontro 1 — Diagnóstico e candidatos (50 min)

| Etapa | Tempo |
|---|---|
| Ler os artefatos do recorte (matriz, tabela de dados, balanço) e marcar o que falta | 5 min |
| Matriz de forças para três candidatos, com evidência em cada célula | 20 min |
| Balanço do candidato mais forte: número ou "não medido" em cada item | 15 min |
| Ordem preliminar dos candidatos, com a restrição abaixo | 10 min |

Entrega do encontro: a matriz e o balanço preenchidos, e uma ordem provisória. Sem ADR ainda: a tentação de já escrever a decisão atrapalha a leitura da evidência.

### Encontro 2 — Proposta e defesa (50 min)

| Etapa | Tempo |
|---|---|
| Fechar o critério de parada e a defesa de "não extrair nada" | 10 min |
| Escrever o ADR da ordem, com consequências positivas e negativas | 25 min |
| Defesa de um grupo, 10 min, com a banca | 15 min |

O fim do encontro comporta uma defesa; as demais acontecem no início da semana seguinte, em sequência, com a mesma banca. O ADR escrito é a entrega; a defesa só avalia se o grupo entende o que escreveu.

!!! danger "A restrição"

    O grupo tem **um trimestre e duas pessoas**. Isso dá para uma extração, não para três. A proposta ordena os candidatos, mas autoriza o time a executar **um** deles antes de rever.

    Escolham a primeira extração. Digam o que ficou de fora e o que pode acontecer por causa disso.

## O que a proposta deve conter

A proposta segue o formato das entregas do Orion Evolution Lab, com três exigências específicas desta oficina.

**A ordem das extrações, com a força que justifica cada uma.** Não é suficiente dizer "`X` primeiro". A justificativa aponta a célula da matriz que a sustenta e a força de integração que a contraria, quando houver.

**O critério de parada.** É a condição observável em que o grupo recomenda não extrair o próximo candidato. "Quando não houver mais o que extrair" não conta, porque nenhuma medida a desmentiria. Um exemplo do formato: "para depois de `Pagamentos`, e só reabre se a espera pelo *deploy* conjunto de `Promocoes` passar de duas vezes por sprint durante um trimestre". O critério precisa de uma medida e de um prazo.

**A alternativa "não extrair nada", defendida.** Não como caricatura, nem como nota de rodapé. O grupo escreve, em um parágrafo, o melhor argumento a favor de manter o monólito modular, com o contexto em que ele vale, o que a extração compraria e por que o grupo, ainda assim, extrai (ou não). Uma proposta que extrai tem de mostrar que a alternativa foi levada a sério, e uma que recomenda não extrair tem de dizer o que a faria mudar de ideia.

## Avaliação

Rubrica do Orion Evolution Lab, com o peso de **Priorização** lido como "ordem das extrações sob orçamento". Dois lembretes que valem nota:

- uma proposta **sem a alternativa "não extrair" defendida** tem teto de nota;
- números que não fecham entre si (arestas remotas contadas de um jeito na matriz e de outro no balanço, por exemplo) zeram o critério de **Diagnóstico**.

E os dois que já valem desde o Módulo 1: proposta sem nenhum custo nomeado tem teto de 60, e alternativa montada só para perder zera o critério de alternativas.

### Perguntas da banca

Cada grupo responde, ao final:

1. Qual extração vem primeiro, e qual célula da matriz a sustenta?
2. Qual força de integração contraria essa escolha, e como o grupo vive com ela?
3. Em que ponto o grupo para, e como esse ponto é medido?
4. **O que vocês observariam daqui a seis meses se a ordem estivesse errada?**
5. Uma alternativa que o grupo não escolheu: por que não *service-based* de poucos domínios, ou por que não manter o monólito modular por mais um ano?

A quarta é a que separa proposta de palpite. A quinta oferece uma alternativa legítima, não para derrubar o grupo, mas para ver se ele entende por que a descartou.

### Erros comuns

Três padrões se repetem quando uma proposta de extração é fraca. O primeiro é **ordenar por contagem**: o candidato com mais arestas ou mais dependentes vai primeiro, sem dizer se a aresta é custo ou motivo. O segundo é **citar ganho sem medida**: "autonomia de time" ou "escala independente" aparecem como fatos, sem dizer quem é o time ou qual carga. O terceiro é **parar sem critério**: a proposta termina na primeira extração e não diz o que reabriria a discussão. Os três vêm do hábito de procurar a resposta que o professor quer, e a rubrica os pune pelo mesmo motivo: o que se avalia é o argumento.

## Fechamento e ponte

Ao fim da oficina, cada grupo tem uma ordem de extração, um critério de parada e a defesa de que não extrair é uma opção legítima. Mais que o plano, importa o hábito que o módulo treinou: toda alternativa de distribuição passa pela conta (rede, dado, consistência, operação) antes de ser recomendada, inclusive a de não distribuir.

O Orion, depois deste módulo, tem serviços que se chamam. A cobrança chama o estorno, o fechamento chama a cobrança, a reconciliação chama a consulta. Cada chamada espera a resposta de outra. E se, em vez de chamar, um serviço publicasse o que aconteceu, e quem se interessasse reagisse? O Módulo 4 pergunta o que isso troca: o acoplamento temporal sai, e entram a ordem dos eventos, a duplicação e a dificuldade de enxergar o fluxo inteiro.

## Leitura complementar

- Richards, Mark; Ford, Neal. *Fundamentals of Software Architecture*. Cap. 17 — Microservices Architecture (as seções sobre granularidade e sobre o que o estilo cobra).
- Newman, Sam. *Building Microservices*. 2. ed. Cap. 3 — Splitting the Monolith (a extração gradual e os padrões de transição).
- Ford, Neal; Richards, Mark; Sadalage, Pramod; Dehghani, Zhamak. *Software Architecture: The Hard Parts*. O'Reilly, 2021. Cap. 7 — Service Granularity.

## Referências

- RICHARDS, Mark; FORD, Neal. *Fundamentals of Software Architecture: An Engineering Approach*. O'Reilly, 2020.
- NEWMAN, Sam. *Building Microservices*. 2. ed. O'Reilly, 2021.
- FORD, Neal; RICHARDS, Mark; SADALAGE, Pramod; DEHGHANI, Zhamak. *Software Architecture: The Hard Parts*. O'Reilly, 2021.
