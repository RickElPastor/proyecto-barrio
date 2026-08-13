"""Acciones de interacción de Proyecto Barrio."""


class ActionManager:
    """Gestiona las acciones disponibles durante una interacción."""

    def execute(self, action, game):
        """Ejecuta una acción y devuelve su resultado."""

        action_id = action["id"]

        if action_id == "talk":
            return self._talk(game)

        if action_id == "help":
            return self._help(game)

        if action_id == "steal":
            return self._steal(game)

        if action_id == "attack":
            return self._attack(game)

        if action_id == "cancel":
            return self._cancel(game)

        return None

    def _talk(self, game):
        """Inicia una conversación."""
        return {
            "action": "talk",
            "returns_to_menu": True,
        }

    def _help(self, game):
        """Ejecuta temporalmente la acción de ayudar."""
        return {
            "action": "help",
            "returns_to_menu": True,
            "message": f"{game.interaction_manager.npc.name} te agradece la ayuda.",
        }

    def _steal(self, game):
        """Ejecuta temporalmente la acción de robar."""
        return {
            "action": "steal",
            "returns_to_menu": False,
        }

    def _attack(self, game):
        """Ejecuta temporalmente la acción de pegar."""
        return {
            "action": "attack",
            "returns_to_menu": False,
        }

    def _cancel(self, game):
        """Cancela la interacción."""
        return {
            "action": "cancel",
            "returns_to_menu": False,
        }
