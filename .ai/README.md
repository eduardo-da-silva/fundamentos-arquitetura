# Manual do Projeto — Arquitetura de Software

> Porta de entrada da pasta `rules`. Leia antes de produzir, revisar ou modificar qualquer material desta disciplina.

Este documento resume a filosofia da disciplina e diz qual documento consultar em cada situação.

---

## O que é este projeto

Um curso de Arquitetura de Software construído sobre a análise e a evolução de um sistema real: o **Marketplace Orion**.

O objetivo não é apresentar um catálogo de estilos arquiteturais. É desenvolver **pensamento arquitetural**: a capacidade de olhar para um sistema, identificar onde estão os riscos estruturais, propor caminhos e justificar a escolha diante de alternativas legítimas.

Ao final, o aluno deve conseguir sustentar uma proposta arquitetural com argumento técnico e evidência — não com preferência pessoal.

---

## Filosofia

- O sintoma vem antes do conceito.
- O diagnóstico vem antes da solução.
- A alternativa descartada vale tanto quanto a escolhida.
- O trade-off vem antes da recomendação.
- A evidência vem antes da opinião.
- A decisão registrada vale mais que o diagrama bonito.

Havendo dúvida entre duas abordagens, escolher a que obriga o aluno a decidir e justificar.

---

## O que diferencia esta disciplina de POO-II

O padrão editorial desta disciplina foi derivado do padrão de POO-II, mas os cursos produzem coisas diferentes e as regras acompanham essa diferença.

| | POO-II | Arquitetura de Software |
|---|---|---|
| Artefato central | a classe que funciona | a decisão registrada |
| Progresso da aula | o sistema ganha um comportamento | o sistema ganha uma fronteira, ou um risco é medido |
| Critério de acerto | o teste passa | o argumento se sustenta diante do trade-off |
| Papel do código | protagonista da implementação | evidência do problema ou da solução |
| Resposta esperada | tende a convergir | legitimamente diverge; a justificativa é o que se avalia |

Consequência prática: aqui, uma aula pode ser excelente com pouco código. Uma aula sem decisão explicitada, não.

---

## O estudo de caso

Todo o curso gira em torno do **Marketplace Orion**, descrito em `rules/05-domain.md`.

O Orion aparece em duas trilhas, e elas nunca se misturam:

- **Mini-Orion Checkout** — recorte pequeno do professor, resolvido em aula. Tem código executável em `code/mini-orion/`, que evolui aula após aula.
- **Orion Evolution Lab** — projeto dos grupos, sobre um recorte maior. Nunca é resolvido no material. Produz artefatos de análise acumuláveis em `docs/orion/`.

`rules/05-domain.md` é a fonte da verdade dos dois. Nenhuma aula inventa componente, dependência ou número que não esteja lá.

---

## Como ensinar

Sempre que possível, cada aula segue esta sequência:

```
Sintoma observável no Orion
    ↓
Diagnóstico (o que a estrutura revela)
    ↓
Alternativas (no mínimo duas)
    ↓
Trade-off (o que cada uma custa)
    ↓
Decisão registrada
    ↓
Evidência (medida, teste, ou consequência demonstrada)
    ↓
Aplicação no Orion Evolution Lab
    ↓
Ponte para a próxima aula
```

Nunca abrir uma aula pela definição do conceito. O conceito aparece porque o sintoma exigiu.

---

## Como utilizar esta pasta

O conjunto completo passa de 80 KB. Carregue apenas o necessário.

| Tarefa | Carregar | Não carregar |
|---|---|---|
| Escrever uma aula nova | `00`, `01`, `02`, `04`, `05`, `08` | `09`, `10`, `11` |
| Revisar uma aula pronta | `11` (mais `05` se houver dados do Orion) | os demais |
| Criar ou ajustar exercícios | `01`, `09`, `08` | `03`, `06`, `10` |
| Escrever ou alterar código de exemplo | `05`, `06` | `03`, `07`, `09` |
| Criar ou alterar diagramas | `03`, `10` | `06`, `07`, `09` |
| Definir avaliação e rubricas | `09`, `01` | `03`, `06`, `10` |
| Alterar currículo ou cronograma | `07`, `08`, `00` | `03`, `06`, `11` |
| Mexer no build, `mkdocs.yml` ou CI | `10` | os demais |
| Entender o estado do material | `12` | os demais |

Em caso de conflito entre documentos, `00-course.md` tem prioridade.

---

## Documentos da pasta `rules`

| Arquivo | Assunto |
|---|---|
| `00-course.md` | Identidade da disciplina, público, escopo, prioridade |
| `01-pedagogy.md` | Metodologia, ciclo da aula, exercícios, níveis cognitivos |
| `02-lesson-structure.md` | Estrutura da aula: obrigatório, opcional e limite de repetição |
| `03-visual-language.md` | Admonitions, marcadores, regras de diagrama e de cor |
| `04-author-voice.md` | Voz do autor, expressões, regras anti-boilerplate |
| `05-domain.md` | Marketplace Orion — fonte da verdade de componentes e números |
| `06-code-style.md` | Python, snippet ilustrativo vs. código do Mini-Orion |
| `07-curriculum.md` | 18 semanas, 4 módulos, progressão de conceitos |
| `08-lesson-roadmap.md` | Roadmap aula a aula, com artefato e avaliação de cada uma |
| `09-assessment.md` | Rubricas, pesos, formato de entrega, orçamento de tempo |
| `10-tooling.md` | Build, zensical, Mermaid suportado, MathJax, `nav` |
| `11-review-checklist.md` | Checklist de revisão e critério de aprovação de uma aula |
| `12-backlog.md` | Pendências conhecidas do material, priorizadas |

Todos os treze arquivos existem. Se um caminho citado aqui não existir em disco, isso é um defeito deste README e deve ser corrigido, não contornado.

---

## Estado atual do material

- **Módulo 1** — 8 aulas escritas e publicadas no `nav`. Passaram por análise crítica; as pendências estão em `rules/12-backlog.md`.
- **Módulos 2 a 4** — não escritos. Escopo definido em `rules/07-curriculum.md`.
- **Mini-Orion** — ainda não existe como código. Item de backlog.
- **Orion Evolution Lab** — ainda não existe como artefato acumulável. Item de backlog.
- **Versionamento** — o repositório ainda não é um repositório git. Item de backlog de risco alto.

---

## Regra mais importante

Se existir conflito entre a elegância do material e a capacidade do aluno de decidir sozinho, priorizar a capacidade de decidir.

O aluno que sai desta disciplina sabendo desenhar arquiteturas bonitas mas incapaz de defender uma escolha diante de uma alternativa razoável não aprendeu arquitetura.
