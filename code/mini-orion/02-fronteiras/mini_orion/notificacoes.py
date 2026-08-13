"""Componente Notificacoes.

Fora do caminho critico do checkout: uma falha aqui nao invalida uma
compra ja cobrada. O preco dessa decisao esta explicito em
`FilaNotificacoes.publicar` — existe uma janela em que o pedido esta
confirmado e o cliente ainda nao sabe.
"""

from dataclasses import dataclass
from typing import Protocol

from mini_orion.dominio import Pedido


@dataclass
class EventoNotificacao:
    destinatario: str
    assunto: str


class Notificador(Protocol):
    def publicar(self, evento: EventoNotificacao) -> None: ...


class FilaNotificacoes:
    """Enfileira em memoria. Nao levanta excecao para o chamador.

    A decisao arquitetural esta no `except`: uma falha de notificacao e
    registrada e engolida, porque perder o aviso e menos grave do que
    perder a compra. Se o negocio decidir o contrario, este e o unico
    lugar a mudar.
    """

    def __init__(self) -> None:
        self.pendentes: list[EventoNotificacao] = []
        self.falhas: list[EventoNotificacao] = []

    def publicar(self, evento: EventoNotificacao) -> None:
        try:
            self.pendentes.append(evento)
        except Exception:  # pragma: no cover - defensivo por design
            self.falhas.append(evento)


def evento_de_confirmacao(pedido: Pedido) -> EventoNotificacao:
    return EventoNotificacao(
        destinatario=pedido.cliente.email,
        assunto=f"Pedido {pedido.numero} confirmado",
    )
