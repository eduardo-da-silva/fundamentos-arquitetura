"""Estado inicial do Mini-Orion: tudo dentro do fluxo de checkout.

Este é o ponto de partida do curso. O código funciona, os testes passam,
e nada aqui foi escrito para ser ruim de propósito. Cada linha resolveu
um problema real pelo caminho mais curto disponível na época.

As decisões arquiteturais existem — elas apenas não estão explícitas.
"""

from dataclasses import dataclass, field


@dataclass
class ItemCarrinho:
    sku: str
    preco_unitario: float
    quantidade: int

    @property
    def subtotal(self) -> float:
        return self.preco_unitario * self.quantidade


@dataclass
class Carrinho:
    itens: list[ItemCarrinho] = field(default_factory=list)


@dataclass
class Cliente:
    nome: str
    email: str
    cartao: str


# --- Integracoes concretas -------------------------------------------------
# O checkout conhece estes dois pelo nome. Trocar de provedor de pagamento
# exige editar o checkout, e nao ha como fechar uma compra em teste sem
# passar pelo envio de e-mail.


class GatewayPagamentoX:
    """Provedor de pagamento contratado. Unico suportado."""

    def cobrar(self, valor: float, cartao: str) -> bool:
        return valor > 0 and cartao.startswith("4")


class ServicoEmail:
    def enviar(self, destinatario: str, assunto: str) -> None:
        print(f"[email] para={destinatario} assunto={assunto}")


class ServicoCheckout:
    def __init__(self) -> None:
        self._gateway = GatewayPagamentoX()
        self._email = ServicoEmail()

    def fechar_pedido(self, carrinho: Carrinho, cliente: Cliente) -> str:
        total = sum(item.subtotal for item in carrinho.itens)

        aprovado = self._gateway.cobrar(total, cliente.cartao)
        if not aprovado:
            return "recusado"

        # A notificacao esta no caminho critico: se o e-mail falhar, a
        # excecao sobe e a compra e perdida, mesmo com a cobranca feita.
        self._email.enviar(cliente.email, "Pedido confirmado")

        return "confirmado"
