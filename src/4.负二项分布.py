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
    print("Negative Binomial Distribution Visualizer")
    r = prompt_int("请输入目标成功次数 r（>=1，例如 3）: ", min_value=1)
    p = prompt_probability("请输入每次成功概率 p（0-1 之间，例如 0.5）: ")
    return r, p


def plot_negative_binomial(r: int, p: float) -> None:
    mean = r / p
    std = np.sqrt(r * (1 - p)) / p
    n_max = max(r + 10, int(np.ceil(mean + 4 * std)))
    n_values = np.arange(r, n_max + 1)
    probabilities = comb(n_values - 1, r - 1) * (p ** r) * ((1 - p) ** (n_values - r))

    plt.figure(figsize=(10, 6))
    plt.bar(n_values, probabilities, color="skyblue")
    plt.xlabel("Number of trials n")
    plt.ylabel("Probability P(X = n)")
    plt.title(f"Negative Binomial Distribution: r={r}, p={p}")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    r, p = read_parameters()
    plot_negative_binomial(r, p)


if __name__ == "__main__":
    main()
