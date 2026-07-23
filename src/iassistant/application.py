from iassistant.specialists.first_meeting import PremiereRencontre


class IAssistant:

    def start(self) -> None:
        print("Bienvenue.")
        print("IAssistant démarre...")

        self.execute_next_step()

    def execute_next_step(self) -> None:
        """Exécute la prochaine mission d'IAssistant."""

        first_meeting = PremiereRencontre()
        first_meeting.execute()

        print("Retour au chef d'orchestre.")
