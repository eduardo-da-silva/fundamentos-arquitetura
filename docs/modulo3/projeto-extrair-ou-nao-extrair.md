# Projeto das Aulas 16 e 17 — Extrair ou não extrair

!!! danger "Entrega"

    Trabalho **individual ou em dupla**. Entregar antes da Aula 18, e apresentar em sala no início dela (ver o fim desta página).

As Aulas 16 e 17 respondem a duas perguntas sobre separar uma parte de um sistema em um serviço próprio. A primeira é **o que a rede custa**: a chamada remota tem desfechos que a local não tem. A segunda é **o que se compra** com a separação: que forma de implantação cabe, e quando mais artefatos trazem independência de verdade. Este projeto junta as duas perguntas numa só decisão: **extrair ou não extrair** um componente do seu cenário.

## O que o projeto pede, em resumo

| Parte | O que você faz | O que entrega |
|---|---|---|
| 0. Cenário | Escolhe o sistema e o componente candidato | descrição de meia página |
| 1. Custo da rede | Roda e altera o `ensaio.py` | tabela, previsão e interpretação |
| 2. Forma de implantação | Altera o `quantum.py` e escreve testes | código, testes passando e tabela |
| 3. Leitura | Lê um de quatro artigos e responde a perguntas | respostas curtas |
| 4. Decisão | Escreve um ADR com o guia "Como ler o resultado" | ADR de uma página |

## Por que mexer no código

Nas duas aulas, o código foi usado para **ler** resultados. Aqui você o altera, por dois motivos.

**O `ensaio.py` guarda hipóteses.** A taxa de falha de 2%, a mediana de 20 ms e o percentil 99 de 400 ms não foram medidos no Orion: são hipóteses de trabalho. Se você trocar os valores e as conclusões da Aula 16 sobreviverem, elas são estruturais; se mudarem, dependiam do número escolhido. A única forma de saber é rodar de novo.

**O `quantum.py` guarda estrutura.** A tabela da Aula 17 foi calculada sobre o grafo do Orion, com os componentes e as arestas escritos num arquivo. Ao trocar o grafo, você separa o que a conta faz (contar artefatos, arestas remotas e *quanta*) do que ela herdou do Orion (nomes, o componente que coordena o fluxo, a fila para `Notificacoes`). E, ao escrever uma forma e o teste que a fixa, você precisa decidir antes o que esperava, e só então ver se o código concorda.

## Parte 0 — Escolha o cenário

Você tem duas opções. Em ambas, **declare de onde vêm os dados** do seu cenário (do código real, de um diagrama público, ou inventados por você).

### Opção A — O Orion (padrão)

Escolha **um componente** do Orion como candidato à extração. Evite `Pagamentos`: a Aula 16 e a Aula 17 já o analisaram, e a sua conta ficaria sem novidade. Alguns candidatos plausíveis, cada um com um perfil diferente:

| Candidato | O que ele tem de interessante |
|---|---|
| `Catalogo` | muitos dependentes: quatro componentes o chamam |
| `Notificacoes` | recebe de quatro, e quase tudo nele pode ser assíncrono |
| `Logistica` | cadeia no meio do fluxo de pedido |
| `Promocoes` | muda com frequência (regras de campanha) e é opcional no fechamento |

O grafo, os módulos e os valores de partida estão no próprio `quantum.py`. Sua tarefa é justificar **um motivador de separação** (escala, cadência de release, isolamento de falha ou autonomia de time) para o candidato que escolher, ou dizer por que ele não existe.

### Opção B — Seu cenário, real ou hipotético

Use um sistema que você conhece (um estágio, um projeto da disciplina, um serviço público que você usa) ou invente um. Para o projeto funcionar, o cenário precisa ter:

- pelo menos **seis componentes** e **oito dependências** entre eles, escritas como pares `A depende de B`;
- um **fluxo principal** coordenado por um componente (o equivalente do `Checkout`), que depende de pelo menos três outros;
- uma operação com **efeito colateral que não pode se repetir** (cobrar, reservar, enviar, emitir), para a Parte 1;
- um **candidato à extração** com um motivador de separação plausível.

Exemplo hipotético, para você ver o formato (uma plataforma de venda de ingressos; não é para copiar, e sim para se inspirar):

```python
ARESTAS = [
    ("Portal", "Eventos"), ("Portal", "Venda"), ("Portal", "Conta"),
    ("Venda", "Eventos"), ("Venda", "Reserva"), ("Venda", "Pagamento"),
    ("Venda", "Conta"), ("Venda", "Fiscal"),
    ("Pagamento", "Aviso"), ("Fiscal", "Aviso"),
]
ORIGEM_DO_FLUXO = "Venda"   # coordena o fluxo medido
DESTINO_DA_FILA = "Aviso"   # recebe de dois e pode ficar atrás de uma fila
```

Se o seu cenário vier de um sistema real, **não precisa ser verdadeiro em todos os detalhes**. Precisa ser coerente e ter as origens declaradas.

## Preparação

O código está no repositório do Mini-Orion, na pasta `07-remoto`. Com Python 3.12 ou superior:

```bash
git clone https://github.com/eduardo-da-silva/fundamentos-arquitetura-code.git
cd fundamentos-arquitetura-code
python -m venv .venv && source .venv/bin/activate   # no Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cd 07-remoto
pytest        # tudo deve passar antes de você mexer em qualquer coisa
```

**Não edite os arquivos originais.** Você vai trabalhar em cópias (`meu_ensaio.py` e `meu_quantum.py`), para que os testes do Orion continuem valendo como referência.

## Parte 1 — O custo da rede (`ensaio.py`)

**Para que serve.** A Aula 16 mostrou, num cenário só, o que acontece quando uma operação que cobra passa a atravessar a rede. Agora você refaz o experimento com **os seus** valores e **uma política a mais**, para ver o que depende da hipótese e o que não depende.

**Qual script usar.** Há dois, e a escolha depende do seu cenário:

| Cenário | Script | O que você edita |
|---|---|---|
| Opção A (Orion) | `ensaio.py`, que executa o código real de `compra` e `pagamentos` | uma cópia, `meu_ensaio.py`, com seus parâmetros e a política nova |
| Opção B (o seu) | `ensaio_generico.py`, que não conhece o Orion | uma cópia, `meu_ensaio.py`, onde você troca o nome da operação e os três parâmetros da rede |

O `ensaio_generico.py` simula uma operação qualquer cujo efeito não pode se repetir (uma reserva, um envio, uma cobrança): o servidor conta quantas vezes executou cada pedido, e com chave ele guarda a resposta e não repete o efeito. Ele usa a mesma rede simulada do `ensaio.py`, mas não depende de nenhum módulo do Orion, e por isso serve a qualquer cenário. Se você escolheu reservar um assento, é a reserva que o script simula; não há substituta a justificar. Na Parte 1, diga em uma frase **o que a simulação deixa de representar** no seu cenário.

### 1.1 Rode a linha de base

```bash
python ensaio.py --varrer              # opção A
python ensaio_generico.py              # opção B
python ensaio_generico.py --semente 7  # opção B, outra rodada
```

Copie para o relatório a tabela das políticas (semente 42) e, na opção A, a varredura em dez sementes; na opção B, rode ao menos três sementes diferentes. Responda em até cinco linhas: **o que muda de uma semente para outra, e o que não muda?** Para cada resposta, aponte o número que a sustenta.

### 1.2 Troque as hipóteses pelas suas

Copie o arquivo e edite a cópia:

```bash
cp ensaio.py meu_ensaio.py            # opção A
cp ensaio_generico.py meu_ensaio.py   # opção B
```

**Opção B:** no começo de `meu_ensaio.py`, entre as linhas marcadas "O que você troca para o seu cenário", altere `OPERACAO` (o nome do seu caso), os três valores de `PARAMETROS` e, se quiser, `TIMEOUT`. Não é preciso mexer no resto.

**Opção A:** em `meu_ensaio.py`, importe `ParametrosRede` junto com o resto de `mini_orion.rede.api`, defina o seu cenário e use-o no lugar de `CAMPANHA` em `rodar`:

```python
from mini_orion.rede.api import ParametrosRede, TIMEOUT_POR_CHAMADA

MEU_CENARIO = ParametrosRede(
    latencia_mediana=0.050,  # 50 ms: troque pelo seu valor
    latencia_p99=0.800,      # 800 ms: troque pelo seu valor
    taxa_falha=0.005,        # 0,5%: troque pelo seu valor
)
```

**Justifique cada um dos três valores** em uma linha: de onde vem (a meta de um provedor, uma medição sua, uma suposição) e por que é plausível para o seu cenário. Rode `python meu_ensaio.py` (na opção A, com `--varrer`) e responda: **quais das conclusões da Aula 16 continuam valendo com os seus valores, e quais mudam?**

### 1.3 Acrescente uma política e preveja o resultado

A lista `politicas` (em `imprimir_politicas`, na opção A, ou em `main`, na opção B) tem quatro entradas. Acrescente uma quinta:

```python
("repetir sem chave (3)", 3, False),
```

**Antes de rodar**, escreva no relatório sua previsão, em duas linhas: com três tentativas e sem chave, as cobranças duplicadas serão **mais**, **menos** ou **iguais** às de duas tentativas sem chave? E os fechamentos que terminam em "não sei"? Dê a razão. Só depois rode e compare a previsão com o resultado.

!!! tip "Uma dica sobre previsões"

    Errar a previsão não custa nota. Custa nota não perceber o erro. Se o resultado contradisser o que você escreveu, explique o que no seu raciocínio estava incompleto.

### 1.4 Interprete

Em até dez linhas: **qual política você adotaria para a operação do seu cenário, e por quê?** Cite os números da sua tabela. Termine com uma linha dizendo o que o ensaio **não** mede (por exemplo, o custo de guardar as chaves, ou a espera entre tentativas).

## Parte 2 — A forma de implantação (`quantum.py`)

**Para que serve.** A Aula 17 comparou cinco formas de implantar o mesmo grafo. Agora você faz a mesma comparação sobre **o seu grafo**, e confere a sua contagem à mão contra o código. O `quantum.py` é autônomo: ele não importa nada do Mini-Orion, só tem o grafo escrito no próprio arquivo, e por isso serve igualmente às duas opções.

### 2.1 Troque o grafo

```bash
cp quantum.py meu_quantum.py
```

Em `meu_quantum.py`, substitua:

- `ARESTAS`: as dependências do seu cenário;
- `MODULOS`: o agrupamento em módulos de domínio (os componentes que você juntaria num mesmo serviço, no *service-based* por domínio);
- `ORIGEM_DO_FLUXO` e `DESTINO_DA_FILA`: os dois nomes das constantes do início do arquivo.

O arquivo ainda tem **funções e entradas de `main` que citam componentes do Orion** (`forma_so_pagamentos`, `forma_service_based_agrupado` e as linhas de `formas` em `main`). Elas quebram com o seu grafo (`KeyError`). Reescreva-as com os seus componentes, ou apague-as. Quando `python meu_quantum.py` rodar sem erro, esta etapa terminou.

### 2.2 Escreva as formas

Defina pelo menos **três formas** como funções `forma_...() -> Forma`, onde `Forma` é um dicionário `componente -> artefato`:

1. o monólito modular (um artefato);
2. a **extração do seu candidato** (o candidato num artefato, o resto em outro);
3. uma terceira forma, à sua escolha: por domínio, ou **agrupada** (como a de sete serviços da Aula 17, que mantém numa mesma unidade os componentes de uma mesma transação).

Acrescente-as à lista `formas` em `main`.

### 2.3 Conte à mão e escreva os testes

Para cada forma, **antes de rodar o script**, conte à mão e anote: quantos artefatos, quantas arestas remotas, quantas chamadas diretas do componente de `ORIGEM_DO_FLUXO`, e quantos *quanta* com tudo síncrono. Depois escreva `tests/test_meu_quantum.py`, com um teste por forma que **fixe os seus números**, seguindo o padrão de `tests/test_quantum.py`:

```python
import meu_quantum as q

def test_extracao_do_candidato() -> None:
    linha = q.avaliar("extração", q.forma_extracao(), banco_compartilhado=True)
    assert (linha.artefatos, linha.remotas, linha.diretas) == (2, 2, 1)  # seus números
    assert linha.quanta_sincrono == 1
```

Rode `pytest tests/test_meu_quantum.py`. Se um teste falhar, **descubra quem erra**: a sua contagem ou o código? Registre no relatório pelo menos um caso em que você teve de corrigir algo, e o que era.

### 2.4 Estenda o código: filas escolhidas por você

Hoje o script só sabe trocar por fila as arestas que chegam em `DESTINO_DA_FILA`. Acrescente uma opção que aceite **qualquer conjunto de arestas**:

```bash
python meu_quantum.py --assincronas "Venda>Fiscal,Pagamento>Aviso"
```

Dicas: use `argparse` como as outras opções; transforme o texto numa lista de pares com `split`; e passe o conjunto a `quanta()` pelo parâmetro `assincronas`, que já existe. Será preciso mudar `avaliar` para receber esse conjunto em vez de chamar `notificacoes_assincronas()`.

Use a opção para responder: **qual é o menor conjunto de arestas que, passando por fila, reduz o número de *quanta* na forma de microsserviços do seu cenário?** E por que, nas formas com banco compartilhado, nenhum conjunto basta?

### 2.5 Reúna a tabela

Para as suas formas, preencha uma tabela com artefatos, arestas remotas, chamadas diretas, chance de falha, disponibilidade, minutos fora do ar por mês e **quanta** em quatro situações: tudo síncrono, e com filas, cada uma com banco compartilhado e com banco por serviço (`--banco-unico`). Diga em uma linha quais dos números são **estruturais** (lidos do grafo) e quais dependem de hipótese.

## Parte 3 — Leitura

**Para que serve.** Os dois cenários que você trabalhou são simulados. Os artigos abaixo descrevem sistemas reais e dão a chance de ver onde a conta e as hipóteses se encontram com a prática. **Escolha um dos quatro.** Os links estavam funcionando quando esta página foi escrita; se algum sair do ar, busque o título e o autor.

Responda a cada pergunta em **três a seis linhas**, com suas palavras. Termine com uma frase ligando o artigo ao seu cenário.

### A. *The Tail at Scale* (Aula 16)

Jeffrey Dean e Luiz André Barroso. *Communications of the ACM*, v. 56, n. 2, 2013. <https://research.google/pubs/pub40801/>

1. Por que a latência do percentil 99 de **cada servidor** passa a importar mais quando uma requisição consulta muitos servidores? Refaça o argumento com a fórmula $P = 1 - (1 - p)^n$ da Aula 16.
2. Escolha **uma** das técnicas que o artigo propõe para tolerar a cauda e explique em suas palavras o que ela adiciona de custo.
3. Essa técnica é segura para uma operação **não idempotente**, como cobrar? O que seria preciso para torná-la segura?

### B. *Designing robust and predictable APIs with idempotency* (Aula 16)

Brandur Leach. Blog de engenharia da Stripe. <https://stripe.com/blog/idempotency>

1. O texto distingue tipos de falha. Qual deles corresponde ao desfecho "não sei se cobrou" da Aula 16? Como o servidor responde quando a mesma chave chega de novo?
2. Quem gera a chave e o que o servidor guarda? Compare com `ChaveIdempotencia` no Mini-Orion (procure em `mini_orion/nucleo/modelos.py`): em que a abordagem do artigo vai além do que o Mini-Orion guarda?
3. O artigo recomenda *backoff* exponencial com *jitter*. O `ensaio.py` repete sem esperar. O que mudaria nos resultados se muitos clientes repetissem ao mesmo tempo, depois de uma falha comum?

### C. *Goodbye Microservices: From 100s of problem children to 1 superstar* (Aula 17)

Alexandra Noonan. Blog da Segment (Twilio), 2018. <https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices>

1. Que **motivador de separação** (dos quatro da Aula 17) levou ao desenho original, com um serviço e uma fila por destino? Que custos apareceram com o tempo?
2. O sistema original tinha vários *quanta*? Responda com os critérios da Aula 17 (mesmo artefato, chamada síncrona, banco compartilhado), e diga quais informações o artigo **não** dá para decidir isso.
3. Quais *trade-offs* o time aceitou ao voltar a um monólito? Qual das opções A a E do guia "Como ler o resultado" a decisão do artigo corresponde?

### D. *Deconstructing the Monolith* (Aula 17)

Kirsten Westeinde. Blog de engenharia da Shopify, 2019. <https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity>

1. Que problema do monólito original motivou a mudança, e por que a Shopify **não** escolheu microsserviços?
2. Que mecanismos o texto descreve para que as fronteiras entre componentes sejam respeitadas? Compare com os contratos de `import-linter` que o Mini-Orion usa desde a Aula 7.
3. O guia da Aula 17 tem a opção A (manter o monólito). A decisão do texto é a A? Qual motivador de separação a escolha **não** atende?

## Parte 4 — A decisão

**Para que serve.** É o fecho: usar os números da Parte 1 e da Parte 2 para decidir, e dizer sob que condição a decisão estaria errada.

Escreva um ADR de **uma página** sobre o seu candidato, com os campos abaixo. Use o guia "Como ler o resultado" da Aula 17 para escolher entre as opções A a E.

| Campo | O que deve conter |
|---|---|
| **Contexto** | o cenário, o candidato e o **motivador de separação** (qual dos quatro tipos, e se está **comprovado por medição** ou apenas alegado) |
| **Decisão** | qual das opções A a E, em uma frase |
| **Alternativas** | pelo menos **três**, uma delas "manter o monólito", defendida como opção real (com o gatilho que a faria envelhecer), e nunca montada para perder |
| **Custo** | números da sua tabela: chamadas remotas, chance de falha, disponibilidade, *quanta*; e o que a política escolhida na Parte 1 acrescenta (estado para guardar chaves, por exemplo) |
| **Condição de falseamento** | o que você observaria, e em que prazo, para concluir que a decisão estava errada |
| **Como mediria** | para cada número do custo, se ele vem do código ou depende de medição em produção, e qual medição |

## O que entregar

Uma pasta (ou um repositório) com:

- `relatorio.md` (ou PDF), com as seções **Cenário**, **Parte 1**, **Parte 2**, **Parte 3** e **ADR**, nessa ordem;
- `meu_ensaio.py`, `meu_quantum.py` e `tests/test_meu_quantum.py`;
- a saída do `pytest` mostrando os testes passando, colada no relatório.

Se for em dupla, indique no início do relatório quem fez cada parte. As duas pessoas apresentam.

## Como será avaliado

Avalia-se a **qualidade da justificativa**, não a escolha: duas decisões opostas podem receber a nota máxima.

| Critério | Peso | A nota máxima exige |
|---|---|---|
| Cenário e hipóteses | 10% | cada valor tem origem declarada, e o que é inventado está dito |
| Parte 1 | 20% | previsão escrita **antes** do resultado, comparação honesta e interpretação com números |
| Parte 2 | 25% | código que roda, testes que passam, contagem manual conferida e a extensão `--assincronas` funcionando |
| Parte 3 | 15% | respostas com as suas palavras, que usam conceitos das aulas, e a ligação com o cenário |
| Parte 4 | 25% | motivador nomeado, alternativas reais, custo com números, condição de falseamento |
| Comunicação | 5% | relatório que outra pessoa entende sem você presente |

**Penalidades.**

- ADR sem nenhum custo nomeado: **teto de 60** na Parte 4.
- Alternativa montada só para perder: **zera** o item de alternativas.
- Números do relatório que não batem com a saída do código: **zera** a Parte 2.
- Código que não roda: **teto de 60** na Parte 2.

## Erros comuns

- **Mudar os valores do ensaio sem justificar.** O valor é uma hipótese, e a hipótese precisa de origem.
- **Contar as arestas do Orion no seu grafo.** Troque `ARESTAS` e `MODULOS`; o `quantum.py` tem constantes do Orion que sobram se você esquecer.
- **Escrever o teste a partir da saída do script.** Assim o teste só confirma o código. Conte à mão primeiro.
- **Responder à Parte 3 com o resumo do artigo.** As perguntas pedem que você use os conceitos das aulas para ler o texto.
- **Esconder o custo da opção que você escolheu.** Toda opção do guia tem um.

## Apresentação em sala

No início da Aula 18, cada pessoa (ou dupla) apresenta, em **cinco minutos**:

1. o cenário e o candidato;
2. o resultado mais surpreendente da Parte 1 ou da Parte 2;
3. a decisão do ADR e a condição em que ela estaria errada.

Haverá uma pergunta da turma sobre uma alternativa que você não escolheu. O objetivo é ver se você entende por que não a escolheu.
