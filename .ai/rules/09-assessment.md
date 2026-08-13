# Avaliação

## O problema desta disciplina

Em POO-II o teste passa ou não passa. Aqui o produto é um argumento, e argumento sem rubrica vira nota por impressão — o que ensina o aluno a escrever para agradar em vez de escrever para sustentar.

Este documento define os critérios. Eles são públicos: o aluno os conhece antes de produzir.

---

## Princípio

**Avalia-se a qualidade da justificativa, não a escolha.**

Duas propostas opostas podem receber nota máxima se ambas nomearem o contexto, as alternativas e o custo. Uma proposta que coincide com a preferência do professor mas não sustenta o porquê recebe nota baixa.

Isso precisa ser dito ao aluno de forma explícita e repetida. O hábito trazido das outras disciplinas é procurar a resposta certa, e ele não se desfaz sozinho.

---

## O que separa argumento de opinião

Estes são os cinco critérios usados em todas as rubricas.

| | Opinião | Argumento |
|---|---|---|
| **Contexto** | vale sempre | nomeia a restrição sob a qual vale |
| **Alternativa** | ausente, ou de palha | alternativa real, que alguém competente escolheria |
| **Custo** | só benefícios | nomeia o que a escolha custa e o que ela impede |
| **Evidência** | "é mais limpo", "é melhor" | métrica, teste, dependência que sumiu, incidente evitado |
| **Falseabilidade** | não se pode discordar | diz o que observaríamos se estivesse errado |

O quinto critério é o mais discriminante e o mais raro. Uma proposta que não diz sob que condição estaria errada não é uma proposta técnica.

---

## Rubrica — entrega do Orion Evolution Lab

Aplica-se a cada entrega parcial e à final.

| Critério | Peso | Nota máxima exige |
|---|---|---|
| **Diagnóstico** | 20% | problemas localizados em componentes específicos, cada um com evidência no grafo, no código ou na métrica |
| **Uso do vocabulário** | 15% | acoplamento, coesão, connascência e métricas usados com precisão; connascência classificada pelos três eixos |
| **Alternativas** | 20% | no mínimo duas por decisão relevante, ambas defensáveis; a descartada explicada sem caricatura |
| **Trade-off** | 20% | custo de cada alternativa nomeado em dimensão concreta: prazo, operação, testabilidade, pessoas, reversão |
| **Priorização** | 15% | ordem justificada por critério explícito, não por facilidade; diz o que fica de fora e por quê |
| **Comunicação** | 10% | diagrama legível que declara o que omite; texto que outra pessoa entende sem o autor presente |

### Faixas

- **90–100** — todos os critérios atendidos; pelo menos uma decisão com condição de falseamento explicitada.
- **75–89** — diagnóstico e alternativas sólidos; trade-off nomeado mas pouco concreto.
- **60–74** — diagnóstico correto; alternativas presentes mas desequilibradas; trade-off genérico.
- **40–59** — descreve o sistema sem diagnosticar; propõe sem alternativa.
- **abaixo de 40** — opinião sem evidência, ou vocabulário aplicado incorretamente.

### Penalidades

- Proposta sem nenhum custo nomeado: teto de 60, independentemente do resto.
- Alternativa de palha (montada para perder): zera o critério "Alternativas".
- Números que não batem entre si dentro da mesma entrega: zera "Diagnóstico". O mesmo padrão que se cobra do material.

---

## Formato de entrega

Estrutura fixa. Formato estável ao longo do curso permite que o aluno acumule em vez de recomeçar.

```
1. Recorte analisado          — o que está dentro, o que ficou fora, por quê
2. Mapa de dependências       — diagrama + tabela Ca/Ce
3. Diagnóstico                — por componente: problema, evidência, impacto
4. Métricas                   — tabela A/I/D + leitura, incluindo onde a métrica engana
5. Decisões propostas         — uma seção por decisão, no formato ADR
6. Priorização                — ordem, critério, e o que fica para depois
7. Critério de sucesso        — o que observaríamos se as decisões funcionassem
```

A seção 7 costuma ser esquecida e é a que mais diferencia. Peça explicitamente.

### Formato do ADR

```
Contexto      — a situação e a restrição
Decisão       — o que foi decidido, em uma frase
Alternativas  — as consideradas e por que foram descartadas
Consequências — positivas E negativas, ambas obrigatórias
Reversão      — o que custaria voltar atrás
```

ADR sem consequência negativa está incompleto — não é decisão, é anúncio.

---

## Orçamento de tempo

Uma aula tem 50 minutos. Uma semana, dois encontros.

| Atividade | Tempo realista |
|---|---|
| Mapear componentes e dependências de um recorte novo | 40–50 min |
| Diagnóstico qualitativo de um recorte já mapeado | 30–40 min |
| Mapa de connascências de 4 a 5 componentes | 40–50 min |
| Calcular $C_a$/$C_e$ de um grafo dado | 15 min |
| Calcular $A$/$I$/$D$ de 3 a 4 componentes com dados fornecidos | 20 min |
| Escrever um ADR completo | 25–30 min |
| Priorizar 5 decisões com justificativa | 30 min |
| Apresentar e defender diante de perguntas | 10–15 min por grupo |

**A oficina da Aula 8, como está escrita, soma cerca de 200 minutos e prevê 90 a 110.** Não é questão de ritmo; não cabe.

Duas saídas, em ordem de preferência:

1. **Oficina ocupa a semana inteira** (dois encontros). Priorizar sob restrição é a competência central do módulo e merece o tempo.
2. **Material fornece mapa e métricas prontos**, e a oficina se concentra em priorizar e defender. Perde-se a prática de mapear, que já foi exercitada nas aulas 4 e 7.

Regra geral ao desenhar atividade: **some os tempos da tabela acima antes de definir a duração.** Atividade que não cabe produz entrega superficial e a rubrica passa a punir o aluno por um erro do material.

---

## Avaliação da defesa oral (semana 18)

Peso próprio, distinto da entrega escrita.

| Critério | Peso |
|---|---|
| Sustenta a decisão diante de contestação | 40% |
| Reconhece o limite da própria proposta | 25% |
| Responde com evidência, não com repetição | 20% |
| Clareza na exposição | 15% |

O segundo critério é deliberado e vale mais do que parece. O aluno que diz "essa parte da nossa proposta é frágil porque não medimos X" demonstra a competência central da disciplina. O que defende tudo com a mesma convicção, não.

Perguntas da banca devem incluir pelo menos uma alternativa legítima que o grupo não escolheu. Não para derrubar — para ver se o grupo entende por que não escolheu.
