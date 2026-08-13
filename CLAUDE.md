# Instruções do repositório

Este repositório contém as notas de aula da disciplina **Arquitetura de Software** do Bacharelado em Sistemas de Informação (IFC). O material é publicado como site estático e gira em torno de um estudo de caso único: o **Marketplace Orion**.

## Antes de produzir ou revisar qualquer material

Leia `.ai/README.md`. Ele é a porta de entrada do padrão editorial da disciplina e indica quais documentos de `.ai/rules/` carregar para cada tarefa.

Não escreva, reescreva ou revise uma aula sem antes carregar as regras aplicáveis. O padrão existe justamente porque material produzido sem ele já gerou inconsistências no Módulo 1 — elas estão catalogadas em `.ai/rules/12-backlog.md`.

## Prioridade em caso de conflito

1. Instruções diretas do professor nesta conversa.
2. `.ai/rules/00-course.md`.
3. Demais documentos de `.ai/rules/`, em ordem numérica.
4. Comportamento padrão.

## Roteamento mínimo

Carregar o conjunto inteiro de `.ai/rules/` desperdiça contexto. Use a tabela de roteamento de `.ai/README.md`. Como referência rápida:

| Tarefa | Carregar |
|---|---|
| Escrever uma aula nova | `00`, `01`, `02`, `04`, `05`, `08` |
| Revisar uma aula existente | `11`, mais o `05` se a aula usar dados do Orion |
| Mexer em diagramas ou visual | `03`, `10` |
| Mexer em código de exemplo | `05`, `06` |
| Criar exercícios ou avaliação | `01`, `09` |
| Alterar currículo ou cronograma | `07`, `08` |

## Regras invioláveis deste repositório

- Este repositório trata **exclusivamente** de arquitetura de software. Nunca introduza conteúdo de outras disciplinas. O Módulo 1 já foi contaminado uma vez por uma cópia incompleta do repositório de POO-II.
- Um arquivo em `docs/` que não esteja no `nav:` de `mkdocs.yml` é um erro, não um rascunho. Rascunhos ficam fora de `docs/`.
- Todo número apresentado ao aluno (Fan-in, Fan-out, métricas, valores em gráficos) deve vir de `.ai/rules/05-domain.md`. Não invente dados por aula.
- Não use `sudo` nem altere permissões de arquivos sem pedir.
