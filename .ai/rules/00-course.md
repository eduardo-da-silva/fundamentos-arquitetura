# A disciplina

> Este documento tem prioridade sobre todos os demais desta pasta. Em caso de conflito, vale o que está aqui.

## Identidade

**Arquitetura de Software** — Bacharelado em Sistemas de Informação, IFC.

Carga: 18 semanas. Estrutura em 4 módulos progressivos, detalhada em `07-curriculum.md`.

Site publicado em <https://eduardo-da-silva.github.io/fundamentos-arquitetura>.

## Escopo

Este repositório trata **exclusivamente** de arquitetura de software.

Esta regra é literal e existe por um motivo concreto: o repositório nasceu como cópia do repositório da disciplina de POO-II, e um módulo inteiro de conteúdo de Orientação a Objetos (pedidos, pagamentos, carrinho) sobreviveu à limpeza inicial, permanecendo em disco por não estar no `nav:`. Foi removido. Não deve voltar.

Consequências práticas:

- nenhum capítulo sobre sintaxe de linguagem, herança, polimorfismo ou padrões de projeto como tema principal;
- padrões de projeto entram apenas quando forem consequência de uma decisão arquitetural, nunca como assunto em si;
- código existe para evidenciar um problema estrutural ou demonstrar uma fronteira, nunca como exercício de programação.

Se um conteúdo caberia igualmente bem na ementa de POO-II, ele não pertence a este repositório.

## Público-alvo

Estudantes de graduação que **já cursaram** Programação Orientada a Objetos.

O que se pode assumir:

- lêem e escrevem Python com conforto;
- conhecem classes, interfaces, composição e injeção de dependência;
- já escreveram testes automatizados;
- já trabalharam em um sistema com mais de uma camada.

O que **não** se pode assumir:

- experiência com sistemas em produção;
- vivência de incidente, plantão ou migração;
- noção de custo de mudança ao longo do tempo;
- exposição a decisões que não têm resposta certa.

Esta última lacuna é a mais importante. O aluno vem de disciplinas onde existe uma resposta correta. Arquitetura é a primeira em que a defesa da resposta vale mais que a resposta. O material deve tratar isso explicitamente, não por osmose.

## Objetivo

Desenvolver **pensamento arquitetural**.

Ao final da disciplina, diante de um sistema desconhecido, o aluno deve ser capaz de:

- localizar os riscos estruturais e explicar por que importam;
- propor mudanças proporcionais ao problema;
- nomear o que cada proposta custa;
- registrar a decisão de forma que outra pessoa entenda o raciocínio meses depois.

O que **não** é objetivo: memorizar taxonomias de estilos arquiteturais, decorar definições, ou reproduzir diagramas de referência.

## Estudo de caso

Único, para todo o curso: o **Marketplace Orion**, definido em `05-domain.md`.

Duas trilhas, que nunca se misturam:

- **Mini-Orion Checkout** — recorte pequeno, do professor, resolvido em aula, com código executável.
- **Orion Evolution Lab** — recorte amplo, dos grupos, nunca resolvido no material.

Proibido introduzir domínio auxiliar (biblioteca, escola, locadora) para ilustrar um conceito. Se o conceito não puder ser mostrado no Orion, ou o conceito não pertence ao curso, ou o Orion precisa ser estendido em `05-domain.md` — nesta ordem de preferência.

## Referência-base

RICHARDS, Mark; FORD, Neal. *Fundamentals of Software Architecture: An Engineering Approach*. O'Reilly, 2020.

Complementares, quando o assunto exigir:

- BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. *Software Architecture in Practice*. 4. ed. Addison-Wesley, 2021.
- FORD, Neal; PARSONS, Rebecca; KUA, Patrick. *Building Evolutionary Architectures*. O'Reilly, 2017.
- PAGE-JONES, Meilir. *What Every Programmer Should Know About Object-Oriented Design*. Dorset House, 1995. (origem de connascência)
- MARTIN, Robert C. *Clean Architecture*. Prentice Hall, 2017.

Toda citação deve indicar capítulo ou seção. Referência genérica ao livro inteiro não serve ao aluno que quiser aprofundar.

## Postura editorial

- Nenhum conceito é apresentado antes de o aluno ter visto o problema que ele resolve.
- Nenhuma recomendação aparece sem o contexto em que ela deixa de valer.
- Nenhum diagrama aparece sem dizer o que ele revela e o que ele esconde.
- Nenhuma métrica aparece sem dizer como ela pode enganar.

Arquitetura ensinada como conjunto de boas práticas universais produz o oposto do pensamento arquitetural.

## Regra de conflito

Se houver conflito entre a fluidez do texto e a obrigação de expor o trade-off, expor o trade-off.

Se houver conflito entre cobrir mais conteúdo e o aluno decidir sozinho pelo menos uma vez, o aluno decide.
