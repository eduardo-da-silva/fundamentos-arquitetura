# Aula 3 — Características arquiteturais

## Objetivo da aula

Identificar as características arquiteturais que importam para um sistema, priorizá-las sob restrição e torná-las mensuráveis — para que decisões arquiteturais deixem de ser disputa de preferência.

## Competências desenvolvidas

- distinguir requisito funcional de característica arquitetural;
- classificar características em operacionais, estruturais e transversais;
- priorizar um conjunto pequeno de características e justificar o que ficou de fora;
- transformar uma característica vaga em critério verificável.

## A reunião que não termina

A Orion vai lançar a campanha de novembro. A reunião de planejamento arquitetural está na terceira semana.

Rafael, da plataforma, quer investir em disponibilidade: "se o checkout cair no pico, perdemos o ano".

Júlia, de produto, quer investir em modifiabilidade: "precisamos lançar três regras de promoção novas durante a campanha, e hoje cada uma leva duas semanas".

Camila, do atendimento, quer investir em consistência: "não podemos confirmar pedido e depois cancelar. O custo de suporte de um cancelamento é maior que a margem da venda".

Os três estão certos. Os três têm dados. E o orçamento dá para um.

O problema não é técnico e não é de comunicação: é que **ninguém escreveu qual dessas propriedades o sistema precisa ter mais**. Sem essa lista, cada decisão de arquitetura vira uma nova rodada da mesma discussão, e quem tem mais senioridade ou mais paciência decide.

## Desenvolvimento conceitual

### O que é uma característica arquitetural

Um requisito funcional diz **o que** o sistema faz: "o cliente finaliza a compra". Uma característica arquitetural diz **como ele precisa ser** enquanto faz isso: rápido, disponível, seguro, fácil de mudar.

A distinção prática é esta: você consegue implementar o requisito funcional ignorando completamente a característica — e o sistema vai funcionar na sua máquina. A conta chega depois, em produção.

Richards e Ford propõem três marcas. Uma característica arquitetural:

1. **é não-funcional** — descreve uma qualidade, não um comportamento;
2. **influencia algum aspecto estrutural** — se ela não muda nada no desenho do sistema, não é arquitetural;
3. **é crítica ou importante para o sucesso** — nem toda qualidade desejável entra na lista.

A segunda marca é a mais útil para filtrar. "O sistema deve ser bonito" é uma qualidade legítima e não muda nenhuma fronteira de componente. "O sistema deve continuar aceitando pedidos com o provedor de pagamento fora do ar" muda o desenho inteiro.

### Três famílias

| Família | Do que trata | Exemplos no Orion |
|---|---|---|
| **Operacionais** | como o sistema se comporta rodando | disponibilidade, desempenho, escalabilidade, recuperação a falhas |
| **Estruturais** | como o sistema se deixa modificar | modifiabilidade, extensibilidade, testabilidade, capacidade de implantação |
| **Transversais** | restrições que atravessam tudo | segurança, privacidade, acessibilidade, conformidade fiscal |

A separação não é rígida e não precisa ser. Ela serve para uma coisa: revelar a família que você esqueceu. Times de produto tendem a listar só operacionais; times de plataforma, só estruturais. Quase todo mundo esquece transversais até o jurídico aparecer.

### Implícitas e explícitas

**Explícitas** são as que alguém pediu. Aparecem no documento de requisitos, na reunião, no contrato com o parceiro.

**Implícitas** são as que ninguém pede porque ninguém imagina viver sem. Ninguém escreve "o sistema não deve expor o cartão de crédito de um cliente para outro". E, no entanto, essa é a característica cuja violação encerra a empresa.

!!! warning "As implícitas são as que derrubam projetos"

    Uma característica explícita mal atendida gera reclamação e uma tarefa no backlog.

    Uma característica implícita violada gera incidente, e quase sempre a descoberta de que a estrutura inteira supunha o contrário.

    Ao levantar características, pergunte sempre: **o que seria tão inaceitável que ninguém pensou em escrever?**

### Menos é mais

A tentação diante da lista é marcar tudo. Disponibilidade? Óbvio. Segurança? Claro. Desempenho? Sem dúvida.

Uma lista com doze características prioritárias é exatamente igual a uma lista com zero: quando duas entram em conflito — e elas entram, o tempo todo — ela não diz qual vence.

Richards e Ford recomendam **no máximo sete**, e argumentam que menos é melhor. A razão é estrutural, não de gestão: cada característica que você resolve suportar de verdade adiciona mecanismo ao sistema. Suportar disponibilidade alta significa redundância, health check, fallback, monitoramento. Suportar elasticidade significa outro conjunto. Suportar os dois significa os dois conjuntos, mais a complexidade da interação entre eles.

Arquitetura para tudo é arquitetura que não entrega nada, atrasada.

### Elas competem entre si

Este é o ponto que devolve a Primeira Lei da Arquitetura, vista na Aula 2, para o centro da conversa.

| Se você prioriza | Costuma pagar em |
|---|---|
| Disponibilidade | consistência — o teorema CAP não é opinião |
| Desempenho | modifiabilidade — cache e desnormalização engessam |
| Segurança | usabilidade e desempenho — toda verificação custa |
| Modifiabilidade | desempenho — indireção tem preço |
| Escalabilidade | simplicidade operacional — mais partes, mais falhas |

Priorizar características **é** escolher trade-offs, antecipadamente e por escrito, em vez de descobri-los na terceira semana de reunião.

### Vaga não serve

"O sistema deve ser escalável" não é utilizável. Não dá para projetar contra isso, não dá para testar, e duas pessoas concordam com a frase pensando em coisas diferentes.

Uma característica só entra na lista quando vira critério verificável:

| Vago | Utilizável |
|---|---|
| "deve ser rápido" | busca no catálogo responde em menos de 300 ms no percentil 95 |
| "deve ser escalável" | suporta 8x o volume normal de checkout sem degradar o percentil 95 |
| "deve ser disponível" | checkout aceita pedidos com um provedor de pagamento fora do ar |
| "deve ser fácil de mudar" | uma nova regra de promoção entra em produção em até 3 dias, sem alterar o `Checkout` |
| "deve ser seguro" | dado de cartão nunca transita por componente fora de `Pagamentos` |

Repare no que aconteceu na coluna da direita: cada frase virou **testável**. E uma característica testável pode virar um teste automatizado que roda na CI — que é exatamente o que faremos na Aula 7 com o `import-linter`.

A última linha da tabela é um bom exemplo: "deve ser seguro" não diz nada a um desenvolvedor; "dado de cartão nunca sai de `Pagamentos`" diz onde a fronteira precisa estar.

## O caso Orion

Voltemos à reunião. Aplicando o método:

**Levantamento.** Disponibilidade, desempenho, escalabilidade, consistência, modifiabilidade, testabilidade, segurança, conformidade fiscal, recuperação a falhas, observabilidade.

Dez candidatas. Nenhuma absurda.

**Corte.** O contexto é uma campanha de duas horas com 8x de volume, três regras de promoção novas durante o período, e uma equipe pequena. Isso descarta o que não é decisivo *neste* recorte — não porque não importe, mas porque não vai mudar nenhuma decisão agora.

**Prioridade.** Três, nesta ordem:

1. **Disponibilidade do checkout** — o checkout aceita pedidos com um provedor de pagamento indisponível.
2. **Modifiabilidade das promoções** — uma regra nova entra em produção em até 3 dias, sem tocar no `Checkout`.
3. **Consistência do pedido** — nenhum pedido confirmado ao cliente é cancelado depois por falha de cobrança.

**O que ficou de fora, e o risco.** Escalabilidade do catálogo: se a busca degradar no pico, perdemos conversão antes mesmo do checkout. Aceitamos o risco porque o catálogo é majoritariamente leitura e já está atrás de cache — mas isso é uma aposta, e está escrita como aposta.

!!! note "1 e 3 se contradizem, e é proposital"

    Aceitar pedido com o provedor fora do ar (característica 1) significa confirmar antes de ter certeza da cobrança. Nunca cancelar um pedido confirmado (característica 3) significa o contrário.

    A ordem resolve o conflito: quando os dois colidirem, disponibilidade ganha. Consequência aceita: haverá uma janela em que o pedido está confirmado e a cobrança, pendente — e alguém do atendimento terá trabalho.

    **Uma lista de prioridades que nunca gera conflito não foi priorizada.** Se todas as suas características convivem em paz, você listou desejos, não escolhas.

## Exercícios

1. **Classifique.** Requisito funcional ou característica arquitetural?

    a. O cliente pode aplicar um cupom no carrinho.
    b. A aplicação do cupom não pode aumentar em mais de 50 ms o tempo do checkout.
    c. O sistema envia e-mail de confirmação.
    d. A falha no envio do e-mail não impede a confirmação do pedido.

    ??? note "Resposta comentada"

        **a** e **c** são funcionais: descrevem o que o sistema faz.

        **b** e **d** são arquiteturais, e repare que cada uma é a contraparte da anterior. Elas não descrevem comportamento novo — descrevem uma qualidade do comportamento já existente, e ambas mudam o desenho.

        **d** em particular determina se `Notificacoes` fica dentro ou fora do caminho crítico do `Checkout`. É uma frase de uma linha que decide uma fronteira de componente, e é exatamente esse tipo de frase que estamos procurando.

2. **Torne mensurável.** Reescreva como critério verificável:

    a. "O catálogo deve ser rápido."
    b. "O sistema deve ser resiliente."
    c. "O código deve ser fácil de manter."

    ??? note "Resposta comentada"

        Não há redação única — há redações utilizáveis e inutilizáveis. Três exemplos aceitáveis:

        a. Busca por termo retorna em menos de 300 ms no percentil 95, com 10 mil produtos ativos.

        b. Com qualquer um dos provedores de pagamento fora do ar, a taxa de pedidos aceitos cai no máximo 5%.

        c. Adicionar uma forma de pagamento não exige alterar `Checkout` nem `Pedidos` — verificável por um contrato de dependência.

        O teste da sua resposta: **duas pessoas conseguiriam discordar sobre se o critério foi atendido?** Se sim, ainda está vago.

3. **Encontre a implícita.** O Orion vende para vendedores parceiros. Cada parceiro vê os próprios pedidos no painel. Qual característica arquitetural ninguém escreveu no documento de requisitos, e o que ela obriga estruturalmente?

    ??? note "Resposta comentada"

        Isolamento entre parceiros: nenhum parceiro pode ver dado de outro. Ninguém escreve isso porque parece óbvio — e é justamente por parecer óbvio que ninguém verifica.

        Estruturalmente, obriga a decidir onde mora a filtragem por parceiro. Se ela estiver espalhada em cada consulta, basta um `WHERE` esquecido em uma consulta nova para vazar. Se estiver concentrada em uma fronteira única por onde todo acesso passa, o esquecimento fica impossível.

        Note que a característica implícita determinou uma decisão de componente. É sempre assim que elas cobram.

4. **Julgue.** A Orion vai abrir operação em outro país, com regras fiscais próprias e prazo de seis meses. Escolha no máximo três características prioritárias para este recorte e justifique. Diga o que ficou de fora e qual o risco.

    Não há resposta única. Uma boa resposta nomeia o critério de corte, torna as três mensuráveis, aponta ao menos um conflito entre elas e diz qual vence. Uma resposta que lista sete características sem conflito não priorizou nada.

## Atividade em grupo

Sobre o recorte do seu Orion Evolution Lab:

1. Levantem todas as características candidatas, sem filtrar. Esperem passar de dez.
2. Cortem para **no máximo cinco**, e escrevam o critério de corte usado.
3. Tornem as cinco mensuráveis. Uma que não vira número ou teste sai da lista.
4. Ordenem por prioridade.
5. Identifiquem **pelo menos um par que se contradiz** e digam qual vence, com a consequência aceita.
6. Registrem o que ficou de fora e o risco de cada omissão.

O item 5 é obrigatório. Se o grupo não encontrar conflito, ou a lista está genérica demais, ou as características não foram tornadas mensuráveis o suficiente para colidir.

Esta lista é a base de todas as entregas seguintes. A partir daqui, toda decisão do grupo deve dizer contra qual característica ela está sendo avaliada.

Formato e critérios em [Orion Evolution Lab](../orion/index.md).

## Resumo

Características arquiteturais são as propriedades que o sistema precisa ter enquanto faz o que faz. Sem elas priorizadas e por escrito, não existe critério para avaliar decisão nenhuma — e toda discussão técnica termina em quem argumenta melhor.

Três coisas tornam uma lista útil: ser **curta** (o conflito precisa ser resolvido em algum lugar, e é na ordem), ser **mensurável** (o que não é verificável não é critério) e ser **conflitante** (uma lista sem tensão não foi priorizada).

Agora temos contra o que decidir. Falta o **onde**: as decisões arquiteturais precisam se materializar em fronteiras concretas dentro do sistema, e até aqui o Orion ainda é uma caixa só. É o que a próxima aula ataca.

## Principais conceitos

- característica arquitetural versus requisito funcional;
- características operacionais, estruturais e transversais;
- características implícitas e explícitas;
- a regra de "menos é mais";
- definição operacional e verificabilidade;
- conflito entre características como consequência da Primeira Lei.

## Leitura complementar

- Richards, Mark; Ford, Neal. *Fundamentals of Software Architecture*. Cap. 4 — Architecture Characteristics Defined; Cap. 5 — Identifying Architectural Characteristics; Cap. 6 — Measuring and Governing Architecture Characteristics.
- Bass, Len; Clements, Paul; Kazman, Rick. *Software Architecture in Practice*. Cap. 3 — Understanding Quality Attributes.

## Referências

- RICHARDS, Mark; FORD, Neal. *Fundamentals of Software Architecture: An Engineering Approach*. O'Reilly, 2020.
- BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. *Software Architecture in Practice*. 4. ed. Addison-Wesley, 2021.
