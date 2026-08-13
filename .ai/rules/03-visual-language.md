# Linguagem visual

## Hierarquia de títulos

- `#` — apenas o título da aula, uma vez por arquivo.
- `##` — seções principais.
- `###` — subseções.
- `####` — evitar. Se for necessário, a seção está grande demais.

Nunca dois `#` no mesmo arquivo. O Módulo 1 herdou de POO-II arquivos com `#` repetido no meio do texto (`docs/modulo2/index.md` fazia isso antes de ser removido) — isso quebra o sumário lateral do tema.

## Admonitions

Extensões `admonition` e `pymdownx.details` estão habilitadas em `mkdocs.yml`. Usar com parcimônia: uma página com sete caixas coloridas não tem destaque nenhum.

| Sintaxe | Quando usar |
|---|---|
| `!!! info` | contexto de apoio, nota histórica sobre a origem de um conceito |
| `!!! tip` | atalho prático, heurística de uso |
| `!!! warning` | armadilha real, algo que costuma dar errado em produção |
| `!!! danger` | consequência grave e irreversível |
| `!!! example` | recorte concreto do Orion |
| `!!! question` | pausa para o aluno pensar antes de continuar |
| `!!! quote` | citação de autor da bibliografia |
| `???` | conteúdo recolhido — cenários longos, gabaritos, material de apoio |
| `???+` | recolhível, aberto por padrão |

Máximo de quatro admonitions por aula, sem contar as recolhidas.

Gabarito de exercício sempre em `??? note "Resposta comentada"`, recolhido.

## Marcadores de seção recorrente

Quando uma seção cumpre um papel fixo no curso, ela usa marcador estável, para o aluno reconhecer à distância:

| Marcador | Seção |
|---|---|
| 🏗️ | Decisão de Projeto |
| 📐 | ADR registrado |
| 🔍 | Diagnóstico |
| ⚖️ | Trade-off |
| 📊 | Evidência / medição |
| ⚠️ | Erro comum |
| 🎯 | Exercícios |
| 🧪 | Orion Evolution Lab |
| 📌 | Resumo |

Emoji só nesses papéis. Não usar emoji decorativo em título comum, em bullet ou no meio de frase.

---

## Diagramas Mermaid

`pymdownx.superfences` está configurado com fence customizado `mermaid` (`mkdocs.yml:90-94`).

### Tipos permitidos

Ver `10-tooling.md` para a lista verificada contra o build. Regra geral: usar apenas tipos estáveis do Mermaid.

`flowchart`, `sequenceDiagram` e `classDiagram` cobrem quase tudo que esta disciplina precisa. Tipos marcados como `-beta` pelo próprio Mermaid não devem ser usados em material publicado — a sintaxe muda entre versões e a CI não fixa versão do zensical.

### Direção da seta

**Em diagrama de dependência, `A --> B` significa: A depende de B.** Sempre. É a mesma convenção do grafo oficial de `05-domain.md`, e dela derivam todos os cálculos de $C_a$ e $C_e$ da disciplina.

Todo diagrama de dependência declara a convenção na legenda. Uma linha basta:

> Leitura das setas: `A --> B` significa que A depende de B.

Isso não é preciosismo. O material publicado usou os dois sentidos em aulas diferentes — a Aula 3 desenhava `Catalogo --> Checkout` com o rótulo "contrato de consulta", enquanto o código mostrava `Checkout` dependendo de `Catalogo`, e a Aula 7 contava setas de entrada como fan-in. Em uma disciplina cujo tema é direção de dependência, seta ambígua invalida o raciocínio inteiro.

Se a seta representar **fluxo** — de dados, de mensagem, de evento — e não dependência, isso precisa estar no rótulo e na legenda. Fluxo e dependência frequentemente apontam para lados opostos: `Checkout` depende de `Pagamentos`, mas a resposta da cobrança flui de `Pagamentos` para `Checkout`.

### Cor

**Proibido `fill:` e `color:` com valor hexadecimal fixo.**

O tema tem alternância claro/escuro (`mkdocs.yml:41-53`). Cor fixa que funciona no tema claro fica ilegível no escuro, e vice-versa. O Módulo 1 tem três ocorrências desse problema, catalogadas em `12-backlog.md`.

Para destacar um nó, em ordem de preferência:

1. **forma** — nó em formato diferente (`[[ ]]`, `(( ))`, `{ }`);
2. **rótulo** — texto que já indica o destaque;
3. **posição** — nó isolado ou no topo do fluxo;
4. `classDef` com `stroke-width`, sem cor de preenchimento.

Se cor for realmente indispensável, usar `classDef` com preenchimento transparente e apenas a borda colorida, testando nos dois temas antes de publicar.

### Acentuação

Rótulos de nó em Mermaid renderizam mal com acento em algumas versões. Preferir rótulos sem acento (`Catalogo`, `Promocoes`, `Logistica`) — é o que o Módulo 1 já faz, e é consistente.

No texto corrido, acentuação normal do português.

### Complexidade

Máximo de sete nós por diagrama. Acima disso, dividir em dois ou aceitar que o diagrama virou consulta e mover para uma seção recolhida.

---

## Fórmulas

`pymdownx.arithmatex` com `generic: true`, MathJax carregado em `mkdocs.yml:105-107`.

Bloco: `$$ ... $$`. Inline: `$...$`.

**Toda fórmula precisa vir acompanhada da leitura em linguagem natural.** A fórmula é a forma compacta; a frase é o que o aluno leva.

Ruim:

```
$$ I = \dfrac{C_e}{C_a + C_e} $$
```

Bom:

```
$$ I = \dfrac{C_e}{C_a + C_e} $$

Ou seja: a instabilidade é a fração das dependências de um componente que apontam para fora dele.
Se ele só depende dos outros e ninguém depende dele, o valor é 1.
```

Toda variável usada precisa ser definida no mesmo bloco.

---

## Código

- Sempre com linguagem no fence (` ```python `).
- `title=` quando o arquivo importar para o entendimento.
- `hl_lines=` para apontar exatamente onde está o problema — mais eficaz que descrever em prosa.
- Blocos de no máximo 25 linhas. Acima disso o aluno para de ler.
- Regras de conteúdo em `06-code-style.md`.

## Tabelas

Cabeçalho sempre. Alinhamento padrão. Máximo quatro colunas.

Tabela de trade-off é o formato mais valioso desta disciplina e deve ter estrutura fixa:

| Alternativa | O que resolve | O que custa | Quando não vale |
|---|---|---|---|

## O que evitar

- Emoji fora dos papéis definidos acima.
- Mais de quatro admonitions abertas na mesma aula.
- Diagrama sem pergunta que o motive.
- Cor hexadecimal fixa em Mermaid.
- Fórmula sem leitura em linguagem natural.
- Bloco de código com mais de 25 linhas.
- Negrito para ênfase genérica. Negrito marca termo técnico na primeira aparição, e só.
