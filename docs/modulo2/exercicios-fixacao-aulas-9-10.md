# Exercícios de fixação — Aulas 9 e 10

!!! danger "Entrega individual"

    Trabalho **individual**. Entregar antes da Aula 11 e trazer pronto para apresentar em sala no início dela.

Os exercícios das Aulas 9 e 10 ficam presos ao grafo e aos números do Orion, por regra deste material. Os cinco a seguir cobrem o mesmo conteúdo pela via oposta: pedem uma busca fora do material, sobre sistemas reais, publicados por quem os construiu. Todo dado usado precisa vir da fonte pesquisada, nunca de número inventado.

1. **Aplicação — Caso real de "voltar para o monólito".** Pesquise o post técnico da equipe do **Amazon Prime Video** (2023) sobre a decisão de sair de uma arquitetura de microsserviços/serverless para um monólito num componente de monitoramento de vídeo.

    a. Qual foi o sintoma que motivou a mudança (custo, latência, complexidade operacional)?
    b. Na linguagem da Aula 9: o que eles descrevem é *big ball of mud* virando monólito estruturado, ou o oposto?
    c. Que custo da distribuição — dos cinco listados na Aula 9: latência, falha parcial, transação, operação, observabilidade — aparece mais evidente no relato?

    ??? note "Resposta comentada — o que a resposta precisa conter"

        Nome da causa técnica citada na fonte, não "ficou caro" genérico, amarrada a pelo menos um dos cinco custos nomeados na Aula 9, com a citação ou o link da fonte usada.

2. **Julgamento — O outro lado do caso Prime Video.** O caso do exercício anterior é usado com frequência como prova de que microsserviços foram um erro. Pesquise pelo menos uma crítica ou contraponto publicado por outro engenheiro ou arquiteto sobre esse mesmo caso.

    Depois, julgue: a conclusão "portanto devemos evitar microsserviços" é sustentável a partir desse único caso?

    Mais de uma resposta é aceitável. O que se avalia: se você distingue "esse componente específico, com essa carga específica, teve esse resultado" de uma regra geral; se nomeia sob que condição a decisão deles faria sentido para outro sistema; e se cita as duas fontes — o post original e o contraponto —, não só uma.

3. **Aplicação — Ferramentas de fronteira em outras linguagens.** O Mini-Orion usa `import-linter` (Python) para transformar a regra de camadas em contrato verificável. Pesquise o equivalente em **duas** destas famílias de ferramentas: `ArchUnit` (Java), `NetArchTest` (.NET), as regras de boundary do `Nx` ou do `eslint-plugin-boundaries` (JavaScript/TypeScript), `Deptrac` (PHP).

    Para cada uma das duas escolhidas: como ela expressa "camada de baixo não pode ser importada por camada de cima"? A violação é detectada em tempo de build ou CI, como no Mini-Orion, ou de outra forma?

    ??? note "Resposta comentada — o que a resposta precisa conter"

        Um trecho de configuração real, do site oficial da ferramenta, equivalente ao `type = layers` do `import-linter`, e a identificação de onde a verificação roda — teste, plugin de build, análise estática isolada.

4. **Julgamento — Monólito modular como escolha deliberada.** Pesquise o texto **"The Majestic Monolith"**, de David Heinemeier Hansson (criador do Rails, Basecamp/37signals), e pelo menos um relato de empresa que o citou para justificar não migrar para microsserviços.

    A posição de Hansson é compatível com o ADR-009 da Aula 9 ("Orion permanece um único *deployable* por 12 meses")? Em que ponto ela vai além do que o ADR-009 argumenta, e em que ponto ela é mais fraca — por exemplo, nomeia gatilho de reversão, ou trata a escolha como definitiva?

    Mais de uma resposta é aceitável. O que se avalia: se a comparação usa o critério de falseabilidade da Aula 9 — o ADR-009 tem gatilho de reversão observável; a posição pesquisada tem? —, não apenas concordância ou discordância de opinião.

5. **Aplicação — Sinais legítimos de extração, fora do Orion.** Escolha um relato público real de uma empresa que extraiu um único serviço de um monólito maior (por exemplo Shopify e o checkout, Segment, Stripe, Uber, GitHub, Etsy — pesquise e escolha um caso bem documentado).

    Usando o critério das Aulas 9 e 10 — sinal legítimo (escala independente, cadência de release própria, isolamento de falha, autonomia de time) versus ilegítimo (moda, estética) —, classifique o motivo real que a empresa deu.

    ??? note "Resposta comentada — o que a resposta precisa conter"

        Citação direta ou paráfrase da fonte, nomeando o motivo, classificado em um dos quatro sinais legítimos — ou marcado como ilegítimo, se for o caso, pois nem todo caso publicado é um bom exemplo. Resposta que classifica sem citar a fonte não conta.

## Apresentação em sala

No início da Aula 11, cada aluno apresenta em poucas frases um dos cinco exercícios: a fonte encontrada e a conclusão a que chegou. A apresentação individual é o que garante que a pesquisa foi feita por quem entrega, não copiada de um colega.
