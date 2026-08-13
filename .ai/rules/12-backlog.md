# Backlog do material

> Estado real do material, em oposição a todos os outros documentos desta pasta, que descrevem como ele **deve** ser. Item resolvido sai daqui.

Última revisão: agosto de 2026, após as três ondas de correção do Módulo 1 e a padronização dos exercícios.

---

## Aberto

### 1. Build e renderização não verificados

**Onde:** todo o Módulo 1.

**Problema:** as correções não foram validadas em um build real. `zensical` não está instalado no ambiente onde o material foi editado. Ficam sem verificação:

- o SVG do plano $A \times I$ em `aula07-metricas-governanca.md` — foi conferido por script contra os dados de `05-domain.md`, mas não visualmente;
- o comportamento do SVG nos temas claro e escuro (usa `currentColor`, mas isso não foi visto);
- `mindmap`, `timeline` e `quadrantChart` no Mermaid 11 do zensical;
- as fórmulas MathJax das aulas 7 e 8.

**Pronto quando:** `zensical serve` rodar e cada página do módulo for aberta nos dois temas.

```bash
docker run --rm -it -p 8006:8000 -v ${PWD}:/docs zensical/zensical serve --dev-addr=0.0.0.0:8000
```

### 2. `site/` com arquivos de propriedade de root

**Onde:** raiz.

**Problema:** 46 arquivos pertencentes a `root`, de um build anterior em container. Não podem ser removidos nem sobrescritos pelo usuário, o que também impede `zensical build --clean`. Já está no `.gitignore`.

**Pronto quando:** `sudo rm -rf site` executado.

### 3. Remoto do GitHub não conectado

**Onde:** `.github/workflows/ci.yml`.

**Problema:** o repositório é local. A CI pressupõe `eduardo-da-silva/fundamentos-arquitetura`, que ainda não existe. Enquanto isso, o site não é publicado e não há backup fora da máquina.

**Pronto quando:** repositório criado e `git push` feito.

### 4. Mini-Orion sem CI

**Onde:** `code/mini-orion/`.

**Problema:** os 18 testes e os 3 contratos de `import-linter` rodam só localmente. A CI atual constrói o site e não toca no código. Um contrato arquitetural que não roda automaticamente é um acordo verbal com passos extras.

**Pronto quando:** um job de CI rodar `pytest` e `lint-imports` nos três checkpoints.

### 5. Cenários de atividade com personagens redundantes

**Onde:** `aula01` (campanha Flash Orion), `aula02` (novo parceiro de pagamentos), `aula04` (fronteiras violadas).

**Problema:** cada cenário inventa personagens próprios (Júlia, Rafael, Camila, Ana, Diego, Bruna). A Aula 3 usa três deles de novo, com papéis compatíveis, mas por coincidência e não por decisão. `05-domain.md` não define elenco.

**Pronto quando:** `05-domain.md` fixar quatro ou cinco personagens com papel estável, e as aulas usarem esses.

### 6. Módulos 2 a 4 não escritos

Escopo em `07-curriculum.md`. Roadmap aula a aula só quando o módulo entrar em produção — escrito com antecedência demais, envelhece antes de ser usado.

---

## Resolvido

### Onda 1 — coerência

- **Direção de dependência indefinida.** A Aula 7 contava setas de entrada como fan-in (`A --> B` = A depende de B) enquanto a Aula 3 desenhava `Catalogo --> Checkout` com o código mostrando o inverso. A convenção nunca era declarada, e as duas aulas usavam sentidos contrários — na disciplina cujo tema é direção de dependência. Convenção agora fixada em `03-visual-language.md`, declarada em todo diagrama e verificada no checklist.
- **Números contraditórios.** `Catalogo` aparecia com fan-in 7, 0 e 3 no mesmo capítulo; `Checkout`, com fan-out 6, 3 e 5. Todos os valores passaram a vir da tabela de `05-domain.md`, validada por script: 17 arestas, $\sum C_a = \sum C_e = 17$.
- **`xychart-beta` com valor sem origem.** O gráfico plotava `Pagamentos` com $D = 0{,}12$, inexistente no texto. Removido.
- **Visualização que não distinguia o que a aula ensina.** Um gráfico de barras de $D$ não separa Zone of Pain de Zone of Uselessness, porque $D$ é simétrico. Substituído por SVG inline do plano $A \times I$, com `Catalogo` e `Integracoes` em cantos opostos.
- **Convenção de contagem de Abstractness ausente.** Adotada a tabela de `06-code-style.md`, com a observação de que a convenção é decisão da disciplina.
- **Cores hexadecimais fixas** em cinco diagramas, sob tema com alternância claro/escuro. Trocadas por destaque de forma.
- **Exemplo de palha.** `_gerar_relatorio_financeiro_mensal()` dentro do checkout era caricatura. Substituído por acúmulo plausível de responsabilidades, com a história de como cada linha chegou lá.
- **Cálculo de preço em `Pedidos`**, que por `05-domain.md` não é responsável por isso.
- **`Usuarios` versus `Clientes`**, para o mesmo componente.

### Onda 2 — substância

- **Trilhas Orion sem artefato.** Eram anunciadas em 8 de 8 capítulos e entregues como dois bullets. Agora: `code/mini-orion/` com três checkpoints executáveis (18 testes, 3 contratos de `import-linter`), e `docs/orion/` com formatos e rubricas do Evolution Lab.
- **Snippets incompatíveis.** Três versões incompatíveis do checkout entre as aulas 1, 3 e 8. Blocos classificados como snippet ilustrativo ou código do Mini-Orion, conforme `06-code-style.md`.
- **Oficina que não cabia no tempo.** 90 a 110 minutos para um roteiro de cerca de 200. Passou a ocupar os dois encontros da semana, com rubrica e pesos no lugar dos "critérios sugeridos".
- **Boilerplate.** Removidas as molduras repetidas em 8 de 8 capítulos: `### Trilhas permanentes...`, `### Uma possível resolução comentada do professor`, `### No início/No final — ...`, `Apresentação do diagrama:` / `Interpretação:`.

### Padronização dos exercícios

- **Formato de exercício inconsistente.** As aulas 1, 2, 4 e 5 mantinham o formato antigo — lista sem gabarito seguida de atividade em grupo com resolução do professor, o inverso da regra de `01-pedagogy.md`. As oito aulas agora seguem o mesmo padrão: `## Exercícios` com quatro questões, gabarito recolhido em `??? note` nas três primeiras, quarta questão de julgamento com critério em vez de resposta, e `## Atividade em grupo` com um item obrigatório que força reconhecer o limite da própria proposta. A Aula 8 é a exceção deliberada: sendo a oficina, substitui os exercícios por um aquecimento individual sem gabarito.

### Onda 3 — estrutura

- **Rebalanceamento da ementa.** Connascência passou de 2 aulas para 1; a vaga virou a Aula 3, "Características arquiteturais", escrita do zero — tema que o livro-base trata em três capítulos e que antes eram cinco bullets na Aula 1.
- **Ordem de força da connascência ausente.** A ordem canônica de Page-Jones — CoN < CoT < CoM < CoP < CoA < CoE < CoTiming < CoV < CoI — nunca era enunciada, sendo o núcleo da ferramenta. Agora abre a seção, e força/localidade/grau entram **antes** das nove formas, não no fim.
- **Exemplo de CoT que não era CoT.** Era um crash de tipagem dinâmica dentro de uma função. Virou acordo de tipo entre dois componentes.
- **"Antes" e "depois" não comparáveis** na Aula 1: o "depois" removia a notificação sem explicação. Agora trata as mesmas três responsabilidades, e o texto explicita que a segunda versão não é universalmente melhor.
- **ADR-002 sem ADR-001.** Renumerado, e o formato ganhou os dois campos que faltavam: alternativa descartada e custo de reversão.
- **Arquivos renomeados** de `capituloN.md` para `aulaNN-slug.md`, alinhando nome de arquivo, número da aula e rótulo do `nav`.
- **Contradição no nome do Módulo 2** e **duas semanas não alocadas** nas 18.
- **Resíduo de POO-II:** `docs/modulo2/` (byte-idêntico ao outro repositório) e `code/` (árvore completa idêntica, nunca referenciada).
