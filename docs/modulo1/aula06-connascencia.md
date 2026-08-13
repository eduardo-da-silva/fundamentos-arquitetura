# Aula 6 — Connascência

## Objetivo da aula

Usar connascência como vocabulário de precisão para acoplamento: nomear exatamente que tipo de dependência liga duas partes, quão forte ela é, e decidir o que fazer com base nisso.

## Competências desenvolvidas

- classificar uma dependência entre as nove formas de connascência;
- avaliar força, localidade e grau, e usar os três juntos para priorizar;
- aplicar a heurística de fronteira: connascência forte fica dentro do componente;
- reduzir connascência com objeto nomeado, enumeração e orquestração explícita.

## Duas mudanças do mesmo tamanho

Semana passada o time do Orion fez duas alterações que, no planejamento, pareciam equivalentes. Ambas de "uma linha".

A primeira renomeou um campo: `valor_total` virou `total_bruto` no contrato entre `Checkout` e `Pagamentos`. Levou vinte minutos. O editor encontrou os quatro usos, os testes apontaram o quinto, e acabou.

A segunda inverteu duas chamadas: passou a reservar estoque antes de cobrar, em vez de depois. Levou três dias, gerou um incidente em produção e um pedido cobrado sem estoque reservado.

Nas duas o diagnóstico da Aula 5 é o mesmo: "`Checkout` e `Pagamentos` estão acoplados". A palavra "acoplado" descreveu igualmente bem uma mudança de vinte minutos e uma de três dias.

**Isso significa que "acoplamento" é vocabulário grosso demais para decidir.** Precisamos separar dependências que custam caro das que custam barato — antes de mexer nelas, e não depois.

## Desenvolvimento conceitual

### A ideia

Duas partes de um sistema têm **connascência** quando uma mudança em uma exige mudança na outra para que o comportamento continue correto.

O termo é de Meilir Page-Jones, e a contribuição dele não foi perceber que dependências existem — todo mundo já sabia. Foi propor que elas se **classificam**, e que a classificação prevê o custo.

### Três eixos, antes das nove formas

A classificação sozinha não decide nada. Dizer "isto é connascência de posição" é como dizer "isto é acoplado": correto e inútil. O que decide é o cruzamento de três eixos.

**Força** — quão difícil é detectar e corrigir. Uma connascência forte não é detectável por leitura rápida nem por ferramenta; ela quebra em runtime, longe do ponto da mudança.

**Localidade** — quão distantes estão as partes ligadas. Mesma função, mesma classe, mesmo módulo, mesmo componente, componentes diferentes, sistemas diferentes, organizações diferentes.

**Grau** — quantas partes precisam mudar juntas. Duas ou duzentas.

A regra prática que amarra os três:

!!! important "A heurística que vale a aula inteira"

    **Connascência forte é aceitável quando a localidade é pequena. Connascência que atravessa fronteira de componente precisa ser fraca.**

    Duas funções vizinhas dentro do mesmo módulo podem compartilhar um algoritmo: quem mexer numa vê a outra. As mesmas duas funções em componentes diferentes, mantidos por times diferentes, são uma bomba-relógio.

    Corolário: aumentar a localidade — trazer as partes para perto — é uma forma legítima de resolver, e frequentemente mais barata que enfraquecer a connascência.

Grau alto multiplica o problema dos outros dois. Uma connascência fraca com grau 200 pode custar mais que uma forte com grau 2.

### As nove formas, em ordem de força

Esta ordem é o núcleo da ferramenta. Ela é o que permite dizer "esta dependência é pior que aquela" com algo mais que intuição.

```
        mais fraca                                              mais forte
   CoN ──> CoT ──> CoM ──> CoP ──> CoA ──> CoE ──> CoTiming ──> CoV ──> CoI
   └──────────── estáticas ────────────┘  └─────────── dinâmicas ──────────┘
```

**Estáticas** são visíveis lendo o código. **Dinâmicas** só se manifestam em execução — e é por isso que todas as dinâmicas são mais fortes que todas as estáticas: nenhuma ferramenta de análise as encontra, e nenhum leitor atento as detecta com confiança.

### As cinco estáticas

**1. Connascência de Nome (CoN)** — partes concordam sobre um nome.

```python
# Contrato implicito: a chave chama-se "status".
def registrar(pedido: dict) -> None:
    print(pedido["status"])

registrar({"status": "confirmado"})
```

A mais fraca, e a mais comum. Renomear é mecânico, e ferramentas ajudam. Foi a mudança de vinte minutos do começo da aula.

**2. Connascência de Tipo (CoT)** — partes concordam sobre um tipo.

```python
# mini_orion/pagamentos.py — publica o contrato
class ResultadoCobranca(Enum):
    APROVADA = "aprovada"
    RECUSADA_PELO_EMISSOR = "recusada_pelo_emissor"

# mini_orion/checkout.py — consome
if resultado is not ResultadoCobranca.APROVADA:
    return resultado.value
```

Os dois componentes precisam concordar que o retorno é um `ResultadoCobranca`. Se `Pagamentos` passar a devolver `str`, o `Checkout` quebra — mesmo que nenhum nome tenha mudado.

Repare que este é um exemplo de acordo **entre dois componentes**, e não de um valor com tipo errado dentro de uma função. Tipagem dinâmica é outro assunto: connascência de tipo existe igual em Java, onde o compilador pega o erro. O que muda é quando você descobre, não se a dependência existe.

**3. Connascência de Significado (CoM)** — partes concordam sobre o que um valor significa.

```python
STATUS_APROVADO = 1
STATUS_RECUSADO = 2

def notificar(status: int) -> str:
    if status == 1:                    # por que 1?
        return "email de sucesso"
    return "email de falha"
```

O `1` não carrega o significado; ele está na cabeça de quem escreveu. Se alguém decidir que `1` passa a significar "pendente", nada quebra — o sistema continua rodando e passa a mandar o e-mail errado.

Este é o primeiro salto de gravidade: **CoM falha silenciosamente**. CoN e CoT quebram alto.

**4. Connascência de Posição (CoP)** — partes concordam sobre a ordem dos dados.

```python
def registrar_entrega(dados: tuple[str, str, str]) -> str:
    cliente, endereco, cep = dados
    return f"Entrega para {cliente} em {endereco}"

registrar_entrega(("Rua A, 100", "Joao", "89000-000"))   # invertido
```

Passa no type checker. Não levanta exceção. Entrega no endereço errado.

**5. Connascência de Algoritmo (CoA)** — partes precisam replicar o mesmo algoritmo.

```python
def gerar_hash(valor: str) -> str:
    return valor[::-1] + "-chk"        # algoritmo didatico, nao criptografico

def validar_hash(valor: str, recebido: str) -> bool:
    return valor[::-1] + "-chk" == recebido    # precisa ser identico
```

Melhorar o algoritmo em um lado sem o outro quebra tudo. E quem faz a melhoria costuma não saber que o outro lado existe — especialmente se estiver em outro componente.

### As quatro dinâmicas

**6. Connascência de Execução (CoE)** — a ordem das chamadas importa.

```python
# O fluxo correto: cobrar, depois reservar.
pagamentos.cobrar(pedido_id)
estoque.reservar(pedido_id)
```

Inverter roda, não levanta exceção e não falha em teste. Falha quando o estoque acaba entre as duas chamadas: o cliente recebe reserva de um produto que não será cobrado, ou é cobrado por um que não será reservado.

Foi a mudança de três dias do começo da aula. Nenhuma linha de código "quebrou" — o comportamento de negócio é que ficou errado, e só em parte dos casos.

**7. Connascência de Tempo (CoTiming)** — o momento ou a duração importam.

```python
class Antifraude:
    def validar(self, pedido_id: str) -> bool:
        time.sleep(2)            # ate 2s em condicoes normais
        return True

# Checkout tem timeout de 3s. Funciona — ate o antifraude ficar
# 1s mais lento em dia de campanha.
```

A dependência é sobre um tempo que ninguém escreveu em lugar nenhum. Aparece em produção, sob carga, e some quando você tenta reproduzir.

**8. Connascência de Valor (CoV)** — valores em partes diferentes precisam ser consistentes entre si.

```python
# Pedidos: total gravado no fechamento
pedido.total = 380.00

# Pagamentos: valor efetivamente cobrado
cobranca.valor = 380.00

# Se um cupom for aplicado depois em apenas um dos lados,
# os dois numeros divergem e nada acusa.
```

Não é o mesmo valor passado adiante — são **dois valores que precisam permanecer iguais** em lugares diferentes. É o que torna transação distribuída difícil, e voltaremos a isso no Módulo 3.

**9. Connascência de Identidade (CoI)** — partes precisam operar sobre a *mesma* entidade, não sobre entidades iguais.

```python
pedido_a = repositorio.buscar("ORI-00001")
pedido_b = repositorio.buscar("ORI-00001")   # outra instancia

pagamentos.aprovar(pedido_a)     # marca pedido_a como pago
expedicao.expedir(pedido_b)      # pedido_b ainda diz "criado"
```

A mais forte de todas. Os dois objetos são iguais em conteúdo e diferentes em identidade, e o sistema toma decisões conflitantes sobre o mesmo pedido de negócio.

### Reduzindo

Três movimentos resolvem a maior parte dos casos, e todos aparecem no Mini-Orion.

**Objeto nomeado elimina CoP.**

```python
@dataclass(frozen=True)
class PedidoCobranca:
    valor: float
    cartao: str
    parcelas: int = 1
```

Inverter dois campos deixa de ser possível: eles têm nome.

**Enumeração elimina CoM.**

```python
class ResultadoCobranca(Enum):
    APROVADA = "aprovada"
    ACIMA_DO_LIMITE = "acima_do_limite"

    @property
    def deve_tentar_outro_provedor(self) -> bool:
        return self is ResultadoCobranca.ACIMA_DO_LIMITE
```

O significado passa a morar no tipo. E a `property` faz mais: leva a **regra** para junto do significado, em vez de deixá-la espalhada em `if` pelos chamadores — o que reduz o grau de uma tacada.

**Orquestração explícita reduz o grau da CoE.**

Quando a ordem está implícita, espalhada entre quem chama o quê, o grau é o número de chamadores. Concentrando a sequência em um único lugar, o grau cai para um.

```python
class ServicoCheckout:
    def fechar_pedido(self, carrinho, cliente) -> str:
        resultado = self._gateway.cobrar(cobranca)
        if resultado is not ResultadoCobranca.APROVADA:
            return resultado.value
        pedido = self._pedidos.emitir(carrinho, cliente, cobranca.valor)
        self._notificador.publicar(evento_de_confirmacao(pedido))
        return "confirmado"
```

A ordem continua existindo — CoE não desaparece, porque a regra de negócio é sequencial de verdade. O que muda é que ela está **em um lugar só, declarada e auditável**, em vez de emergir da soma de chamadas espalhadas.

!!! tip "Nem toda connascência deve ser eliminada"

    O objetivo nunca é zerar. Um sistema sem connascência nenhuma é um sistema cujas partes não colaboram.

    O objetivo é que **a força seja proporcional à proximidade**. Connascência forte dentro de um componente é design normal. A mesma connascência atravessando fronteira, entre times diferentes, é dívida.

## No Mini-Orion

Compare `02-fronteiras/` e `03-governado/` em `code/mini-orion/`. A passagem entre os dois é exatamente esta aula:

| Antes | Depois | O que caiu |
|---|---|---|
| `cobrar(valor, cartao)` posicional | `PedidoCobranca` nomeado | CoP eliminada |
| retorno `bool` | `ResultadoCobranca` | CoM eliminada; quatro motivos de falha distinguíveis |
| `if` de contingência no checkout | `deve_tentar_outro_provedor` no `Enum` | grau reduzido |

O teste `test_pedido_de_cobranca_e_imutavel_e_nomeado` existe para impedir a volta. Rode `pytest` no `03-governado` e depois desfaça uma das mudanças de propósito.

## Exercícios

1. **Classifique.** Que forma de connascência predomina em cada trecho?

    ```python
    # A
    def aplicar_taxa(total: float, taxa: float) -> float:
        return total + taxa

    # B
    STATUS_OK = 1
    def resposta_api() -> int:
        return STATUS_OK

    # C
    def salvar_entrega(dados: tuple[str, str, str]) -> None:
        cliente, endereco, cep = dados
    ```

    ??? note "Resposta comentada"

        **A — CoN e CoT.** Quem chama precisa acertar os nomes dos parâmetros (se usar argumento nomeado) e os tipos. É o par mais fraco: qualquer erro aparece cedo e alto.

        **B — CoM.** O `1` não diz o que significa. Quem consumir `resposta_api()` precisa saber, por fora do código, que `1` quer dizer sucesso.

        **C — CoP.** A tupla depende de ordem. Trocar cliente e endereço não gera erro nenhum — gera entrega errada.

        Em ordem de gravidade: C, B, A. E note que a gravidade é inversa à facilidade de perceber lendo o código, o que é justamente o problema.

2. **Compare.** Duas equipes duplicaram o mesmo cálculo de frete. No caso X, as duas cópias estão no mesmo módulo, vinte linhas uma da outra. No caso Y, estão em `Checkout` e `Logistica`, mantidos por times diferentes. É a mesma connascência? Merece a mesma prioridade?

    ??? note "Resposta comentada"

        Mesma **forma** (CoA) e mesma **força**. O que muda é a **localidade**, e isso muda tudo.

        Em X, quem alterar uma das cópias muito provavelmente vê a outra na mesma tela. O risco é baixo e o custo de arrumar também — dá para deixar para depois.

        Em Y, o time do `Checkout` pode passar meses sem saber que existe uma segunda implementação. Quando as tabelas de frete divergirem, o cliente vê um preço na vitrine e outro na fatura, e ninguém vai suspeitar de duplicação de algoritmo.

        Prioridade: Y, com folga. **É por isso que classificar sem avaliar localidade não produz decisão** — a forma sozinha teria dado o mesmo veredito para os dois casos.

3. **Reduza.** Reescreva eliminando a connascência mais forte:

    ```python
    def emitir_nota(dados: tuple[str, float, int]) -> str:
        cliente, valor, tipo = dados
        if tipo == 2:
            return f"NFS-e para {cliente}: {valor}"
        return f"NF-e para {cliente}: {valor}"
    ```

    ??? note "Resposta comentada"

        Há duas: CoP na tupla e CoM no `tipo == 2`. A CoP é mais forte, então vai primeiro — mas resolver as duas custa o mesmo esforço:

        ```python
        class TipoNota(Enum):
            PRODUTO = "nf-e"
            SERVICO = "nfs-e"

        @dataclass(frozen=True)
        class DadosNota:
            cliente: str
            valor: float
            tipo: TipoNota

        def emitir_nota(dados: DadosNota) -> str:
            return f"{dados.tipo.value.upper()} para {dados.cliente}: {dados.valor}"
        ```

        Note que o `if` desapareceu junto. Isso é comum: quando o significado sai do número e vai para o tipo, a ramificação que existia só para interpretar o número perde a razão de existir.

4. **Julgue.** No Orion, `Pagamentos` e `Pedidos` mantêm cada um o valor total do pedido (CoV, grau 2, atravessando componentes). Eliminar isso significaria um dos dois consultar o outro toda vez — criando dependência nova e um ponto de falha a mais. Vale?

    Não há resposta única. Uma boa resposta reconhece que **eliminar a connascência aqui cria um problema diferente, não menor**, e escolhe com base no que o negócio tolera: divergência silenciosa de valor ou indisponibilidade acoplada. Uma resposta que só diz "duplicação é ruim, eliminar" não considerou o custo do outro lado.

## Atividade em grupo

Sobre o recorte do seu Orion Evolution Lab:

1. Encontrem **cinco** connascências que atravessam fronteira de componente.
2. Para cada uma, registrem: forma, força, localidade e grau. Os quatro campos são obrigatórios.
3. Ordenem por risco — que não é a mesma ordem que a de força, porque localidade e grau entram na conta.
4. Escolham **duas** para reduzir e descrevam o movimento (objeto nomeado, enumeração, orquestração, aproximação).
5. Para uma delas, digam por que **não** vale a pena eliminar.

O item 5 é obrigatório e costuma ser o mais difícil. Sempre existe uma connascência cuja eliminação custa mais do que entrega.

Formato e critérios em [Orion Evolution Lab](../orion/index.md).

## Resumo

"Acoplado" descrevia igualmente uma mudança de vinte minutos e uma de três dias. Connascência resolve isso: nove formas em ordem de força, com uma linha divisória clara entre as que se enxergam no código e as que só aparecem em execução.

Mas a forma sozinha não decide — o exercício 2 mostrou o mesmo CoA merecendo prioridades opostas conforme a localidade. Força, localidade e grau **precisam ser lidos juntos**, e a heurística que sai daí é uma só: connascência forte pode ficar dentro do componente, nunca atravessando a fronteira.

Isso encerra o diagnóstico qualitativo do módulo. Sabemos nomear com precisão o que liga as partes do Orion e quanto isso custa. O que ainda não sabemos é **comparar**: quando dois componentes disputam o mesmo trimestre de trabalho, três pessoas experientes classificam as connascências igual e priorizam diferente. Falta evidência que não dependa de quem está olhando.

## Principais conceitos

- connascência;
- as nove formas: CoN, CoT, CoM, CoP, CoA, CoE, CoTiming, CoV, CoI;
- ordem canônica de força;
- estática versus dinâmica;
- força, localidade e grau;
- heurística de fronteira.

## Leitura complementar

- Richards, Mark; Ford, Neal. *Fundamentals of Software Architecture*. Cap. 3 — Modularity, seção de connascência.
- Page-Jones, Meilir. *What Every Programmer Should Know About Object-Oriented Design*. Cap. 6 — Connascence.

## Referências

- RICHARDS, Mark; FORD, Neal. *Fundamentals of Software Architecture: An Engineering Approach*. O'Reilly, 2020.
- PAGE-JONES, Meilir. *What Every Programmer Should Know About Object-Oriented Design*. Dorset House, 1995.
