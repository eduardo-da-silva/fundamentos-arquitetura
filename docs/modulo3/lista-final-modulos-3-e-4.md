# Lista final — Módulos 3 e 4

!!! danger "Entrega"

    Trabalho **individual ou em dupla**. Entregar até **[DATA]**, em formato digital, antes do último encontro. No último encontro, cada dupla apresenta o tema da Parte B em cinco minutos (sem nota).

Esta lista fecha a disciplina. A **Parte A** aplica o Módulo 3 (Aulas 18 a 21) ao Orion, em quatro exercícios curtos e um ADR final. A **Parte B** abre o Módulo 4: cada dupla pesquisa um tema que não foi dado em aula e o liga ao que já decidimos sobre o Orion.

Como em todo o curso, avalia-se a **qualidade da justificativa**, não a escolha. Duas respostas opostas podem receber a nota máxima se ambas nomearem o contexto, a alternativa, o custo, a evidência e a condição em que estariam erradas.

## O que a lista pede, em resumo

| Parte | O que você faz | Pontos |
|---|---|---|
| A1 | Granularidade e contrato: avaliar uma proposta de corte e classificar mudanças de contrato | 10 |
| A2 | Dado: escolher como um serviço lê um dado que mudou de dono | 10 |
| A3 | Saga: classificar e ordenar os passos de um fluxo novo | 10 |
| A4 | Operação: preencher um balanço de extração e ler registros de dois serviços | 10 |
| A5 | ADR final do módulo: o que extrair primeiro, o que fica e quando parar | 20 |
| B | Pesquisa de um tema do Módulo 4, em uma página | 40 |

O tempo de esforço previsto é de cerca de cinco horas, distribuídas ao longo das duas semanas.

## Regras que valem para toda a lista

- **Os números vêm das aulas.** Use os fan-in e fan-out do grafo do Orion e os valores que as Aulas 16 a 21 apresentam. Onde não houver número, escreva **"não medido"** e diga como mediria. Não invente valores.
- **Toda decisão tem pelo menos duas alternativas reais**, que um time competente poderia escolher, e nomeia o que a escolha custa.
- **Exercícios de julgamento** (A2, A3 em parte, A5) aceitam mais de uma resposta. Não procure a preferência do professor: sustente a sua.
- **Diga o que observaríamos se a decisão estivesse errada.** É o critério que mais separa um argumento de uma opinião.

## Parte A — Módulo 3

Para os exercícios, o Orion é o do grafo das aulas. Lembrete dos números que interessam aqui: `Notificacoes` tem fan-in $C_a = 4$ e fan-out $C_e = 0$; `Logistica` e `Pagamentos` têm, cada um, $C_a = 1$ e $C_e = 1$. `Pedidos` depende de `Logistica`, e `Logistica` depende de `Notificacoes`.

### A1 — Granularidade e contrato (Aula 18) — 10 pontos

Uma colega propõe separar `Logistica` "porque tem $C_a = 1$ e $C_e = 1$, igual a `Pagamentos`, que já é o candidato ao corte".

1. Diga o que essas duas métricas dizem sobre o corte de `Logistica` e o que elas **não** enxergam.
2. Escolha **três** das dez forças da Aula 18 (de desintegração ou de integração) e diga que evidência você pediria para cada uma antes de aceitar a proposta.

Depois do corte, o contrato da cobrança chega à v3 com duas mudanças:

- (a) acrescenta o campo `motivo_recusa` na resposta;
- (b) passa a devolver `aprovada` também para cobranças "aprovadas com revisão posterior", que o provedor pode reverter.

3. Classifique cada mudança como aditiva, quebra de formato ou quebra de significado.
4. Diga qual leitor da Aula 18 (rígido, ingênuo ou tolerante) é pego por cada uma, e que teste de contrato detectaria (b).

### A2 — Dado (Aula 19) — 10 pontos

A tela de pedidos do Orion quer mostrar ao cliente o final do cartão usado na compra. Depois do corte de `Pagamentos`, o dado da cobrança é de `pagamentos`, e `compra` não lê os dados dele (é o que o ADR da Aula 19 decidiu).

1. Compare as três maneiras de ler um dado que mudou de dono: banco compartilhado, composição na borda e cópia local. Para cada uma, diga o que resolve e o que custa **neste caso**.
2. Escolha uma. Se escolher a cópia, diga **quais campos copiaria, quais não copiaria** e quem corrige a cópia quando ela envelhece.
3. Diga o que observaríamos em produção se a sua escolha estivesse errada.

Aqui há mais de uma resposta defensável. Uma boa resposta mostra que entendeu por que a alternativa que você não escolheu também seria razoável.

### A3 — Saga (Aula 20) — 10 pontos

O Orion ganha o fluxo de **cancelamento de pedido**, com quatro passos: estornar a cobrança, cancelar a entrega em `Logistica`, marcar o pedido como cancelado em `Pedidos` e avisar o cliente.

1. Classifique cada passo como compensável, pivô ou repetível. Justifique, usando o que sabemos de cada um (por exemplo, o que acontece se a entrega já foi despachada).
2. Escolha a ordem dos passos e diga por que ela reduz o que precisa ser compensado.
3. Para cada compensação que o seu desenho precisa, diga que tipo de custo pesa (monetário, de tempo, efeito visível ou irreversibilidade) e quem arca com ele.
4. Em até três linhas cada: (a) descreva um contexto em que você usaria *two-phase commit* e (b) um contexto em que a saga deixaria de servir.

### A4 — Operação (Aula 21) — 10 pontos

**Balanço.** A diretoria cogita extrair `Logistica`, em vez de `Pagamentos`. Monte o balanço de ganho e custo dessa extração, com as mesmas linhas da tabela da Aula 21. Cada linha recebe um número ou **"não medido"**, com a forma de medir.

- Conte as arestas remotas a partir do grafo do Orion.
- Diga quais valores do balanço de `Pagamentos` **não** valem para `Logistica` e por quê.
- Diga que time seria dono do serviço e em qual dos três arranjos da Lei de Conway você estaria.

**Registros.** Os dois serviços do fechamento gravaram estas linhas durante uma campanha. Os horários e os identificadores são fictícios.

```text
compra       10:00:01  fechamento iniciado: cobrar          id=f-17
pagamentos   10:00:02  cobranca aprovada                    id=f-17
compra       10:00:02  fechamento iniciado: cobrar          id=f-18
pagamentos   10:00:03  cobranca aprovada                    id=f-18
compra       10:00:04  emissao falhou: compensar            id=f-17
pagamentos   10:00:05  estorno executado
```

- A qual fechamento pertence o estorno da última linha? Diga o que você **consegue** afirmar e o que seria apenas suposição.
- Qual das três regras do identificador de correlação (nasce na borda, viaja em toda chamada, é gravado em toda linha) foi quebrada, e onde?
- Que risco isso traz quando dois fechamentos acontecem ao mesmo tempo?

### A5 — ADR final do módulo — 20 pontos

A diretoria do Orion aprovou **"extrair com critério"**, com orçamento de um trimestre. Escreva um ADR que responda:

1. **O que sai primeiro**, e por quê.
2. **O que fica** no monólito, e por quê.
3. **Quando parar**: que sinal medido faria a equipe interromper as extrações.

O ADR segue o formato do curso: contexto, decisão, alternativas, consequências (positivas **e** negativas) e reversão. Acrescente duas seções:

- **A alternativa de não extrair nada**, defendida em um parágrafo como opção real, e não como caricatura.
- **Critério de sucesso**: o que observaríamos, depois de um trimestre, se a decisão tivesse funcionado, e o que observaríamos se estivesse errada.

Use o que as aulas deram: as forças de granularidade (Aula 18), o dono do dado (19), a janela de inconsistência (20) e o balanço com números e "não medido" (21).

## Parte B — Pesquisa do Módulo 4 — 40 pontos

Cada dupla sorteia **um** tema. Se houver mais duplas que temas, o tema se repete. Responda às perguntas do seu tema usando as fontes de partida e o que vimos nas Aulas 16 a 21. As fontes estão nos livros da disciplina; as indicações são de capítulo.

### Tema 1 — Broker contra mediator

Fonte de partida: Richards e Ford, *Fundamentals of Software Architecture*, Cap. 14.

- Como funciona cada topologia, e quem guarda o estado do fluxo em cada uma?
- Qual delas serviria melhor ao fechamento do Orion (cobrar, emitir, notificar)? Por quê?
- O que cada uma custa para acompanhar um fechamento que falhou? Use o que vimos sobre o identificador de correlação na Aula 21.

### Tema 2 — Coreografia contra orquestração

Fonte de partida: Ford et al., *Software Architecture: The Hard Parts*, Cap. 11 e Cap. 12.

- Como ficaria a saga da Aula 20 coreografada? Diga quais eventos cada serviço publica e escuta.
- Onde fica o estado de cada fechamento, e quem decide a compensação?
- Qual das duas você escolheria para o Orion, e em que condição trocaria?

### Tema 3 — Acoplamento temporal

Fontes de partida: Newman, *Building Microservices*, Cap. 2 (nota sobre acoplamento temporal); *The Hard Parts*, Cap. 2.

- O que é acoplamento temporal, e como ele difere do acoplamento por dado?
- Quais chamadas do fechamento do Orion são temporalmente acopladas?
- Se `Pagamentos` passasse a responder por fila, o que mudaria na disponibilidade (Aula 17) e na janela de inconsistência (Aula 20)? O que a assincronia não resolve?

### Tema 4 — *Fitness functions*

Fonte de partida: Ford et al., *Building Evolutionary Architectures*, Cap. 2 e Cap. 4.

- O que é uma *fitness function*, e qual a diferença entre as atômicas e as holísticas, entre as gatilhadas e as contínuas?
- Transforme em *fitness function* três decisões das Aulas 16 a 21 (por exemplo, o teste de contrato, os contratos do `import-linter`, a janela da reconciliação). Diga como cada uma rodaria na CI e o que a faria falhar.
- Dê uma decisão que **não** dá para transformar em *fitness function*, e diga por quê.

### Tema 5 — Dívida arquitetural

Fonte de partida: *Building Evolutionary Architectures*, Cap. 7 (seção sobre dívida técnica).

- O que é dívida arquitetural, e como ela difere da dívida de código?
- Aponte três dívidas que as decisões das Aulas 16 a 21 criam no Orion. Dois exemplos possíveis: a cópia local que pode envelhecer e o intervalo de 15 minutos da reconciliação, que ninguém mediu.
- Proponha um plano para pagá-las em parcelas, com a ordem e o critério da ordem.

### Tema 6 — Entrega duplicada e ordem em filas

Fonte de partida: *Fundamentals of Software Architecture*, Cap. 14 (como evitar a perda de mensagem), mais uma fonte à sua escolha.

- O que prometem as garantias de entrega "no máximo uma vez", "ao menos uma vez" e "exatamente uma vez"?
- Se o evento "cobrança aprovada" chegar duas vezes a `compra`, o que acontece? Ligue com a idempotência das Aulas 16 e 20.
- E se "pedido emitido" chegar antes de "cobrança aprovada"? Diga o que o sistema precisaria fazer para aguentar isso.

### O que entregar da Parte B

Uma página, com estas quatro partes, nesta ordem:

| Item | O que é | Pontos |
|---|---|---|
| Respostas | as perguntas do tema, com as suas palavras e a ligação com o Orion | 15 |
| ADR curto | uma decisão sobre o Orion que o tema permite, com alternativa, custo e condição de falseamento | 10 |
| Fontes | pelo menos duas, uma delas dos livros da disciplina, com o capítulo | 5 |
| Pergunta aberta | uma pergunta que as fontes não respondem, com a sua hipótese | 10 |

## O que entregar

Um único arquivo (`lista-final.md` ou PDF) com as seções **A1**, **A2**, **A3**, **A4**, **A5** e **B**, nessa ordem. Se for em dupla, indique no início quem fez cada parte; as duas pessoas respondem pela lista inteira.

## Como será avaliado

| Critério | O que a nota máxima exige |
|---|---|
| Contexto | a resposta diz sob que restrição vale |
| Alternativa | há uma alternativa real, que alguém competente escolheria, descrita sem caricatura |
| Custo | o que a escolha custa e o que ela impede |
| Evidência | número, dependência, teste ou incidente, e não "é mais limpo" |
| Falseabilidade | a resposta diz o que observaríamos se estivesse errada |

Cada item da lista é avaliado por esses critérios, com o peso indicado nos pontos de cada exercício.

**Penalidades.**

- Decisão sem nenhum custo nomeado: **teto de 60%** do valor do item.
- Alternativa montada só para perder: **zera** o critério de alternativa.
- Números que não batem entre si dentro de um mesmo item: **zera** o item de diagnóstico ou de balanço.

## Erros comuns

- **Usar uma métrica como veredito.** $C_a$ e $C_e$ contam arestas; dizem onde olhar, e a decisão continua precisando das forças e da evidência.
- **Copiar para o ADR a resposta da aula.** O Orion é o mesmo, mas `Logistica` e o cancelamento de pedido não foram resolvidos em aula.
- **Esconder o custo da opção escolhida.** Toda opção tem um, e uma proposta sem custo nomeado é um anúncio.
- **Responder a Parte B com o resumo do livro.** As perguntas pedem que você use o tema para decidir algo sobre o Orion.
- **Inventar números.** Onde não há medida, escreva "não medido" e diga como medir.
