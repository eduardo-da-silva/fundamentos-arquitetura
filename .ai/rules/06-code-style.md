# Código

## Duas categorias, regras diferentes

O material do Módulo 1 tratou todo código igual, e o resultado é que o `Checkout` da Aula 1, o da Aula 3 e o `CoreService` da Aula 8 são três sistemas incompatíveis. O aluno não consegue rastrear nada.

A distinção abaixo resolve isso.

### Snippet ilustrativo

Existe para mostrar **um** ponto. Pode ser incompleto, pode não rodar isolado.

- 5 a 25 linhas;
- não precisa ser consistente com outras aulas;
- **precisa declarar que é ilustrativo** — via `title=` do bloco ou pela frase que o introduz;
- não usa nomes do Mini-Orion, para não sugerir continuidade que não existe. Use nomes genéricos (`ServicoA`, `ComponenteX`) ou nomes do recorte legado.

### Código do Mini-Orion

É um sistema. Vive em `code/mini-orion/aulaNN/`, roda, tem teste.

- nomes de classe e método **estáveis** ao longo de todo o curso;
- cada aula parte do estado da aula anterior;
- toda mudança de nome propaga para as aulas seguintes, não só para a atual;
- o que aparece na página é recorte do arquivo real, nunca reescrita para a página.

Se a aula mostra código do Mini-Orion, o arquivo correspondente existe em `code/`. Sem exceção.

---

## Python

Versão 3.12 ou superior.

- **Type hints obrigatórios** em assinatura pública. Ajudam o argumento arquitetural: contrato explícito é visível no tipo.
- Nomes do domínio, em português, iguais aos de `05-domain.md`. Nunca `obj`, `tmp`, `data`, `x`.
- `Enum` para estado e categoria; nunca inteiro ou string mágica.
- Exceção específica, nunca `Exception` genérica.
- `@dataclass` para estrutura de dados; classe comum quando houver comportamento.
- `Protocol` para contrato entre componentes — é o que torna a fronteira visível sem herança.
- Métodos de 5 a 20 linhas.
- Sem framework, sem ORM, sem I/O real. O Mini-Orion demonstra estrutura, não infraestrutura.

## Comentário

Comentário explica **decisão**, não mecânica.

Ruim:

```python
# incrementa o contador
contador += 1
```

Bom:

```python
# Notificação fora do caminho crítico: se falhar, o pedido continua válido.
self._fila_notificacao.publicar(evento)
```

Em bloco que demonstra problema, o comentário aponta o problema:

```python
# Acoplado ao provedor concreto: trocar de gateway exige mexer aqui.
resposta = gateway_x_cobrar(total, cartao)
```

---

## Contagem para métricas

A aula de métricas pede $A = N_a / N_c$. Em Java a conta é direta; em Python, não — e sem convenção o exercício não tem resposta verificável. O Módulo 1 pede o cálculo sem definir a convenção.

**Convenção oficial da disciplina.**

Conta como **elemento** ($N_c$): toda classe definida no componente, incluindo `Protocol`, `ABC`, `Enum` e `dataclass`.

Não conta: função de módulo, variável, constante, `TypeAlias`, classe aninhada usada só como detalhe interno.

Conta como **abstrato** ($N_a$):

| Elemento | Abstrato? |
|---|---|
| `class X(Protocol)` | sim |
| `class X(ABC)` com pelo menos um `@abstractmethod` | sim |
| `class X(ABC)` sem nenhum `@abstractmethod` | não |
| Classe base concreta, ainda que herdada | não |
| `Enum` | não |
| `@dataclass` | não |
| `TypedDict` | não |

Justificativa da regra do meio: `ABC` sem método abstrato é concreta na prática — é convenção do autor, não contrato imposto. A métrica mede contrato.

Esta convenção é decisão desta disciplina, não do livro-base. Diga isso ao aluno quando ela aparecer: uma métrica sempre depende de uma decisão de contagem, e conhecer a decisão faz parte de saber ler a métrica.

---

## Ferramentas

A aula de métricas deve usar ferramenta real sobre código real pelo menos uma vez — cálculo manual sobre número inventado ensina aritmética, não diagnóstico.

Sugeridas, sobre o Mini-Orion:

| Ferramenta | Para |
|---|---|
| `pydeps` | grafo de dependência entre módulos |
| `import-linter` | contratos de dependência que falham no CI |
| `radon` | complexidade, como sinal complementar |
| `pytest` | evidência de que a fronteira melhorou a testabilidade |

`import-linter` é a mais valiosa: transforma uma decisão arquitetural em teste executável. É a porta de entrada natural para fitness functions.

Ver `10-tooling.md` antes de adicionar dependência ao repositório.

---

## Testes

Todo estado do Mini-Orion tem teste que passa. `pytest`, em `code/mini-orion/aulaNN/tests/`.

O teste tem papel argumentativo aqui: quando uma fronteira é introduzida, o teste que passou a ser possível **é** a evidência. Mostrar o teste que antes exigia infraestrutura e agora não exige mais vale mais que qualquer parágrafo sobre testabilidade.

---

## O que evitar

- Código sem propósito argumentativo, só para ter código na página.
- Bloco acima de 25 linhas.
- Nome do Mini-Orion em snippet ilustrativo.
- Mais de três conceitos novos no mesmo bloco.
- "Antes" e "depois" que não sejam comparáveis. A Aula 1 tem um caso disso: o "antes" faz cálculo, cobrança e notificação; o "depois" só cobra. A notificação sumiu, e a comparação deixa de demonstrar desacoplamento — demonstra remoção de escopo. Se o "depois" não faz tudo que o "antes" fazia, a diferença precisa ser explicada.
- Abstração introduzida sem que a aula tenha mostrado o problema que ela resolve.
