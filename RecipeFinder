import requests
from bs4 import BeautifulSoup


url = input("Please enter the recipe web address: ")


response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


recipe_title = soup.find("h1").text
print("Recipe Title:", recipe_title)


ingredients = []
ingredient_list = soup.find("ul", class_="recipe-ingredients")
if ingredient_list:
    ingredients = [ingredient.text.strip() for ingredient in ingredient_list.find_all("li")]
    print("\nIngredients:")
    for ingredient in ingredients:
        print(ingredient)

instructions = []
instruction_list = soup.find("ol", class_="recipe-instructions")
if instruction_list:
    instructions = [instruction.text.strip() for instruction in instruction_list.find_all("li")]
    print("\nInstructions:")
    for i, instruction in enumerate(instructions, start=1):
        print(f"{i}. {instruction}")
