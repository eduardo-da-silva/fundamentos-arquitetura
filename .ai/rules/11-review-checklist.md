# Checklist de revisão

> Aplicar antes de publicar qualquer aula. Uma aula com item desmarcado não vai para o `nav`.

## Contexto e continuidade

- [ ] A aula abre com um sintoma concreto do Orion, não com uma definição.
- [ ] O sintoma é específico e verificável no domínio, não genérico ("o sistema é difícil de manter").
- [ ] Retoma o estado deixado pela aula anterior sem repetir seu conteúdo.
- [ ] A ponte final é uma pergunta real, não um anúncio de sumário.
- [ ] Nenhum conceito é usado antes de ter sido introduzido em alguma aula anterior.

## Estrutura

- [ ] As seis seções obrigatórias de `02-lesson-structure.md` estão presentes, ainda que com títulos próprios.
- [ ] A ordem lógica (sintoma → conceito → decisão → exercício) foi respeitada.
- [ ] Entre 200 e 320 linhas, se for aula conceitual.
- [ ] A aula produz o artefato previsto para ela em `08-lesson-roadmap.md`, nas duas trilhas.

## Voz e anti-boilerplate

- [ ] **Nenhum bloco de texto aparece literalmente igual em mais de duas aulas.**
- [ ] Comparada lado a lado com a aula anterior, menos da metade dos títulos de seção coincide.
- [ ] Apagando o título, dá para identificar qual aula é pelas primeiras vinte linhas.
- [ ] Nenhuma expressão da lista de proibidas de `04-author-voice.md` ("obviamente", "basta", "a melhor prática é", "sempre", "nunca").
- [ ] Nenhuma pergunta retórica com a resposta embutida.
- [ ] Primeira pessoa do plural para o raciocínio, segunda do singular para o aluno, nunca primeira do singular.

## Argumento

- [ ] Toda decisão apresenta **no mínimo duas** alternativas.
- [ ] Nenhuma alternativa é de palha — todas teriam defensor competente em algum contexto.
- [ ] Toda decisão nomeia o que custa.
- [ ] Toda recomendação diz sob qual condição deixa de valer.
- [ ] A aula diz o que observaríamos se a decisão estivesse errada.
- [ ] Nenhum princípio é apresentado como universal.

## Domínio

- [ ] Todos os componentes citados existem em `05-domain.md`.
- [ ] Todas as dependências citadas constam do grafo oficial.
- [ ] Os nomes seguem a linguagem ubíqua — `Clientes`, nunca `Usuarios`; `Catalogo`, nunca "produtos".
- [ ] Se a aula usa recorte, ela diz que é recorte.
- [ ] O recorte legado (`CoreService`) só aparece identificado como histórico.
- [ ] Nenhum domínio auxiliar (biblioteca, escola, locadora) foi introduzido.

## Números

- [ ] **Todo número vem de `05-domain.md`.** Nenhum valor inventado na aula.
- [ ] **Todo número usado em exemplo, diagrama, exercício e atividade da mesma aula bate entre si.**
- [ ] **Todo valor exibido em gráfico ou tabela tem origem rastreável no texto.**
- [ ] Os cálculos foram refeitos, não copiados.
- [ ] Fan-in e Fan-out mostrados em diagrama batem com a tabela oficial.

!!! danger "Os três itens em negrito são os mais importantes do checklist"

    São exatamente os que falharam na Aula 7 publicada: `Catalogo` aparece com Fan-in 7, 0 e 3 no mesmo capítulo; `Checkout` com Fan-out 6, 3 e 5; e o gráfico plota `Pagamentos` com $D = 0{,}12$, valor que não existe em lugar nenhum do texto.

    O aluno que tentar refazer as contas não fecha com nada, e conclui que não entendeu — quando o material é que está errado.

## Código

- [ ] Cada bloco está classificado: snippet ilustrativo ou código do Mini-Orion (`06-code-style.md`).
- [ ] Snippet ilustrativo não usa nomes do Mini-Orion.
- [ ] Código do Mini-Orion existe de verdade em `code/mini-orion/aulaNN/` e roda.
- [ ] Nomes de classe e método são consistentes com as aulas anteriores.
- [ ] Nenhum bloco passa de 25 linhas.
- [ ] "Antes" e "depois" são comparáveis — o "depois" faz tudo que o "antes" fazia, ou a diferença é explicada.
- [ ] Type hints presentes nas assinaturas públicas.
- [ ] Comentários explicam decisão, não mecânica.

## Diagramas

- [ ] **Todo diagrama de dependência declara a convenção de leitura das setas.**
- [ ] **A direção das setas é `A --> B` = A depende de B, e bate com o grafo de `05-domain.md`.**
- [ ] Seta que representa fluxo, e não dependência, está identificada como tal no rótulo.
- [ ] Cada diagrama responde a uma pergunta que o texto fez.
- [ ] Cada diagrama diz o que **não** representa.
- [ ] Nenhum tipo `-beta` (ver `10-tooling.md`).
- [ ] Nenhuma cor hexadecimal fixa em `fill:` ou `color:`.
- [ ] Máximo de sete nós.
- [ ] Rótulos sem acento.
- [ ] Renderizou no preview local — verificado de fato, não presumido.

## Fórmulas

- [ ] Toda fórmula tem leitura em linguagem natural logo abaixo.
- [ ] Toda variável está definida no mesmo bloco.
- [ ] A informação essencial não existe apenas dentro da fórmula.

## Exercícios e avaliação

- [ ] Exercício de estudo autônomo tem resposta comentada, recolhida em `??? note`.
- [ ] Exercício de julgamento declara que mais de uma resposta é aceitável.
- [ ] Exercício de julgamento traz critério de avaliação, não gabarito.
- [ ] A atividade cabe no tempo previsto — tempos somados conforme `09-assessment.md`.
- [ ] O nível *aplicar* está presente, não só *analisar* e *avaliar*.
- [ ] Nada do Orion Evolution Lab foi resolvido pelo material.

## Visual

- [ ] Um único `#` no arquivo.
- [ ] No máximo quatro admonitions abertas.
- [ ] Emoji apenas nos papéis definidos em `03-visual-language.md`.
- [ ] Negrito só para termo técnico na primeira aparição.
- [ ] A aula não é majoritariamente bullet point.

## Publicação

- [ ] A aula está no `nav:` de `mkdocs.yml`.
- [ ] Nenhum arquivo órfão em `docs/` (comando de verificação em `10-tooling.md`).
- [ ] Build local sem erro.
- [ ] Página vista renderizada, nos temas claro **e** escuro.

## Referências

- [ ] Toda citação indica capítulo ou seção, não só o livro.
- [ ] Toda obra citada consta de `00-course.md`.

---

## Erros a evitar

Recorrentes no material atual, todos catalogados em `12-backlog.md`:

1. Números contraditórios para o mesmo componente dentro do mesmo capítulo.
2. Valor em gráfico sem origem no texto.
3. Visualização que não distingue o que a aula precisa distinguir — gráfico de barras de $D$ para separar *Zone of Pain* de *Zone of Uselessness*.
4. Métrica pedida sem convenção de contagem definida.
5. Trilha anunciada em toda aula e nunca materializada.
6. Snippets do mesmo componente incompatíveis entre aulas.
7. Seção idêntica em oito de oito capítulos.
8. "Antes" e "depois" não comparáveis.
9. Ordem de força da connascência nunca enunciada, sendo ela o núcleo da ferramenta.
10. Conceito introduzido tarde demais para ser usado onde faz falta.

---

## Critério de aprovação

Uma aula está pronta quando:

- o aluno que a leu sozinho consegue refazer as contas e chegar aos mesmos números;
- consegue nomear pelo menos uma alternativa legítima à decisão tomada;
- consegue dizer o que a decisão custou;
- consegue apontar o que ele produziu de concreto ao final;
- e, lendo a aula anterior em seguida, percebe que são aulas diferentes.

Se qualquer um dos cinco falhar, a aula volta para revisão.
