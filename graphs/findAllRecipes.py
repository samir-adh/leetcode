from typing import DefaultDict, List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        table = DefaultDict(list)
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                table[recipe].append(ingredient)

        visited = set(supplies)
        cycle = set()

        def dfs(recipe: str):
            if recipe in visited:
                return True
            if table[recipe] == [] or recipe in cycle:
                return False
            cycle.add(recipe)
            for ingredient in table[recipe]:
                if not dfs(ingredient):
                    return False
            cycle.remove(recipe)
            visited.add(recipe)
            return True

        output = []
        for recipe in recipes:
            if dfs(recipe):
                output.append(recipe)
        return output
