# Módulo 2 — Arquiteturas Monolíticas — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Escrever e publicar o Módulo 2 do curso (7 aulas, semanas 5–8), com a evolução do Mini-Orion em três checkpoints executáveis e a extensão do domínio que as aulas exigem.

**Architecture:** O Módulo 2 transforma o *big ball of mud* do Orion num monólito modular sem distribuir nada. Cada aula abre por um sintoma do Orion, introduz um estilo de monólito (camadas, modular, pipeline, microkernel), e produz um artefato nas duas trilhas (Mini-Orion executável e Evolution Lab). O código do Mini-Orion evolui de `03-governado/` (fim do Módulo 1) por três estados, cada um com contratos de `import-linter` que falham quando a decisão é desfeita.

**Tech Stack:** Markdown (zensical / MkDocs Material), Mermaid 11, MathJax 3, Python 3.12+, pytest, import-linter. Sem framework, sem I/O real no Mini-Orion.

**Spec:** `.ai/planos/2026-09-01-modulo2-design.md` — leia antes de executar qualquer tarefa. Este plano argumenta a partir dela.

## Global Constraints

Requisitos do projeto que valem para **todas** as tarefas (de `.ai/rules/` e da spec):

- **Escopo:** só arquitetura de software. Nunca introduzir conteúdo de POO-II (herança, polimorfismo, padrões de projeto como tema).
- **Números:** todo valor apresentado ao aluno (Fan-in, Fan-out, métricas, contagem de arestas) vem de `.ai/rules/05-domain.md`. Nenhum número inventado por aula.
- **`docs/` = `nav`:** todo `.md` em `docs/` tem de estar no `nav:` de `mkdocs.yml`. Arquivo órfão é erro. Rascunho fica fora de `docs/`.
- **Mermaid:** só tipos sem sufixo `-beta`. Permitidos: `flowchart`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`, `quadrantChart`, `mindmap`, `timeline`. `xychart-beta` proibido em material publicado.
- **Fórmula e diagrama:** nenhuma informação essencial só na fórmula ou só no diagrama — sempre há leitura em linguagem natural. Todo diagrama declara o que **não** representa.
- **Convenção de setas:** `A --> B` significa "A depende de B". Declarar em todo diagrama de dependência.
- **Python:** 3.12+; type hints em assinatura pública; nomes do domínio em português iguais aos de `05-domain.md`; `Enum` para estado; `Protocol` para contrato entre componentes; exceção específica; métodos de 5–20 linhas; sem framework, ORM ou I/O real.
- **Dependências:** nenhuma nova. O build do site instala só `zensical`; as ferramentas de análise já estão em `code/mini-orion/requirements-dev.txt`.
- **Código do Mini-Orion:** nomes de classe e método estáveis ao longo do curso; cada estado parte do anterior; o que aparece na página é recorte do arquivo real.
- **Snippet ilustrativo:** 5–25 linhas; declara que é ilustrativo; **não** usa nomes do Mini-Orion (usar `ServicoA`, `FiltroX` etc.).
- **Tamanho de aula:** 200–320 linhas de Markdown para aula conceitual. Oficina pode exceder com material de apoio.
- **Proporção por aula:** ~50% texto argumentativo, ~25% diagrama/tabela/ADR, ~25% código.
- **Voz:** primeira do plural para o raciocínio ("vamos analisar"), segunda do singular para o trabalho do aluno. Nunca primeira do singular. Presente do indicativo.
- **Expressões proibidas:** "obviamente", "claramente", "evidentemente", "como todos sabem", "é sabido que", "basta", "simplesmente", "é só", "a melhor prática é", "sempre"/"nunca"/"em qualquer caso" (em recomendação), "o correto é", "nesta aula aprenderemos", "é importante ressaltar que".
- **Anti-boilerplate:** nenhum bloco de texto igual em mais de duas aulas. Ao terminar uma aula, abrir a anterior lado a lado; se mais da metade dos títulos `##`/`###` coincidir, reescrever. Não reproduzir as molduras do Módulo 1: `### Trilhas permanentes de exemplo nesta aula`, `### Uma possível resolução comentada do professor`, `### No início — conexão com a aula anterior`, `### No final — conexão com a próxima aula`, `Apresentação do diagrama:` / `Interpretação:`.
- **Exercícios:** `## Exercícios` com quatro questões — gabarito recolhido em `??? note "Resposta comentada"` nas três primeiras; a quarta é de julgamento, com **critério de avaliação** em vez de resposta, e diz explicitamente que mais de uma resposta é aceitável. `## Atividade em grupo` com um item obrigatório que força o grupo a reconhecer o limite da própria proposta. Exceção: a oficina (Aula 15) substitui isso por um aquecimento individual sem gabarito.
- **ADR:** formato Contexto / Decisão / Alternativas / Consequências (positivas **e** negativas) / Reversão. ADR sem consequência negativa está incompleto.
- **Sem `sudo`**, sem alterar permissões de arquivo.
- **Commits frequentes:** um commit por tarefa concluída, na `main` (o professor autorizou). Mensagem em português. Terminar a mensagem com:
  ```
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw
  ```

---

## Estrutura de arquivos

**Regras editoriais (modificar):**
- `.ai/rules/05-domain.md` — acrescenta a seção de agrupamento em módulos de domínio.
- `.ai/rules/07-curriculum.md` — Módulo 2 passa a 7 aulas; realoca 1 encontro.
- `.ai/rules/08-lesson-roadmap.md` — preenche o Módulo 2 no formato de 5 colunas.
- `.ai/rules/12-backlog.md` — fecha itens 4 e (parcial) 6.

**Código do Mini-Orion (criar):**
- `code/mini-orion/04-camadas/` — pacote em camadas técnicas + contrato `layers`.
- `code/mini-orion/05-modular/` — módulos de domínio com API pública + contratos `independence`/`forbidden`.
- `code/mini-orion/06-microkernel/` — `Promocoes` como registro de plugins + contrato núcleo↛plugin.
- `code/mini-orion/README.md` — documenta os três novos estados (modificar).
- `.github/workflows/mini-orion.yml` — CI que roda `pytest` + `lint-imports` nos checkpoints (criar).

**Conteúdo publicado (criar), todos entram no `nav` de `mkdocs.yml`:**
- `docs/modulo2/index.md` — visão geral do módulo.
- `docs/modulo2/aula09-monolito-nao-e-o-problema.md`
- `docs/modulo2/aula10-monolito-em-camadas.md`
- `docs/modulo2/aula11-monolito-modular.md`
- `docs/modulo2/aula12-reorganizar-o-grafo.md`
- `docs/modulo2/aula13-pipeline-e-microkernel.md`
- `docs/modulo2/aula14-quando-o-monolito-deixa-de-servir.md`
- `docs/modulo2/aula15-oficina-orion-modular.md`
- `docs/orion/index.md` — estende os formatos do Evolution Lab (modificar).
- `mkdocs.yml` — bloco de `nav` do Módulo 2 (modificar).

**Ordem de dependência:** Task 1 bloqueia tudo. Tasks 4→5→6 em sequência. A10 precisa da Task 4; A11 e A12 precisam da Task 5; A13 precisa da Task 6. Task 3 antes de qualquer aula. Task 8 (formatos do Lab) antes de A12.

---

## Task 1: Agrupamento em módulos de domínio em `05-domain.md`

**Files:**
- Modify: `.ai/rules/05-domain.md` (acrescentar seção nova antes de "Recorte legado")

**Interfaces:**
- Produces: a tabela canônica de 8 módulos de domínio e a contagem "2 arestas internas + 15 inter-módulo = 17", referenciada por Tasks 3, 8, 12 e 15.

- [ ] **Step 1: Acrescentar a seção "Agrupamento em módulos de domínio"**

Inserir após a seção "Números oficiais" e antes de "Recorte legado (para a aula de acoplamento)". Conteúdo:

- Frase de abertura: o agrupamento é **decisão da disciplina**, como a convenção de contagem de Abstractness. Existe para dar resposta verificável ao exercício de reorganização do Módulo 2; um agrupamento diferente seria defensável.
- Tabela (copiar exatamente):

  | Módulo de domínio | Componentes | Arestas internas |
  |---|---|---|
  | Borda | `Portal` | — |
  | Vitrine | `Catalogo`, `Promocoes` | `Promocoes → Catalogo` |
  | Compra | `Checkout`, `Pedidos` | `Checkout → Pedidos` |
  | Financeiro | `Pagamentos` | — |
  | Distribuição | `Logistica` | — |
  | Comunicação | `Notificacoes` | — |
  | Identidade | `Clientes` | — |
  | Integração | `Integracoes` | — |

- Bloco com as 15 arestas inter-módulo enumeradas:
  `Portal→Catalogo`, `Portal→Checkout`, `Portal→Pedidos`, `Portal→Clientes`, `Checkout→Catalogo`, `Checkout→Clientes`, `Checkout→Promocoes`, `Checkout→Pagamentos`, `Pedidos→Notificacoes`, `Pedidos→Logistica`, `Pagamentos→Notificacoes`, `Logistica→Notificacoes`, `Integracoes→Catalogo`, `Integracoes→Pedidos`, `Integracoes→Notificacoes`.
- Verificação declarada: `2 internas + 15 inter-módulo = 17 arestas`, igual ao grafo oficial.
- Leitura em camadas: `Borda` → módulos de domínio → tipos compartilhados (`dominio`). Nenhum módulo de domínio importa `Borda`.
- Leitura de ensino (parágrafo curto): 15 de 17 arestas atravessam fronteira de módulo — o grafo atual mal é modular, e o agrupamento torna isso visível. `Checkout` aparece em 5 arestas inter-módulo; é o hub, o mesmo componente com $D = 0{,}03$ e o que mais causa incidente.
- Nota: a tabela $C_a$/$C_e$/$A$/$I$/$D$ **não muda** — é por componente, não por módulo.

- [ ] **Step 2: Verificar a contagem de arestas**

Run:
```bash
cd /home/eduardo/Documentos/IFC/Aulas/Fundamentos-Arquitetura/notas-aula-site
python3 - <<'EOF'
arestas = [
 ("Portal","Catalogo"),("Portal","Checkout"),("Portal","Pedidos"),("Portal","Clientes"),
 ("Checkout","Catalogo"),("Checkout","Clientes"),("Checkout","Promocoes"),
 ("Checkout","Pagamentos"),("Checkout","Pedidos"),("Promocoes","Catalogo"),
 ("Pedidos","Notificacoes"),("Pedidos","Logistica"),("Pagamentos","Notificacoes"),
 ("Logistica","Notificacoes"),("Integracoes","Catalogo"),("Integracoes","Pedidos"),
 ("Integracoes","Notificacoes"),
]
mod = {"Portal":"Borda","Catalogo":"Vitrine","Promocoes":"Vitrine","Checkout":"Compra",
 "Pedidos":"Compra","Pagamentos":"Financeiro","Logistica":"Distribuicao",
 "Notificacoes":"Comunicacao","Clientes":"Identidade","Integracoes":"Integracao"}
internas = [(a,b) for a,b in arestas if mod[a]==mod[b]]
inter = [(a,b) for a,b in arestas if mod[a]!=mod[b]]
print("total:", len(arestas), "internas:", len(internas), "inter:", len(inter))
assert len(arestas)==17 and len(internas)==2 and len(inter)==15
print("OK")
EOF
```
Expected: `total: 17 internas: 2 inter: 15` seguido de `OK`.

- [ ] **Step 3: Verificar linguagem ubíqua**

Run: `grep -nE 'Usuarios|usuários|vitrine|fechamento|cobrança' .ai/rules/05-domain.md | grep -v 'Nunca'`
Expected: nenhuma linha nova introduzida pela edição (apenas as ocorrências que já existiam na tabela "Sempre / Nunca").

- [ ] **Step 4: Commit**

```bash
git add .ai/rules/05-domain.md
git commit -m "$(printf 'dominio: agrupamento dos 10 componentes em 8 modulos de dominio\n\nBase para a reorganizacao do grafo no Modulo 2. 2 arestas internas,\n15 inter-modulo, soma 17 = grafo oficial. Tabela de metricas inalterada.\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Task 2: Ajustar o currículo em `07-curriculum.md`

**Files:**
- Modify: `.ai/rules/07-curriculum.md`

**Interfaces:**
- Produces: Módulo 2 = 7 aulas na tabela das 18 semanas; demais módulos inalterados; total 36.

- [ ] **Step 1: Atualizar a tabela das 18 semanas**

Trocar a linha do Módulo 2 de `8` para `7` aulas. As demais linhas não mudam (Módulo 3 continua `10`). Acrescentar nota de rodapé curta: "As 7 aulas do Módulo 2 preenchem os 8 encontros das semanas 5–8 — seis aulas conceituais (9–14) e a oficina (Aula 15) nos dois encontros da semana 8. Foi a fusão das duas aulas de camadas que abriu espaço para a oficina dupla caber; com 8 aulas, não cabia."

- [ ] **Step 2: Reescrever a seção "Módulo 2 — Arquiteturas Monolíticas"**

Substituir o parágrafo de escopo atual pela composição detalhada (7 aulas, uma linha cada):

- Aula 9 — O monólito não é o problema
- Aula 10 — Monólito em camadas: o que governa e o que não isola
- Aula 11 — Monólito modular: fronteira lógica sem fronteira física
- Aula 12 — Reorganizar o grafo do Orion
- Aula 13 — Pipeline e microkernel: monólitos com forma
- Aula 14 — Quando o monólito deixa de servir
- Aula 15 — Oficina: o Orion modular sob restrição (dois encontros da semana 8)

Manter o parágrafo "Aplicação no Orion: reorganizar o grafo atual sem distribuir nada, e medir o ganho."

Acrescentar duas frases de justificativa, no tom das que já existem no Módulo 1: por que fundir as duas aulas de camadas (camadas técnicas e o limite delas são um arco só); por que o `06-microkernel/` é checkpoint executável (microkernel sem código vira definição solta).

- [ ] **Step 3: Verificar a aritmética**

Run:
```bash
python3 -c "assert 8+8+10+8+2 == 36; print('36 encontros OK')"
```
Expected: `36 encontros OK`. (Encontros de cada módulo = semanas × 2. As 7 aulas do Módulo 2 preenchem 8 encontros porque a oficina conta como dois.)

- [ ] **Step 4: Verificar consistência de nomes de módulo**

Run: `grep -n 'Arquiteturas Monolíticas' .ai/rules/07-curriculum.md mkdocs.yml docs/index.md`
Expected: o nome do Módulo 2 aparece idêntico ("Arquiteturas Monolíticas") em todos.

- [ ] **Step 5: Commit**

```bash
git add .ai/rules/07-curriculum.md
git commit -m "$(printf 'curriculo: Modulo 2 passa de 8 para 7 aulas\n\nA fusao das duas aulas de camadas deixa o Modulo 2 com 7 aulas, que\ncabem exatas nos 8 encontros das semanas 5-8 (oficina dupla na semana\n8). Demais modulos inalterados; total das 18 semanas segue 36.\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Task 3: Preencher o roadmap do Módulo 2 em `08-lesson-roadmap.md`

**Files:**
- Modify: `.ai/rules/08-lesson-roadmap.md` (seção "Módulos 2 a 4" — inserir "## Módulo 2" antes dela)

**Interfaces:**
- Consumes: agrupamento de domínios da Task 1.
- Produces: as 7 entradas de aula no formato de 5 colunas (Sintoma / Conceitos / Artefato / Avaliação / Ponte), fonte para o conteúdo das Tasks 9–15.

- [ ] **Step 1: Escrever as 7 entradas**

Usar exatamente o conteúdo da seção 3 da spec (`.ai/planos/2026-09-01-modulo2-design.md`), no mesmo formato das entradas do Módulo 1 já presentes no arquivo: cabeçalho `### Aula N — Título`, e as cinco subseções em negrito (**Sintoma:**, **Conceitos:**, **Artefato:** com *Mini-Orion:* e *Evolution Lab:*, **Avaliação:**, **Ponte:**).

Incluir os dois `!!! note` de apoio, no estilo dos do Módulo 1:
- em Aula 10, nota "Fusão": explica que esta aula funde as duas aulas de camadas previstas.
- em Aula 15, nota "Escopo e tempo": ocupa os dois encontros da semana 8; o mapa e as métricas não são reconstruídos (vêm das Aulas 10–12); o que se exercita é priorizar a introdução de fronteiras sob orçamento.

- [ ] **Step 2: Ajustar a nota de status do topo do arquivo**

Trocar "Detalhado apenas para o Módulo 1" por "Detalhado para os Módulos 1 e 2".

- [ ] **Step 3: Verificar as 5 colunas em cada aula**

Run:
```bash
python3 - <<'EOF'
import re, pathlib
t = pathlib.Path(".ai/rules/08-lesson-roadmap.md").read_text(encoding="utf-8")
m2 = t.split("## Módulo 2")[1].split("## Módulos 2 a 4")[0]
for n in range(9, 16):
    bloco = re.split(rf"### Aula {n} —", m2)[1].split("### Aula")[0]
    faltando = [k for k in ["**Sintoma:**","**Conceitos:**","**Artefato:**","**Avaliação:**","**Ponte:**"] if k not in bloco]
    assert not faltando, f"Aula {n} sem: {faltando}"
    assert "*Mini-Orion:*" in bloco and "*Evolution Lab:*" in bloco, f"Aula {n} sem as duas trilhas"
print("7 aulas, 5 colunas cada, 2 trilhas cada: OK")
EOF
```
Expected: `7 aulas, 5 colunas cada, 2 trilhas cada: OK`.

- [ ] **Step 4: Commit**

```bash
git add .ai/rules/08-lesson-roadmap.md
git commit -m "$(printf 'roadmap: detalha as 7 aulas do Modulo 2 no formato de 5 colunas\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Task 4: Mini-Orion `04-camadas/`

**Files:**
- Create: `code/mini-orion/04-camadas/` (cópia reestruturada de `03-governado/`)
  - `mini_orion/apresentacao/app.py`
  - `mini_orion/aplicacao/checkout.py`
  - `mini_orion/dominio/__init__.py`, `mini_orion/dominio/modelos.py`, `mini_orion/dominio/contratos.py`
  - `mini_orion/infraestrutura/pagamentos.py`, `mini_orion/infraestrutura/notificacoes.py`, `mini_orion/infraestrutura/pedidos.py`
  - `mini_orion/__init__.py` e um `__init__.py` em cada subpacote
  - `setup.cfg`, `pytest.ini`
  - `tests/test_checkout.py`, `tests/test_camadas.py`, `tests/__init__.py`

**Interfaces:**
- Consumes: código de `code/mini-orion/03-governado/mini_orion/*.py` (ponto de partida).
- Produces: o estado `04-camadas` com o contrato `import-linter` `layers`. Nomes públicos preservados: `ServicoCheckout.fechar_pedido(carrinho, cliente) -> str`, `PedidoCobranca(valor, cartao, parcelas=1)`, `ResultadoCobranca`, `Gateway`, `Notificador`, `RepositorioPedidos.emitir(...)`, `FilaNotificacoes`, `NotificacaoTolerante`, `GatewayPagamentoX/Y/ForaDoAr`, `evento_de_confirmacao(pedido)`.

- [ ] **Step 1: Copiar o checkpoint anterior**

Run:
```bash
cd /home/eduardo/Documentos/IFC/Aulas/Fundamentos-Arquitetura/notas-aula-site/code/mini-orion
cp -r 03-governado 04-camadas
rm -rf 04-camadas/.pytest_cache 04-camadas/.import_linter_cache 04-camadas/mini_orion/__pycache__ 04-camadas/mini_orion.svg
```

- [ ] **Step 2: Escrever o teste-fitness das camadas (falhando)**

Criar `04-camadas/tests/test_camadas.py`:

```python
"""Fitness function da estrutura em camadas.

Le o codigo-fonte com `ast` (nao o namespace ja carregado) e verifica a
regra de dependencia: apresentacao > aplicacao > dominio, e o dominio
nao conhece infraestrutura.
"""

import ast
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent / "mini_orion"


def _imports(modulo: Path) -> set[str]:
    arvore = ast.parse(modulo.read_text(encoding="utf-8"))
    nomes: set[str] = set()
    for no in ast.walk(arvore):
        if isinstance(no, ast.Import):
            nomes.update(a.name for a in no.names)
        elif isinstance(no, ast.ImportFrom) and no.module:
            nomes.add(no.module)
    return nomes


def _imports_do_pacote(nome: str) -> set[str]:
    total: set[str] = set()
    for arq in (RAIZ / nome).rglob("*.py"):
        total |= _imports(arq)
    return total


def test_dominio_nao_importa_aplicacao_nem_infra_nem_apresentacao() -> None:
    proibidos = {
        "mini_orion.aplicacao",
        "mini_orion.infraestrutura",
        "mini_orion.apresentacao",
    }
    achados = {i for i in _imports_do_pacote("dominio")
               if any(i == p or i.startswith(p + ".") for p in proibidos)}
    assert not achados, f"dominio olhou para fora: {achados}"


def test_aplicacao_nao_importa_infra_nem_apresentacao() -> None:
    proibidos = {"mini_orion.infraestrutura", "mini_orion.apresentacao"}
    achados = {i for i in _imports_do_pacote("aplicacao")
               if any(i == p or i.startswith(p + ".") for p in proibidos)}
    assert not achados, f"aplicacao olhou para fora: {achados}"
```

- [ ] **Step 3: Rodar o teste e ver falhar**

Run:
```bash
cd code/mini-orion && python3 -m pytest 04-camadas/tests/test_camadas.py -v
```
Expected: FAIL (o pacote ainda é plano — `mini_orion.dominio` não existe; erro de import/coleta).

- [ ] **Step 4: Reestruturar o pacote em camadas**

- `mini_orion/dominio/modelos.py` ← conteúdo de `dominio.py` (Carrinho, Cliente, Pedido, ItemCarrinho).
- `mini_orion/dominio/contratos.py` ← conteúdo de `contratos.py`, ajustando `from mini_orion.dominio import Pedido` → `from mini_orion.dominio.modelos import Pedido`.
- `mini_orion/dominio/__init__.py` — re-exporta os nomes públicos de `modelos` e `contratos` (para preservar `from mini_orion.dominio import Carrinho`, `Gateway` etc.).
- `mini_orion/aplicacao/checkout.py` ← `checkout.py`, ajustando imports para `from mini_orion.dominio import (...)`.
- `mini_orion/infraestrutura/pagamentos.py`, `notificacoes.py`, `pedidos.py` ← respectivos, imports para `from mini_orion.dominio import (...)`.
- `mini_orion/apresentacao/app.py` — função `montar_servico(gateway, contingencia=None) -> ServicoCheckout` que faz a fiação (cria `RepositorioPedidos`, embrulha `FilaNotificacoes` em `NotificacaoTolerante`, injeta no `ServicoCheckout`). É a única camada que importa `aplicacao` **e** `infraestrutura`.
- `__init__.py` vazio em cada subpacote.
- Remover `mini_orion/dominio.py`, `contratos.py`, `checkout.py`, `pagamentos.py`, `notificacoes.py`, `pedidos.py` da raiz do pacote.

- [ ] **Step 5: Ajustar os testes de comportamento**

Em `04-camadas/tests/test_checkout.py`, trocar a função auxiliar `montar(...)` para usar `from mini_orion.apresentacao.app import montar_servico` (mantendo as asserções). Imports de `EventoNotificacao`, `ResultadoCobranca` passam a vir de `mini_orion.dominio`.

- [ ] **Step 6: Escrever o contrato `layers` no `setup.cfg`**

Substituir o `setup.cfg` por:

```ini
[importlinter]
root_package = mini_orion

[importlinter:contract:camadas]
name = Regra de dependencia: apresentacao > aplicacao > dominio
type = layers
layers =
    mini_orion.apresentacao
    mini_orion.aplicacao
    mini_orion.dominio

[importlinter:contract:dominio-nao-conhece-infra]
name = Dominio e aplicacao nao conhecem infraestrutura
type = forbidden
source_modules =
    mini_orion.dominio
    mini_orion.aplicacao
forbidden_modules =
    mini_orion.infraestrutura
```

- [ ] **Step 7: Rodar pytest e ver tudo passar**

Run:
```bash
cd code/mini-orion && python3 -m pytest 04-camadas -v
```
Expected: PASS em todos (comportamento + `test_camadas.py`).

- [ ] **Step 8: Rodar o import-linter e ver os contratos passarem**

Run:
```bash
cd code/mini-orion/04-camadas && python3 -m importlinter.cli lint --config setup.cfg || lint-imports
```
Expected: `Contracts: 2 kept, 0 broken.`

- [ ] **Step 9: Demonstrar que o contrato pega a regressão**

Run:
```bash
cd code/mini-orion/04-camadas
printf '\nfrom mini_orion.infraestrutura import pagamentos  # regressao proposital\n' >> mini_orion/dominio/modelos.py
lint-imports; echo "exit=$?"
git checkout -- mini_orion/dominio/modelos.py 2>/dev/null || sed -i '/regressao proposital/d' mini_orion/dominio/modelos.py
```
Expected: `1 broken` e `exit=1`; depois o arquivo volta ao estado bom.

- [ ] **Step 10: Rodar pytest de novo para confirmar reversão**

Run: `cd code/mini-orion && python3 -m pytest 04-camadas -q`
Expected: PASS.

- [ ] **Step 11: Commit**

```bash
git add code/mini-orion/04-camadas
git commit -m "$(printf 'mini-orion: checkpoint 04-camadas com contrato de camadas\n\nPacote plano de 03-governado reorganizado em apresentacao/aplicacao/\ndominio/infraestrutura. Contrato import-linter type=layers + forbidden\ndominio->infra. Testes de comportamento e fitness verdes.\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Task 5: Mini-Orion `05-modular/`

**Files:**
- Create: `code/mini-orion/05-modular/` (de `04-camadas/`, reagrupado por domínio)
  - `mini_orion/nucleo/modelos.py` — tipos compartilhados (Carrinho, Cliente, Pedido, ItemCarrinho)
  - `mini_orion/compra/api.py` — `ServicoCheckout`, `montar_servico`
  - `mini_orion/compra/_pedidos.py` — `RepositorioPedidos` (interno)
  - `mini_orion/pagamentos/api.py` — `Gateway`, `PedidoCobranca`, `ResultadoCobranca`
  - `mini_orion/pagamentos/_provedores.py` — `GatewayPagamentoX/Y/ForaDoAr` (interno)
  - `mini_orion/notificacoes/api.py` — `Notificador`, `EventoNotificacao`, `evento_de_confirmacao`
  - `mini_orion/notificacoes/_fila.py` — `FilaNotificacoes`, `NotificacaoTolerante` (interno)
  - `setup.cfg`, `pytest.ini`
  - `tests/test_checkout.py`, `tests/test_modular.py`, `tests/test_isolamento.py`

**Interfaces:**
- Consumes: `code/mini-orion/04-camadas/` (ponto de partida).
- Produces: o estado `05-modular`. API pública por módulo: `mini_orion.compra.api`, `mini_orion.pagamentos.api`, `mini_orion.notificacoes.api`. Regra: `compra` pode importar `pagamentos.api` e `notificacoes.api`, nunca os módulos `_*`; `pagamentos` e `notificacoes` não importam `compra` nem um ao outro.

- [ ] **Step 1: Copiar o checkpoint anterior**

Run:
```bash
cd /home/eduardo/Documentos/IFC/Aulas/Fundamentos-Arquitetura/notas-aula-site/code/mini-orion
cp -r 04-camadas 05-modular
rm -rf 05-modular/.pytest_cache 05-modular/.import_linter_cache 05-modular/mini_orion/**/__pycache__
```

- [ ] **Step 2: Escrever `tests/test_isolamento.py` (falhando)**

```python
"""Cada modulo de dominio se testa sem instanciar os outros."""

from mini_orion.pagamentos.api import PedidoCobranca, ResultadoCobranca
from mini_orion.pagamentos._provedores import GatewayPagamentoX
from mini_orion.notificacoes.api import EventoNotificacao
from mini_orion.notificacoes._fila import FilaNotificacoes, NotificacaoTolerante


def test_pagamentos_isolado() -> None:
    resultado = GatewayPagamentoX().cobrar(PedidoCobranca(valor=100.0, cartao="4111111111"))
    assert resultado is ResultadoCobranca.APROVADA


def test_notificacoes_isolado() -> None:
    fila = FilaNotificacoes()
    NotificacaoTolerante(fila).publicar(EventoNotificacao(destinatario="a@b.c", assunto="x"))
    assert len(fila.pendentes) == 1
```

- [ ] **Step 3: Escrever `tests/test_modular.py` (falhando)**

Fitness function por `ast` (mesmo molde do `test_camadas.py`): 
- `test_compra_nao_alcanca_internals()` — nenhum arquivo de `compra/` importa `mini_orion.pagamentos._provedores` nem `mini_orion.notificacoes._fila`.
- `test_pagamentos_nao_importa_compra_nem_notificacoes()`.
- `test_notificacoes_nao_importa_compra_nem_pagamentos()`.

- [ ] **Step 4: Rodar os dois e ver falhar**

Run: `cd code/mini-orion && python3 -m pytest 05-modular/tests/test_isolamento.py 05-modular/tests/test_modular.py -v`
Expected: FAIL (estrutura ainda em camadas; `mini_orion.pagamentos.api` não existe).

- [ ] **Step 5: Reagrupar por domínio**

- Mover `dominio/modelos.py` → `nucleo/modelos.py`. `nucleo/` é o *shared kernel*: só tipos de dados, sem comportamento de negócio.
- `pagamentos/api.py` ← parte de `dominio/contratos.py` referente a pagamentos (`Gateway`, `PedidoCobranca`, `ResultadoCobranca`).
- `pagamentos/_provedores.py` ← `infraestrutura/pagamentos.py`.
- `notificacoes/api.py` ← parte de `contratos.py` referente a notificações (`Notificador`, `EventoNotificacao`, `evento_de_confirmacao`).
- `notificacoes/_fila.py` ← `infraestrutura/notificacoes.py`.
- `compra/api.py` ← `aplicacao/checkout.py` (`ServicoCheckout`) + `apresentacao/app.py` (`montar_servico`), ajustando imports para `from mini_orion.pagamentos.api import ...`, `from mini_orion.notificacoes.api import ...`, `from mini_orion.compra._pedidos import RepositorioPedidos`.
- `compra/_pedidos.py` ← `infraestrutura/pedidos.py`.
- Remover os pacotes `dominio/`, `aplicacao/`, `apresentacao/`, `infraestrutura/`.
- `__init__.py` vazio em cada novo subpacote.

- [ ] **Step 6: Ajustar `tests/test_checkout.py`**

Imports: `from mini_orion.compra.api import ServicoCheckout, montar_servico`, `from mini_orion.pagamentos.api import ResultadoCobranca`, `from mini_orion.notificacoes.api import EventoNotificacao`. Asserções inalteradas.

- [ ] **Step 7: Escrever o `setup.cfg`**

```ini
[importlinter]
root_package = mini_orion

[importlinter:contract:pagamentos-e-notificacoes-independentes]
name = Pagamentos e Notificacoes nao se conhecem
type = independence
modules =
    mini_orion.pagamentos
    mini_orion.notificacoes

[importlinter:contract:downstream-nao-importa-compra]
name = Pagamentos e Notificacoes nao dependem de Compra
type = forbidden
source_modules =
    mini_orion.pagamentos
    mini_orion.notificacoes
forbidden_modules =
    mini_orion.compra

[importlinter:contract:sem-reach-in-nos-internals]
name = Ninguem alcanca os internals de outro modulo
type = forbidden
source_modules =
    mini_orion.compra
forbidden_modules =
    mini_orion.pagamentos._provedores
    mini_orion.notificacoes._fila
```

- [ ] **Step 8: Rodar pytest**

Run: `cd code/mini-orion && python3 -m pytest 05-modular -v`
Expected: PASS em todos.

- [ ] **Step 9: Rodar import-linter**

Run: `cd code/mini-orion/05-modular && lint-imports`
Expected: `Contracts: 3 kept, 0 broken.`

- [ ] **Step 10: Demonstrar a regressão**

Run:
```bash
cd code/mini-orion/05-modular
printf '\nfrom mini_orion.pagamentos._provedores import GatewayPagamentoX  # regressao\n' >> mini_orion/compra/api.py
lint-imports; echo "exit=$?"
sed -i '/# regressao/d' mini_orion/compra/api.py
lint-imports
```
Expected: primeiro `1 broken` / `exit=1`; depois `3 kept, 0 broken`.

- [ ] **Step 11: Commit**

```bash
git add code/mini-orion/05-modular
git commit -m "$(printf 'mini-orion: checkpoint 05-modular com modulos de dominio e API publica\n\nReagrupado por dominio (compra/pagamentos/notificacoes), cada um com\napi.py publico e internals _*. Contratos independence + forbidden\ncontra reach-in. Testes de isolamento por modulo verdes.\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Task 6: Mini-Orion `06-microkernel/` + README

**Files:**
- Create: `code/mini-orion/06-microkernel/` (de `05-modular/`, acrescentando `promocoes/`)
  - `mini_orion/promocoes/api.py` — `RegraDesconto` (Protocol), `Desconto` (dataclass), `MotorPromocoes` (núcleo)
  - `mini_orion/promocoes/_regras/cupom_percentual.py` — plugin de exemplo
  - `mini_orion/promocoes/_regras/frete_gratis_acima_de.py` — segundo plugin
  - `setup.cfg` (+1 contrato), `tests/test_microkernel.py`
- Modify: `code/mini-orion/README.md`

**Interfaces:**
- Consumes: `code/mini-orion/05-modular/`.
- Produces: o estado `06-microkernel`. `MotorPromocoes.registrar(regra: RegraDesconto) -> None`; `MotorPromocoes.aplicar(carrinho: Carrinho) -> list[Desconto]`. O núcleo (`promocoes/api.py`) **não** importa `promocoes._regras`.

- [ ] **Step 1: Copiar o checkpoint anterior**

```bash
cd /home/eduardo/Documentos/IFC/Aulas/Fundamentos-Arquitetura/notas-aula-site/code/mini-orion
cp -r 05-modular 06-microkernel
rm -rf 06-microkernel/.pytest_cache 06-microkernel/.import_linter_cache 06-microkernel/mini_orion/**/__pycache__
```

- [ ] **Step 2: Escrever `tests/test_microkernel.py` (falhando)**

```python
"""Microkernel de regras de desconto: nucleo estavel, plugins removiveis."""

import ast
from pathlib import Path

from mini_orion.nucleo.modelos import Carrinho, ItemCarrinho
from mini_orion.promocoes.api import MotorPromocoes
from mini_orion.promocoes._regras.cupom_percentual import CupomPercentual
from mini_orion.promocoes._regras.frete_gratis_acima_de import FreteGratisAcimaDe


def _carrinho() -> Carrinho:
    return Carrinho(itens=[ItemCarrinho(sku="TEC-01", preco_unitario=200.0, quantidade=1)])


def test_composicao_de_dois_plugins() -> None:
    motor = MotorPromocoes()
    motor.registrar(CupomPercentual(0.10))
    motor.registrar(FreteGratisAcimaDe(150.0))
    descontos = motor.aplicar(_carrinho())
    assert len(descontos) == 2


def test_motor_funciona_sem_nenhum_plugin() -> None:
    assert MotorPromocoes().aplicar(_carrinho()) == []


def test_nucleo_nao_importa_plugins_concretos() -> None:
    fonte = (Path(__file__).resolve().parent.parent
             / "mini_orion" / "promocoes" / "api.py").read_text(encoding="utf-8")
    for no in ast.walk(ast.parse(fonte)):
        if isinstance(no, ast.ImportFrom) and no.module:
            assert "_regras" not in no.module, f"nucleo importou plugin: {no.module}"
```

- [ ] **Step 3: Rodar e ver falhar**

Run: `cd code/mini-orion && python3 -m pytest 06-microkernel/tests/test_microkernel.py -v`
Expected: FAIL (`mini_orion.promocoes` não existe).

- [ ] **Step 4: Implementar o núcleo `promocoes/api.py`**

```python
"""Nucleo do microkernel de promocoes.

O nucleo conhece o CONTRATO de uma regra (`RegraDesconto`) e sabe
compor regras registradas. Nao conhece nenhuma regra concreta — essas
vivem em `_regras/` e sao injetadas via `registrar`.
"""

from dataclasses import dataclass
from typing import Protocol

from mini_orion.nucleo.modelos import Carrinho


@dataclass(frozen=True)
class Desconto:
    origem: str
    valor: float


class RegraDesconto(Protocol):
    def avalia(self, carrinho: Carrinho) -> Desconto | None: ...


class MotorPromocoes:
    def __init__(self) -> None:
        self._regras: list[RegraDesconto] = []

    def registrar(self, regra: RegraDesconto) -> None:
        self._regras.append(regra)

    def aplicar(self, carrinho: Carrinho) -> list[Desconto]:
        resultados = (r.avalia(carrinho) for r in self._regras)
        return [d for d in resultados if d is not None]
```

- [ ] **Step 5: Implementar os dois plugins**

`_regras/cupom_percentual.py`:
```python
from dataclasses import dataclass

from mini_orion.nucleo.modelos import Carrinho
from mini_orion.promocoes.api import Desconto


@dataclass
class CupomPercentual:
    fracao: float

    def avalia(self, carrinho: Carrinho) -> Desconto | None:
        if self.fracao <= 0:
            return None
        return Desconto(origem="cupom_percentual", valor=carrinho.total * self.fracao)
```

`_regras/frete_gratis_acima_de.py`:
```python
from dataclasses import dataclass

from mini_orion.nucleo.modelos import Carrinho
from mini_orion.promocoes.api import Desconto

FRETE_PADRAO = 25.0


@dataclass
class FreteGratisAcimaDe:
    piso: float

    def avalia(self, carrinho: Carrinho) -> Desconto | None:
        if carrinho.total < self.piso:
            return None
        return Desconto(origem="frete_gratis", valor=FRETE_PADRAO)
```

`_regras/__init__.py` vazio.

- [ ] **Step 6: Acrescentar o contrato ao `setup.cfg`**

```ini
[importlinter:contract:nucleo-nao-conhece-plugins]
name = O nucleo de promocoes nao importa regras concretas
type = forbidden
source_modules =
    mini_orion.promocoes.api
forbidden_modules =
    mini_orion.promocoes._regras
```

- [ ] **Step 7: Rodar pytest e import-linter**

Run:
```bash
cd code/mini-orion && python3 -m pytest 06-microkernel -q
cd 06-microkernel && lint-imports
```
Expected: pytest PASS; `Contracts: 4 kept, 0 broken.`

- [ ] **Step 8: Demonstrar a regressão**

Run:
```bash
cd code/mini-orion/06-microkernel
printf '\nfrom mini_orion.promocoes._regras.cupom_percentual import CupomPercentual  # regressao\n' >> mini_orion/promocoes/api.py
lint-imports; echo "exit=$?"
sed -i '/# regressao/d' mini_orion/promocoes/api.py
lint-imports
```
Expected: `1 broken` / `exit=1`; depois `4 kept, 0 broken`.

- [ ] **Step 9: Atualizar `code/mini-orion/README.md`**

Acrescentar à tabela/lista de estados as três novas linhas, no mesmo formato das existentes:

| Estado | O que tem | Aulas |
|---|---|---|
| `04-camadas` | pacote em camadas técnicas, contrato `layers` | 10 |
| `05-modular` | módulos de domínio com API pública, contratos `independence`/`forbidden` | 11–12 |
| `06-microkernel` | `Promocoes` como registro de plugins, contrato núcleo↛plugin | 13 |

E uma frase: a leitura mais proveitosa continua sendo comparar os **contratos de `setup.cfg`** de um estado para o outro antes de comparar o código.

- [ ] **Step 10: Commit**

```bash
git add code/mini-orion/06-microkernel code/mini-orion/README.md
git commit -m "$(printf 'mini-orion: checkpoint 06-microkernel e README dos tres estados novos\n\nPromocoes como microkernel: nucleo MotorPromocoes + RegraDesconto, dois\nplugins em _regras/, contrato forbidden nucleo->_regras. README lista\n04-camadas, 05-modular e 06-microkernel.\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Task 7: CI do Mini-Orion

**Files:**
- Create: `.github/workflows/mini-orion.yml`

**Interfaces:**
- Consumes: os seis checkpoints `code/mini-orion/0{1..6}-*/`.
- Produces: um workflow que roda `pytest` e `lint-imports` em cada checkpoint. Fecha o backlog #4.

- [ ] **Step 1: Escrever o workflow**

```yaml
name: mini-orion

on:
  push:
    branches: [main]
    paths: ["code/mini-orion/**", ".github/workflows/mini-orion.yml"]
  pull_request:
    paths: ["code/mini-orion/**"]

jobs:
  checkpoints:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        checkpoint:
          - "01-acoplado"
          - "02-fronteiras"
          - "03-governado"
          - "04-camadas"
          - "05-modular"
          - "06-microkernel"
    defaults:
      run:
        working-directory: code/mini-orion/${{ matrix.checkpoint }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r ../requirements-dev.txt
      - run: python -m pytest -q
      - run: lint-imports
        if: hashFiles('code/mini-orion/${{ matrix.checkpoint }}/setup.cfg') != ''
```

- [ ] **Step 2: Validar o YAML**

Run:
```bash
python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/mini-orion.yml')); print('YAML OK')"
```
Expected: `YAML OK`. (Se `pyyaml` não estiver disponível, rodar `python3 -c "import json"` não ajuda — nesse caso conferir a indentação manualmente contra `.github/workflows/ci.yml`.)

- [ ] **Step 3: Rodar localmente o que a CI rodaria**

Run:
```bash
cd code/mini-orion
for c in 01-acoplado 02-fronteiras 03-governado 04-camadas 05-modular 06-microkernel; do
  echo "== $c =="; ( cd "$c" && python3 -m pytest -q && { [ -f setup.cfg ] && lint-imports || echo "sem setup.cfg"; } )
done
```
Expected: todos os checkpoints com pytest PASS; `03`–`06` com `Contracts: N kept, 0 broken`.

- [ ] **Step 4: Atualizar `12-backlog.md`**

Mover o item 4 ("Mini-Orion sem CI") para a seção "Resolvido", com uma linha explicando que `mini-orion.yml` roda `pytest` + `lint-imports` nos seis checkpoints.

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/mini-orion.yml .ai/rules/12-backlog.md
git commit -m "$(printf 'ci: job que roda pytest e lint-imports nos 6 checkpoints do mini-orion\n\nFecha o backlog #4. Separado do build do site (que instala so zensical).\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Task 8: Estender os formatos do Evolution Lab em `docs/orion/index.md`

**Files:**
- Modify: `docs/orion/index.md`

**Interfaces:**
- Consumes: agrupamento de domínios da Task 1.
- Produces: formato "tabela de arestas inter-módulo" e o campo "critério de parada" na proposta de evolução — referenciados pelas Aulas 12 e 15.

- [ ] **Step 1: Acrescentar a camada de módulos ao artefato "Mapa de componentes e dependências"**

Na seção "1. Mapa de componentes e dependências", acrescentar um parágrafo: a partir da Aula 11, o mapa ganha uma segunda leitura — cada componente pertence a um módulo de domínio, e o diagrama marca quais arestas ficam dentro de um módulo e quais atravessam fronteira.

- [ ] **Step 2: Acrescentar o artefato "Tabela de arestas inter-módulo"**

Novo item numerado (entre o mapa e o registro de diagnóstico ou logo após o mapa):

```markdown
### Tabela de arestas inter-módulo

A partir da Aula 12.

| Origem (módulo) | Destino (módulo) | Fronteira justificada por |
|---|---|---|

Confiram: arestas internas + inter-módulo = total de arestas do recorte.
Ciclo entre módulos é bloqueio de extração — nomeiem o custo de removê-lo.
```

- [ ] **Step 3: Acrescentar "critério de parada" à Proposta de evolução**

Na seção "5. Proposta de evolução", acrescentar: além das no máximo três ações, a proposta declara um **critério de parada** — até que ponto modularizar, e por que não distribuir além disso. Proposta sem critério de parada tem teto de nota.

- [ ] **Step 4: Verificar que nada quebrou o formato**

Run: `grep -nE '^### |^## ' docs/orion/index.md`
Expected: a lista de seções continua coerente; os artefatos numerados seguem em ordem.

- [ ] **Step 5: Commit**

```bash
git add docs/orion/index.md
git commit -m "$(printf 'orion-lab: tabela de arestas inter-modulo e criterio de parada\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Convenções para as Tasks 9–15 (aulas)

Cada aula é um arquivo em `docs/modulo2/` e uma linha nova no `nav` de `mkdocs.yml`. Toda aula tem as **seis seções obrigatórias** de `02-lesson-structure.md` (os títulos variam por aula, a função não):

1. Objetivo e competências — verbo de ação, curto.
2. Sintoma — o fato do Orion que abre a aula (texto na tarefa).
3. Desenvolvimento — o conteúdo conceitual, amarrado ao sintoma.
4. Decisão sobre o Orion — o artefato: ADR, refatoração do Mini-Orion, contrato de linter, mapa.
5. Trabalho do aluno — `## Exercícios` (4 questões, ver Global Constraints) + `## Atividade em grupo`.
6. Fechamento e ponte — o que ficou decidido + a pergunta que a próxima aula abre (texto na tarefa).

**Verificação comum a toda aula (rodar antes do commit):**

```bash
ARQ=docs/modulo2/<arquivo-da-aula>.md
wc -l "$ARQ"   # 200–320 para aula conceitual; a oficina pode exceder
grep -nEi 'obviamente|claramente|evidentemente|como todos sabem|é sabido que|\bbasta\b|simplesmente|\bé só\b|a melhor prática é|o correto é|nesta aula (aprenderemos|estudaremos)|é importante ressaltar' "$ARQ" || echo "sem expressoes proibidas: OK"
grep -nE 'xychart-beta|-beta' "$ARQ" || echo "sem mermaid beta: OK"
# orfaos: nenhuma saida = OK
comm -23 <(find docs -name '*.md' | sed 's|^docs/||' | sort) <(grep -oE '[a-z0-9_/-]+\.md' mkdocs.yml | sort -u)
# anti-boilerplate: comparar titulos com a aula anterior
diff <(grep -E '^#{2,3} ' docs/modulo2/<aula-anterior>.md) <(grep -E '^#{2,3} ' "$ARQ")
```
Nenhuma expressão proibida; nenhum `-beta`; saída vazia no `comm`; menos da metade dos títulos coincidindo no `diff`.

Se `zensical` estiver instalado: `zensical build --clean` sem erro e abrir a página nos temas claro e escuro. Se não estiver, registrar isso como pendência de verificação de build (backlog #1) e seguir.

**Números:** só de `05-domain.md`. Os que este módulo usa: 17 arestas; 10 componentes; 15 arestas inter-módulo, 2 internas; `Checkout` $C_e = 5$, $D = 0{,}03$, em 5 arestas inter-módulo; `Integracoes` $C_a = 0$, $C_e = 3$, $A = 0{,}83$, $D = 0{,}83$; `Catalogo` $C_a = 4$, $D = 0{,}90$; `Clientes` $C_a = 2$, $D = 1{,}00$; `Notificacoes` $C_a = 4$, $C_e = 0$.

---

## Task 9: Aula 9 — O monólito não é o problema + índice do módulo + `nav`

**Files:**
- Create: `docs/modulo2/index.md`
- Create: `docs/modulo2/aula09-monolito-nao-e-o-problema.md`
- Modify: `mkdocs.yml` (bloco de `nav` do Módulo 2)

**Interfaces:**
- Consumes: Tasks 1–3.
- Produces: a página inicial do módulo; a Aula 9; o bloco `nav` do Módulo 2 (as 7 linhas, todas apontando para arquivos que serão criados nas Tasks 9–15 — por isso o `nav` recebe só a linha da Aula 9 agora, e cada tarefa seguinte acrescenta a sua).

- [ ] **Step 1: Criar `docs/modulo2/index.md`**

Visão geral do módulo. **Não** clonar `docs/modulo1/index.md`. Conteúdo próprio:
- Abertura pela tese do módulo: o Módulo 1 diagnosticou o monólito do Orion; a Aula 8 perguntou se ele é problema. A resposta do Módulo 2 é que o monólito é uma decisão legítima e revisável — o que trava não é o empacotamento, é a falta de fronteira interna.
- Tabela das 4 semanas com as 7 aulas (semana 8 = oficina em dois encontros).
- Um `mindmap` Mermaid com os quatro estilos de monólito (camadas, modular, pipeline, microkernel) pendurados em "monólito estruturado", e "distribuir" como ramo separado marcado "Módulo 3". Declarar o que o diagrama não mostra (não é ordem de aula, é espaço de opções).
- Frase sobre o Mini-Orion: evolui de `03-governado` por `04-camadas` → `05-modular` → `06-microkernel`; a leitura proveitosa é comparar os contratos de `setup.cfg`.
- Link para `../orion/index.md`.

- [ ] **Step 2: Escrever a Aula 9**

- **Objetivo:** distinguir monólito (empacotamento) de ausência de arquitetura; escrever um ADR que fixa "não distribuir agora" com gatilho de reversão.
- **Sintoma (texto-base, expandir para ~2 parágrafos):** numa reunião de planejamento trimestral, a diretoria da Orion pede um "plano de migração para microsserviços" para o ano seguinte. O pedido trata o monólito como dívida a quitar. Quando o time pergunta o que a migração resolveria, a resposta é "monólito não escala" — sem apontar qual parte, sob qual carga, com qual evidência.
- **Desenvolvimento:** monólito = uma decisão de empacotamento e deploy, não a ausência de fronteiras; *big ball of mud* × monólito estruturado (o Orion hoje é o primeiro); o que a distribuição cobra todo dia — latência de rede, falha parcial, transação sem garantia, operação e observabilidade (só nomear; o Módulo 3 mede); a pergunta certa não é "quando sair do monólito", é "o que na estrutura interna trava a entrega". Reusar o vocabulário do Módulo 1: os três contratos de `import-linter` de `03-governado` já são fronteira interna.
- **Decisão sobre o Orion:** ADR "Orion permanece um único *deployable* pelos próximos 12 meses". Mostrar o ADR completo no formato de `09-assessment.md`, com alternativa real (começar a extrair `Pagamentos` já), consequência negativa aceita (um bug de `Catalogo` ainda pode derrubar o checkout), e gatilho de reversão observável (ex.: "a fila de deploy de um módulo bloquear release de outro mais de uma vez por sprint durante um trimestre").
- **Trabalho do aluno:** 4 exercícios — (1) verificação: classificar afirmações sobre monólito em verdadeiras/falsas com justificativa; (2) aplicação: dado um trecho de log de incidente do Orion, dizer se ele sustenta ou não "precisamos de microsserviços"; (3) aplicação: completar um ADR a que falta a consequência negativa e a reversão; (4) julgamento: "a Orion deveria começar a extrair agora?" — critério de avaliação em vez de resposta, dizendo que as duas posições são defensáveis. `## Atividade em grupo`: o grupo escreve o ADR de não-distribuir para o próprio recorte, e o item obrigatório é nomear a condição sob a qual esse ADR estaria errado.
- **Fechamento e ponte:** ficou decidido não distribuir e por quê. Ponte: que estrutura interna o Orion tem hoje? Quase nenhuma imposta — só sugerida pela nomeação dos componentes. A Aula 10 olha para isso.
- Diagrama: um `flowchart` do grafo oficial (17 arestas) com uma legenda dizendo "nenhuma fronteira interna imposta — só nomes". Declarar o que omite (não mostra volume de tráfego nem quais arestas doem).

- [ ] **Step 3: Acrescentar o bloco `nav` do Módulo 2**

Em `mkdocs.yml`, após o bloco do Módulo 1 e antes de `- Orion Evolution Lab:`:

```yaml
  - Módulo 2 — Arquiteturas Monolíticas:
    - Visão geral do módulo: modulo2/index.md
    - Aula 9 — O monólito não é o problema: modulo2/aula09-monolito-nao-e-o-problema.md
```

- [ ] **Step 4: Verificação comum das aulas**

Rodar o bloco de verificação da seção "Convenções para as Tasks 9–15" com `ARQ=docs/modulo2/aula09-monolito-nao-e-o-problema.md` e `<aula-anterior>` = `../modulo1/aula08-oficina-diagnostico.md`. Confirmar `comm` vazio (index.md e aula09 ambos no `nav`).

- [ ] **Step 5: Commit**

```bash
git add docs/modulo2/index.md docs/modulo2/aula09-monolito-nao-e-o-problema.md mkdocs.yml
git commit -m "$(printf 'aula 9: O monolito nao e o problema + indice do Modulo 2\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Task 10: Aula 10 — Monólito em camadas: o que governa e o que não isola

**Files:**
- Create: `docs/modulo2/aula10-monolito-em-camadas.md`
- Modify: `mkdocs.yml` (+1 linha no `nav`)

**Interfaces:**
- Consumes: Task 4 (`code/mini-orion/04-camadas/`), Task 9.

- [ ] **Step 1: Escrever a Aula 10**

- **Objetivo:** aplicar a regra de dependência de camadas; reconhecer quando a camada técnica **não** isola uma mudança.
- **Sintoma:** dois integrantes desenham "a arquitetura do Orion" e os desenhos não batem (um põe camadas, o outro diz que não há). O grafo oficial mostra `Portal → Catalogo` direto e `Checkout` dependendo de cinco componentes: nenhuma camada imposta. Semanas depois, uma mudança de "cupom de frete grátis" toca `Portal`, `Checkout`, `Promocoes` e `Pedidos` — quatro componentes para uma regra só.
- **Desenvolvimento:** camadas técnicas (apresentação/aplicação/domínio/infraestrutura); camada fechada × aberta; a regra de dependência apontando para dentro; **o que a camada governa** — a direção da dependência, agora verificável; **o que a camada não isola** — mudança de negócio é vertical, camada é horizontal; coesão por camada é coesão fraca (agrupa "todos os serviços" por serem serviços); por que $C_a$/$C_e$ por camada não revelam esse custo; connascência que atravessa a camada (retomar os três eixos do Módulo 1).
- **Decisão sobre o Orion:** recorte do Mini-Orion `04-camadas/` — mostrar (a) o `setup.cfg` com o contrato `layers`, (b) a saída de `lint-imports` (`2 kept`), (c) a saída quando `dominio` importa `infraestrutura` (`1 broken`). E um registro curto de diagnóstico: dois pontos onde a camada ajuda (direção de dependência; trocar `GatewayPagamentoX` por `Y` sem tocar em `aplicacao`), dois onde não (mudança de regra; testar uma regra isolada).
- **Trabalho do aluno:** 4 exercícios — (1) verificação: rotular imports como "permitido / proibido" pela regra de camadas; (2) aplicação: dado um diff que quebra a regra, dizer qual contrato falha e por quê; (3) aplicação: para uma mudança de negócio dada, listar quantas camadas ela atravessa e por quê; (4) julgamento: "camadas fechadas ou abertas para o Orion?" — critério, não resposta. `## Atividade em grupo`: reler o mapa do grupo como camadas; item obrigatório — apontar o componente que não encaixa em camada nenhuma e dizer o que isso revela.
- **Fechamento e ponte:** camadas governam a direção das dependências e ainda assim a mudança de cupom tocou quatro componentes. Ponte: e se cada assunto de negócio fosse uma caixa com uma porta só?
- Diagrama: um `flowchart` com as três camadas do Mini-Orion e as setas entre elas; e, ao lado no texto, a observação de que a mudança de negócio "corta" as três de cima a baixo. Declarar o que omite (não mostra `infraestrutura` como sibling nem a fiação em `apresentacao`).

- [ ] **Step 2: `nav`** — acrescentar `- Aula 10 — Monólito em camadas: modulo2/aula10-monolito-em-camadas.md`.

- [ ] **Step 3: Verificação comum** — `ARQ=docs/modulo2/aula10-...`, `<aula-anterior>`=`aula09-...`.

- [ ] **Step 4: Commit** — `aula 10: Monolito em camadas` + trailers.

---

## Task 11: Aula 11 — Monólito modular: fronteira lógica sem fronteira física

**Files:**
- Create: `docs/modulo2/aula11-monolito-modular.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: Task 5 (`code/mini-orion/05-modular/`), Task 10.

- [ ] **Step 1: Escrever a Aula 11**

- **Objetivo:** definir módulo de domínio, API pública e *internals*; distinguir fronteira lógica de fronteira física.
- **Sintoma:** `Promocoes` de novo. A pergunta: o que muda se ninguém puder importar o interior de `Promocoes`, só a sua API?
- **Desenvolvimento:** módulo de domínio; API pública × *internals* (`_*`); encapsulamento no nível de pacote; **fronteira lógica** (imposta pelo linter/compilador) × **fronteira física** (imposta pela rede) — a segunda é o Módulo 3; a heurística de connascência do Módulo 1: forte fica dentro do módulo, só as fracas atravessam. Ponto honesto: no `05-modular/`, `compra` ainda depende de `pagamentos.api` e `notificacoes.api` — a fronteira é lógica, e independência total exigiria eventos (Módulo 4).
- **Decisão sobre o Orion:** recorte do `05-modular/` — a árvore de pacotes (`compra/api.py` + `compra/_pedidos.py`, etc.), o `setup.cfg` com `independence` + `forbidden` de *reach-in*, e o `tests/test_isolamento.py` rodando sem instanciar os outros módulos. O teste que passou a ser possível **é** a evidência.
- **Trabalho do aluno:** 4 exercícios — (1) verificação: dado um pacote, apontar o que é API e o que é *internal*; (2) aplicação: classificar 3 connascências entre módulos pelos três eixos e dizer se cada uma pode atravessar a fronteira; (3) aplicação: escrever a assinatura da API pública mínima de um módulo dado; (4) julgamento: "vale a pena a fronteira lógica sem a física?" — critério. `## Atividade em grupo`: definir os módulos de domínio do recorte e a API pública de cada; item obrigatório — nomear a dependência entre módulos que **não** dá para eliminar sem eventos.
- **Fechamento e ponte:** no Mini-Orion são três módulos; no Orion, dez componentes e dezessete arestas. Ponte: quais arestas atravessam fronteira de módulo?
- Diagrama: `flowchart` com `compra`, `pagamentos`, `notificacoes`, `nucleo`; setas só a partir de `compra` para as APIs; caixa tracejada em volta dos `_*` marcada "ninguém de fora entra aqui". Declarar o que omite (não mostra as classes dentro de cada módulo).

- [ ] **Step 2: `nav`** — `- Aula 11 — Monólito modular: modulo2/aula11-monolito-modular.md`.
- [ ] **Step 3: Verificação comum** — anterior = `aula10-...`.
- [ ] **Step 4: Commit** — `aula 11: Monolito modular` + trailers.

---

## Task 12: Aula 12 — Reorganizar o grafo do Orion

**Files:**
- Create: `docs/modulo2/aula12-reorganizar-o-grafo.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: Task 1 (agrupamento), Task 5 (referência resolvida), Task 8 (formato da tabela inter-módulo), Task 11.

- [ ] **Step 1: Escrever a Aula 12**

- **Objetivo:** aplicar o agrupamento de domínios ao grafo inteiro do Orion; medir arestas inter-módulo.
- **Sintoma:** o grafo oficial de dezessete arestas. Sem agrupamento, toda aresta parece igual; com módulos de domínio, algumas viram fronteira e outras, detalhe interno.
- **Desenvolvimento:** aplicar a tabela de 8 módulos de `05-domain.md`; aresta inter-módulo como o custo que se mede (15 de 17 no Orion — dizer explicitamente que isso significa "mal modularizado", e que é o ponto da aula, não uma falha do exercício); ciclo entre módulos como bloqueio de extração; `Integracoes` relido — módulo que ninguém importa ($C_a = 0$) não é fronteira, é peso morto; a *Zone of Uselessness* da Aula 7 vira problema de modularização, com a história do componente (de `05-domain.md`).
- **Decisão sobre o Orion:** o `05-modular/` do Mini-Orion como referência resolvida (2 arestas internas: `compra` interno; 0 ciclos). Para o Orion inteiro: a tabela de arestas inter-módulo preenchida com as 15 arestas e a fronteira de cada uma; destacar `Checkout` em 5 delas.
- **Trabalho do aluno:** 4 exercícios — (1) verificação: dada uma aresta, dizer se é interna ou inter-módulo pelo agrupamento; (2) aplicação: contar arestas inter-módulo de um recorte de 4 componentes e conferir a soma; (3) aplicação: apontar um ciclo entre módulos num recorte dado e o custo de removê-lo; (4) julgamento: "o agrupamento proposto é bom?" — critério; dizer que outro corte é defensável. `## Atividade em grupo`: preencher a tabela de arestas inter-módulo do recorte; item obrigatório — nomear a aresta que o grupo **não** consegue justificar como fronteira e o que isso sugere sobre o agrupamento.
- **Fechamento e ponte:** o Orion modular ainda roda como um processo só. Ponte: existem monólitos com forma além de camadas e módulos?
- Diagrama: o `flowchart` do grafo oficial com os 8 módulos como `subgraph`, arestas inter-módulo em destaque de forma (não cor — regra de `03-visual-language.md`). Declarar o que omite (não mostra direção de negócio nem frequência de mudança).

- [ ] **Step 2: `nav`** — `- Aula 12 — Reorganizar o grafo do Orion: modulo2/aula12-reorganizar-o-grafo.md`.
- [ ] **Step 3: Verificação comum** — anterior = `aula11-...`. Conferir à mão que todo número citado (15, 17, 2, 5, $C_a$ de `Integracoes`) bate com `05-domain.md`.
- [ ] **Step 4: Commit** — `aula 12: Reorganizar o grafo do Orion` + trailers.

---

## Task 13: Aula 13 — Pipeline e microkernel: monólitos com forma

**Files:**
- Create: `docs/modulo2/aula13-pipeline-e-microkernel.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: Task 6 (`code/mini-orion/06-microkernel/`), Task 12.

- [ ] **Step 1: Escrever a Aula 13**

- **Objetivo:** reconhecer quando pipeline ou microkernel são a forma certa de um monólito; nomear o custo do microkernel.
- **Sintoma:** `fechar_pedido` do Mini-Orion é uma sequência fixa — validar, montar, cobrar, emitir, notificar. E `Promocoes` recebe um tipo novo de regra de desconto quase todo trimestre, sempre exigindo deploy do sistema inteiro.
- **Desenvolvimento:** arquitetura em pipeline — filtros, fluxo unidirecional, quando o domínio *é* uma transformação; microkernel — núcleo estável + plugins, quando a variação é conhecida e recorrente; os dois como formas de monólito, não saídas dele; o trade-off do microkernel — deploy isolado da regra × contrato de plugin, teste de composição, risco de plugin mal-comportado.
- **Decisão sobre o Orion:**
  - *Snippet ilustrativo* (nomes genéricos, não os do Mini-Orion): o checkout como pipeline de filtros — `FiltroValidacao`, `FiltroMontagem`, `FiltroCobranca`… encadeados. Declarar que é ilustrativo.
  - *Recorte do Mini-Orion `06-microkernel/`*: `promocoes/api.py` (`MotorPromocoes`, `RegraDesconto`), um plugin de `_regras/`, o contrato núcleo↛plugin no `setup.cfg`, e `test_microkernel.py` (composição de dois plugins; motor sem plugin nenhum).
  - *ADR* "regra de desconto como plugin de `Promocoes`" — formato completo, com o custo nomeado (contrato de plugin a manter; teste de composição a cada regra nova; um plugin que lança exceção derruba a aplicação do desconto).
- **Trabalho do aluno:** 4 exercícios — (1) verificação: dado um domínio, dizer se pipeline se aplica e por quê; (2) aplicação: reordenar/edição de um pipeline dado e dizer o efeito; (3) aplicação: escrever a assinatura de um plugin para um `RegraDesconto` novo; (4) julgamento: "`Promocoes` como microkernel vale o custo?" — critério. `## Atividade em grupo`: identificar no recorte um ponto candidato a pipeline **ou** a microkernel; item obrigatório — nomear o custo que a forma escolhida cobra.
- **Fechamento e ponte:** pipeline e microkernel adiam a distribuição, não a substituem. Ponte: quando ela deixa de ser adiável?
- Diagrama: um `flowchart` do pipeline do checkout (5 filtros em linha) **ou** um `flowchart` núcleo-e-plugins do microkernel — um diagrama por ideia (`02-lesson-structure.md`); escolher o do microkernel, que é o que tem código. Declarar o que omite.

- [ ] **Step 2: `nav`** — `- Aula 13 — Pipeline e microkernel: modulo2/aula13-pipeline-e-microkernel.md`.
- [ ] **Step 3: Verificação comum** — anterior = `aula12-...`. Conferir que o snippet de pipeline **não** usa nomes do Mini-Orion (`grep -E 'ServicoCheckout|PedidoCobranca|MotorPromocoes' no bloco do snippet` deve dar vazio).
- [ ] **Step 4: Commit** — `aula 13: Pipeline e microkernel` + trailers.

---

## Task 14: Aula 14 — Quando o monólito deixa de servir

**Files:**
- Create: `docs/modulo2/aula14-quando-o-monolito-deixa-de-servir.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: Task 11 (`05-modular/` como referência), Task 13.

- [ ] **Step 1: Escrever a Aula 14**

- **Objetivo:** distinguir sinais legítimos de extração dos ilegítimos; nomear o que a extração custa.
- **Sintoma:** a conciliação de `Pagamentos` em campanha precisa reprocessar em lote num ritmo próprio, com janela de manutenção própria, e hoje sobe e desce junto com o checkout. É o primeiro caso no Orion em que uma parte tem requisito operacional genuinamente diferente do resto.
- **Desenvolvimento:** sinais legítimos — escala independente, cadência de release própria, isolamento de falha, autonomia de time; ilegítimos — moda, estética, "monólito é feio"; o monólito modular como pré-condição (não se extrai o que não tem fronteira — retomar o `05-modular/`); o que se perde ao extrair — transação local, deploy único, teste sem rede.
- **Decisão sobre o Orion:** ADR "candidato a extração" — qual módulo do `05-modular/` (o `pagamentos`, pelo sintoma), sob que gatilho mensurável, e o que ainda **não** justifica extrair. Formato completo; falseabilidade obrigatória ("estaria errado se, medido durante um trimestre, a cadência de release de `pagamentos` não divergir da dos demais módulos").
- **Trabalho do aluno:** 4 exercícios — (1) verificação: rotular sinais como legítimos/ilegítimos para extração; (2) aplicação: dado um cenário do Orion, dizer se o sinal justifica extrair; (3) aplicação: completar um ADR de candidato a extração a que falta o gatilho e a falseabilidade; (4) julgamento: "extrair `Pagamentos` agora?" — critério; as duas posições defensáveis. `## Atividade em grupo`: escrever o ADR de candidato a extração do recorte; item obrigatório — nomear o que o grupo perde ao extrair esse módulo.
- **Fechamento e ponte:** se a decisão for extrair, tudo o que a rede cobra entra na conta. Ponte: é isso que o Módulo 3 mede antes de recomendar qualquer coisa.
- Diagrama: `quadrantChart` com eixos "cadência de release própria" × "escala própria", posicionando 3–4 módulos do Orion; `pagamentos` no quadrante alto-alto. Declarar o que omite (posições são qualitativas, não medidas).

- [ ] **Step 2: `nav`** — `- Aula 14 — Quando o monólito deixa de servir: modulo2/aula14-quando-o-monolito-deixa-de-servir.md`.
- [ ] **Step 3: Verificação comum** — anterior = `aula13-...`.
- [ ] **Step 4: Commit** — `aula 14: Quando o monolito deixa de servir` + trailers.

---

## Task 15: Aula 15 — Oficina: o Orion modular sob restrição

**Files:**
- Create: `docs/modulo2/aula15-oficina-orion-modular.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: Tasks 9–14 (todo o vocabulário do módulo); Task 8 (critério de parada).

- [ ] **Step 1: Escrever a Aula 15 (oficina — pode exceder 320 linhas com material de apoio)**

- **Objetivo:** produzir uma proposta de modularização priorizada, com ordem de fronteiras, contratos de CI, métrica de acompanhamento e critério de parada.
- **Sintoma:** a diretoria aprovou "modularizar antes de distribuir" e quer um plano com marcos, ordem e critério de parada.
- **Desenvolvimento:** nenhum conceito novo — roteiro da oficina para os dois encontros. Encontro 1: revisar o agrupamento do recorte, a tabela de arestas inter-módulo e os ciclos; priorizar quais fronteiras introduzir primeiro (critério: quanto acoplamento inter-módulo cada fronteira remove × custo de introduzi-la). Encontro 2: transformar as 3 fronteiras prioritárias em contratos de `import-linter` para a CI; definir a métrica de acompanhamento (nº de arestas inter-módulo, nº de ciclos); redigir o critério de parada. Incluir uma tabela de orçamento de tempo (de `09-assessment.md`) para o roteiro caber.
- **Decisão sobre o Orion:** o roteiro produz a **Proposta de modularização** do Evolution Lab — no formato de `docs/orion/index.md`, com o campo "critério de parada" novo.
- **Trabalho do aluno:** exceção à regra dos 4 exercícios (`01-pedagogy.md`): um **aquecimento individual sem gabarito** — cada aluno traz, antes do encontro 1, três arestas inter-módulo do recorte já classificadas. A oficina em si é a atividade.
- **Fechamento e ponte:** o Orion está modular e continua um processo só. Ponte: o Módulo 3 pergunta o que muda quando uma dessas fronteiras vira uma chamada de rede — e por que a resposta raramente compensa.
- Diagrama: `timeline` dos marcos de modularização (fronteira 1 → contrato na CI → fronteira 2 → …). Declarar o que omite (não é cronograma com datas; é ordem).

- [ ] **Step 2: `nav`** — `- Aula 15 — Oficina: o Orion modular: modulo2/aula15-oficina-orion-modular.md`.
- [ ] **Step 3: Verificação comum** — anterior = `aula14-...`. Aceitar > 320 linhas se o excedente for material de apoio (tabela de orçamento, roteiro), não exposição.
- [ ] **Step 4: Commit** — `aula 15: Oficina - o Orion modular sob restricao` + trailers.

---

## Task 16: Revisão e verificação do módulo inteiro

**Files:**
- Modify (se a revisão exigir): qualquer arquivo de `docs/modulo2/`, `mkdocs.yml`, `.ai/rules/12-backlog.md`

**Interfaces:**
- Consumes: Tasks 1–15.

- [ ] **Step 1: Checklist de revisão aula a aula**

Para cada uma das 7 aulas, rodar o `.ai/rules/11-review-checklist.md` item a item. Registrar num comentário do commit final quais aulas passaram e o que foi ajustado.

- [ ] **Step 2: Verificar órfãos e nomes de módulo**

Run:
```bash
cd /home/eduardo/Documentos/IFC/Aulas/Fundamentos-Arquitetura/notas-aula-site
comm -23 <(find docs -name '*.md' | sed 's|^docs/||' | sort) <(grep -oE '[a-z0-9_/-]+\.md' mkdocs.yml | sort -u)
grep -c 'modulo2/aula' mkdocs.yml   # deve ser 7
```
Expected: `comm` sem saída; contagem `7`.

- [ ] **Step 3: Verificar Mermaid e expressões proibidas no módulo todo**

Run:
```bash
grep -rnE '-beta' docs/modulo2/ || echo "sem mermaid beta: OK"
grep -rnEi 'obviamente|claramente|evidentemente|como todos sabem|é sabido que|\bbasta\b|simplesmente|\bé só\b|a melhor prática é|o correto é|nesta aula (aprenderemos|estudaremos)|é importante ressaltar' docs/modulo2/ || echo "sem expressoes proibidas: OK"
```
Expected: ambas as linhas "OK".

- [ ] **Step 4: Verificar os números contra `05-domain.md`**

Run: `grep -rnoE '\b(17|15|10|[0-9],[0-9]{2})\b' docs/modulo2/*.md` e conferir cada ocorrência contra a tabela e o grafo de `05-domain.md`. Nenhum número sem origem no documento de domínio.

- [ ] **Step 5: Build (best effort)**

Run: `zensical build --clean 2>&1 | tail -20`
Expected: build sem erro. Se `zensical` não estiver instalado, registrar no `12-backlog.md` (item 1) que o build do Módulo 2 continua não verificado e seguir — **não** instalar nada além do que já existe.

- [ ] **Step 6: Anti-boilerplate — varredura final**

Run:
```bash
for a in 09 10 11 12 13 14; do
  b=$((a+1)); [ "$b" -lt 10 ] && b="0$b"
  echo "== aula$a x aula$b =="
  diff <(grep -E '^#{2,3} ' docs/modulo2/aula$a-*.md) <(grep -E '^#{2,3} ' docs/modulo2/aula$b-*.md) | grep -c '^>'
done
```
Expected: para cada par, a contagem de títulos idênticos é menos da metade dos títulos da aula. Onde não for, reescrever os títulos da aula posterior.

- [ ] **Step 7: Atualizar `12-backlog.md`**

- Item 6 ("Módulos 2 a 4 não escritos") → passa a "Módulos 3 e 4 não escritos"; registrar que o Módulo 2 está escrito e publicado no `nav`, com os checkpoints `04`–`06` do Mini-Orion.
- Confirmar que o item 4 já foi para "Resolvido" na Task 7.

- [ ] **Step 8: Commit final**

```bash
git add -A
git commit -m "$(printf 'modulo 2: revisao final, verificacao de nav/numeros/boilerplate, backlog\n\nChecklist 11 aplicado nas 7 aulas. Orfaos: nenhum. Numeros conferidos\ncontra 05-domain.md. Backlog #6 atualizado.\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_013Rfq2SSrHESURLW3XDgVmw')"
```

---

## Auto-revisão do plano (feita — registro)

**Cobertura da spec:**
- §1 enquadramento → Tasks 9–15 (conteúdo) + Task 3 (roadmap).
- §2 extensão de `05-domain.md` → Task 1.
- §3 roadmap das 7 aulas → Task 3, detalhado nas Tasks 9–15.
- §4 evolução do Mini-Orion → Tasks 4, 5, 6.
- §5 Evolution Lab → Task 8.
- §6 infraestrutura (nav, docs, CI, regras) → Tasks 7, 9 (nav+index), 2, 16.
- §7 decisões registradas → refletidas nas tarefas (fusão A10/A11 na Task 3/10; `06-microkernel` executável na Task 6; agrupamento na Task 1; spec em `.ai/planos/`).
- §8 alteração de currículo → Task 2.
- §9 sequência de execução → ordem das Tasks 1→16.
- §10 riscos → tratados: "15/17 arestas é ponto de ensino" explicitado na Task 12 Step 1; `06-microkernel` mínimo na Task 6; build não verificado tratado na Task 16 Step 5; voz/catálogo coberto pelas Global Constraints e Task 16 Step 1.

**Placeholders:** nenhum "TBD/TODO". As aulas trazem sintoma, conceitos, artefato, exercícios e diagrama especificados; a prosa final é trabalho da execução, guiada por `.ai/rules/` — não é placeholder, é a divisão correta de trabalho para material didático.

**Consistência de tipos/nomes:** `ServicoCheckout.fechar_pedido`, `PedidoCobranca(valor, cartao, parcelas=1)`, `ResultadoCobranca`, `Gateway`, `Notificador`, `RepositorioPedidos`, `MotorPromocoes.registrar/aplicar`, `RegraDesconto.avalia`, `Desconto` — usados de forma idêntica entre as Tasks 4, 5, 6 e 13. Contratos de `import-linter` nomeados de forma única por checkpoint.
