# Currículo

!!! success "Status"

    Aprovado e aplicado. O Módulo 1 foi rebalanceado em agosto de 2026 e a composição abaixo é a que está publicada.

## As 18 semanas

Duas aulas por semana. Total de 36 encontros.

| Módulo | Semanas | Aulas | Tema |
|---|---|---|---|
| 1 | 1–4 | 8 | Fundamentos Arquiteturais |
| 2 | 5–8 | 7 | Arquiteturas Monolíticas |
| 3 | 9–13 | 10 | Arquiteturas Distribuídas |
| 4 | 14–17 | 8 | Eventos e Arquitetura Evolutiva |
| — | 18 | 2 | Apresentação final do Orion Evolution Lab e fechamento |

*O Módulo 2 tem 7 aulas e ocupa os 8 encontros das semanas 5–8: seis aulas conceituais (9–14) em um encontro cada e a oficina (aula 15) nos dois encontros da semana 8. A fusão das duas aulas de camadas é o que faz a oficina dupla caber — com 8 aulas e oficina dupla não cabia, e é essa a inconsistência que o Módulo 1 ainda carrega. Nada é transferido para outro módulo.*

Isso resolve uma inconsistência do material atual: `docs/index.md` anuncia 18 semanas e 4 módulos, enquanto `docs/modulo1/index.md` estabelece 4 semanas por módulo — o que soma 16 e deixa duas semanas sem destino. O Módulo 3 recebe uma semana a mais por ser o de maior densidade, e a semana 18 é dedicada à entrega final.

**Nomes dos módulos são normativos.** Qualquer página que os cite usa exatamente estes. O material atual tem contradição direta: `docs/index.md` anuncia "Módulo 2 — Arquiteturas Monolíticas" e o diretório `docs/modulo2/` continha "Módulo 2 — Evoluindo o domínio", resíduo do repositório de POO-II (removido).

---

## Progressão obrigatória

A ordem existe porque cada bloco depende do vocabulário do anterior:

```
Decisão arquitetural
    ↓
Trade-off e custo da mudança
    ↓
Características arquiteturais (identificar, priorizar, medir)
    ↓
Modularidade e fronteira de componente
    ↓
Acoplamento, coesão, connascência
    ↓
Métrica e governança automatizada
    ↓
Estilos arquiteturais (mono → distribuído → eventos)
    ↓
Evolução e fitness functions
```

Nenhum estilo arquitetural aparece antes de o aluno ter critério para avaliá-lo. Apresentar microsserviços a quem ainda não sabe medir acoplamento produz opinião, não julgamento.

---

## Módulo 1 — Fundamentos Arquiteturais

### Composição

| Aula | Tema | Origem |
|---|---|---|
| 1 | O que é Arquitetura de Software? | mantém |
| 2 | Leis da Arquitetura, trade-offs e ADR | ADR como prática formal |
| 3 | **Características arquiteturais: identificar, priorizar, medir** | escrita do zero |
| 4 | Modularidade e Componentes | antiga aula 3 |
| 5 | Acoplamento e Coesão | antiga aula 4 |
| 6 | **Connascência** | fusão das antigas 5 e 6 |
| 7 | Métricas e governança automatizada | ganhou pydeps e import-linter |
| 8 | Oficina de Diagnóstico Arquitetural | ocupa os dois encontros da semana |

**Por que fundir connascência.** Hoje ela ocupa 2 de 8 aulas — 25% do módulo. No livro-base é parte de um capítulo. É um vocabulário de precisão para falar de acoplamento, valioso mas instrumental. Uma aula bem construída cobre as nove formas, os três eixos (força, localidade, grau) e a heurística de uso.

**Por que criar a aula de características arquiteturais.** É o tema que o livro-base trata em três capítulos e que o material atual resolve com uma lista de cinco bullets na Aula 1. Sem saber identificar e priorizar características, o aluno não tem contra o que avaliar arquitetura nenhuma — é a fundação de todos os módulos seguintes. A troca com connascência é o rebalanceamento mais defensável do módulo.

**Por que ADR na Aula 2.** O ciclo pedagógico da disciplina termina em "decisão registrada" (`01-pedagogy.md`). Sem formato de registro estabelecido cedo, o Orion Evolution Lab não tem como acumular artefato. Hoje o ADR aparece como "registro simples de decisão" num exemplo isolado.

### Conceitos do módulo

Decisão arquitetural; arquitetura versus design; características arquiteturais; trade-off; custo da mudança; ADR; modularidade; componente; fronteira; contrato; acoplamento aferente e eferente; coesão; connascência (força, localidade, grau); Fan-in; Fan-out; Abstractness; Instability; Distance from Main Sequence; governança por teste de arquitetura.

---

## Módulo 2 — Arquiteturas Monolíticas

Semanas 5–8.

### Composição

| Aula | Tema |
|---|---|
| 9 | O monólito não é o problema |
| 10 | Monólito em camadas: o que governa e o que não isola |
| 11 | Monólito modular: fronteira lógica sem fronteira física |
| 12 | Reorganizar o grafo do Orion |
| 13 | Pipeline e microkernel: monólitos com forma |
| 14 | Quando o monólito deixa de servir |
| 15 | Oficina: o Orion modular sob restrição (dois encontros da semana 8) |

Aplicação no Orion: reorganizar o grafo atual sem distribuir nada, e medir o ganho.

**Por que fundir as duas aulas de camadas.** As camadas técnicas e o limite delas são um arco só, e separá-las em duas aulas faria o aluno sair da primeira com a técnica antes de ver o que ela não isola.

**Por que o `06-microkernel/` é checkpoint executável.** Microkernel descrito sem código vira definição solta; um núcleo com plug-ins que de fato rodam obriga o conceito a se sustentar na prática, como a Oficina de Diagnóstico faz no Módulo 1.

---

## Módulo 3 — Arquiteturas Distribuídas

Semanas 9–13. Não escrito. Módulo mais longo.

Falácias da computação distribuída. Service-based, microsserviços, granularidade e os critérios de desintegração. Consistência, transação distribuída, saga. O custo real: operação, observabilidade, contrato entre times.

Aplicação no Orion: decidir o que extrair primeiro, e defender a decisão contra a alternativa de não extrair nada.

---

## Módulo 4 — Eventos e Arquitetura Evolutiva

Semanas 14–17. Não escrito.

Arquitetura orientada a eventos: broker e mediator, coreografia e orquestração. Acoplamento temporal. Arquitetura evolutiva, fitness functions, governança contínua. Dívida arquitetural e como pagá-la em parcelas.

Aplicação no Orion: converter as decisões acumuladas em fitness functions que rodam na CI.

---

## Continuidade entre módulos

Todo módulo reutiliza o vocabulário do Módulo 1 explicitamente. Ao discutir extração de serviço no Módulo 3, o argumento se faz com acoplamento, coesão, connascência e métrica — não com preferência por microsserviços.

Se um módulo introduz vocabulário próprio que não se conecta ao anterior, ele está desenhado errado.

---

## Semana 18

Apresentação final do Orion Evolution Lab: cada grupo defende sua proposta arquitetural diante de perguntas. Critérios e pesos em `09-assessment.md`.

A defesa oral é deliberada. Arquitetura se sustenta em argumento diante de contestação, e um documento entregue não exercita isso.
