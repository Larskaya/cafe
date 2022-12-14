from Machine import Machine


class EliteMachine(Machine):
    def __init__(self, recipes, actions) -> None:
        super().__init__(recipes, actions)

    def filter(self, string) -> str:
        return string + "#"
