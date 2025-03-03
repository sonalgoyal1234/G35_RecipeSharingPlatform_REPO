from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Sample recipes database
recipes = [
    {
        "title": "Spaghetti Aglio e Olio",
        "ingredients": ["Spaghetti", "Garlic", "Olive oil", "Red pepper flakes", "Parsley", "Parmesan"],
        "steps": [
            "Boil spaghetti until al dente.",
            "Sauté garlic in olive oil with red pepper flakes.",
            "Mix spaghetti with the garlic oil mixture.",
            "Garnish with parsley and Parmesan.",
        ],
    },
    {
        "title": "Avocado Toast",
        "ingredients": ["Bread", "Avocado", "Lemon juice", "Salt", "Pepper", "Chili flakes"],
        "steps": [
            "Toast the bread until golden brown.",
            "Mash avocado with lemon juice, salt, and pepper.",
            "Spread mashed avocado on toast.",
            "Sprinkle chili flakes for extra flavor.",
        ],
    },
    {
        "title": "Banana Pancakes",
        "ingredients": ["Banana", "Eggs", "Flour", "Milk", "Baking powder", "Butter"],
        "steps": [
            "Mash banana and mix with eggs, flour, milk, and baking powder.",
            "Heat butter in a pan and pour the batter.",
            "Cook until golden brown on both sides.",
            "Serve with honey or syrup.",
        ],
    },
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_recipe")
def generate_recipe():
    recipe = random.choice(recipes)  # Pick a random recipe
    return jsonify(recipe)

if __name__ == "__main__":
    app.run(debug=True)
