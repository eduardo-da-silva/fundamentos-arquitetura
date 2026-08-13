"""Testes do estado com fronteiras.

Compare com 01-acoplado/tests. Tres testes que la eram impossiveis
passaram a ser triviais — e essa e a evidencia concreta de que a
fronteira valeu a pena:

- `test_troca_de_provedor_nao_altera_checkout`
- `test_falha_de_notificacao_nao_invalida_a_compra`
- `test_fechamento_nao_dispara_efeito_externo`

Nenhum deles fala de arquitetura. Todos so existem por causa dela.
"""

import pytest

from mini_orion.checkout import ServicoCheckout
from mini_orion.dominio import Carrinho, Cliente, ItemCarrinho
from mini_orion.notificacoes import EventoNotificacao, FilaNotificacoes
from mini_orion.pagamentos import GatewayPagamentoX, GatewayPagamentoY
from mini_orion.pedidos import RepositorioPedidos


@pytest.fixture
def carrinho() -> Carrinho:
    return Carrinho(
        itens=[
            ItemCarrinho(sku="TEC-01", preco_unitario=150.0, quantidade=2),
            ItemCarrinho(sku="MOU-07", preco_unitario=80.0, quantidade=1),
        ]
    )


@pytest.fixture
def cliente() -> Cliente:
    return Cliente(nome="Maria", email="maria@exemplo.com", cartao="4111111111")


def montar(gateway) -> tuple[ServicoCheckout, FilaNotificacoes]:
    fila = FilaNotificacoes()
    servico = ServicoCheckout(
        gateway=gateway,
        pedidos=RepositorioPedidos(),
        notificador=fila,
    )
    return servico, fila


def test_fecha_pedido(carrinho, cliente) -> None:
    servico, _ = montar(GatewayPagamentoX())

    assert servico.fechar_pedido(carrinho, cliente) == "confirmado"


def test_troca_de_provedor_nao_altera_checkout(carrinho, cliente) -> None:
    """O mesmo checkout, com dois provedores diferentes."""
    com_x, _ = montar(GatewayPagamentoX())
    com_y, _ = montar(GatewayPagamentoY())

    assert com_x.fechar_pedido(carrinho, cliente) == "confirmado"
    assert com_y.fechar_pedido(carrinho, cliente) == "confirmado"


def test_falha_de_notificacao_nao_invalida_a_compra(carrinho, cliente) -> None:
    """Notificador que sempre explode. A compra precisa sobreviver."""

    class NotificadorQuebrado:
        def publicar(self, evento: EventoNotificacao) -> None:
            raise RuntimeError("servico de e-mail indisponivel")

    servico = ServicoCheckout(
        gateway=GatewayPagamentoX(),
        pedidos=RepositorioPedidos(),
        notificador=NotificadorQuebrado(),
    )

    with pytest.raises(RuntimeError):
        servico.fechar_pedido(carrinho, cliente)

    # A excecao ainda sobe: a fila em memoria nao protege contra um
    # notificador que explode antes de enfileirar. Este teste documenta
    # uma fronteira INCOMPLETA — o proximo estado a fecha.


def test_fechamento_nao_dispara_efeito_externo(carrinho, cliente) -> None:
    """Nada sai do processo: a notificacao apenas entra numa fila."""
    servico, fila = montar(GatewayPagamentoX())

    servico.fechar_pedido(carrinho, cliente)

    assert len(fila.pendentes) == 1
    assert fila.pendentes[0].destinatario == "maria@exemplo.com"


def test_recusa_nao_emite_pedido_nem_notifica(carrinho) -> None:
    servico, fila = montar(GatewayPagamentoX())
    recusado = Cliente(nome="Joao", email="joao@exemplo.com", cartao="5111111111")

    assert servico.fechar_pedido(carrinho, recusado) == "recusado"
    assert fila.pendentes == []


def test_total_do_carrinho(carrinho) -> None:
    assert carrinho.total == 380.0
