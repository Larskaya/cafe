from BadMachine import BadMachine


class Machine(BadMachine):
    def __init__(self, recipes, actions) -> None:
        super().__init__(recipes, actions)

    def foam(self, string) -> str:
        return string + "*"
