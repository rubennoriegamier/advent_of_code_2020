import fileinput
from bisect import insort
from collections import Counter, defaultdict
from operator import itemgetter


def main():
    foods = list(map(parse_food, map(str.rstrip, fileinput.input())))

    print(part_1(foods))
    print(part_2(foods))


def part_1(foods):
    ingredients_counter = Counter()
    allergens_counter = defaultdict(Counter)

    for ingredients, allergens in foods:
        for ingredient in ingredients:
            ingredients_counter[ingredient] += 1
            for allergen in allergens:
                allergens_counter[allergen][ingredient] += 1

    for allergen, counter in allergens_counter.items():
        most_common = counter.most_common()

        for ingredient, count in most_common:
            if count == most_common[0][1]:
                ingredients_counter.pop(ingredient, None)

    return sum(ingredients_counter.values())


def part_2(foods):
    allergens_counter = defaultdict(Counter)

    for ingredients, allergens in foods:
        for ingredient in ingredients:
            for allergen in allergens:
                allergens_counter[allergen][ingredient] += 1

    ingredients = defaultdict(set)

    for allergen, counter in allergens_counter.items():
        most_common = counter.most_common()

        for ingredient, count in most_common:
            if count == most_common[0][1]:
                ingredients[ingredient].add(allergen)

    sorted_ingredients = []

    while ingredients:
        allergen, ingredient = next((allergens.pop(), ingredient) for ingredient, allergens in ingredients.items()
                                    if len(allergens) == 1)

        insort(sorted_ingredients, (allergen, ingredient))
        ingredients.pop(ingredient)

        for allergens in ingredients.values():
            if len(allergens) > 1:
                allergens.discard(allergen)

    # noinspection PyTypeChecker
    return ','.join(map(itemgetter(1), sorted_ingredients))


def parse_food(raw_food):
    ingredients, allergens = raw_food.split(' (contains ')

    return ingredients.split(), allergens[:-1].split(', ')


if __name__ == '__main__':
    main()
