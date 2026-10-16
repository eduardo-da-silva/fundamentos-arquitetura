# Exercícios de fixação — Aulas 16 e 17

!!! danger "Entrega individual"

    Trabalho **individual**. Entregar antes da Aula 18 e trazer pronto para apresentar em sala no início dela.

As Aulas 16 e 17 ficam presas ao Mini-Orion, a uma rede simulada e a hipóteses de trabalho. Os cinco exercícios a seguir cobrem o mesmo conteúdo pela via oposta: pedem uma busca fora do material, sobre sistemas reais, publicados por quem os construiu. Em todos, cite a fonte (autor, título, endereço) e diga o que na fonte é medição e o que é suposição, como a Aula 16 fez com os seus próprios números.

1. **Aplicação — Uma repetição que cobrou duas vezes.** Pesquise um relato real (post-mortem, artigo técnico ou documentação de um provedor) de uma operação **repetida depois de um *timeout*** que produziu um efeito duplicado: cobrança em dobro, pedido duplicado, mensagem enviada duas vezes.

    a. Em qual dos dois casos do diagrama da Aula 16 o relato se encaixa: o pedido se perdeu na ida, ou a resposta se perdeu na volta?
    b. O relato descreve alguma defesa (chave de idempotência, deduplicação no destino, conciliação posterior)? Onde ela foi colocada: em quem chama, em quem atende, ou depois, na conciliação?

    ??? note "Resposta comentada — o que a resposta precisa conter"

        A fonte citada, o caso classificado (perda na ida ou na volta) com o trecho que o sustenta, e a defesa nomeada com o lado em que ela foi posta. Um relato que só diz "houve duplicidade" sem dizer por que a repetição era possível não responde à pergunta.

2. **Julgamento — A chave de idempotência, na documentação de um provedor.** Pesquise a documentação pública de um provedor de pagamento (ou de outro serviço que cobre dinheiro ou crie recursos) que descreva **chaves de idempotência**. Leia o que ela diz sobre quem gera a chave, por quanto tempo o provedor a guarda e o que acontece quando a mesma chave chega com um conteúdo diferente.

    Compare com o ADR da Aula 16: `compra` gera a chave uma vez por fechamento e `pagamentos` guarda as chaves vistas, sem prazo de expiração no Mini-Orion. A documentação que você leu resolve algum ponto que o ADR deixou em aberto (expiração, conflito de conteúdo), ou cria uma obrigação nova para quem chama?

    Mais de uma resposta é aceitável. O que se avalia: se você identifica o ponto exato em que a documentação e o ADR diferem, e o custo que cada decisão deixa para o outro lado.

3. **Aplicação — A cauda, num relato publicado.** Pesquise um texto técnico que trate de **latência de cauda** (percentis altos, e não média) em sistemas com muitas chamadas em cadeia. Há um artigo clássico sobre o tema, que você pode usar se não achar outro; vale qualquer relato de equipe que mostre percentis reais.

    a. O texto mostra, com números, que a chance de uma requisição ver a cauda cresce com o número de chamadas que ela faz? Compare com a conta $1 - (1 - p)^n$ da Aula 16.
    b. Que medida o texto propõe para conter a cauda (limite de tempo, repetição com cuidado, chamadas redundantes)? Qual o custo que ele admite?

    ??? note "Resposta comentada — o que a resposta precisa conter"

        O resultado numérico do texto sobre a composição da cauda, comparado com a fórmula da aula (mesma forma, parâmetros diferentes), e a medida de contenção com o seu custo declarado. Uma resposta que só repete que "a média engana" não usa a fonte.

4. **Julgamento — Menos serviços do que antes.** Pesquise um relato de engenharia em que uma equipe **reduziu a granularidade** de uma arquitetura distribuída: juntou serviços, voltou parte de um sistema para um único processo, ou desistiu de separar um componente.

    Usando o vocabulário da Aula 17, diga o que o relato apresenta como motivo: o custo de rede (chamadas remotas, falha parcial), o custo de operação (artefatos a mais), ou a falta de independência real (serviços que só funcionavam juntos). Em qual dessas três categorias ele cai?

    Mais de uma resposta é aceitável. O que se avalia: se você separa o que o relato **mediu** do que ele **supõe**, e se identifica o que, na decisão de juntar, teria de ser verdade para ela ter sido a decisão certa em outro contexto. Resposta sem a fonte citada não conta.

5. **Aplicação — Os quanta de um diagrama de verdade.** Encontre um diagrama de arquitetura de microsserviços publicado por uma equipe (em um artigo, uma palestra transcrita ou uma documentação). Marque no diagrama quais chamadas são **síncronas** e quais passam por fila ou evento.

    Usando a definição operacional da Aula 17 (mesmo artefato ou chamada síncrona liga dois componentes no mesmo quantum), conte quantos quanta o diagrama tem e quantos artefatos.

    ??? note "Resposta comentada — o que a resposta precisa conter"

        O diagrama citado, as chamadas classificadas como síncronas ou assíncronas, a contagem de artefatos e de quanta, e uma frase sobre a diferença entre os dois números. O resultado esperado, na maioria dos casos, é mais artefatos do que quanta; um diagrama em que os dois números coincidem merece uma nota sobre por que as chamadas são todas assíncronas. Se o diagrama não deixar claro o que é síncrono, diga isso: é a omissão que a Aula 17 chama a atenção para checar.

## Apresentação em sala

No início da Aula 18, cada aluno apresenta em poucas frases um dos cinco exercícios: a fonte encontrada e a conclusão a que chegou. A apresentação individual é o que garante que a pesquisa foi feita por quem entrega, não copiada de um colega.
