import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


def prompt_int(message: str, *, min_value: int = None, max_value: int = None) -> int:
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("请输入有效的整数。")
            continue
        if min_value is not None and value < min_value:
            print(f"数值必须 >= {min_value}。")
            continue
        if max_value is not None and value > max_value:
            print(f"数值必须 <= {max_value}。")
            continue
        return value


def prompt_probability(message: str) -> float:
    while True:
        try:
            value = float(input(message))
        except ValueError:
            print("请输入有效的小数。")
            continue
        if not (0 < value < 1):
            print("概率需要在 0 和 1 之间（不含端点）。")
            continue
        return value


def read_parameters():
    print("Binomial Distribution Visualizer")
    n = prompt_int("请输入试验次数 n（>=1，例如 10）: ", min_value=1)
    p = prompt_probability("请输入成功概率 p（0-1 之间，例如 0.5）: ")
    return n, p


def plot_binomial_distribution(n: int, p: float) -> None:
    k_values = np.arange(0, n + 1)
    probabilities = comb(n, k_values) * (p ** k_values) * ((1 - p) ** (n - k_values))

    plt.figure(figsize=(10, 6))
    plt.bar(k_values, probabilities, color="skyblue")
    plt.xlabel("Number of successes k")
    plt.ylabel("Probability P(X = k)")
    plt.title(f"Binomial Distribution: n={n}, p={p}")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    n, p = read_parameters()
    plot_binomial_distribution(n, p)


if __name__ == "__main__":
    main()
