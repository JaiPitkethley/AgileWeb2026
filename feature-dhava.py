def get_fruit_list():
    """Returns a list of common fruits"""
    return ["apple", "banana", "orange", "strawberry", "grape", "mango"]


def is_fruit(item):
    """Check if an item is in the fruit list"""
    return item.lower() in get_fruit_list()


def count_fruits(fruits):
    """Count the number of fruits in a list"""
    return len(fruits)


def filter_fruits(items):
    """Filter and return only fruits from a list of items"""
    fruit_list = get_fruit_list()
    return [item for item in items if item.lower() in fruit_list]


def fruit_calories(fruit):
    """Return calorie info for common fruits"""
    calories = {
        "apple": 95,
        "banana": 105,
        "orange": 62,
        "strawberry": 49,
        "grape": 67,
        "mango": 99
    }
    return calories.get(fruit.lower(), "Unknown fruit")