# Estrutura da aula

## Objetivo deste documento

Definir o esqueleto de uma aula garantindo consistência **sem** produzir clones.

O material do Módulo 1 errou por excesso: os oito capítulos têm exatamente os mesmos títulos de seção, na mesma ordem, com as mesmas frases de ligação. O resultado lê como formulário preenchido. Consistência é o leitor reconhecer onde está; uniformidade total é o leitor parar de ler porque já sabe o que vem.

Este documento existe para produzir a primeira e evitar a segunda.

---

## Seções obrigatórias

Toda aula precisa ter estas seis coisas. **Os títulos não precisam ser os mesmos entre aulas** — a função é que é obrigatória.

### 1. Objetivo e competências

Curto. O que o aluno vai conseguir fazer que não conseguia antes. Verbo de ação, não "compreender".

### 2. Sintoma

A situação concreta no Orion que dispara a aula. Ver `01-pedagogy.md`.

Esta seção varia muito de aula para aula, e deve variar: um incidente se escreve diferente de um prazo estourado, que se escreve diferente de uma métrica que degradou.

### 3. Desenvolvimento

O conteúdo conceitual, sempre amarrado ao sintoma. Sem definição solta.

### 4. Decisão sobre o Orion

O ponto em que a aula produz alguma coisa: uma fronteira definida, um ADR, uma métrica medida, uma refatoração no Mini-Orion.

Uma aula que passa por aqui sem produzir artefato não cumpriu sua função. Ver `05-domain.md` e `08-lesson-roadmap.md` para o que cada aula deve produzir.

### 5. Trabalho do aluno

Exercícios e/ou atividade do Orion Evolution Lab. Ver `01-pedagogy.md` para a regra do gabarito e `09-assessment.md` para critérios.

### 6. Fechamento e ponte

O que ficou decidido e qual pergunta a próxima aula abre.

A ponte precisa ser uma pergunta real, não um anúncio de sumário. "Na Aula 5 veremos connascência" é sumário. "Sabemos que Checkout e Pagamentos estão acoplados, mas 'acoplado' descreve coisas muito diferentes — trocar o nome de um campo e depender da ordem de duas chamadas não são o mesmo problema. Falta vocabulário" é ponte.

---

## Seções opcionais

Usar quando servirem, não por preencher formulário:

- diagrama de componentes ou de sequência;
- tabela comparando alternativas;
- nota histórica sobre a origem do conceito;
- erros comuns;
- leitura complementar;
- referências (obrigatória apenas quando a aula citar fonte específica).

---

## Limite de repetição

**Nenhum bloco de texto pode aparecer literalmente igual em mais de duas aulas.**

Isso vale para frases de transição, aberturas de seção e rótulos de subseção. Se uma frase serve para qualquer aula, ela não está informando nada sobre esta aula.

Formulações hoje repetidas no Módulo 1 e que não devem ser reproduzidas em material novo:

- `### Trilhas permanentes de exemplo nesta aula` — 8 de 8 capítulos, com duas linhas de bullet que só reafirmam o que as trilhas são. Se a aula usa as trilhas, isso aparece no corpo da aula, não numa seção declaratória.
- `### Uma possível resolução comentada do professor` — 8 de 8.
- `Apresentação do diagrama:` seguido de `Interpretação:` — em praticamente todo diagrama. Um diagrama que precisa de uma frase padronizada antes e outra depois provavelmente não está no lugar certo.
- `### No início — conexão com a aula anterior` — 5 de 8, com texto quase idêntico.
- `### No final — conexão com a próxima aula` — 8 de 8.

Regra prática: ao terminar uma aula, abrir a anterior lado a lado. Se os títulos de seção coincidirem quase todos, reescrever.

---

## Ordem

A ordem lógica (sintoma antes de conceito, conceito antes de decisão, decisão antes de exercício) é obrigatória.

A granularidade e os títulos não são. Uma aula de oficina não tem a mesma cara de uma aula conceitual, e forçar o mesmo esqueleto nas duas prejudica as duas.

---

## Proporção

Alvo aproximado, por aula:

| Elemento | Proporção |
|---|---|
| Texto argumentativo | 50% |
| Diagrama, tabela de decisão, ADR | 25% |
| Código | 25% |

Diferente de POO-II (60% texto / 40% código) porque aqui o diagrama e a tabela de trade-off carregam parte do argumento.

Consequência: uma aula desta disciplina pode ser boa com pouco código. Não pode ser boa sem nada decidido.

---

## Tamanho

Entre 200 e 320 linhas de Markdown para uma aula conceitual. Acima disso, ou a aula está cobrindo dois assuntos, ou está diluída.

Aula de oficina pode passar, desde que o excedente seja material de apoio para os grupos, não exposição.

---

## Diagramas

- Um diagrama por ideia. Diagrama que mostra tudo não mostra nada.
- Todo diagrama precisa responder a uma pergunta que o texto fez. Se não houver a pergunta, não há o diagrama.
- Todo diagrama precisa dizer o que **não** está representado ali. Diagrama arquitetural sempre omite; omitir sem avisar é o defeito clássico.
- Regras técnicas (tipos permitidos, cor, tema) em `03-visual-language.md`.

## Tabelas

Boas para comparar alternativas, listar trade-offs e resumir responsabilidades. É o formato mais adequado ao conteúdo desta disciplina — use mais do que parece necessário.

Evitar tabela com mais de seis linhas ou quatro colunas; acima disso vira consulta, não leitura.

## Listas

Só quando os itens forem realmente paralelos e independentes. Argumento arquitetural raramente é paralelo e independente — quase sempre um ponto depende do anterior, e isso se escreve em prosa.

Uma aula que é majoritariamente bullet point não está argumentando.
