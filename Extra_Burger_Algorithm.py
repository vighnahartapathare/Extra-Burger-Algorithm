ingredients = ["bun", "lettuce", "tomato", "cheese", "patty", "onion","sauce"]
saved_ingredients = []
days = 7
extra_burgers = 0

for day in range(days):
    todays_burger = ingredients.copy()
    if todays_burger:
        removed = todays_burger.pop(day % len(ingredients))  # Rotate through the list
        saved_ingredients.append(removed)
        print(f"Day {day+1}: Removed '{removed}' and saved it. Burger today: {todays_burger}")
    else:
        print(f"Day {day+1}: No ingredients left to remove.")

    # Check if we have at least one of each ingredient
    while all(saved_ingredients.count(item) >= 1 for item in ingredients):
        extra_burgers += 1
        for item in ingredients:
            saved_ingredients.remove(item)
        print(f"Made an extra burger! Total extra burgers: {extra_burgers}")

print(f"\nTotal extra burgers made: {extra_burgers}")

