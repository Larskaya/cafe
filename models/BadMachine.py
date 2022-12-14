class BadMachine:
    def __init__(self, recipes, actions):
        self.recipes = recipes
        self.actions = actions

    def boil(self, string) -> str:
        return string + "%"

    def modelsly(self, coffee_name) -> list:
        return list(map(lambda ingredient: self.choose_action(ingredient['name'], ingredient['action']), self.recipes[coffee_name]))
    
    def choose_action(self, ingredient_name, action_name) -> str:
        if hasattr(self, action_name) and callable(getattr(self, action_name)):
            return getattr(self, action_name)(ingredient_name)
        return ingredient_name

    def make_coffee(self, coffee_name) -> str:
        return "i am making {0} with ingredients {1}".format(coffee_name, self.modelsly(coffee_name))
