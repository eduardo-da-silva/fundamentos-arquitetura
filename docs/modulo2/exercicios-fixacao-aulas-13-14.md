# Exercícios de fixação — Aulas 13 e 14

!!! danger "Entrega individual"

    Trabalho **individual**. Entregar antes da Aula 15 e trazer pronto para apresentar em sala no início dela.

As Aulas 13 e 14 ficam presas ao Mini-Orion e ao candidato `Pagamentos`, por regra deste material. Os cinco a seguir cobrem o mesmo conteúdo pela via oposta: pedem uma busca fora do material, sobre sistemas reais, publicados por quem os construiu.

1. **Aplicação — Pipeline de verdade, fora do checkout.** Pesquise um sistema real, documentado por quem o construiu, organizado como **pipeline de filtros** — pode ser um pipeline de dados (por exemplo, com Apache Camel, Kafka Streams ou Apache Beam), um pipeline de build/CI, ou o próprio encadeamento de comandos Unix num caso de uso real.

    a. Quais são as etapas (filtros) que a fonte descreve, e o que cada uma recebe e devolve?
    b. A fonte relata algum caso em que a ordem das etapas foi trocada, ou uma etapa removida, e algo quebrou por causa disso? Se sim, isso é a connascência de execução da Aula 13 aparecendo fora do Orion.

    ??? note "Resposta comentada — o que a resposta precisa conter"

        A lista de etapas citada na fonte (não inventada), com a entrada e a saída de cada uma, e — se a fonte relatar — o incidente de reordenação ou remoção, com a citação ou o link usado.

2. **Julgamento — Um plugin mal-comportado, de verdade.** Pesquise um relato real (post-mortem, *changelog* de correção, ou artigo técnico) em que um **plugin** de uma arquitetura microkernel — extensão de navegador, plugin de WordPress, extensão de IDE, plugin de um sistema de build — quebrou ou degradou o sistema principal por um comportamento que o núcleo não isolava.

    Compare com o risco nomeado no ADR da Aula 13: `MotorPromocoes.aplicar` chama `regra.avalia` sem isolar a exceção de cada plugin. O caso que você encontrou tem o mesmo formato de risco, ou o núcleo pesquisado já isola cada plugin (com *timeout*, processo separado, ou captura de exceção por chamada)? Se isola, isso é um mecanismo de robustez que o Mini-Orion **não** tem — nomeie-o.

    Mais de uma resposta é aceitável. O que se avalia: se você identifica exatamente o ponto do núcleo que falhou (ou que evitou a falha) em isolar o plugin, e não apenas "o plugin deu erro".

3. **Aplicação — Um sinal de extração, medido.** Pesquise um relato de engenharia que descreva a extração de um único serviço de um monólito maior, motivada por um sinal operacional **medido** — não por preferência de arquitetura. Escolha um relato bem documentado (por exemplo, extrações de componentes de pagamento, de busca, ou de processamento em lote em empresas de e-commerce ou fintech) e identifique a métrica ou o evento citado como gatilho.

    Classifique o sinal usando os quatro da Aula 14 — escala própria, cadência de release própria, isolamento de falha, autonomia de time — e diga se o relato nomeia também o custo da extração (transação distribuída, deploy coordenado, observabilidade), ou só o ganho.

    ??? note "Resposta comentada — o que a resposta precisa conter"

        O sinal citado na fonte, classificado em um dos quatro tipos da Aula 14, com a métrica ou o evento que o tornou observável — não "a equipe decidiu que era hora", mas o dado que embasou a decisão.

4. **Julgamento — Extração pela moda, extração pelo sinal.** Pesquise dois relatos de engenharia sobre decisões de extrair (ou não extrair) um serviço de um monólito: um em que a motivação declarada é predominantemente uma tendência do setor ou uma preferência estética ("microsserviços é o padrão da indústria agora"), e outro em que a motivação é um sinal operacional nomeado e medido, no formato da Aula 14.

    Comparando os dois, o que muda no texto de quem escreveu cada decisão — a presença de um número, de um prazo, de uma condição sob a qual a decisão estaria errada?

    Mais de uma resposta é aceitável. O que se avalia: se a comparação usa o critério de falseabilidade das Aulas 9 e 14 — a decisão diz o que a faria estar errada? — e não apenas qual das duas você prefere.

5. **Aplicação — Um gatilho mensurável, publicado.** Pesquise um relato de engenharia que publique o **número exato** ou o **evento exato** que disparou uma decisão de separar um componente — por exemplo, um limiar de latência, uma frequência de incidente, uma divergência de cadência de deploy entre times, ou um limite de capacidade atingido.

    Usando o formato do ADR da Aula 14, escreva em uma frase o gatilho como ele apareceria num campo "Gatilho mensurável": precisa ter número (ou evento nomeado) e prazo ou janela de observação, como no ADR de `Pagamentos` ("mais de uma vez por sprint, medido por um trimestre").

    ??? note "Resposta comentada — o que a resposta precisa conter"

        O gatilho reescrito no formato número/evento + prazo, com a citação da fonte. Uma resposta que só diz "quando o sistema não aguentava mais" não conta — o critério é o mesmo que a Aula 9 já cobrou do ADR-009: gatilho observável e datável, não "quando incomodar".

## Apresentação em sala

No início da Aula 15, cada aluno apresenta em poucas frases um dos cinco exercícios: a fonte encontrada e a conclusão a que chegou. A apresentação individual é o que garante que a pesquisa foi feita por quem entrega, não copiada de um colega.
