# Metodologia

## O ciclo da aula

Toda aula segue este ciclo. Ele é diferente do ciclo da disciplina de POO-II (`Problema → Discussão → Modelagem → Implementação → Refatoração`) porque o produto é diferente: lá se constrói um sistema, aqui se constrói um julgamento.

```
Sintoma → Diagnóstico → Alternativas → Trade-off → Decisão → Evidência
```

### Sintoma

A aula abre com algo observável no Orion. Um incidente, uma reclamação, um prazo que estourou, uma métrica que piorou.

Não abre com definição. Não abre com "nesta aula estudaremos acoplamento".

Ruim:

> Nesta aula, estudaremos acoplamento e coesão.

Bom:

> Na campanha de novembro, uma mudança na regra de frete quebrou a emissão de nota fiscal. As duas coisas não têm relação de negócio nenhuma. Por que uma quebrou a outra?

O sintoma precisa ser específico e verificável dentro do Orion. Sintoma genérico ("o sistema é difícil de manter") não serve, porque não aponta para lugar nenhum.

### Diagnóstico

O que a estrutura do sistema revela sobre o sintoma. Aqui entra o vocabulário técnico — e ele entra porque é necessário para nomear o que se está vendo, não porque está na ementa.

### Alternativas

**No mínimo duas, e as duas precisam ser defensáveis.**

Esta é a regra mais violada e a mais importante. Apresentar uma alternativa obviamente ruim ao lado da solução pretendida não ensina a decidir — ensina a reconhecer a resposta do professor.

Ruim:

> Poderíamos deixar tudo numa classe só, ou separar em componentes com contratos explícitos.

Bom:

> Podemos manter a chamada direta, que é simples de ler e de depurar, mas acopla o checkout ao pagamento. Ou publicar um evento, que desacopla, mas nos obriga a lidar com falha assíncrona, ordem de entrega e observabilidade distribuída. As duas escolhas são feitas por times competentes.

Se uma das alternativas não tem nenhum defensor razoável no mundo real, ela não conta como alternativa.

### Trade-off

O que cada alternativa custa. Custo em quê: tempo de entrega, complexidade operacional, dificuldade de teste, número de pessoas que precisam entender o sistema, custo de reverter.

Toda decisão arquitetural tem custo. Uma aula que apresenta uma solução sem custo está mentindo, e o aluno descobre isso no primeiro emprego.

### Decisão

A escolha, com a justificativa amarrada ao contexto do Orion — não a um princípio abstrato.

"Escolhemos evento porque desacopla" é fraco. "Escolhemos evento porque o pico de campanha torna o bloqueio do checkout pela notificação um risco de receita, e aceitamos o custo de observabilidade porque já temos rastreamento distribuído" é uma decisão.

Sempre que a decisão for relevante para as aulas seguintes, ela vira um ADR registrado em `docs/orion/`.

### Evidência

Algo que sustente a decisão além do argumento: uma métrica calculada, um teste que passa a ser possível, uma dependência que sumiu do grafo, um tempo de build.

Nem toda aula terá evidência quantitativa. Mas a aula precisa dizer **o que observaríamos** se a decisão estivesse certa, e o que observaríamos se estivesse errada. Decisão que não é falseável é preferência.

---

## Níveis cognitivos

O material do Módulo 1 concentrou-se quase todo em *analisar* e *avaliar*, com pouquíssimo *aplicar*. Isso produz alunos que discutem bem e travam diante de uma ferramenta.

Distribuição-alvo por aula:

| Nível | Peso | Como aparece |
|---|---|---|
| Lembrar / Entender | ~15% | vocabulário mínimo, no desenvolvimento conceitual |
| **Aplicar** | ~30% | calcular métrica com ferramenta real, escrever o ADR, refatorar o Mini-Orion, rodar análise de dependência |
| **Analisar** | ~30% | diagnosticar o recorte, mapear connascências, ler o grafo |
| **Avaliar** | ~25% | comparar alternativas, priorizar, defender a escolha |

O nível *aplicar* é onde falta massa. Sempre que uma aula tratar de algo mensurável, ela deve usar ferramenta de verdade sobre código de verdade — não cálculo manual sobre número inventado. Ver `10-tooling.md`.

---

## Exercícios

### Regra do gabarito

**Exercício destinado a estudo autônomo tem resposta comentada. Atividade feita em grupo com o professor presente pode não ter.**

O material do Módulo 1 fez o inverso: deixou os "exercícios durante a aula" sem gabarito e deu resolução comentada à atividade em grupo. O aluno que estuda sozinho ficou sem retorno exatamente onde mais precisava.

Quando a resposta comentada puder induzir cópia, use `??? note "Resposta comentada"` (recolhido por padrão) em vez de omitir.

### Tipos de exercício

- **Verificação** — resposta convergente, serve para o aluno conferir se entendeu o vocabulário. Gabarito obrigatório.
- **Aplicação** — usar a técnica sobre um recorte dado. Gabarito com o raciocínio, não só o número.
- **Julgamento** — comparar alternativas e defender uma. Não tem gabarito; tem **critério de avaliação** (ver `09-assessment.md`). O material deve dizer o que caracteriza uma boa resposta, sem dar a resposta.

Todo exercício de julgamento precisa deixar explícito que mais de uma resposta é aceitável. Caso contrário o aluno tenta adivinhar a preferência do professor, que é o hábito exatamente oposto ao pretendido.

### Exercícios de reflexão no meio do texto

Pausas curtas, uma pergunta, sem resposta imediata. Usar com moderação: se aparecerem em toda seção, viram ruído e o aluno pula. No máximo dois por aula.

---

## O que evitar

- Apresentar um princípio como universal. Todo princípio arquitetural tem um contexto em que ele custa mais do que entrega.
- "Boas práticas" sem dizer para quem e quando.
- Alternativa de palha, montada só para perder.
- Métrica apresentada como veredito em vez de sintoma.
- Diagrama que só ilustra o texto, sem revelar nada que o texto não disse.
- Exemplo de domínio auxiliar. O Orion basta.
- Conceito introduzido porque está no livro, sem sintoma que o justifique.
- Aula que termina sem que nada tenha sido decidido.

---

## O papel do erro

Sempre que possível, mostrar uma decisão que parecia certa e envelheceu mal. Não como pegadinha, mas porque é assim que arquitetura funciona: as decisões são tomadas com a informação disponível na época.

Isso ensina algo que o material bem-comportado não ensina — que revisitar uma decisão não é sinal de incompetência, é o trabalho.
