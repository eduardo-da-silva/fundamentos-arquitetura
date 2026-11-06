# Aula 21 — O custo real: operação, observabilidade e times

## Objetivo e competências

Ao fechar esta aula, conseguimos:

- explicar o que significa **operar** um artefato a mais e por que esse custo não aparece no grafo de dependências;
- distinguir monitoramento de observabilidade e descrever o que registro, métrica e rastro respondem, cada um;
- explicar o **identificador de correlação**, onde ele nasce, como se propaga e o que ele não resolve;
- relacionar a disponibilidade composta da Aula 17 ao tempo de diagnóstico, que a observabilidade reduz sem alterar a frequência da falha;
- aplicar a **Lei de Conway** a uma proposta de extração, perguntando que time seria dono de cada artefato;
- montar um balanço de ganho e custo de uma extração em que **todo item tem número ou a marca "não medido"** com a forma de medir;
- rodar o Mini-Orion e reconstruir, a partir de dois registros, o caminho de um fechamento que falhou.

## Cobrança sem pedido, e ninguém sabe onde parou

Depois da campanha, o suporte recebe reclamações de clientes cobrados sem pedido. A Aula 20 deu ao fechamento a compensação e a reconciliação, e elas corrigem o que podem. Mas a pergunta que o time de plataforma recebe é outra: **em que passo e em que serviço aquele fechamento parou?** `Compra` tem seu registro. `Pagamentos` tem o dele. Cada um escreve uma linha por evento, com horário e mensagem. Nenhuma linha de um tem algo em comum com uma linha do outro. Para juntar a história de um cliente, alguém compara horários, valores e e-mails nos dois arquivos, e a campanha produziu milhares de linhas por minuto.

Esta é a parte do custo da distribuição que o grafo não mostra e que o orçamento raramente considera: a **operação**. A conta da Aula 14 listou, entre os custos de extrair, "mais um artefato para operar". Esta aula olha para essa frase e a desdobra em itens que se possam contar.

## O que significa operar

Um artefato implantável, antes de entregar valor, precisa de tudo o que o mantém no ar. Ele tem **um caminho de entrega** próprio (compilar, testar, publicar, subir), **monitoramento** (saber se está vivo e saudável), **alertas** (quem é avisado e de quê), **versões e contratos** a manter (a Aula 18), **dado** com cópia de segurança e migração (a Aula 19) e **alguém de plantão** quando algo cai de madrugada. Dentro de um monólito, tudo isso existe uma vez. Extrair um serviço cria uma segunda cópia de cada item.

O custo cresce com o número de artefatos, e não com o número de linhas de código. Dez serviços pequenos têm dez caminhos de entrega, dez painéis e dez dados a salvar. Por isso a conclusão da Aula 17 (cortar pouco) é também uma conclusão sobre operação: cada artefato evitado é uma cópia a menos de tudo isso. O Orion, no entanto, **ainda não mediu** esse custo. Nem o tempo que o time gasta com cada item, nem o número de pessoas de plantão. A aula marca esses itens como "não medido" e diz como medi-los, em vez de inventar um número.

## Ver o que acontece: monitoramento e observabilidade

**Monitoramento** responde a perguntas que alguém já previu: a CPU passou de um limite? A fila está maior que o normal? É preciso decidir antes quais perguntas importam. **Observabilidade** é a propriedade de um sistema que permite entender o que ele está fazendo a partir do que ele emite para fora, inclusive para perguntas que ninguém previu. Newman a define nesses termos, e acrescenta um aviso: ela é uma propriedade, não uma lista de ferramentas; o foco deve estar em tornar o sistema compreensível, e não em instalar mais ferramentas.

Três tipos de informação costumam sustentá-la. O **registro** (*log*) é uma linha por evento, com instante e mensagem: responde "o que aconteceu, em detalhe". A **métrica** é um número agregado ao longo do tempo (taxa de erro, latência no percentil 95): responde "quanto, e se está piorando". O **rastro** (*trace*) é a trilha de uma única requisição atravessando vários serviços: responde "por onde passou, quanto demorou em cada trecho". Newman nota que os três se sobrepõem (é possível guardar métricas em arquivo de registro, ou construir um rastro a partir de linhas de registro), e é isso que permite começar pequeno.

### O identificador de correlação

Um **identificador de correlação** (*correlation ID*) é um valor gerado quando uma requisição entra no sistema e carregado em toda chamada que ela provoca. Cada serviço o grava em todas as linhas de registro que escreve por causa dela. Com ele, juntar os registros de serviços diferentes deixa de ser comparar horários e passa a ser uma busca por um valor.

Três regras tornam o identificador útil. Ele **nasce na borda**, no começo do fluxo, e não em cada serviço (senão há um por serviço e nenhum em comum). Ele **viaja em toda chamada**, como campo da mensagem. E ele é **gravado em toda linha**. Esquecer qualquer um dos três faz o rastro ter buracos justamente onde a falha aconteceu.

A Aula 18 já deu a ferramenta que torna a propagação barata: um campo novo e opcional na mensagem é uma **mudança aditiva**, e um leitor tolerante o ignora. Um serviço que ainda não grava o identificador continua funcionando; apenas aparece como buraco no rastro. Newman recomenda introduzir o identificador cedo: ele não parece útil no começo, mas é caro de acrescentar depois.

Uma limitação conhecida: reconstruir a ordem dos eventos entre serviços exige confiar nos relógios. No simulador, o relógio é um só e a ordem é exata. Num sistema real, cada serviço tem o seu relógio, e a ordem entre serviços é uma inferência, com uma margem de erro. É por isso que ferramentas de rastro guardam, além do horário, a relação de quem chamou quem.

## Disponibilidade composta e tempo de diagnóstico

A Aula 17 calculou que dois artefatos em série, cada um com 99,9% de disponibilidade, entregam cerca de 99,8%: 86 minutos fora do ar por mês, contra 43 de um só. Esse número descreve a **frequência** com que o fechamento falha, e a observabilidade não o altera. O que ela altera é a **duração do diagnóstico**: o tempo entre alguém perceber o problema e saber onde ele está. Em um sistema de dois registros sem identificador em comum, esse tempo é o de comparar à mão. Com o identificador, é o de uma busca.

Vale não prometer mais do que isso. A observabilidade não corta nenhum dos 43 minutos adicionais; ela encurta a parte de cada incidente que se gasta procurando. Quanto isso vale depende de quantos incidentes e de quanto custa cada hora de busca, e o Orion ainda não mediu nenhum dos dois.

## Conway: quem é dono de quê

A **Lei de Conway**, formulada por Melvin Conway em 1968, diz que as organizações que projetam sistemas produzem projetos que são cópias das suas estruturas de comunicação. O corolário prático é que a fronteira de um serviço tende a acompanhar a fronteira de um time. Se dois serviços pertencem ao mesmo time, a fronteira entre eles custa mais do que rende: a autonomia que ela promete é a de um time em relação a si mesmo. Se um serviço atravessa dois times, cada mudança vira uma negociação.

A consequência para o Orion é uma pergunta a fazer antes de extrair: **que time seria dono de `Pagamentos`**, e esse time tem plantão, ritmo de entrega e conhecimento de provedores para sustentá-lo? O Orion tem uma equipe de plataforma de porte médio. Se a mesma equipe fosse dona do monólito e de `Pagamentos`, a extração entregaria isolamento de processo e de entrega, e não autonomia de time, que é o motivador mais citado dos microsserviços e o que menos se aplica aqui. Existe também a manobra inversa (*Inverse Conway Maneuver*): reorganizar os times primeiro para favorecer a arquitetura desejada. Qualquer das duas leituras é defensável, e nenhuma é sem custo: a segunda custa uma reorganização que a diretoria precisa aprovar.

## Estudo de caso: o balanço da extração de `Pagamentos`

A Aula 14 deixou a conta em aberto: o que a extração de `Pagamentos` ganha e o que ela custa. Com as Aulas 16 a 20, cada item tem agora um número ou uma forma de medi-lo. A tabela abaixo é o balanço. A coluna "Valor" traz o número do ensaio ou da hipótese de trabalho, e a coluna "Como medir" diz o que substituiria a hipótese por uma medição do Orion.

| Item | Ganho ou custo | Valor | Como medir |
|---|---|---|---|
| Arestas remotas | custo | 2 no grafo do Orion (1 no Mini-Orion) | extrair as dependências do código |
| Falha por chamada remota | custo | 2% em campanha (hipótese) | contagem de *timeouts* por destino |
| Disponibilidade do fechamento | custo | 99,8%, contra 99,9% (86 contra 43 min/mês) | fechamentos concluídos sobre tentados, na borda |
| Cobrança duplicada | custo, mitigado | 1% sem chave; 0 com chave | extrato do provedor contra os fechamentos |
| Cobrança sem pedido | custo, mitigado | 2 em 2000 (0,1%) | conciliação entre cobranças e pedidos |
| Janela de inconsistência | custo | 0,01 s com compensação; ~900 s sem resposta (hipótese) | tempo entre cobrança e estorno, no registro |
| Artefatos para operar | custo | 2, contra 1 | contagem direta |
| Esforço de operação (entrega, alertas, plantão) | custo | **não medido** | horas por semana por artefato, registradas por um trimestre |
| Tempo de diagnóstico | custo, mitigado | **não medido** | tempo entre alerta e causa identificada |
| Transação local, deploy único, teste sem rede | custo (perdido) | 3 itens que deixam de existir | já identificados na Aula 14 |
| Cadência de release própria | ganho | **não medido** (gatilho da Aula 14) | releases fora do trem compartilhado, por sprint |
| Janela própria para a conciliação | ganho | **não medido** | deploys bloqueados por janela de conciliação |
| Autonomia de time | ganho | **não medido**; depende de quem seria o dono | quem é dono e quem faz plantão |

A tabela é o ponto principal da aula. Duas colunas dela merecem leitura. Os **custos** têm quase todos algum número, porque vieram do ensaio e da conta das aulas anteriores: a rede foi simulada, e simulado é mensurável. Os **ganhos**, ao contrário, estão quase todos marcados "não medido", porque dependem do que o Orion ainda não observou: o gatilho da Aula 14 não disparou, e ninguém mediu a espera por *deploy*. Isso muda o peso do que a tabela diz. Ela não condena a extração; mostra que o lado do custo tem evidência e o do ganho, ainda não.

### 📐 ADR — Registrar o identificador de correlação de ponta a ponta

| Campo | Conteúdo |
|---|---|
| **Identificador** | ADR — Identificador de correlação de ponta a ponta |
| **Status** | Aceito para o `09-saga`. |
| **Contexto** | Depois da campanha, clientes cobrados sem pedido não podem ser rastreados: `compra` e `pagamentos` têm registros separados, sem identificador em comum. |
| **Decisão** | O orquestrador gera um identificador por fechamento, na entrada. Ele viaja num campo opcional da mensagem para `pagamentos` (mudança aditiva, ignorada por quem não o conhece) e é gravado em toda linha de registro dos dois lados, inclusive nas pendências e na reconciliação. |
| **Alternativas** | (a) Comparar horários, valores e e-mails à mão: sem código novo, e inviável em campanha. (b) Usar a chave de idempotência como identificador: já existe, mas mistura dois papéis (evitar repetição e rastrear) e uma chave pode ser reusada em outro contexto. (c) Uma ferramenta de rastro distribuído completa: mais capacidade, com um custo de operação que o Orion não mediu e que seria mais um artefato. |
| **Consequências positivas** | O caminho de um fechamento que falhou se reconstrói por uma busca. A pendência e a reconciliação entram na mesma história. |
| **Consequências negativas** | O campo é mais uma regra a respeitar em toda chamada futura: um serviço que esqueça o identificador deixa um buraco. A ordem entre serviços só é exata no simulador. O registro continua em memória por serviço; reunir os registros num lugar é outro custo. |
| **Reversão** | Barata: o campo é opcional. |
| **Condição de falseamento** | Estaria errado se, em produção, uma fração relevante dos fechamentos que falham não pudesse ser reconstruída (identificador perdido em algum trecho). |

### Na prática: Python

O checkpoint é o mesmo `09-saga/` da Aula 20. A observabilidade mora em um módulo próprio, `mini_orion/observabilidade/api.py`, que não conhece nenhum módulo de domínio (um contrato do `import-linter` verifica isso). Cada módulo tem o seu registro, como dois serviços teriam dois arquivos. O que os liga é a função que filtra pelo identificador e ordena:

```python title="09-saga/mini_orion/observabilidade/api.py (recorte)"
class Registro:
    def __init__(self, origem: str, agora: Callable[[], float]) -> None:
        self._origem = origem
        self._agora = agora
        self.eventos: list[Evento] = []

    def registrar(self, mensagem: str, correlacao: str | None = None) -> None:
        self.eventos.append(
            Evento(next(_SEQUENCIA), self._agora(), self._origem, correlacao, mensagem)
        )


def reconstruir(correlacao: str, *registros: Registro) -> list[Evento]:
    """Junta, em ordem, os eventos de todos os registros que levam o identificador."""
    todos = [e for r in registros for e in r.eventos if e.correlacao == correlacao]
    return sorted(todos, key=lambda e: (e.instante, e.sequencia))
```

O identificador viaja como campo opcional do pedido de cobrança, o que é a mudança aditiva da Aula 18. O servidor de `pagamentos` o lê com `carga.get("correlacao")` e o grava em cada linha. O teste `test_sem_identificador_os_dois_registros_nao_se_juntam` reproduz o início da aula: os dois registros têm linhas, nenhuma com identificador, e a busca devolve uma lista vazia. O teste ao lado, `test_com_o_identificador_o_caminho_do_fechamento_que_falhou_se_reconstroi`, mostra a história inteira de um fechamento cuja emissão falhou:

```text
compra       fechamento iniciado: cobrar
pagamentos   cobranca recebida
pagamentos   cobranca aprovada
compra       emissao falhou: compensar
pagamentos   estorno executado
compra       compensado: cobranca estornada
```

E o caso mais difícil, de uma cobrança que expirou e só a reconciliação resolveu, aparece com o intervalo que separa os eventos:

```text
   0.0 s  compra       fechamento iniciado: cobrar
   0.0 s  pagamentos   cobranca recebida
   0.0 s  pagamentos   cobranca aprovada
   1.0 s  pagamentos   repeticao reconhecida
   2.0 s  compra       pendencia aberta: cobranca_indeterminada
 902.0 s  pagamentos   consulta: aprovada
 902.1 s  pagamentos   estorno executado
 902.1 s  compra       pendencia corrigida pela reconciliacao
```

Perceba o que o rastro mostra e as métricas não mostrariam: a cobrança foi aprovada às 0,0 s, a resposta não chegou, e o cliente ficou cerca de 900 s cobrado e sem pedido. O número 900 é a hipótese do intervalo do job, e o rastro é o instrumento que o mediria em produção.

```bash
cd fundamentos-arquitetura-code/09-saga
pytest tests/test_observabilidade.py     # 4 testes
pytest                                   # 82 testes
lint-imports                             # 9 contratos
```

O que vale experimentar:

- **Ver o buraco.** Em `montar_saga`, passe `gerar_correlacao=lambda: None` e rode a reconstrução de um fechamento que falhou. O que o rastro mostra e o que ele perdeu?
- **Esquecer um ponto.** Em `_servidor.py`, retire o `correlacao` de uma das chamadas a `_registrar`. Qual evento some do rastro, e em que ponto da história a falta dele atrapalharia mais?
- **Preencher o balanço.** Escolha uma linha "não medido" da tabela do estudo de caso e escreva, em duas frases, como o Orion mediria o item em um trimestre.

## O que ficou decidido e o que a Aula 22 pergunta

Ficou decidido que cada fechamento carrega um identificador de correlação de ponta a ponta, gravado dos dois lados, e que o balanço da extração de `Pagamentos` tem um número ou a marca "não medido" em cada item. Ficou registrado também que a observabilidade encurta o diagnóstico sem reduzir a frequência da falha, que a Lei de Conway pergunta que time seria dono do serviço antes de extraí-lo, e que o lado do custo tem mais evidência do que o do ganho.

Temos a conta inteira, com seus buracos à vista. Falta o que o módulo inteiro vinha preparando: decidir sob orçamento. Se a diretoria aprovar "extrair com critério", o que sai primeiro, o que fica e quando parar? A Aula 22 pede essa proposta, e pede também que o grupo defenda a alternativa de não extrair nada como opção real.

## Leitura complementar

- Newman, Sam. *Building Microservices*. 2. ed. Cap. 10 — From Monitoring to Observability (a definição de observabilidade, registros, métricas, rastro distribuído e a recomendação de adotar o identificador de correlação cedo).
- Conway, Melvin E. "How Do Committees Invent?". *Datamation*, abril de 1968.
- Richards, Mark; Ford, Neal. *Fundamentals of Software Architecture*. Seção "Conway's Law" (a lei e a manobra inversa de Conway).
- Ford, Neal; Parsons, Rebecca; Kua, Patrick; Sadalage, Pramod. *Building Evolutionary Architectures*. 2. ed. (observabilidade e métricas como base de funções de aptidão, tema do Módulo 4).

## Referências

- NEWMAN, Sam. *Building Microservices*. 2. ed. O'Reilly, 2021.
- CONWAY, Melvin E. How Do Committees Invent? *Datamation*, v. 14, n. 4, 1968.
- RICHARDS, Mark; FORD, Neal. *Fundamentals of Software Architecture: An Engineering Approach*. O'Reilly, 2020.
- FORD, Neal; PARSONS, Rebecca; KUA, Patrick; SADALAGE, Pramod. *Building Evolutionary Architectures*. 2. ed. O'Reilly, 2023.
