# Exercícios de fixação — Aulas 11 e 12

!!! danger "Entrega individual"

    Trabalho **individual**. Entregar antes da Aula 13 e trazer pronto para apresentar em sala no início dela.

As Aulas 11 e 12 ficam presas ao agrupamento de domínio e ao grafo do Orion, por regra deste material. Os cinco a seguir cobrem o mesmo conteúdo pela via oposta: pedem uma busca fora do material, sobre sistemas reais, publicados por quem os construiu. Todo dado usado tem de vir da fonte pesquisada — número sem fonte citável não entra na resposta.

1. **Aplicação — Um monólito modular real, antes de qualquer distribuição.** Pesquise um relato técnico de uma empresa que descreve explicitamente ter adotado (ou reforçado) um **monólito modular** — módulos de domínio com fronteira imposta dentro do mesmo processo — antes de considerar, ou em vez de, distribuir em serviços.

    a. Qual mecanismo a empresa usa para impor a fronteira entre módulos — convenção de linguagem, ferramenta de análise estática, teste de arquitetura?
    b. Na linguagem da Aula 11: o mecanismo relatado impõe uma fronteira lógica, uma fronteira física, ou os dois em momentos diferentes da vida do sistema?
    c. A fonte nomeia algum custo dessa escolha, ou só benefícios? Se só benefícios, isso enfraquece o relato como evidência técnica.

    ??? note "Resposta comentada — o que a resposta precisa conter"

        Nome do mecanismo de fronteira citado na fonte (não "eles organizaram o código", mas a ferramenta ou convenção específica), classificado como lógico ou físico conforme a Aula 11, com a citação ou o link da fonte usada.

2. **Julgamento — Extrair sem fronteira, e voltar atrás.** Pesquise o caso de uma empresa que extraiu um componente de um monólito para um serviço distribuído e depois reverteu a decisão, voltando a integrá-lo (por exemplo, o relato de **Segment**, "Goodbye Microservices", 2020, ou outro caso equivalente que você encontre e documente).

    Usando o critério da Aula 14 — "não se extrai o que não tem fronteira" —, avalie: o relato indica que o componente tinha uma fronteira lógica (API pública, *internals* fechados, contrato verificado) **antes** da extração, ou a fronteira só apareceu depois, como parte do conserto?

    Mais de uma resposta é aceitável. O que se avalia: se você distingue "faltava fronteira lógica" de "microsserviços são um erro em geral"; se cita o trecho da fonte que sustenta sua leitura; se nomeia o que a equipe teve de reconstruir para reverter.

3. **Aplicação — Contrato de independência entre módulos, fora do Python.** O Mini-Orion usa `type = independence` do `import-linter` para garantir que `pagamentos` e `notificacoes` não se conheçam. Pesquise o equivalente em **duas** destas ferramentas: `ArchUnit` (slices e `SlicesRuleDefinition`, Java), `Spring Modulith` (verificação de módulos de aplicação), `NetArchTest` (.NET), as tags de módulo do `Nx` (JavaScript/TypeScript).

    Para cada uma das duas escolhidas: como ela expressa "o módulo A não pode importar o módulo B, em nenhum sentido"? A checagem roda em teste, em build, ou em análise isolada?

    ??? note "Resposta comentada — o que a resposta precisa conter"

        Um trecho de configuração ou de código real, do site oficial ou da documentação da ferramenta, equivalente ao `type = independence` do `import-linter`, com a identificação de onde a verificação roda.

4. **Julgamento — Um grafo real com proporção parecida com 15 de 17.** Pesquise uma análise pública de dependências de um sistema real (relatório de engenharia, post técnico, ou saída de uma ferramenta como `madge`, `pydeps`, `Structure101` ou o grafo de um monorepo `Nx`) em que a maioria das dependências atravesse fronteira de módulo ou de time.

    A fonte trata esse número alto como falha do sistema, como falha da medição, ou como ponto de partida para priorizar fronteiras — na mesma leitura que a Aula 12 faz do 15/17 do Orion?

    Mais de uma resposta é aceitável. O que se avalia: se você identifica o critério de agrupamento que a fonte usou (por time, por camada, por domínio) antes de comparar o número com o do Orion — números de agrupamentos diferentes não são comparáveis entre si, como a Aula 12 já observou para o próprio Orion.

5. **Aplicação — Um componente que ninguém importou.** Pesquise um relato de engenharia (post técnico, retrospectiva, ou *postmortem*) que descreva uma abstração, um serviço ou uma camada construída para ser reaproveitada por múltiplas partes do sistema, mas que **nenhum consumidor real adotou** — o equivalente de `Integracoes` no Orion.

    Classifique o caso: a fonte trata isso como um problema de comunicação entre times, como abstração construída antes de existir um consumidor real para ela, ou como as duas coisas? O que a equipe fez com o componente depois de perceber isso — dissolveu, deu consumidores, ou manteve como está?

    ??? note "Resposta comentada — o que a resposta precisa conter"

        Citação direta ou paráfrase da fonte, nomeando o motivo da não adoção, e o desfecho relatado (dissolvido, adotado, ou mantido como peso morto). Resposta que classifica sem citar a fonte não conta.

## Apresentação em sala

No início da Aula 13, cada aluno apresenta em poucas frases um dos cinco exercícios: a fonte encontrada e a conclusão a que chegou. A apresentação individual é o que garante que a pesquisa foi feita por quem entrega, não copiada de um colega.
