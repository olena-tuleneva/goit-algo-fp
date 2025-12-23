import random
import matplotlib.pyplot as plt

# Аналітичні ймовірності
analytical_probs = {
    2: (1/36, "1/36"), 3: (2/36, "2/36"), 4: (3/36, "3/36"),
    5: (4/36, "4/36"), 6: (5/36, "5/36"), 7: (6/36, "6/36"),
    8: (5/36, "5/36"), 9: (4/36, "4/36"), 10: (3/36, "3/36"),
    11: (2/36, "2/36"), 12: (1/36, "1/36")
}

def simulate_dice_rolls(num_rolls):
    counts = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        counts[die1 + die2] += 1

    probabilities = {total: count / num_rolls for total, count in counts.items()}
    return probabilities

def plot_probabilities(probabilities, num_rolls):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, tick_label=sums, alpha=0.7, color='skyblue', label='Monte-Carlo')
    analytical_values = [analytical_probs[s][0] for s in sums]
    plt.plot(sums, analytical_values, color='red', marker='o', linestyle='-', linewidth=2, label='Analytical')
    
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title(f'Ймовірності сум при {num_rolls} кидках')
    plt.legend()
    
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob + 0.005, f"{prob*100:.2f}%", ha='center')
    
    plt.show()

if __name__ == "__main__":
    for num_rolls in [100, 1000, 10000, 100000]:
        print(f"\n=== Кидків: {num_rolls} ===")
        monte_probs = simulate_dice_rolls(num_rolls)

        print(f"{'Сума':<5} {'Ймовірність':<12}")
        print("-" * 20)
        for s in range(2, 13):
            prob_percent = monte_probs[s] * 100
            analytic_frac = analytical_probs[s][1]
            print(f"{s:<5} {prob_percent:>6.2f}% ({analytic_frac})")

        plot_probabilities(monte_probs, num_rolls)
