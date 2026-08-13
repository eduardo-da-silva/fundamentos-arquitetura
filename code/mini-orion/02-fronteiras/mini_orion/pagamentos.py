"""Componente Pagamentos.

A fronteira e o Protocol `Gateway`. O checkout depende dele, e nao de
nenhum provedor concreto. Trocar de provedor passa a ser adicionar uma
classe aqui, sem tocar no checkout.
"""

from typing import Protocol


class Gateway(Protocol):
    """Contrato de cobranca. Esta e a fronteira do componente."""

    def cobrar(self, valor: float, cartao: str) -> bool: ...


class GatewayPagamentoX:
    """Provedor principal."""

    def cobrar(self, valor: float, cartao: str) -> bool:
        return valor > 0 and cartao.startswith("4")


class GatewayPagamentoY:
    """Provedor de contingencia, contratado para as campanhas.

    Existe para tornar visivel o ganho da fronteira: adicionar este
    provedor nao exigiu nenhuma alteracao no checkout.
    """

    def cobrar(self, valor: float, cartao: str) -> bool:
        return 0 < valor <= 5000 and len(cartao) >= 10
