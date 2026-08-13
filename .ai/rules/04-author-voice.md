# Voz do autor

## Quem escreve

Um arquiteto experiente conversando com alguém que já sabe programar e está começando a decidir.

Não é professor recitando ementa. Não é consultor vendendo prática. É alguém que já tomou essas decisões, já errou algumas, e está mostrando como pensa.

A diferença aparece no verbo. Quem recita afirma. Quem decidiu, pondera:

> Vamos separar notificação do fluxo de checkout.

versus

> Vamos tirar a notificação do caminho crítico do checkout. Isso resolve o bloqueio no pico, mas cria uma janela em que o pedido existe e o cliente ainda não sabe. Numa loja de nicho isso seria inaceitável; num marketplace com 8x de pico em campanha, é o menor dos custos.

## Pessoa

Primeira do plural para o raciocínio conjunto: "vamos analisar", "percebemos que", "nossa decisão".

Segunda do singular para o trabalho do aluno: "analise o recorte", "justifique sua escolha".

Nunca primeira do singular. O autor não é personagem.

## Tempo

Presente. O Orion está acontecendo agora.

## Tom

Direto, técnico, sem cerimônia. Frases curtas para afirmações; frases longas quando o raciocínio realmente tem dependências.

Pode admitir incerteza — deve, inclusive. "Não há consenso sobre isso" e "essa escolha depende de coisas que não sabemos aqui" são frases honestas e ensinam mais que uma certeza fabricada.

---

## Expressões preferidas

- "Vamos analisar o que está acontecendo aqui."
- "Perceba que..."
- "Isso funciona, mas cobra um preço."
- "A pergunta certa não é X, é Y."
- "Aqui há mais de uma resposta defensável."
- "Um time competente escolheria diferente, e teria razão se o contexto fosse outro."
- "O que observaríamos se essa decisão estivesse errada?"
- "Essa decisão envelhece bem? Sob quais condições ela deixa de valer?"

## Expressões proibidas

- "Obviamente", "claramente", "evidentemente" — se fosse óbvio, não estaria na aula.
- "Como todos sabem", "é sabido que" — exclui quem não sabe, que é o público.
- "Basta", "simplesmente", "é só" — nada em arquitetura é só.
- "A melhor prática é" — melhor para quem, sob que restrição.
- "Sempre", "nunca", "em qualquer caso" — quando aplicados a recomendação arquitetural.
- "O correto é" — existe adequado ao contexto, não correto.
- "Nesta aula, aprenderemos..." — abertura de sumário, não de aula. Ver `01-pedagogy.md`.
- "É importante ressaltar que" — se é importante, ressalte; não anuncie que vai ressaltar.

---

## Anti-boilerplate

Esta seção existe porque o Módulo 1 foi escrito com estrutura tão uniforme que o texto lê como preenchimento de formulário.

### O princípio

**Seção que não muda de aula para aula não está informando nada sobre a aula.**

Se uma frase pode ser copiada para qualquer capítulo sem ficar errada, ela não deveria estar em nenhum.

### Frases hoje repetidas, a não reproduzir

| Frase | Ocorrências no Módulo 1 |
|---|---|
| `### Trilhas permanentes de exemplo nesta aula` | 8 de 8 |
| `### Uma possível resolução comentada do professor` | 8 de 8 |
| `### No final — conexão com a próxima aula` | 8 de 8 |
| `Apresentação do diagrama:` | quase todo diagrama |
| `Interpretação:` / `Interpretação do diagrama:` | quase todo diagrama |
| `### No início — conexão com a aula anterior` | 5 de 8, texto quase idêntico |

O problema não é o rótulo em si. É que o conteúdo abaixo dele também é intercambiável — dois bullets que reafirmam o que as trilhas são, em vez de dizer o que a trilha fez **nesta** aula.

### Como corrigir

Não substitua por outro rótulo padronizado. Elimine a moldura e escreva a coisa:

Antes:

```markdown
### Trilhas permanentes de exemplo nesta aula

- **Exemplo do professor (Mini-Orion Checkout)**: detectar connascências em um fluxo e refatorar.
- **Projeto dos alunos (Orion Evolution Lab)**: mapear connascências entre componentes.
```

Depois — no corpo da aula, onde a trilha efetivamente age:

```markdown
No Mini-Orion, o `ServicoCheckout` monta o payload de cobrança como uma tupla posicional.
Vamos ver o que acontece quando o gateway inverte dois campos na v2 da API.
```

### Teste prático

Ao terminar uma aula, abra a anterior ao lado e compare os títulos de `##` e `###`. Se mais de metade coincidir, reescreva.

Um segundo teste: apague o título da aula e leia o texto. Se não der para saber qual aula é pelo conteúdo das primeiras vinte linhas, o texto está genérico.

---

## Perguntas

O autor pergunta muito, mas com propósito.

Pergunta boa força uma escolha ou expõe uma tensão:

> Quem deveria saber que o pagamento falhou: o checkout, o pedido, ou os dois?

Pergunta ruim é retórica disfarçada, com resposta embutida:

> Não seria melhor desacoplar esses componentes?

Se a resposta está na pergunta, é afirmação. Escreva como afirmação.

---

## Referência ao aluno

O aluno é tratado como alguém competente que ainda não viu certas coisas — não como iniciante.

Evitar: "não se preocupe", "é mais simples do que parece", "com o tempo você entenderá".

Preferir: "isso costuma pegar quem vem de POO, porque lá o critério é outro".

A primeira formulação tranquiliza e não informa. A segunda diz de onde vem a dificuldade.
