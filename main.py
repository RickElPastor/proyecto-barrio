"""Punto de entrada de Proyecto Barrio."""

from proyecto_barrio.core.game import Game


def main():
    """Inicia el juego."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
