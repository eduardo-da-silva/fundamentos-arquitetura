# Marketplace Orion — fonte da verdade

> Nenhuma aula inventa componente, dependência ou número. Tudo vem daqui. Se uma aula precisar de algo que não está neste documento, o documento é estendido primeiro.
>
> Este documento é de orientação: **o leitor do livro não o vê, e nenhuma aula o cita.** Cada valor, ao entrar em uma aula, é apresentado e explicado no texto (ver `02-lesson-structure.md`).

Esta regra existe por um motivo concreto: a aula de métricas do Módulo 1 apresenta três valores diferentes de Fan-in para o mesmo componente, dentro do mesmo capítulo. O aluno que tentar refazer as contas não fecha com nada. Um documento único de números elimina essa classe inteira de erro.

---

## A empresa

A Orion começou como loja online de nicho vendendo eletrônicos de catálogo próprio. Em dois anos abriu a plataforma para vendedores parceiros e passou a operar como marketplace.

**Situação atual:**

- picos de até 8x o volume normal de pedidos em campanhas;
- múltiplos parceiros de pagamento e de logística, com contratos e prazos distintos;
- operação em regiões com regras comerciais e fiscais diferentes;
- equipe de plataforma de porte médio, sem espaço para reescrita completa.

**Sintomas recorrentes** (matéria-prima das aulas):

- incidentes intermitentes no checkout em horário de pico;
- alto custo para substituir uma integração crítica;
- tempo crescente entre pedir uma mudança de negócio e entregá-la;
- regressões em funcionalidades sem relação aparente com o que foi alterado;
- discussões técnicas que terminam em preferência pessoal por falta de evidência.

---

## Componentes canônicos

Dez componentes. Os nomes são fixos — ver "Linguagem ubíqua" abaixo.

| Componente | Responsabilidade | Não é responsável por |
|---|---|---|
| `Portal` | camada de entrada web e mobile; compõe telas | regra de negócio de qualquer tipo |
| `Checkout` | orquestrar o fechamento de compra | calcular preço, cobrar, despachar |
| `Catalogo` | produtos, categorias, preço de tabela, disponibilidade | desconto, reserva de estoque |
| `Clientes` | cadastro, identificação, endereços | autenticação de parceiro, crédito |
| `Promocoes` | cupons, campanhas, regras de desconto | aplicar desconto no pedido já emitido |
| `Pagamentos` | cobrança, estorno, conciliação com provedores | decidir se a compra pode ser fechada |
| `Pedidos` | pedido emitido, itens, ciclo de vida, histórico | cobrar, despachar, notificar diretamente |
| `Logistica` | frete, despacho, rastreio, parceiros logísticos | prazo prometido na vitrine |
| `Notificacoes` | e-mail, push, SMS transacional | decidir quando algo deve ser comunicado |
| `Integracoes` | camada genérica de adaptação a parceiros | ver nota abaixo |

!!! info "Sobre `Integracoes`"

    Componente construído há um ano para "padronizar toda integração com parceiro". Foi projetado de forma altamente abstrata, mas nenhum time adotou: `Pagamentos` e `Logistica` continuaram falando direto com seus provedores. Hoje ele depende de meio sistema e ninguém depende dele.

    É um caso real e deliberado no domínio. Serve para a aula de métricas mostrar a *Zone of Uselessness* com um exemplo que tem história, e não como categoria abstrata.

---

## Grafo de dependências oficial

`A --> B` significa: **A depende de B**.

```mermaid
flowchart LR
    Portal --> Catalogo
    Portal --> Checkout
    Portal --> Pedidos
    Portal --> Clientes
    Checkout --> Catalogo
    Checkout --> Clientes
    Checkout --> Promocoes
    Checkout --> Pagamentos
    Checkout --> Pedidos
    Promocoes --> Catalogo
    Pedidos --> Notificacoes
    Pedidos --> Logistica
    Pagamentos --> Notificacoes
    Logistica --> Notificacoes
    Integracoes --> Catalogo
    Integracoes --> Pedidos
    Integracoes --> Notificacoes
```

**17 arestas.** Este é o estado atual do sistema, e é o único grafo do qual as aulas derivam.

Uma aula pode usar um **recorte** (subconjunto de componentes), e deve dizer que é recorte. Não pode usar um grafo diferente.

---

## Números oficiais

Convenções de contagem em `06-code-style.md`. Definições:

- $C_a$ (fan-in) — quantos componentes dependem deste;
- $C_e$ (fan-out) — de quantos componentes este depende;
- $N_a$ — elementos abstratos do componente;
- $N_c$ — total de elementos do componente.

| Componente | $C_a$ | $C_e$ | $I$ | $N_a$ | $N_c$ | $A$ | $D$ |
|---|---|---|---|---|---|---|---|
| `Portal` | 0 | 4 | 1,00 | 0 | 6 | 0,00 | **0,00** |
| `Checkout` | 1 | 5 | 0,83 | 2 | 10 | 0,20 | **0,03** |
| `Logistica` | 1 | 1 | 0,50 | 2 | 5 | 0,40 | **0,10** |
| `Pagamentos` | 1 | 1 | 0,50 | 2 | 6 | 0,33 | **0,17** |
| `Promocoes` | 1 | 1 | 0,50 | 1 | 7 | 0,14 | **0,36** |
| `Pedidos` | 3 | 2 | 0,40 | 1 | 9 | 0,11 | **0,49** |
| `Notificacoes` | 4 | 0 | 0,00 | 2 | 4 | 0,50 | **0,50** |
| `Integracoes` | 0 | 3 | 1,00 | 5 | 6 | 0,83 | **0,83** |
| `Catalogo` | 4 | 0 | 0,00 | 1 | 10 | 0,10 | **0,90** |
| `Clientes` | 2 | 0 | 0,00 | 0 | 5 | 0,00 | **1,00** |

Verificação: a soma dos $C_a$ é 17 e a soma dos $C_e$ é 17, iguais ao número de arestas do grafo. Qualquer alteração no grafo exige refazer esta conta.

Valores arredondados para duas casas. As frações exatas menos óbvias: `Checkout` $I = 5/6$; `Promocoes` $A = 1/7$; `Pedidos` $A = 1/9$; `Integracoes` $A = 5/6$.

### Inventário de elementos por componente

O par $N_a / N_c$ de cada linha vem da convenção de contagem de `06-code-style.md` aplicada a um inventário de classes. Os dois inventários abaixo são a referência para a aula de métricas — os demais componentes seguem a mesma convenção e serão detalhados aqui quando uma aula precisar deles.

**`Checkout` — $N_a = 2$, $N_c = 10$**

| Elemento | Tipo | Abstrato? |
|---|---|---|
| `ServicoCheckout` | classe com comportamento | não |
| `SessaoCheckout` | classe com comportamento | não |
| `EstadoCheckout` | `Enum` | não |
| `ResumoValores` | `@dataclass` | não |
| `SnapshotEndereco` | `@dataclass` | não |
| `ChaveIdempotencia` | `@dataclass` | não |
| `ValidadorCarrinho` | classe com comportamento | não |
| `MontadorPedido` | classe com comportamento | não |
| `PoliticaDeCheckout` | `Protocol` | sim |
| `SelecaoDeGateway` | `Protocol` | sim |

Fora da conta: `calcular_frete_estimado` e `formatar_recibo` (funções de módulo) e as constantes de timeout. A convenção conta classes.

No Mini-Orion existe só o recorte do componente (`ServicoCheckout` e os contratos que ele consome); o restante é o modelo do componente completo.

**`Portal` — $N_a = 0$, $N_c = 6$**

Seis classes de composição de tela — `PaginaProduto`, `PaginaCheckout`, `PaginaPedidos`, `PaginaCliente`, `ResumoCarrinho`, `SessaoNavegacao` — todas concretas. Nenhum `Protocol`, nenhum `ABC`. Componente de borda não define contrato próprio.

### Leituras que estes números permitem

Estes casos são deliberados. Cada um sustenta um argumento de aula:

- **`Clientes` com $D = 1,00$** — o pior caso possível. Totalmente concreto, e duas coisas dependem dele. Qualquer mudança propaga, e não há ponto de extensão. *Zone of Pain* no extremo.
- **`Catalogo` com $D = 0,90$** — quatro dependentes, quase nenhuma abstração. Mesmo diagnóstico, com mais gente afetada.
- **`Integracoes` com $D = 0,83$** — abstração alta e ninguém consumindo. *Zone of Uselessness*. Junto com `Catalogo`, permite a demonstração central: **$D$ alto não diz qual dos dois problemas é.** Os dois estão longe da sequência principal por motivos opostos, e $D$, sozinho, não distingue. Só o plano $A \times I$ distingue.
- **`Checkout` com $D = 0,03$** — praticamente em cima da sequência principal, e é o componente que mais causa incidente. Este é o contraexemplo mais valioso do curso: a métrica está ótima e o problema é real. Fan-out 5 e posição no caminho crítico não aparecem em $D$. **Métrica é sintoma, não veredito.**
- **`Portal` com $D = 0,00$** — instabilidade máxima e zero abstração, e está correto assim. Componente de borda deve ser volátil. Serve para desfazer a ideia de que instabilidade alta é defeito.

---

## Agrupamento em módulos de domínio

Os dez componentes canônicos se agrupam em **oito módulos de domínio**. Este agrupamento é **decisão da disciplina**, da mesma natureza que a convenção de contagem de Abstractness em `06-code-style.md`: não é a única leitura possível do domínio, é a leitura fixada para que o exercício de reorganização do grafo, no Módulo 2, tenha resposta verificável. Um agrupamento diferente — separar `Pedidos` de `Checkout`, juntar `Financeiro` e `Distribuição` sob um módulo de pós-venda — seria defensável e não estaria errado. O que não se admite é uma aula derivar números de um agrupamento que não seja este.

| Módulo de domínio | Componentes | Arestas internas |
|---|---|---|
| Borda | `Portal` | — |
| Vitrine | `Catalogo`, `Promocoes` | `Promocoes → Catalogo` |
| Compra | `Checkout`, `Pedidos` | `Checkout → Pedidos` |
| Financeiro | `Pagamentos` | — |
| Distribuição | `Logistica` | — |
| Comunicação | `Notificacoes` | — |
| Identidade | `Clientes` | — |
| Integração | `Integracoes` | — |

### Arestas inter-módulo

Das 17 arestas do grafo oficial, apenas **2 ficam dentro de um módulo** — as duas listadas na coluna acima. As **15 restantes atravessam fronteira de módulo**:

```
de Portal:       → Catalogo    → Checkout    → Pedidos    → Clientes
de Checkout:     → Catalogo    → Clientes    → Promocoes  → Pagamentos
de Pedidos:      → Notificacoes    → Logistica
de Pagamentos:   → Notificacoes
de Logistica:    → Notificacoes
de Integracoes:  → Catalogo    → Pedidos    → Notificacoes
```

Verificação declarada: `2 internas + 15 inter-módulo = 17 arestas`, igual ao total do grafo oficial e à soma dos $C_a$. Qualquer alteração no grafo obriga a refazer esta separação.

### Leitura em camadas

O agrupamento induz uma direção de dependência em camadas: `Borda` (só `Portal`) depende dos módulos de domínio; os módulos de domínio dependem uns dos outros e dos tipos compartilhados do pacote `dominio`; nenhum módulo de domínio depende de `Borda`. `Portal` é o único ponto de entrada, e ninguém entra por ele.

!!! note "Por que 15 de 17 é o ponto de ensino"

    Quase toda dependência do sistema cruza uma fronteira de módulo. O grafo atual **mal é modular**: o agrupamento não cria esse problema, só o torna visível. `Checkout` sozinho aparece em 5 das 15 arestas inter-módulo — é o hub do grafo, o mesmo componente com $D = 0{,}03$ (métrica ótima) e o que mais causa incidente em produção. O contraexemplo do Módulo 1, relido aqui como problema de modularização.

!!! warning "A tabela de métricas não muda"

    A tabela $C_a$/$C_e$/$I$/$N_a$/$N_c$/$A$/$D$ continua sendo **por componente**, não por módulo. O agrupamento em módulos de domínio é uma camada de leitura adicional sobre o mesmo grafo de 17 arestas — não redefine fan-in, fan-out nem nenhum número já publicado acima.

---

## Extensão para o Módulo 3: o que a rede muda no grafo

O Módulo 3 não acrescenta componente nem aresta. Ele lê o mesmo grafo de 17 arestas com uma pergunta nova: qual dessas arestas passa a atravessar a rede se um módulo virar serviço.

### Candidato: `Pagamentos`

Foi o candidato registrado na Aula 14. Com $C_a = 1$ e $C_e = 1$, extraí-lo corta exatamente $C_a + C_e = 2$ arestas, que passam a ser chamadas remotas:

| Aresta | Sentido | Natureza |
|---|---|---|
| `Checkout → Pagamentos` | cobrança no caminho crítico do fechamento | síncrona |
| `Pagamentos → Notificacoes` | aviso de resultado da cobrança | pode sair do caminho crítico |

As outras 15 arestas continuam chamadas no mesmo processo. A conta é verificável: $17 - 2 = 15$.

No Mini-Orion a conta é menor. `pagamentos` e `notificacoes` não se conhecem (contrato `independence`), então só a aresta `compra → pagamentos.api` atravessa a rede. A diferença entre 2 e 1 é diferença entre o Orion e o seu recorte, e as aulas devem dizer qual dos dois estão medindo.

### Parâmetros da rede simulada

Estes valores são **decisão da disciplina**, da mesma natureza que a convenção de contagem de `06-code-style.md`: são hipóteses de enunciado, não medições do Orion real. Existem para que o exercício tenha resposta verificável. O Orion ainda não tem instrumentação para medir nada disso, e o material não deve fingir que tem.

| Parâmetro | Valor |
|---|---|
| Chamada entre módulos no mesmo processo | custo desprezível (ordem de microssegundos) |
| Latência de uma chamada remota, mediana | 20 ms |
| Latência de uma chamada remota, percentil 99 em campanha | 400 ms |
| Timeout por chamada remota | 1 s |
| Timeout total do fechamento de compra | 3 s (o mesmo da Aula 6) |
| Falha transitória por chamada remota em campanha | 2% |
| Falha transitória por chamada remota fora de campanha | 0,2% |
| Parcela das falhas transitórias em que o pedido chega e a resposta se perde | 50% (nas demais, o pedido se perde na ida) |
| Orçamento do fechamento de compra, percentil 95 | 2 s |
| Disponibilidade mensal alvo de cada módulo ou serviço | 99,9% |

Derivados, que as aulas podem usar sem recalcular de outro jeito:

- **Disponibilidade composta.** Dois serviços em série, cada um com 99,9%, entregam $0{,}999 \times 0{,}999 \approx 99{,}8\%$. No mês de 30 dias isso é cerca de 86 minutos de indisponibilidade, contra 43 minutos de um serviço só. Dentro do mesmo processo, `Checkout` e `Pagamentos` falham juntos e a conta não se multiplica.
- **Cobrança duplicada.** Com repetição depois de timeout e sem chave de idempotência, o cliente é cobrado duas vezes quando a resposta se perde: $2\% \times 50\% = 1\%$ dos fechamentos em campanha. A conta é aproximada: a repetição também pode falhar, e uma resposta mais lenta que o timeout de 1 s (cerca de 0,1% das chamadas, com a latência acima) executa o servidor e perde a resposta do mesmo jeito, então fora de campanha o piso não é zero.
- **Chamadas remotas por fechamento.** Uma, no Mini-Orion; duas, no grafo do Orion, se a notificação de `Pagamentos` ficar no caminho crítico.

!!! warning "O que este bloco não autoriza"

    Nenhuma aula do Módulo 3 inventa outro valor operacional. Precisando de um (tamanho de lote, custo de infraestrutura, número de times), estende-se esta seção primeiro, como em "Estendendo o domínio".

---

## Recorte legado (para a aula de acoplamento)

Antes da separação atual, `Checkout`, `Promocoes` e parte de `Pedidos` viviam em um único componente chamado `CoreService`, que tinha ciclo com `Promocoes`:

```mermaid
flowchart LR
    Portal --> CoreService
    CoreService --> Catalogo
    CoreService --> GatewayPagamentoX
    CoreService --> ServicoEmail
    CoreService --> MotorPromocoes
    MotorPromocoes --> CoreService
```

Este recorte é **histórico** e só pode ser usado para demonstrar o problema que a estrutura atual resolveu. Nunca misturar com os números oficiais acima — os componentes nem existem mais com esses nomes.

---

## Linguagem ubíqua

Nomes fixos. Sem sinônimos, em texto, código ou diagrama.

| Sempre | Nunca |
|---|---|
| `Checkout` | fechamento, finalização, carrinho |
| `Catalogo` | produtos, vitrine, estoque |
| `Clientes` | usuários, compradores, `Usuarios` |
| `Pedidos` | vendas, ordens, compras |
| `Pagamentos` | cobrança, financeiro, gateway |
| `Promocoes` | descontos, cupons, campanhas |
| `Logistica` | entrega, envio, frete |
| `Notificacoes` | comunicação, avisos, e-mails |
| Marketplace Orion | Orion Marketplace, a Orion S.A. |

O Módulo 1 usa `Usuarios` em um diagrama e `Clientes` em outro, para a mesma coisa. Corrigir ao revisar.

---

## As duas trilhas

Nunca se misturam. Cada uma tem escopo, artefato e destino próprios.

### Mini-Orion Checkout — trilha do professor

**O que é:** recorte pequeno e executável, resolvido em aula.

**Escopo fixo:** `Checkout`, `Pagamentos`, `Notificacoes` e o mínimo de `Catalogo` e `Pedidos` para o fluxo fechar.

**Onde vive:** no repositório do código, uma pasta por checkpoint (`NN-nome/`). Executável, com testes.

**Regra de evolução:** o código de uma aula parte do estado da aula anterior. Nomes de classe e de método são estáveis ao longo do curso — se `ServicoCheckout` mudar de nome, muda em todas as aulas seguintes, não só na atual.

**O que nunca contém:** persistência real, framework web, infraestrutura, concorrência de verdade. É evidência de decisão estrutural, não sistema de produção.

!!! info "Onde o código vive"

    O Mini-Orion existe, com seis estados (`01-acoplado` a `06-microkernel`) e mais os do Módulo 3. O código mora em um repositório à parte, `code-site/mini-orion`, ao lado deste, e não é versionado aqui. Nas aulas o caminho lógico continua `code/mini-orion/NN-nome/`.

### Orion Evolution Lab — trilha dos grupos

**O que é:** projeto dos alunos sobre um recorte amplo do Orion. **Nunca resolvido no material.**

**Escopo:** grafo completo, ou recorte escolhido pelo grupo e justificado.

**Artefatos, acumuláveis ao longo do curso:**

| Artefato | Formato | Aparece a partir de |
|---|---|---|
| Mapa de componentes e dependências | diagrama + tabela | primeiras aulas |
| Registro de diagnóstico | componente, problema, evidência, impacto | aulas de acoplamento |
| ADR | contexto, decisão, alternativas, consequências | aula de decisões |
| Tabela de métricas | $C_a$, $C_e$, $A$, $I$, $D$ + leitura | aula de métricas |
| Proposta de evolução | priorizada, com trade-off por item | oficina |

Cada grupo mantém seus artefatos em pasta própria; o material publica apenas o **formato** e os **critérios** (`09-assessment.md`), nunca o conteúdo preenchido.

**Regra dura:** se o material entregar a resposta do Evolution Lab, a trilha perde a função. Resolução comentada do professor só existe sobre o Mini-Orion.

---

## Estendendo o domínio

Quando uma aula precisar de algo que não existe aqui:

1. verificar se o conceito não pode ser demonstrado com o que já existe (quase sempre pode);
2. se não puder, estender **este documento** primeiro — componente, dependências, números;
3. recalcular a tabela de métricas inteira, já que $C_a$ e $C_e$ de outros componentes mudam;
4. só então escrever a aula.

Nunca o inverso. Componente que nasce dentro de uma aula é como o Módulo 1 acumulou três versões incompatíveis do mesmo checkout.
