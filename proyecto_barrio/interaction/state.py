"""Estados de interacción de Proyecto Barrio."""

from enum import Enum


class InteractionState(Enum):
    """Representa el estado actual de una interacción."""

    NONE = "none"
    MENU = "menu"
    DIALOGUE = "dialogue"
    MESSAGE = "message"
