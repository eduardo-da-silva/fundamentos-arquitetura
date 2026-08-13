# Build e ferramentas

## Como o site é construído

Gerador: **zensical**, compatível com o ecossistema MkDocs Material. Configuração em `mkdocs.yml`.

CI em `.github/workflows/ci.yml`, disparada por push em `main`:

```yaml
- run: pip install zensical
- run: zensical build --clean
```

Saída em `site/`, publicada no GitHub Pages.

!!! warning "Versão não fixada"

    `pip install zensical` sem versão. Um build de hoje e um de daqui a seis meses podem usar versões diferentes, sem nenhuma mudança no repositório. Se o site quebrar sem que ninguém tenha mexido nele, é o primeiro lugar a olhar.

## Preview local

```bash
pip install zensical
zensical serve
```

Toda aula deve ser vista renderizada antes de publicar. Diagrama que não renderiza aparece como bloco de texto cru, e isso passa despercebido em revisão de Markdown.

---

## Mermaid

`pymdownx.superfences` com fence customizado (`mkdocs.yml:90-94`).

**Versão carregada:** `https://unpkg.com/mermaid@11/dist/mermaid.min.js` — major flutuante.

Consequência: correções e mudanças de minor chegam sem aviso e sem alteração no repositório.

### Tipos verificados

Verificado contra o Mermaid 11 do build atual:

| Tipo | Status | Uso |
|---|---|---|
| `flowchart` | estável | padrão para componentes e dependências |
| `sequenceDiagram` | estável | fluxo de colaboração |
| `classDiagram` | estável | estrutura interna de um componente |
| `stateDiagram-v2` | estável | ciclo de vida |
| `quadrantChart` | estável desde a 10 | posicionar componentes em dois eixos |
| `mindmap` | estável desde a 10 | mapa conceitual de módulo |
| `timeline` | estável desde a 9.4 | cronograma |
| `xychart-beta` | **beta** | ver abaixo |

O `-v2` de `stateDiagram-v2` faz parte do nome estável do tipo e não indica instabilidade — não confundir com o sufixo `-beta`.

### Sobre `xychart-beta`

Renderiza no Mermaid 11 — mas o sufixo `-beta` é declaração do próprio projeto de que a sintaxe pode mudar sem major bump. Como a versão é flutuante, uma mudança de sintaxe quebra a página publicada sem que ninguém tenha tocado no repositório.

**Não usar em material publicado.** Para gráfico de dados, as alternativas em ordem de preferência:

1. **tabela Markdown** — quase sempre suficiente e mais acessível;
2. **SVG estático** commitado em `docs/images/`;
3. `xychart-beta` apenas em rascunho local.

Há uma ocorrência hoje em `docs/modulo1/capitulo7.md`. Item de `12-backlog.md` — e a substituição prevista ali é o plano $A \times I$, que um gráfico de barras não consegue representar de qualquer forma.

### Regra geral

Tipo com `-beta` ou `-v2-beta` no nome não vai para material publicado.

Cor, acentuação e complexidade: ver `03-visual-language.md`.

---

## MathJax

`pymdownx.arithmatex` com `generic: true` (`mkdocs.yml:67-68`), MathJax 3 via unpkg (`mkdocs.yml:105-107`), configurado em `docs/javascripts/mathjax.js`.

`$$...$$` para bloco, `$...$` inline.

Duas dependências externas em runtime — MathJax e Mermaid. Se o aluno estiver sem rede ou atrás de proxy restritivo, fórmulas e diagramas não aparecem. Por isso: **nenhuma informação essencial pode existir apenas na fórmula ou apenas no diagrama.** É a razão prática da regra de `03-visual-language.md` que exige leitura em linguagem natural para toda fórmula.

---

## `nav` e o que está publicado

O `nav:` de `mkdocs.yml` é a **única** fonte do que existe no site.

**Arquivo em `docs/` fora do `nav` é erro, não rascunho.**

Foi assim que um módulo inteiro de conteúdo de POO-II sobreviveu neste repositório: `docs/modulo2/` tinha quatro arquivos completos, fora do `nav`, invisíveis no site e presentes em disco. Ninguém percebeu porque nada verifica isso.

Rascunho vive fora de `docs/`. Sugestão: `_rascunhos/`, incluído no `.gitignore`.

Verificação rápida:

```bash
comm -23 \
  <(find docs -name '*.md' | sed 's|^docs/||' | sort) \
  <(grep -oE '[a-z0-9_/-]+\.md' mkdocs.yml | sort -u)
```

Saída vazia é o esperado. Qualquer linha é um arquivo órfão.

---

## Estrutura de diretórios

```
docs/            conteúdo publicado — tudo aqui está no nav
  images/        assets (favicon)
  javascripts/   mathjax.js
  modulo1/       aulas do módulo 1
  orion/         artefatos acumulados do Orion (formatos e exemplos)
code/
  mini-orion/    código executável do professor, uma pasta por aula
.ai/             padrão editorial (não publicado)
site/            build — gerado, nunca editado
```

---

## Versionamento

!!! danger "O repositório não é um repositório git"

    Não há `git init`, não há histórico, não há remoto. Todo o material do Módulo 1 existe em uma única cópia local, sem backup e sem possibilidade de reverter uma edição ruim.

    A CI em `.github/workflows/ci.yml` pressupõe um remoto no GitHub que ainda não está conectado.

    É o item de risco mais alto do repositório. Ver `12-backlog.md`.

`.gitignore` necessário quando o git for inicializado:

```
site/
.cache/
__pycache__/
.venv/
_rascunhos/
```

!!! warning "Permissões em `site/` e `.cache/`"

    Ambos contêm arquivos pertencentes a `root`, provavelmente de um build feito em container. Não podem ser removidos nem sobrescritos pelo usuário comum, o que também impede `zensical build --clean` de funcionar.

    Correção:

    ```bash
    sudo rm -rf site .cache
    ```

---

## Dependências de análise

A aula de métricas usa ferramenta real sobre o Mini-Orion (`06-code-style.md`). Essas dependências pertencem ao Mini-Orion, **não** ao build do site:

```
code/mini-orion/requirements-dev.txt   # pytest, pydeps, import-linter, radon
```

Nunca adicionar ferramenta de análise às dependências do site. O build do site instala apenas `zensical`.
