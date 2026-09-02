# Spec — Módulo 2: Arquiteturas Monolíticas

> Documento de planejamento. Versionado, **não publicado** (fora de `docs/`, fora do `nav`).
> Data: 2026-09-01. Autor: Eduardo da Silva.
> Regras carregadas para produzir esta spec: `00`, `01`, `02`, `04`, `05`, `06`, `07`, `08`, `09`, `10`.

---

## 1. Enquadramento

O Módulo 1 diagnosticou o monólito do Orion. A Aula 8 fecha com *"o Orion continua
monolítico. Isso é problema? — a resposta não é a esperada."*

**Tese do Módulo 2:** o monólito não é o problema — a ausência de fronteira interna é.
O módulo transforma o *big ball of mud* num **monólito modular**, mede o ganho, e
**não distribui nada**.

**Competência central:** decidir a estrutura interna de um monólito e defender que
não distribuir é a escolha certa agora — com condição de falseamento.

**Posição na progressão obrigatória (`07-curriculum.md`):** vem depois de "Métrica e
governança automatizada" e antes de "Estilos distribuídos". É o primeiro módulo sobre
estilo arquitetural, e todo argumento se faz com o vocabulário do Módulo 1:
acoplamento, coesão, connascência (força/localidade/grau), $C_a$/$C_e$/$A$/$I$/$D$,
ADR, contrato de `import-linter` como fitness function.

**Numeração:** Aulas 9–15. Sete aulas, oito encontros (a Aula 15, oficina, ocupa os
dois encontros da semana 8). Ver seção 8 para a alteração de currículo que isso exige.

**Cobertura dos temas de `07-curriculum.md`:**

| Tema do currículo | Onde entra |
|---|---|
| Monólito em camadas | A10 |
| Monólito modular; fronteira lógica sem fronteira física | A11, A12 |
| Arquitetura em pipeline; microkernel | A13 |
| Quando o monólito é a escolha certa, e por que quase sempre é no começo | A9 |
| Monólito modular como preparação honesta para extração | A12, A14 |
| Aplicação no Orion: reorganizar o grafo sem distribuir, e medir o ganho | A12, A15 |

---

## 2. Extensão de `.ai/rules/05-domain.md` (bloqueia as aulas)

"Reorganizar o grafo" pressupõe um agrupamento-alvo que hoje não existe no documento
de domínio. Esta é a **primeira tarefa de execução** (seção 9, passo 1), porque
nenhuma aula pode derivar números de um agrupamento não ratificado.

### 2.1 Agrupamento canônico (a ratificar)

Oito módulos de domínio sobre os dez componentes canônicos:

| Módulo de domínio | Componentes | Arestas internas (do grafo oficial) |
|---|---|---|
| Borda | `Portal` | — |
| Vitrine | `Catalogo`, `Promocoes` | `Promocoes → Catalogo` |
| Compra | `Checkout`, `Pedidos` | `Checkout → Pedidos` |
| Financeiro | `Pagamentos` | — |
| Distribuição | `Logistica` | — |
| Comunicação | `Notificacoes` | — |
| Identidade | `Clientes` | — |
| Integração | `Integracoes` | — |

### 2.2 Contagem derivada de arestas inter-módulo

Das 17 arestas oficiais, **2 são internas** (listadas acima) e **15 atravessam
fronteira de módulo**:

```
Portal → Catalogo          Checkout → Pagamentos      Integracoes → Catalogo
Portal → Checkout          Pedidos → Notificacoes     Integracoes → Pedidos
Portal → Pedidos           Pedidos → Logistica        Integracoes → Notificacoes
Portal → Clientes          Pagamentos → Notificacoes
Checkout → Catalogo        Logistica → Notificacoes
Checkout → Clientes
Checkout → Promocoes
```

O número alto (15/17) é o ponto de ensino: o grafo atual **mal é modular**, e o
agrupamento torna isso visível. `Checkout` aparece em 5 arestas inter-módulo — é o
hub, o mesmo componente que mais causa incidente e que tem $D = 0{,}03$ (métrica
ótima, problema real — contraexemplo do Módulo 1, agora relido como problema de
modularização).

### 2.3 O que NÃO muda em `05-domain.md`

- A tabela $C_a$/$C_e$/$I$/$N_a$/$N_c$/$A$/$D$ — é por componente, não por módulo.
- O grafo de 17 arestas.
- Os nomes dos componentes e a linguagem ubíqua.
- O recorte legado `CoreService`.

### 2.4 O que se acrescenta a `05-domain.md`

- Seção "Agrupamento em módulos de domínio" com a tabela 2.1.
- A contagem derivada de 2.2 (com a verificação: internas + inter-módulo = 17).
- Uma leitura em camadas: `Borda` → módulos de domínio → tipos compartilhados
  (`dominio`), sem que nenhum módulo de domínio importe `Borda`.
- Nota de que o agrupamento é **decisão da disciplina**, como a convenção de
  contagem de Abstractness — existe para dar resposta verificável ao exercício de
  reorganização, e um agrupamento diferente seria defensável.

---

## 3. Roadmap das aulas (formato de `08-lesson-roadmap.md`)

As cinco colunas: **Sintoma** / **Conceitos** / **Artefato** (Mini-Orion + Evolution
Lab) / **Avaliação** / **Ponte**. Tamanho-alvo: 200–320 linhas de Markdown por aula
conceitual (`02-lesson-structure.md`); a oficina pode exceder com material de apoio.

Proporção-alvo por aula: ~50% texto argumentativo, ~25% diagrama/tabela/ADR, ~25%
código (`02-lesson-structure.md`).

### Aula 9 — O monólito não é o problema

- **Sintoma:** numa reunião de planejamento, a diretoria pede um "plano de migração
  para microsserviços" para o próximo ano. O pedido trata o monólito como dívida a
  quitar; ninguém no time sabe dizer o que a migração resolveria além de "monólito
  não escala".
- **Conceitos:** monólito como decisão de empacotamento e deploy, não como ausência
  de arquitetura; *big ball of mud* × monólito estruturado; o que a distribuição
  cobra todo dia (apenas nomeado aqui — latência, falha parcial, operação,
  observabilidade — e detalhado no Módulo 3); a pergunta certa não é "quando sair do
  monólito", é "o que na estrutura interna está travando a entrega".
- **Artefato:**
    - *Mini-Orion:* nenhum código novo. `code/mini-orion/03-governado/` é declarado o
      ponto de partida; os três contratos de `setup.cfg` são relidos como a fronteira
      interna que o Módulo 1 já deixou pronta.
    - *Evolution Lab:* ADR "Orion permanece um único *deployable* pelos próximos 12
      meses", com alternativa real (começar a extrair já) e **gatilho observável de
      reversão** — que sinais fariam essa decisão envelhecer.
- **Avaliação:** o ADR nomeia um gatilho concreto e mensurável. "Quando crescer" não
  conta; "quando a fila de deploy de `Pagamentos` bloquear release de `Catalogo` mais
  de uma vez por sprint" conta.
- **Ponte:** que estrutura interna o Orion tem hoje? A resposta honesta: quase
  nenhuma imposta — só sugerida pela nomeação dos componentes.

### Aula 10 — Monólito em camadas: o que governa e o que não isola

> Funde as duas aulas de camadas previstas no rascunho inicial. Camadas técnicas e o
> limite delas são um arco único e ganham densidade juntos.

- **Sintoma:** dois integrantes descrevem "a arquitetura do Orion" em desenhos que
  não batem — um põe camadas, o outro diz que não há nenhuma. O grafo oficial mostra
  `Portal → Catalogo` direto e `Checkout` com cinco dependências: nenhuma camada está
  imposta. Semanas depois, adicionar "cupom de frete grátis" toca `Portal`,
  `Checkout`, `Promocoes` e `Pedidos`.
- **Conceitos:** camadas técnicas (apresentação, aplicação, domínio, infraestrutura);
  camada fechada × aberta; a regra de dependência apontando para dentro; o ganho —
  direção de dependência governável e verificável; o primeiro custo — mudança de
  domínio atravessa todas as camadas; **coesão por camada é coesão fraca** (agrupa
  "todos os serviços" por serem serviços, não por servirem ao mesmo propósito);
  feature vertical × camada horizontal; por que $C_a$/$C_e$ medidos por camada não
  revelam esse custo; connascência que atravessa a camada.
- **Artefato:**
    - *Mini-Orion:* `code/mini-orion/04-camadas/`. O pacote plano de `03-governado/`
      passa a `mini_orion/apresentacao/`, `mini_orion/aplicacao/`,
      `mini_orion/dominio/`. Contrato `layers` do `import-linter` substitui parte dos
      `forbidden`. Todos os testes seguem verdes. Além disso, um registro curto de
      diagnóstico do próprio checkpoint: dois pontos onde a camada ajuda (direção de
      dependência; trocar provedor de pagamento), dois onde não ajuda (mudança de
      regra de negócio; testar uma regra isolada sem subir a aplicação).
    - *Evolution Lab:* releitura do mapa do grupo como camadas — quais componentes são
      de borda, de aplicação, de domínio, e o que não encaixa em camada nenhuma; e o
      traçado de duas mudanças de negócio plausíveis mostrando quantos componentes
      cada uma toca.
- **Avaliação:** o contrato `layers` falha de fato quando se força `dominio` a
  importar `apresentacao` — a evidência é o linter vermelho, não o argumento. Cada
  ponto do diagnóstico cita a aresta ou o trecho, não impressão.
- **Ponte:** as camadas governam a direção das dependências e mesmo assim a mudança de
  cupom tocou quatro componentes. E se cada assunto de negócio fosse uma caixa com
  uma porta só?

### Aula 11 — Monólito modular: fronteira lógica sem fronteira física

- **Sintoma:** `Promocoes` de novo — a pergunta agora é o que mudaria se ninguém
  pudesse importar o interior de `Promocoes`, só a sua API.
- **Conceitos:** módulo de domínio; API pública × *internals*; encapsulamento no
  nível de pacote; **fronteira lógica** (imposta pelo linter ou pelo compilador) ×
  **fronteira física** (imposta pela rede); a heurística de connascência do Módulo 1
  aplicada — connascência forte fica dentro do módulo, só as fracas atravessam;
  módulo modular como preparação honesta para uma eventual extração (não se extrai o
  que não tem fronteira).
- **Artefato:**
    - *Mini-Orion:* `code/mini-orion/05-modular/`. Reagrupamento por domínio:
      `mini_orion/compra/`, `mini_orion/pagamentos/`, `mini_orion/notificacoes/`,
      cada módulo com `api.py` público e *internals* privados. Contratos
      `independence` entre módulos + `forbidden` contra *reach-in* nos *internals*.
    - *Evolution Lab:* para o recorte do grupo, propor os módulos de domínio e, para
      cada um, a API pública mínima que os demais consomem.
- **Avaliação:** cada módulo do Mini-Orion tem pelo menos um teste que roda sem
  instanciar nenhum outro módulo — o isolamento é a evidência. A classificação de
  connascência entre módulos usa os três eixos e mostra que só as formas fracas
  atravessam a fronteira.
- **Ponte:** no Mini-Orion são três módulos. No Orion inteiro são dez componentes e
  dezessete arestas. Quais arestas atravessam fronteira de módulo?

### Aula 12 — Reorganizar o grafo do Orion

- **Sintoma:** o grafo oficial de dezessete arestas. Sem um agrupamento, toda aresta
  parece igual; com módulos de domínio, algumas viram fronteira e outras viram
  detalhe interno.
- **Conceitos:** aplicar o agrupamento de domínios (seção 2) ao grafo inteiro; aresta
  inter-módulo como o custo que se mede; ciclo entre módulos como bloqueio de
  extração; `Integracoes` relido — módulo que ninguém importa não é fronteira, é peso
  morto (a *Zone of Uselessness* da Aula 7 vira problema de modularização, com
  história em vez de categoria abstrata).
- **Artefato:**
    - *Mini-Orion:* nada novo; `05-modular/` serve de referência resolvida.
    - *Evolution Lab:* agrupamento do recorte do grupo em módulos, com a lista de
      arestas inter-módulo e a justificativa de cada fronteira; ADR de pelo menos uma
      fronteira escolhida.
- **Avaliação:** a contagem de arestas inter-módulo fecha com o grafo (internas +
  inter-módulo = total de arestas do recorte); nenhum ciclo entre módulos, ou o ciclo
  é nomeado explicitamente como pendência com o custo de removê-lo.
- **Ponte:** o Orion modular ainda roda como um processo só. Existem monólitos que têm
  forma além de camadas e módulos?

### Aula 13 — Pipeline e microkernel: monólitos com forma

- **Sintoma:** `fechar_pedido` do Mini-Orion é uma sequência fixa — validar, montar,
  cobrar, emitir, notificar. E `Promocoes` recebe um tipo novo de regra de desconto
  quase todo trimestre, sempre exigindo deploy do sistema inteiro.
- **Conceitos:** arquitetura em pipeline — filtros, fluxo unidirecional, quando o
  domínio *é* uma transformação; microkernel — núcleo estável mais plugins, quando a
  variação é conhecida e recorrente; os dois como formas de monólito, não como saídas
  dele; o trade-off do microkernel (deploy isolado da regra × contrato de plugin,
  teste de composição, risco de plugin mal-comportado).
- **Artefato:**
    - *Mini-Orion:* snippet ilustrativo do checkout como pipeline de filtros — nomes
      genéricos (`FiltroValidacao`, `EtapaX`), não os do Mini-Orion, conforme `06`.
      E `code/mini-orion/06-microkernel/`: `Promocoes` como registro de plugins de
      regra de desconto, com contrato núcleo↛plugin no `import-linter`, um plugin de
      exemplo e testes de composição.
    - *Evolution Lab:* ADR "regra de desconto como plugin" com o trade-off nomeado em
      dimensão concreta (prazo de deploy de uma regra, esforço de contrato, risco
      operacional).
- **Avaliação:** o ADR nomeia o custo do microkernel, não só o ganho; o uso de
  pipeline é justificado pelo formato do domínio (uma transformação em etapas), não
  por estética. O checkpoint `06-microkernel/` roda com `pytest` e `lint-imports`
  verdes.
- **Ponte:** pipeline e microkernel adiam a distribuição, não a substituem. Quando ela
  deixa de ser adiável?

### Aula 14 — Quando o monólito deixa de servir

- **Sintoma:** a conciliação de `Pagamentos` em campanha precisa reprocessar em lote
  num ritmo próprio, com janela de manutenção própria, e hoje sobe e desce junto com
  o checkout. É o primeiro caso no Orion em que uma parte tem requisito operacional
  genuinamente diferente do resto.
- **Conceitos:** os sinais legítimos para extrair um módulo — escala independente,
  cadência de release própria, isolamento de falha, autonomia de time; os ilegítimos
  — moda, estética, "monólito é feio"; o monólito modular como pré-condição: não se
  extrai o que não tem fronteira; o que se perde ao extrair — transação local, deploy
  único, teste sem rede.
- **Artefato:**
    - *Mini-Orion:* nenhum código novo; a aula aponta qual módulo de `05-modular/`
      seria o candidato a extração e por quê, usando os contratos existentes como
      evidência de que a fronteira já está pronta.
    - *Evolution Lab:* ADR "candidato a extração" — qual módulo, sob que gatilho
      mensurável, e o que ainda **não** justifica extrair; condição de falseamento
      obrigatória.
- **Avaliação:** o ADR distingue sinal legítimo de ilegítimo com um critério
  explícito, e nomeia o que a extração custa. ADR que só lista benefícios está
  incompleto (`09-assessment.md`).
- **Ponte:** se a decisão for extrair, tudo o que a rede cobra entra na conta — e é
  isso que o Módulo 3 mede antes de recomendar qualquer coisa.

### Aula 15 — Oficina: o Orion modular sob restrição

> Ocupa os **dois encontros** da semana 8, espelhando a Aula 8 do Módulo 1. O mapa e
> as métricas não são reconstruídos na oficina: já existem das Aulas 10–12. O que se
> exercita é priorizar a introdução de fronteiras sob orçamento e definir critério de
> parada.

- **Sintoma:** a diretoria aprovou "modularizar antes de distribuir" e quer um plano
  com marcos, ordem e critério de parada.
- **Conceitos:** nenhum novo. Integração de camadas, módulos de domínio, arestas
  inter-módulo, contratos de linter e ADR.
- **Artefato:**
    - *Mini-Orion:* a cadeia `03-governado → 04-camadas → 05-modular → 06-microkernel`
      como referência resolvida, não reconstruída.
    - *Evolution Lab:* proposta de modularização priorizada — agrupamento-alvo, ordem
      de introdução das fronteiras, contratos de `import-linter` que entram na CI,
      métrica de acompanhamento, e o **critério explícito de "até aqui, e não
      distribuímos"**.
- **Avaliação:** rubrica de `09-assessment.md`, com o peso de Priorização lido como
  "ordem das fronteiras sob orçamento". Proposta sem critério de parada nomeado tem
  teto de nota. Números que não fecham entre si zeram o Diagnóstico.
- **Ponte:** o Orion está modular e continua um processo só. O Módulo 3 pergunta o que
  muda quando uma dessas fronteiras vira uma chamada de rede — e por que a resposta
  raramente compensa.

---

## 4. Evolução do Mini-Orion

Continua de `code/mini-orion/03-governado/` (pacote plano; `contratos.py` separando
contratos de implementações; três contratos de `import-linter`; testes que verificam
decisões).

| Checkpoint | Estado | Introduzido em | Diagnóstico/uso em | Contratos `import-linter` |
|---|---|---|---|---|
| `04-camadas/` | pacote em camadas técnicas (`apresentacao`, `aplicacao`, `dominio`) | A10 | A10 | `layers` (apresentacao > aplicacao > dominio), fechadas |
| `05-modular/` | módulos de domínio (`compra`, `pagamentos`, `notificacoes`), cada um com API pública e *internals* privados | A11 | A12 | `independence` entre módulos + `forbidden` contra *reach-in* |
| `06-microkernel/` | `Promocoes` como registro de plugins de regra de desconto | A13 | A13 | núcleo↛plugin (`forbidden`) |

Regras (de `06-code-style.md` e `10-tooling.md`):

- Cada checkpoint: `pytest` verde **e** `lint-imports` verde **antes** de escrever a
  aula que o usa.
- Nomes de classe e método estáveis ao longo do curso (`ServicoCheckout`,
  `PedidoCobranca`, `ResultadoCobranca`, `RepositorioPedidos` etc. seguem).
- O que aparece na página é recorte do arquivo real, nunca reescrita para a página.
- Sem framework, sem ORM, sem I/O real, sem concorrência de verdade.
- `requirements-dev.txt` já contém `pytest`, `pydeps`, `import-linter`, `radon` —
  **nenhuma dependência nova**.
- `code/mini-orion/README.md` atualizado com os três novos estados.

**Fecha o backlog #4:** adicionar um job de CI que rode `pytest` e `lint-imports` nos
checkpoints (`01-acoplado` … `06-microkernel`). Esse job é separado do build do site
(`10-tooling.md`: o build do site instala apenas `zensical`).

---

## 5. Evolution Lab (`docs/orion/index.md`)

Estende os formatos existentes; continua **nunca resolvendo** o Lab.

- **Mapa de componentes:** ganha a camada de agrupamento em módulos de domínio.
- **Novo artefato — tabela de arestas inter-módulo:** origem, destino, "fronteira
  justificada por…". Aparece a partir da Aula 12.
- **ADR:** exemplos novos de ADR de fronteira de módulo e de "candidato a extração"
  (formato inalterado — Contexto / Decisão / Alternativas / Consequências / Reversão).
- **Proposta de evolução:** passa a exigir um **critério de parada** explícito ("até
  aqui, e não distribuímos") além das no máximo três ações priorizadas.

Rubrica e pesos permanecem os de `09-assessment.md`. A leitura do peso "Priorização"
na entrega do Módulo 2 é "ordem de introdução das fronteiras sob orçamento".

---

## 6. Mudanças de infraestrutura e de conteúdo publicado

### 6.1 `mkdocs.yml` — `nav`

Novo bloco após o do Módulo 1 e antes de "Orion Evolution Lab":

```yaml
  - Módulo 2 — Arquiteturas Monolíticas:
    - Visão geral do módulo: modulo2/index.md
    - Aula 9 — O monólito não é o problema: modulo2/aula09-monolito-nao-e-o-problema.md
    - Aula 10 — Monólito em camadas: modulo2/aula10-monolito-em-camadas.md
    - Aula 11 — Monólito modular: modulo2/aula11-monolito-modular.md
    - Aula 12 — Reorganizar o grafo do Orion: modulo2/aula12-reorganizar-o-grafo.md
    - Aula 13 — Pipeline e microkernel: modulo2/aula13-pipeline-e-microkernel.md
    - Aula 14 — Quando o monólito deixa de servir: modulo2/aula14-quando-o-monolito-deixa-de-servir.md
    - Aula 15 — Oficina: o Orion modular: modulo2/aula15-oficina-orion-modular.md
```

### 6.2 `docs/modulo2/`

- `index.md` — visão geral do módulo. **Não clonar** a prosa de `docs/modulo1/index.md`
  (regra anti-boilerplate de `04-author-voice.md`): sem repetir as molduras "As duas
  trilhas", "Como cada aula funciona" com o mesmo texto. O índice do Módulo 2 fala do
  que é próprio dele — a tese de que o monólito é uma decisão legítima e revisável.
- Sete arquivos de aula (`aula09-…` a `aula15-…`), 200–320 linhas cada; a oficina
  pode exceder com material de apoio para os grupos.
- Diagramas apenas dos tipos verificados em `10-tooling.md` (nada com sufixo `-beta`).
  Toda fórmula com leitura em linguagem natural; todo diagrama declarando o que omite.

### 6.3 CI do Mini-Orion

Job novo em `.github/workflows/` (ou etapa no `ci.yml` existente, isolada do build do
site): instala `code/mini-orion/requirements-dev.txt`, roda `pytest` e `lint-imports`
em cada checkpoint. Fecha o backlog #4.

### 6.4 Regras de `.ai/rules/` a atualizar

| Arquivo | Mudança |
|---|---|
| `05-domain.md` | acrescenta a seção "Agrupamento em módulos de domínio" (seção 2 desta spec) |
| `07-curriculum.md` | Módulo 2 passa a 7 aulas; detalha a composição; realoca 1 encontro (seção 8) |
| `08-lesson-roadmap.md` | preenche o Módulo 2 com as sete aulas no formato de cinco colunas (versão detalhada da seção 3) |
| `12-backlog.md` | fecha o item 4 (CI do Mini-Orion) e o item 6 parcialmente (Módulo 2 escrito); registra os checkpoints `04`–`06` |

---

## 7. Decisões registradas (respostas do professor, 2026-09-01)

| Decisão | Escolha | Consequência |
|---|---|---|
| Entregável deste plano | Spec completa de produção | roadmap 5 colunas + plano de execução + extensão de domínio + infra |
| Composição das aulas | Professor revisa proposta do assistente | seção 3 |
| Mini-Orion no Módulo 2 | Novos checkpoints de código | `04-camadas`, `05-modular`, `06-microkernel` (seção 4) |
| Extensão de `05-domain.md` | Sim, incluir no plano | seção 2; é o passo 1 da execução |
| Orçamento de encontros | Fundir as duas aulas de camadas | 7 aulas; oficina volta a ocupar 2 encontros |
| `06-microkernel/` | Checkpoint executável pequeno | mais um checkpoint para manter; microkernel com evidência executável |
| Agrupamento de domínios | Ratificar o corte de 8 módulos proposto | 15 arestas inter-módulo, 2 internas |
| Local da spec | `.ai/planos/` | este arquivo; versionado, não publicado |

---

## 8. Alteração de currículo exigida pela fusão

Reduzir o Módulo 2 para 7 aulas contradiz `07-curriculum.md` ("Módulo 2 … 8 aulas").

**Proposta:** editar `07-curriculum.md`:

- Tabela das 18 semanas: Módulo 2 passa de **8** para **7** aulas. Os demais módulos
  não mudam.
- As 7 aulas cabem exatas nos 8 encontros das semanas 5–8: seis aulas conceituais
  (9–14), uma por encontro, e a oficina (Aula 15) ocupando os dois encontros da
  semana 8. Foi justamente a fusão das duas aulas de camadas que abriu espaço para a
  oficina dupla caber sem estourar a contagem — com 8 aulas, não cabia (é a
  inconsistência que o Módulo 1 ainda carrega).
- Nada é transferido para outro módulo. O Módulo 3 segue com 10 aulas nas semanas
  9–13.
- Total das 18 semanas inalterado: 8 + 8 + 10 + 8 + 2 = 36 encontros (encontros de
  cada módulo = semanas × 2; as 7 aulas do Módulo 2 preenchem 8 encontros porque a
  oficina conta como dois).

Semana a semana:

| Semana | Aulas |
|---|---|
| 5 | 9 — O monólito não é o problema · 10 — Monólito em camadas |
| 6 | 11 — Monólito modular · 12 — Reorganizar o grafo do Orion |
| 7 | 13 — Pipeline e microkernel · 14 — Quando o monólito deixa de servir |
| 8 | 15 — Oficina: o Orion modular (dois encontros) |

---

## 9. Sequência de execução (entrada para o plano de implementação)

1. **Ratificar `05-domain.md`** — acrescentar o agrupamento em módulos de domínio e a
   contagem de arestas inter-módulo (seção 2). Verificar internas + inter-módulo = 17.
   *Bloqueia todo o resto.*
2. **Editar `07-curriculum.md`** — Módulo 2 = 7 aulas; realocar 1 encontro ao Módulo 3
   (seção 8).
3. **Preencher `08-lesson-roadmap.md`** — as sete aulas no formato de cinco colunas
   (versão detalhada da seção 3).
4. **Evoluir o Mini-Orion**, em ordem, cada checkpoint com `pytest` + `lint-imports`
   verdes antes da aula correspondente:
   1. `04-camadas/`
   2. `05-modular/`
   3. `06-microkernel/`
   4. atualizar `code/mini-orion/README.md`.
5. **Escrever as aulas 9 → 15**, em ordem. Cada aula parte do estado da anterior; a
   ponte de cada uma é verificada contra a abertura da seguinte. Carregar
   `00`, `01`, `02`, `04`, `05`, `08` por aula; `06` nas que mexem em código.
   Ao terminar cada aula, abrir a anterior lado a lado e conferir que os títulos de
   `##`/`###` não coincidem em mais da metade (`04-author-voice.md`).
6. **Atualizar `docs/modulo2/index.md`, `docs/orion/index.md`, `mkdocs.yml` (`nav`).**
7. **Adicionar o job de CI do Mini-Orion** (`pytest` + `lint-imports` nos checkpoints).
8. **Revisão do módulo inteiro:**
   - `.ai/rules/11-review-checklist.md` aula a aula;
   - `zensical serve` e abrir cada página nova nos temas claro e escuro;
   - check de órfãos de `10-tooling.md` (nenhum `.md` em `docs/` fora do `nav`);
   - atualizar `12-backlog.md` (fecha #4; #6 parcial).

---

## 10. Riscos e pontos de atenção

- **Agrupamento com 15/17 arestas inter-módulo** pode parecer "modularização que não
  modularizou". É deliberado e é o ponto de ensino da Aula 12 — mas o texto precisa
  dizer isso explicitamente, senão lê como falha do exercício.
- **Quatro checkpoints novos de código** (`04`–`06` mais o snippet de pipeline)
  aumentam a superfície de manutenção do Mini-Orion. Cada um precisa de teste que
  falha quando a decisão é desfeita, não só teste de comportamento.
- **`06-microkernel/`** é o checkpoint de maior risco de virar exercício de
  programação em vez de evidência arquitetural (`00-course.md`: código é evidência,
  nunca exercício). Manter mínimo: um registro, um contrato, um plugin, um teste de
  composição.
- **Build não verificado** (backlog #1) ainda vale: `mindmap`/`timeline` e MathJax das
  aulas novas precisam ser vistos renderizados, não só revisados em Markdown.
- **Voz do autor:** o Módulo 2 introduz o primeiro "estilo arquitetural" do curso. O
  risco é escorregar para catálogo ("o monólito em camadas tem estas vantagens"). Cada
  estilo entra por um sintoma do Orion e sai com um trade-off nomeado
  (`01-pedagogy.md`, `04-author-voice.md`).
