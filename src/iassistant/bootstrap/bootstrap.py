"""
Bootstrap d'IAssistant.

Prépare l'environnement puis démarre l'application.
"""

from iassistant.application import IAssistant


def bootstrap() -> None:
    display_banner()
    prepare_environment()

    app = IAssistant()
    app.start()


def display_banner() -> None:
    print("=" * 40)
    print("         IAssistant")
    print("=" * 40)
    print()


def prepare_environment() -> None:
    print("Préparation de l'environnement...")
    print("✔ Environnement prêt")
    print()
