# Roadmap das aulas

!!! info "Status"

    Detalhado para os Módulos 1 a 3, na composição de `07-curriculum.md`, já aplicada. O Módulo 4 tem apenas escopo definido.

## Como ler este documento

Cada aula declara cinco coisas. As três primeiras são o que a aula precisa entregar; as duas últimas são o que ela deixa para trás.

- **Sintoma** — o fato do Orion que abre a aula.
- **Conceitos** — o vocabulário introduzido.
- **Artefato** — o que passa a existir depois da aula, nas duas trilhas.
- **Avaliação** — como se verifica que funcionou.
- **Ponte** — a pergunta que a próxima aula abre.

A coluna **Artefato** é a mais importante: é o que torna verificável a promessa das duas trilhas. Ela existe porque a versão anterior do módulo anunciava as trilhas em todas as aulas sem produzir nada persistente em nenhuma.

---

## Módulo 1

### Aula 1 — O que é Arquitetura de Software?

- **Sintoma:** mudança na regra de frete quebrou a emissão de nota fiscal. As duas coisas não têm relação de negócio.
- **Conceitos:** decisão arquitetural; arquitetura versus design; as três marcas de uma decisão arquitetural (impacto estrutural, custo de reversão, efeito sobre características).
- **Artefato:**
    - *Mini-Orion:* `code/mini-orion/01-acoplado/` — `Checkout` com cobrança e notificação no mesmo fluxo, funcionando e testado. Ponto de partida de tudo.
    - *Evolution Lab:* cada grupo classifica dez decisões do próprio recorte em arquitetural ou de design, com justificativa.
- **Avaliação:** a classificação distingue as duas categorias por critério, não por intuição.
- **Ponte:** se toda decisão arquitetural é cara de reverter, como decidir sem paralisar?

### Aula 2 — Leis da Arquitetura, trade-offs e ADR

- **Sintoma:** a decisão de manter a notificação dentro do checkout foi tomada há dois anos, ninguém lembra por quê, e agora ninguém quer mexer.
- **Conceitos:** Primeira e Segunda Leis; trade-off; custo da mudança ao longo do tempo; ADR como formato.
- **Artefato:**
    - *Mini-Orion:* o primeiro ADR do curso, registrando a decisão original — inclusive a que vai envelhecer mal.
    - *Evolution Lab:* ADR de uma decisão já existente no recorte do grupo, escrita retroativamente.
- **Avaliação:** o ADR nomeia alternativa descartada e consequência negativa aceita. ADR sem consequência negativa está incompleto.
- **Ponte:** decidimos com base em quê? Sem características priorizadas, todo trade-off vira preferência.

### Aula 3 — Características arquiteturais

- **Sintoma:** o time discute há três sprints se o checkout deve priorizar disponibilidade ou consistência, e a discussão reinicia toda vez.
- **Conceitos:** características implícitas e explícitas; operacionais, estruturais e transversais; a regra de "menos é mais"; como tornar uma característica mensurável.
- **Artefato:**
    - *Mini-Orion:* lista priorizada de três características do checkout, cada uma com definição operacional mensurável.
    - *Evolution Lab:* mesma priorização sobre o recorte do grupo, com a justificativa amarrada ao contexto de negócio.
- **Avaliação:** cada característica tem um número ou um teste associado. "Escalabilidade" sem definição operacional não conta.
- **Ponte:** temos critério. Falta saber onde no sistema ele é atendido ou violado — e para isso precisamos enxergar as partes.

### Aula 4 — Modularidade e Componentes

- **Sintoma:** ninguém no time consegue desenhar o sistema de memória, e dois desenhos feitos por pessoas diferentes não batem.
- **Conceitos:** módulo versus componente; fronteira; contrato; encapsulamento em nível arquitetural; decomposição.
- **Artefato:**
    - *Mini-Orion:* passagem para `02-fronteiras/` — `Pagamentos` atrás de um `Protocol`. Primeira fronteira explícita do curso.
    - *Evolution Lab:* mapa de componentes e dependências do recorte, no formato de `05-domain.md`.
- **Avaliação:** o mapa declara o que ele **não** representa. Diagrama que omite sem avisar reprova.
- **Ponte:** agora vemos as partes e as setas. Mas nem toda seta custa o mesmo.

### Aula 5 — Acoplamento e Coesão

- **Sintoma:** `Checkout` depende de cinco componentes; qualquer um deles em manutenção derruba a compra.
- **Conceitos:** acoplamento aferente e eferente; coesão e seus tipos; a tensão entre os dois; dependência cíclica (recorte legado do `CoreService`).
- **Artefato:**
    - *Mini-Orion:* em `02-fronteiras/`, notificação fora do caminho crítico — com a janela de inconsistência nomeada, não escondida.
    - *Evolution Lab:* registro de diagnóstico com dois pontos de alto acoplamento e duas evidências de baixa coesão.
- **Avaliação:** cada item do diagnóstico cita evidência no código ou no grafo, não impressão.
- **Ponte:** "acoplado" descreve coisas muito diferentes. Depender do nome de um campo e depender da ordem de duas chamadas não são o mesmo problema. Falta precisão.

### Aula 6 — Connascência

- **Sintoma:** duas mudanças aparentemente iguais em tamanho — renomear um campo e inverter duas chamadas — tiveram custos de correção muito diferentes.
- **Conceitos:** as nove formas (CoN, CoT, CoM, CoP, CoA, CoE, CoTiming, CoV, CoI); os três eixos — **força, localidade e grau**; a heurística: connascência forte fica dentro do componente, fraca atravessa a fronteira.
- **Artefato:**
    - *Mini-Orion:* passagem para `03-governado/` — CoP eliminada com `PedidoCobranca`, CoM com `ResultadoCobranca`, e os testes que detectam a regressão.
    - *Evolution Lab:* mapa de connascências entre componentes do recorte, classificado por força e localidade.
- **Avaliação:** a classificação usa os três eixos juntos. Dizer que algo é CoP sem dizer se atravessa fronteira não é diagnóstico.
- **Ponte:** o diagnóstico é qualitativo e cada pessoa prioriza diferente. Como comparar?

!!! note "Ordem de força"

    A ordem canônica de Page-Jones — CoN < CoT < CoM < CoP < CoA < CoE < CoTiming < CoV < CoI — é o núcleo da ferramenta e precisa ser enunciada explicitamente. Os três eixos entram nesta aula, não depois: sem eles a classificação não vira decisão.

### Aula 7 — Métricas e governança automatizada

- **Sintoma:** duas propostas de refatoração concorrem pelo mesmo trimestre e a discussão empatou em opinião.
- **Conceitos:** $C_a$, $C_e$, $A$, $I$, $D$; o plano $A \times I$ e a sequência principal; *Zone of Pain* e *Zone of Uselessness*; limites da medição; teste de arquitetura como governança contínua.
- **Artefato:**
    - *Mini-Orion:* `pydeps` sobre o código real, e os três contratos de `03-governado/setup.cfg`, que falham quando `Checkout` volta a importar implementação.
    - *Evolution Lab:* tabela de métricas do recorte com leitura arquitetural de cada valor.
- **Avaliação:** a leitura explica pelo menos um caso em que a métrica **não** aponta o problema real.
- **Ponte:** temos vocabulário, diagnóstico e evidência. Falta juntar tudo sobre um sistema inteiro.

!!! danger "Dois pontos inegociáveis"

    **Todos os números vêm de `05-domain.md`.** Nenhum valor inventado por aula. A versão anterior trazia três valores contraditórios de Fan-in para `Catalogo` dentro do mesmo capítulo.

    **A visualização é o plano $A \times I$, não um ranking de $D$.** $D = |A + I - 1|$ é simétrico: `Catalogo` ($D = 0{,}90$, concreto e estável) e `Integracoes` ($D = 0{,}83$, abstrato e instável) têm $D$ parecido por motivos opostos, e um gráfico de barras os torna indistinguíveis — que é exatamente o que a aula precisa distinguir.

### Aula 8 — Oficina de Diagnóstico Arquitetural

- **Sintoma:** a diretoria pediu um plano de evolução com prazo e justificativa.
- **Conceitos:** nenhum novo. Integração de tudo.
- **Artefato:**
    - *Mini-Orion:* nada novo; serve de referência resolvida.
    - *Evolution Lab:* proposta de evolução priorizada, com trade-off por item e critério de sucesso observável.
- **Avaliação:** rubrica completa em `09-assessment.md`.
- **Ponte:** o Orion continua monolítico. Isso é problema? O Módulo 2 responde — e a resposta não é a esperada.

!!! note "Escopo e tempo"

    A oficina ocupa os **dois encontros** da semana 4. A versão anterior previa 90 a 110 minutos para um roteiro que soma cerca de 200 pela tabela de `09-assessment.md`.

    O mapa e as métricas não são reconstruídos na oficina: já existem das Aulas 4 e 7. O que se exercita é priorizar sob restrição de orçamento, que é a competência central do módulo.

---

## Módulo 2

### Aula 9 — O monólito não é o problema

- **Sintoma:** numa reunião de planejamento, a diretoria pede um "plano de migração para microsserviços" para o próximo ano. O pedido trata o monólito como dívida a quitar; ninguém no time sabe dizer o que a migração resolveria além de "monólito não escala".
- **Conceitos:** monólito como decisão de empacotamento e deploy, não como ausência de arquitetura; *big ball of mud* × monólito estruturado; o que a distribuição cobra todo dia (apenas nomeado aqui — latência, falha parcial, operação, observabilidade — e detalhado no Módulo 3); a pergunta certa não é "quando sair do monólito", é "o que na estrutura interna está travando a entrega".
- **Artefato:**
    - *Mini-Orion:* nenhum código novo. `code/mini-orion/03-governado/` é declarado o ponto de partida; os três contratos de `setup.cfg` são relidos como a fronteira interna que o Módulo 1 já deixou pronta.
    - *Evolution Lab:* ADR "Orion permanece um único *deployable* pelos próximos 12 meses", com alternativa real (começar a extrair já) e **gatilho observável de reversão** — que sinais fariam essa decisão envelhecer.
- **Avaliação:** o ADR nomeia um gatilho concreto e mensurável. "Quando crescer" não conta; "quando a fila de deploy de `Pagamentos` bloquear release de `Catalogo` mais de uma vez por sprint" conta.
- **Ponte:** que estrutura interna o Orion tem hoje? A resposta honesta: quase nenhuma imposta — só sugerida pela nomeação dos componentes.

### Aula 10 — Monólito em camadas: o que governa e o que não isola

- **Sintoma:** dois integrantes descrevem "a arquitetura do Orion" em desenhos que não batem — um põe camadas, o outro diz que não há nenhuma. O grafo oficial mostra `Portal → Catalogo` direto e `Checkout` com cinco dependências: nenhuma camada está imposta. Semanas depois, adicionar "cupom de frete grátis" toca `Portal`, `Checkout`, `Promocoes` e `Pedidos`.
- **Conceitos:** camadas técnicas (apresentação, aplicação, domínio, infraestrutura); camada fechada × aberta; a regra de dependência apontando para dentro; o ganho — direção de dependência governável e verificável; o primeiro custo — mudança de domínio atravessa todas as camadas; **coesão por camada é coesão fraca** (agrupa "todos os serviços" por serem serviços, não por servirem ao mesmo propósito); feature vertical × camada horizontal; por que $C_a$/$C_e$ medidos por camada não revelam esse custo; connascência que atravessa a camada.
- **Artefato:**
    - *Mini-Orion:* `code/mini-orion/04-camadas/`. O pacote plano de `03-governado/` passa a `mini_orion/apresentacao/`, `mini_orion/aplicacao/`, `mini_orion/dominio/`. Contrato `layers` do `import-linter` substitui parte dos `forbidden`. Todos os testes seguem verdes. Além disso, um registro curto de diagnóstico do próprio checkpoint: dois pontos onde a camada ajuda (direção de dependência; trocar provedor de pagamento), dois onde não ajuda (mudança de regra de negócio; testar uma regra isolada sem subir a aplicação).
    - *Evolution Lab:* releitura do mapa do grupo como camadas — quais componentes são de borda, de aplicação, de domínio, e o que não encaixa em camada nenhuma; e o traçado de duas mudanças de negócio plausíveis mostrando quantos componentes cada uma toca.
- **Avaliação:** o contrato `layers` falha de fato quando se força `dominio` a importar `apresentacao` — a evidência é o linter vermelho, não o argumento. Cada ponto do diagnóstico cita a aresta ou o trecho, não impressão.
- **Ponte:** as camadas governam a direção das dependências e mesmo assim a mudança de cupom tocou quatro componentes. E se cada assunto de negócio fosse uma caixa com uma porta só?

!!! note "Fusão"

    Esta aula funde as duas aulas de camadas previstas no escopo original. Camadas técnicas e o limite delas são um arco único e ganham densidade juntos.

### Aula 11 — Monólito modular: fronteira lógica sem fronteira física

- **Sintoma:** `Promocoes` de novo — a pergunta agora é o que mudaria se ninguém pudesse importar o interior de `Promocoes`, só a sua API.
- **Conceitos:** módulo de domínio; API pública × *internals*; encapsulamento no nível de pacote; **fronteira lógica** (imposta pelo linter ou pelo compilador) × **fronteira física** (imposta pela rede); a heurística de connascência do Módulo 1 aplicada — connascência forte fica dentro do módulo, só as fracas atravessam; módulo modular como preparação honesta para uma eventual extração (não se extrai o que não tem fronteira).
- **Artefato:**
    - *Mini-Orion:* `code/mini-orion/05-modular/`. Reagrupamento por domínio: `mini_orion/compra/`, `mini_orion/pagamentos/`, `mini_orion/notificacoes/`, cada módulo com `api.py` público e *internals* privados. Contratos `independence` entre módulos + `forbidden` contra *reach-in* nos *internals*.
    - *Evolution Lab:* para o recorte do grupo, propor os módulos de domínio e, para cada um, a API pública mínima que os demais consomem.
- **Avaliação:** cada módulo do Mini-Orion tem pelo menos um teste que roda sem instanciar nenhum outro módulo — o isolamento é a evidência. A classificação de connascência entre módulos usa os três eixos e mostra que só as formas fracas atravessam a fronteira.
- **Ponte:** no Mini-Orion são três módulos. No Orion inteiro são dez componentes e dezessete arestas. Quais arestas atravessam fronteira de módulo?

### Aula 12 — Reorganizar o grafo do Orion

- **Sintoma:** o grafo oficial de dezessete arestas. Sem um agrupamento, toda aresta parece igual; com módulos de domínio, algumas viram fronteira e outras viram detalhe interno.
- **Conceitos:** aplicar o agrupamento de domínios de `05-domain.md` ao grafo inteiro; aresta inter-módulo como o custo que se mede; ciclo entre módulos como bloqueio de extração; `Integracoes` relido — módulo que ninguém importa não é fronteira, é peso morto (a *Zone of Uselessness* da Aula 7 vira problema de modularização, com história em vez de categoria abstrata).
- **Artefato:**
    - *Mini-Orion:* nada novo; `05-modular/` serve de referência resolvida.
    - *Evolution Lab:* agrupamento do recorte do grupo em módulos, com a lista de arestas inter-módulo e a justificativa de cada fronteira; ADR de pelo menos uma fronteira escolhida.
- **Avaliação:** a contagem de arestas inter-módulo fecha com o grafo (internas + inter-módulo = total de arestas do recorte); nenhum ciclo entre módulos, ou o ciclo é nomeado explicitamente como pendência com o custo de removê-lo.
- **Ponte:** o Orion modular ainda roda como um processo só. Existem monólitos que têm forma além de camadas e módulos?

### Aula 13 — Pipeline e microkernel: monólitos com forma

- **Sintoma:** `fechar_pedido` do Mini-Orion é uma sequência fixa — validar, montar, cobrar, emitir, notificar. E `Promocoes` recebe um tipo novo de regra de desconto quase todo trimestre, sempre exigindo deploy do sistema inteiro.
- **Conceitos:** arquitetura em pipeline — filtros, fluxo unidirecional, quando o domínio *é* uma transformação; microkernel — núcleo estável mais plugins, quando a variação é conhecida e recorrente; os dois como formas de monólito, não como saídas dele; o trade-off do microkernel (deploy isolado da regra × contrato de plugin, teste de composição, risco de plugin mal-comportado).
- **Artefato:**
    - *Mini-Orion:* snippet ilustrativo do checkout como pipeline de filtros — nomes genéricos (`FiltroValidacao`, `EtapaX`), não os do Mini-Orion, conforme `06-code-style.md`. E `code/mini-orion/06-microkernel/`: `Promocoes` como registro de plugins de regra de desconto, com contrato núcleo↛plugin no `import-linter`, um plugin de exemplo e testes de composição.
    - *Evolution Lab:* ADR "regra de desconto como plugin" com o trade-off nomeado em dimensão concreta (prazo de deploy de uma regra, esforço de contrato, risco operacional).
- **Avaliação:** o ADR nomeia o custo do microkernel, não só o ganho; o uso de pipeline é justificado pelo formato do domínio (uma transformação em etapas), não por estética. O checkpoint `06-microkernel/` roda com `pytest` e `lint-imports` verdes.
- **Ponte:** pipeline e microkernel adiam a distribuição, não a substituem. Quando ela deixa de ser adiável?

### Aula 14 — Quando o monólito deixa de servir

- **Sintoma:** a conciliação de `Pagamentos` em campanha precisa reprocessar em lote num ritmo próprio, com janela de manutenção própria, e hoje sobe e desce junto com o checkout. É o primeiro caso no Orion em que uma parte tem requisito operacional genuinamente diferente do resto.
- **Conceitos:** os sinais legítimos para extrair um módulo — escala independente, cadência de release própria, isolamento de falha, autonomia de time; os ilegítimos — moda, estética, "monólito é feio"; o monólito modular como pré-condição: não se extrai o que não tem fronteira; o que se perde ao extrair — transação local, deploy único, teste sem rede.
- **Artefato:**
    - *Mini-Orion:* nenhum código novo; a aula aponta qual módulo de `05-modular/` seria o candidato a extração e por quê, usando os contratos existentes como evidência de que a fronteira já está pronta.
    - *Evolution Lab:* ADR "candidato a extração" — qual módulo, sob que gatilho mensurável, e o que ainda **não** justifica extrair; condição de falseamento obrigatória.
- **Avaliação:** o ADR distingue sinal legítimo de ilegítimo com um critério explícito, e nomeia o que a extração custa. ADR que só lista benefícios está incompleto (`09-assessment.md`).
- **Ponte:** se a decisão for extrair, tudo o que a rede cobra entra na conta — e é isso que o Módulo 3 mede antes de recomendar qualquer coisa.

### Aula 15 — Oficina: o Orion modular sob restrição

- **Sintoma:** a diretoria aprovou "modularizar antes de distribuir" e quer um plano com marcos, ordem e critério de parada.
- **Conceitos:** nenhum novo. Integração de camadas, módulos de domínio, arestas inter-módulo, contratos de linter e ADR.
- **Artefato:**
    - *Mini-Orion:* a cadeia `03-governado → 04-camadas → 05-modular → 06-microkernel` como referência resolvida, não reconstruída.
    - *Evolution Lab:* proposta de modularização priorizada — agrupamento-alvo, ordem de introdução das fronteiras, contratos de `import-linter` que entram na CI, métrica de acompanhamento, e o **critério explícito de "até aqui, e não distribuímos"**.
- **Avaliação:** rubrica de `09-assessment.md`, com o peso de Priorização lido como "ordem das fronteiras sob orçamento". Proposta sem critério de parada nomeado tem teto de nota. Números que não fecham entre si zeram o Diagnóstico.
- **Ponte:** o Orion está modular e continua um processo só. O Módulo 3 pergunta o que muda quando uma dessas fronteiras vira uma chamada de rede — e por que a resposta raramente compensa.

!!! note "Escopo e tempo"

    Ocupa os **dois encontros** da semana 8, espelhando a Aula 8 do Módulo 1. O mapa e as métricas não são reconstruídos na oficina: já existem das Aulas 10–12. O que se exercita é priorizar a introdução de fronteiras sob orçamento e definir critério de parada.

---

## Módulo 3

Todas as aulas do módulo fecham a seção de decisão com uma subseção **"Na prática: Python"**: o recorte real do checkpoint e o teste que serve de evidência. Os checkpoints são `07-remoto/` (Aulas 16–19), `08-dados/` (20) e `09-saga/` (21–23), cada um partindo do anterior, e todos partem de `06-microkernel/`. A rede é simulada (`06-code-style.md`) e os parâmetros vêm de `05-domain.md`.

### Aula 16 — Falácias da computação distribuída

- **Sintoma:** em ensaio de campanha, `compra` chama `pagamentos` pela rede. Nos testes tudo passa. O percentil 95 do fechamento (cerca de 0,2 s) continua dentro do orçamento de 2 s, e é isso que engana. O que a rede cria é cauda (2% das chamadas expiram em 1 s em campanha) e um erro que não existia: a repetição depois de um timeout cobra o cliente duas vezes em cerca de 1% dos fechamentos.
- **Conceitos:** as falácias, organizadas pelas que o Orion encontra primeiro (a rede é confiável, a latência é zero, o custo de transporte é zero); latência, falha parcial e estado ambíguo; timeout, repetição e idempotência (`ChaveIdempotencia` do domínio); a chamada remota que se disfarça de local.
- **Artefato:**
    - *Mini-Orion:* `07-remoto/`. Módulo `rede/` com o transporte simulado. `pagamentos` passa a ser alcançado por um `ClientePagamentos` que satisfaz o mesmo `Gateway`. Um teste reproduz a cobrança duplicada com repetição ingênua, e outro passa com chave de idempotência.
    - *Evolution Lab:* tabela das arestas do recorte que atravessam a rede se o módulo candidato for extraído (contagem $C_a + C_e$), com a falácia que cada aresta expõe.
- **Avaliação:** o teste da cobrança duplicada falha antes da chave e passa depois — a evidência é o teste, não o argumento. A tabela do grupo fecha com o grafo.
- **Ponte:** sabemos o que uma chamada remota custa. Quantos serviços o Orion precisa para pagar esse custo só onde ele compensa?

### Aula 17 — Do *service-based* aos microsserviços

- **Sintoma:** a diretoria ouviu duas propostas: "um microsserviço por componente" e "só tirar `Pagamentos`". Nenhuma das duas vem com número, e as duas se chamam "arquitetura de serviços".
- **Conceitos:** espectro de granularidade; *service-based* (poucos serviços de domínio, grossos, dado possivelmente compartilhado) contra microsserviços (finos, dado próprio, deploy independente); *architectural quantum*; o que cada estilo otimiza e o que cobra; quando "manter o monólito modular" continua sendo a resposta.
- **Artefato:**
    - *Mini-Orion:* `07-remoto/` ganha uma ferramenta pequena que, dado o conjunto de arestas remotas, lista os componentes que ainda precisam ser implantados juntos — o *quantum* calculado do grafo, não desenhado.
    - *Evolution Lab:* ADR "forma do *deployable*" com no mínimo três alternativas (manter, *service-based*, microsserviços) e gatilho de reversão.
- **Avaliação:** o ADR compara pelo menos dois estilos em duas características priorizadas na Aula 3 do recorte. "Microsserviços escalam melhor" sem a característica nomeada não conta.
- **Ponte:** *service-based* ou microsserviços é pergunta de tamanho. Que critério diz onde cortar?

### Aula 18 — Granularidade: o que desintegra e o que integra

- **Sintoma:** um time quer separar `Catalogo` porque ele tem quatro dependentes. Outro quer separar `Promocoes` porque ele muda todo trimestre. Os dois argumentos são de naturezas diferentes, e a reunião os trata como um só.
- **Conceitos:** forças que desintegram (escopo da função, volatilidade, escala, tolerância a falha, segurança, extensibilidade) e forças que integram (transação, fluxo entre serviços, dado compartilhado); $C_a$, $C_e$ e connascência como evidência de cada força; o que a métrica não vê.
- **Artefato:**
    - *Mini-Orion:* `07-remoto/setup.cfg` ganha um contrato que impede `compra` de importar `pagamentos` por qualquer caminho que não seja o cliente remoto. A fronteira nova nasce verificada.
    - *Evolution Lab:* matriz módulo × força, com a ordenação dos candidatos e a evidência de cada célula.
- **Avaliação:** cada força citada aponta para aresta, métrica ou incidente. A matriz contém pelo menos uma força integradora que contraria o candidato preferido do grupo.
- **Ponte:** decidimos onde cortar. Do outro lado do corte o contrato muda de dono. Quem manda quando um campo muda?

### Aula 19 — Contratos entre serviços

- **Sintoma:** `pagamentos` publica uma versão que acrescenta um resultado novo de cobrança, `EM_ANALISE`. `compra`, que não conhece o valor, o trata como cobrança aprovada.
- **Conceitos:** contrato remoto como API pública; mudança aditiva e mudança que quebra; leitor tolerante e seus limites; teste de contrato guiado pelo consumidor; connascência de tipo e de significado atravessando a rede (força, localidade, grau); deploys coordenados.
- **Artefato:**
    - *Mini-Orion:* `07-remoto/` serializa o contrato (v1 e v2) e traz um teste de contrato do lado do consumidor, que falha quando o produtor quebra o acordo, e um leitor tolerante que trata o valor desconhecido como falha, não como aprovação.
    - *Evolution Lab:* contrato de uma aresta remota do recorte, com a regra de evolução (o que pode mudar sem aviso e o que exige versão).
- **Avaliação:** o teste de contrato falha de verdade quando o produtor remove ou renomeia um campo. A classificação de connascência usa os três eixos.
- **Ponte:** o contrato descreve o que atravessa a rede. E o que fica do outro lado, os dados? De quem é a tabela?

### Aula 20 — Dados: de quem é a tabela

- **Sintoma:** a conciliação de `Pagamentos` casa transações com `Pedidos` por um *join*. Depois da extração, o *join* deixa de existir, e o relatório de conciliação do mês fecha com diferença.
- **Conceitos:** banco compartilhado contra dado por serviço; dono do dado; composição de consulta na borda contra cópia local; duplicação intencional e seu custo; acoplamento por esquema; o que se perde (*join*, integridade referencial, transação).
- **Artefato:**
    - *Mini-Orion:* `08-dados/`. `pagamentos` com repositório próprio. A conciliação passa a usar a cópia local dos campos de que precisa, gravada no momento da cobrança, e roda sem importar `compra`.
    - *Evolution Lab:* tabela de dados do recorte: dono, quem lê, como lê depois do corte.
- **Avaliação:** o teste de conciliação roda sem `compra`, e um contrato do `import-linter` garante isso. A tabela do grupo nomeia pelo menos um *join* que deixa de existir e o que o substitui.
- **Ponte:** com o dado separado, cobrar e emitir já não cabem numa transação. O que existe entre os dois passos?

### Aula 21 — Transação distribuída e consistência

- **Sintoma:** a cobrança é aprovada e a emissão do pedido falha, ou o timeout acontece depois de a cobrança ter ocorrido. O cliente foi cobrado e não tem pedido.
- **Conceitos:** ACID local; *two-phase commit* (coordenador, bloqueio, por que raramente se usa entre serviços); consistência forte e eventual; janela de inconsistência, já nomeada no Módulo 1; estado ambíguo e reconciliação; CAP e PACELC só como vocabulário de trade-off.
- **Artefato:**
    - *Mini-Orion:* `09-saga/`. A simulação reproduz o "cobrou e não emitiu", e um teste mede a janela até a reconciliação corrigir.
    - *Evolution Lab:* para a operação mais crítica do recorte, escolha entre consistência forte e eventual, com a janela tolerada em segundos e a consequência de negócio.
- **Avaliação:** a janela de inconsistência aparece em tempo e em consequência de negócio. "Consistência eventual" sem janela não conta.
- **Ponte:** *two-phase commit* bloqueia, e a eventual deixa o estado errado por um tempo. Existe uma forma de desfazer o que já foi feito?

### Aula 22 — Saga orquestrada

- **Sintoma:** quando a emissão falha depois da cobrança, alguém do suporte estorna à mão, quando percebe.
- **Conceitos:** saga; transação compensável; compensação não é *rollback*; passo pivô e passo repetível; idempotência de cada passo; a compensação que também falha; orquestração como estado explícito (coreografia só nomeada, pertence ao Módulo 4).
- **Artefato:**
    - *Mini-Orion:* `09-saga/` com um orquestrador do fechamento (cobrar, emitir, notificar), a compensação (estornar) e uma matriz de testes que injeta falha em cada passo.
    - *Evolution Lab:* a saga da operação escolhida na Aula 21, em tabela: passo, compensação, o que o cliente enxerga no intervalo.
- **Avaliação:** a matriz de falhas cobre cada passo, e a compensação que pode falhar tem tratamento nomeado.
- **Ponte:** já sabemos cortar, chamar, versionar, separar o dado e compensar. Quanto custa operar tudo isso?

### Aula 23 — O custo real: operação, observabilidade e times

- **Sintoma:** depois da campanha, clientes reclamam de cobrança sem pedido e ninguém diz em que serviço o fechamento parou: os registros estão em dois lugares, sem identificador em comum.
- **Conceitos:** observabilidade (registro, métrica, rastro); identificador de correlação; disponibilidade composta (derivada em `05-domain.md`); custo de operar mais um artefato; Lei de Conway e autonomia de time; o balanço final de ganho e custo.
- **Artefato:**
    - *Mini-Orion:* `09-saga/` propaga um identificador de correlação de ponta a ponta e reconstrói o caminho de um fechamento que falhou.
    - *Evolution Lab:* planilha de custo e benefício da extração do candidato, com cada item da conta da Aula 14 em número de `05-domain.md` ou marcado "não medido".
- **Avaliação:** todo item da conta tem número ou a marca "não medido" com a forma de medir. O balanço não esconde custo.
- **Ponte:** temos a conta inteira. Falta decidir sob orçamento.

### Aula 24 — Oficina: o que extrair primeiro

- **Sintoma:** a diretoria aprovou "extrair com critério" e quer um plano: o que sai primeiro, o que fica, e quando parar.
- **Conceitos:** nenhum novo. Integração de falácias, granularidade, contrato, dado, consistência, saga e custo.
- **Artefato:**
    - *Mini-Orion:* a cadeia `06-microkernel → 07-remoto → 08-dados → 09-saga` como referência resolvida, não reconstruída.
    - *Evolution Lab:* proposta de extração priorizada, ADR da ordem, **critério de parada** e a alternativa "não extrair nada" defendida como opção real.
- **Avaliação:** rubrica de `09-assessment.md`. Proposta sem a alternativa "não extrair" defendida tem teto de nota; números que não fecham com `05-domain.md` zeram o Diagnóstico.
- **Ponte:** o Orion agora tem serviços que se chamam. E se, em vez de chamar, publicassem o que aconteceu? O Módulo 4 pergunta.

!!! note "Escopo e tempo"

    Ocupa os **dois encontros** da semana 13, espelhando as Aulas 8 e 15. Nada é reconstruído na oficina; exercita-se a ordem e o critério de parada sob orçamento.

---

## Módulo 4

Escopo em `07-curriculum.md`. Numeração a partir da aula 25. Detalhar aula a aula somente quando o módulo entrar em produção — roadmap escrito com antecedência demais envelhece antes de ser usado.

Quando detalhar, manter as cinco colunas. A coluna **Artefato** é o que impede as trilhas de virarem promessa retórica de novo.

Quando detalhar, manter as cinco colunas. A coluna **Artefato** é o que impede as trilhas de virarem promessa retórica de novo.
