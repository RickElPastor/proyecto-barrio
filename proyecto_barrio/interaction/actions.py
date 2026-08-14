"""Acciones de interacción de Proyecto Barrio."""


class ActionManager:
    """Gestiona las acciones disponibles durante una interacción."""

    def execute(self, action, npc):
        """Ejecuta una acción y devuelve su resultado."""

        action_id = action["id"]

        if action_id == "talk":
            return self._talk(npc)

        if action_id == "help":
            return self._help(npc)

        if action_id == "steal":
            return self._steal(npc)

        if action_id == "attack":
            return self._attack(npc)

        if action_id == "cancel":
            return self._cancel(npc)

        return None

    def _talk(self, npc):
        """Inicia una conversación."""
        return {
            "action": "talk",
        }

    def _help(self, npc):
        """Ejecuta temporalmente la acción de ayudar."""
        return {
            "action": "help",
            "message": f"{npc.name} te agradece la ayuda.",
        }

    def _steal(self, npc):
        """Ejecuta temporalmente la acción de robar."""
        return {
            "action": "steal",
        }

    def _attack(self, npc):
        """Ejecuta temporalmente la acción de pegar."""
        return {
            "action": "attack",
        }

    def _cancel(self, npc):
        """Cancela la interacción."""
        return {
            "action": "cancel",
        }
