"""Administrador central de interacciones."""

from proyecto_barrio.interaction.state import InteractionState


class InteractionManager:
    """Controla el estado general de las interacciones."""

    def __init__(self):
        self.state = InteractionState.NONE
        self.npc = None

    @property
    def active(self):
        """Indica si existe una interacción activa."""
        return self.state != InteractionState.NONE

    def open_menu(self, npc):
        """Abre el menú de interacción con un NPC."""
        self.npc = npc
        self.state = InteractionState.MENU

    def close(self):
        """Cierra completamente la interacción."""
        self.npc = None
        self.state = InteractionState.NONE

    def set_state(self, state):
        """Cambia el estado actual de la interacción."""
        self.state = state
