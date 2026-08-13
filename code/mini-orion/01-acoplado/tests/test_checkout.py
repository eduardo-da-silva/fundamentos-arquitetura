"""Testes do estado inicial.

Repare no que NAO da para testar aqui:

- nao ha como verificar o fechamento sem disparar o envio de e-mail;
- nao ha como simular recusa do gateway sem conhecer a regra interna
  dele (cartao que comeca com "4");
- nao ha como testar o comportamento com um provedor diferente, porque
  so existe um e ele e instanciado dentro do construtor.

Essas tres limitacoes nao sao falta de caprichonos testes. Sao consequencia
direta da estrutura, e e assim que a arquitetura se manifesta primeiro:
como dificuldade de testar.
"""

from mini_orion.checkout import (
    Carrinho,
    Cliente,
    ItemCarrinho,
    ServicoCheckout,
)


def carrinho_exemplo() -> Carrinho:
    return Carrinho(
        itens=[
            ItemCarrinho(sku="TEC-01", preco_unitario=150.0, quantidade=2),
            ItemCarrinho(sku="MOU-07", preco_unitario=80.0, quantidade=1),
        ]
    )


def test_fecha_pedido_com_cartao_valido() -> None:
    servico = ServicoCheckout()
    cliente = Cliente(nome="Maria", email="maria@exemplo.com", cartao="4111111111")

    assert servico.fechar_pedido(carrinho_exemplo(), cliente) == "confirmado"


def test_recusa_pedido_com_cartao_invalido() -> None:
    servico = ServicoCheckout()
    cliente = Cliente(nome="Joao", email="joao@exemplo.com", cartao="5111111111")

    assert servico.fechar_pedido(carrinho_exemplo(), cliente) == "recusado"


def test_subtotal_do_item() -> None:
    item = ItemCarrinho(sku="TEC-01", preco_unitario=150.0, quantidade=2)

    assert item.subtotal == 300.0
