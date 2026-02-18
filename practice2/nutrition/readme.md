
# Nutrition.py README

This program implements a simple nutrition lookup tool based on the FDA's raw fruits poster.

​
# Purpose

Users input a fruit name (case-insensitive), and the program outputs the calories for one portion if the fruit matches exactly (e.g., "strawberries") from the 20 listed fruits. Invalid inputs are ignored silently.

​# How It Works

    A dictionary maps lowercase fruit names to their calorie values, sourced directly from the FDA poster.

    Example keys: "apple" → "130", "banana" → "110", "strawberries" → "50".

    Prompts with "Item: ", converts input to lowercase, checks dictionary membership, and prints "Calories: {value}" if found.

    ​

# Fruits Covered

. The program supports these 20 fruits with their calories:

fruits = {
    "apple": "130",
    "avocado": "50", 
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80"
}

# Example : 
text
$ python nutrition.py
Item: Apple
Calories: 130
Item: banana
Calories: 110
Item: carrot

No output for invalid items.
​
