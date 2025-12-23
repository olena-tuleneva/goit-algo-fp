# Дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for item, details in sorted_items:
        if details["cost"] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]

    return total_calories, budget - remaining_budget, chosen_items

# Динамічне програмування (Knapsack)
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(items)

    dp = [[0 for w in range(budget + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        cal = items[name]["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], cal + dp[i - 1][w - cost])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення оптимального набору страв
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = item_names[i - 1]
            chosen_items.append(name)
            w -= items[name]["cost"]

    chosen_items.reverse()
    total_calories = dp[n][budget]
    used_budget = budget - w

    return total_calories, used_budget, chosen_items

if __name__ == '__main__':
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy approach:")
    print(f"  Total calories: {greedy_result[0]}")
    print(f"  Used budget: {greedy_result[1]}")
    print(f"  Chosen items: {greedy_result[2]}\n")

    print("Dynamic Programming approach:")
    print(f"  Total calories: {dp_result[0]}")
    print(f"  Used budget: {dp_result[1]}")
    print(f"  Chosen items: {dp_result[2]}\n")

    # Порівняння
    diff_calories = dp_result[0] - greedy_result[0]
    print(f"Difference in total calories (DP - Greedy): {diff_calories}")