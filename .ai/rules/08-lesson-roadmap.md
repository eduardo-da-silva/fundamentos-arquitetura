# Roadmap das aulas

!!! info "Status"

    Detalhado apenas para o Módulo 1, na composição de `07-curriculum.md`, já aplicada. Módulos 2 a 4 têm apenas escopo definido.

## Como ler este documento

Cada aula declara cinco coisas. As três primeiras são o que a aula precisa entregar; as duas últimas são o que ela deixa para trás.

- **Sintoma** — o fato do Orion que abre a aula.
- **Conceitos** — o vocabulário introduzido.
- **Artefato** — o que passa a existir depois da aula, nas duas trilhas.
- **Avaliação** — como se verifica que funcionou.
- **Ponte** — a pergunta que a próxima aula abre.

A coluna **Artefato** é a mais importante: é o que torna verificável a promessa das duas trilhas. Ela existe porque a versão anterior do módulo anunciava as trilhas em todas as aulas sem produzir nada persistente em nenhuma.

---

## Módulo 1

### Aula 1 — O que é Arquitetura de Software?

- **Sintoma:** mudança na regra de frete quebrou a emissão de nota fiscal. As duas coisas não têm relação de negócio.
- **Conceitos:** decisão arquitetural; arquitetura versus design; as três marcas de uma decisão arquitetural (impacto estrutural, custo de reversão, efeito sobre características).
- **Artefato:**
    - *Mini-Orion:* `code/mini-orion/01-acoplado/` — `Checkout` com cobrança e notificação no mesmo fluxo, funcionando e testado. Ponto de partida de tudo.
    - *Evolution Lab:* cada grupo classifica dez decisões do próprio recorte em arquitetural ou de design, com justificativa.
- **Avaliação:** a classificação distingue as duas categorias por critério, não por intuição.
- **Ponte:** se toda decisão arquitetural é cara de reverter, como decidir sem paralisar?

### Aula 2 — Leis da Arquitetura, trade-offs e ADR

- **Sintoma:** a decisão de manter a notificação dentro do checkout foi tomada há dois anos, ninguém lembra por quê, e agora ninguém quer mexer.
- **Conceitos:** Primeira e Segunda Leis; trade-off; custo da mudança ao longo do tempo; ADR como formato.
- **Artefato:**
    - *Mini-Orion:* o primeiro ADR do curso, registrando a decisão original — inclusive a que vai envelhecer mal.
    - *Evolution Lab:* ADR de uma decisão já existente no recorte do grupo, escrita retroativamente.
- **Avaliação:** o ADR nomeia alternativa descartada e consequência negativa aceita. ADR sem consequência negativa está incompleto.
- **Ponte:** decidimos com base em quê? Sem características priorizadas, todo trade-off vira preferência.

### Aula 3 — Características arquiteturais

- **Sintoma:** o time discute há três sprints se o checkout deve priorizar disponibilidade ou consistência, e a discussão reinicia toda vez.
- **Conceitos:** características implícitas e explícitas; operacionais, estruturais e transversais; a regra de "menos é mais"; como tornar uma característica mensurável.
- **Artefato:**
    - *Mini-Orion:* lista priorizada de três características do checkout, cada uma com definição operacional mensurável.
    - *Evolution Lab:* mesma priorização sobre o recorte do grupo, com a justificativa amarrada ao contexto de negócio.
- **Avaliação:** cada característica tem um número ou um teste associado. "Escalabilidade" sem definição operacional não conta.
- **Ponte:** temos critério. Falta saber onde no sistema ele é atendido ou violado — e para isso precisamos enxergar as partes.

### Aula 4 — Modularidade e Componentes

- **Sintoma:** ninguém no time consegue desenhar o sistema de memória, e dois desenhos feitos por pessoas diferentes não batem.
- **Conceitos:** módulo versus componente; fronteira; contrato; encapsulamento em nível arquitetural; decomposição.
- **Artefato:**
    - *Mini-Orion:* passagem para `02-fronteiras/` — `Pagamentos` atrás de um `Protocol`. Primeira fronteira explícita do curso.
    - *Evolution Lab:* mapa de componentes e dependências do recorte, no formato de `05-domain.md`.
- **Avaliação:** o mapa declara o que ele **não** representa. Diagrama que omite sem avisar reprova.
- **Ponte:** agora vemos as partes e as setas. Mas nem toda seta custa o mesmo.

### Aula 5 — Acoplamento e Coesão

- **Sintoma:** `Checkout` depende de cinco componentes; qualquer um deles em manutenção derruba a compra.
- **Conceitos:** acoplamento aferente e eferente; coesão e seus tipos; a tensão entre os dois; dependência cíclica (recorte legado do `CoreService`).
- **Artefato:**
    - *Mini-Orion:* em `02-fronteiras/`, notificação fora do caminho crítico — com a janela de inconsistência nomeada, não escondida.
    - *Evolution Lab:* registro de diagnóstico com dois pontos de alto acoplamento e duas evidências de baixa coesão.
- **Avaliação:** cada item do diagnóstico cita evidência no código ou no grafo, não impressão.
- **Ponte:** "acoplado" descreve coisas muito diferentes. Depender do nome de um campo e depender da ordem de duas chamadas não são o mesmo problema. Falta precisão.

### Aula 6 — Connascência

- **Sintoma:** duas mudanças aparentemente iguais em tamanho — renomear um campo e inverter duas chamadas — tiveram custos de correção muito diferentes.
- **Conceitos:** as nove formas (CoN, CoT, CoM, CoP, CoA, CoE, CoTiming, CoV, CoI); os três eixos — **força, localidade e grau**; a heurística: connascência forte fica dentro do componente, fraca atravessa a fronteira.
- **Artefato:**
    - *Mini-Orion:* passagem para `03-governado/` — CoP eliminada com `PedidoCobranca`, CoM com `ResultadoCobranca`, e os testes que detectam a regressão.
    - *Evolution Lab:* mapa de connascências entre componentes do recorte, classificado por força e localidade.
- **Avaliação:** a classificação usa os três eixos juntos. Dizer que algo é CoP sem dizer se atravessa fronteira não é diagnóstico.
- **Ponte:** o diagnóstico é qualitativo e cada pessoa prioriza diferente. Como comparar?

!!! note "Ordem de força"

    A ordem canônica de Page-Jones — CoN < CoT < CoM < CoP < CoA < CoE < CoTiming < CoV < CoI — é o núcleo da ferramenta e precisa ser enunciada explicitamente. Os três eixos entram nesta aula, não depois: sem eles a classificação não vira decisão.

### Aula 7 — Métricas e governança automatizada

- **Sintoma:** duas propostas de refatoração concorrem pelo mesmo trimestre e a discussão empatou em opinião.
- **Conceitos:** $C_a$, $C_e$, $A$, $I$, $D$; o plano $A \times I$ e a sequência principal; *Zone of Pain* e *Zone of Uselessness*; limites da medição; teste de arquitetura como governança contínua.
- **Artefato:**
    - *Mini-Orion:* `pydeps` sobre o código real, e os três contratos de `03-governado/setup.cfg`, que falham quando `Checkout` volta a importar implementação.
    - *Evolution Lab:* tabela de métricas do recorte com leitura arquitetural de cada valor.
- **Avaliação:** a leitura explica pelo menos um caso em que a métrica **não** aponta o problema real.
- **Ponte:** temos vocabulário, diagnóstico e evidência. Falta juntar tudo sobre um sistema inteiro.

!!! danger "Dois pontos inegociáveis"

    **Todos os números vêm de `05-domain.md`.** Nenhum valor inventado por aula. A versão anterior trazia três valores contraditórios de Fan-in para `Catalogo` dentro do mesmo capítulo.

    **A visualização é o plano $A \times I$, não um ranking de $D$.** $D = |A + I - 1|$ é simétrico: `Catalogo` ($D = 0{,}90$, concreto e estável) e `Integracoes` ($D = 0{,}83$, abstrato e instável) têm $D$ parecido por motivos opostos, e um gráfico de barras os torna indistinguíveis — que é exatamente o que a aula precisa distinguir.

### Aula 8 — Oficina de Diagnóstico Arquitetural

- **Sintoma:** a diretoria pediu um plano de evolução com prazo e justificativa.
- **Conceitos:** nenhum novo. Integração de tudo.
- **Artefato:**
    - *Mini-Orion:* nada novo; serve de referência resolvida.
    - *Evolution Lab:* proposta de evolução priorizada, com trade-off por item e critério de sucesso observável.
- **Avaliação:** rubrica completa em `09-assessment.md`.
- **Ponte:** o Orion continua monolítico. Isso é problema? O Módulo 2 responde — e a resposta não é a esperada.

!!! note "Escopo e tempo"

    A oficina ocupa os **dois encontros** da semana 4. A versão anterior previa 90 a 110 minutos para um roteiro que soma cerca de 200 pela tabela de `09-assessment.md`.

    O mapa e as métricas não são reconstruídos na oficina: já existem das Aulas 4 e 7. O que se exercita é priorizar sob restrição de orçamento, que é a competência central do módulo.

---

## Módulos 2 a 4

Escopo em `07-curriculum.md`. Detalhar aula a aula somente quando o módulo entrar em produção — roadmap escrito com antecedência demais envelhece antes de ser usado.

Quando detalhar, manter as cinco colunas. A coluna **Artefato** é o que impede as trilhas de virarem promessa retórica de novo.
