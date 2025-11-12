import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial


def prompt_positive_float(message: str) -> float:
    while True:
        try:
            value = float(input(message))
        except ValueError:
            print("请输入有效的小数。")
            continue
        if value <= 0:
            print("参数必须大于 0。")
            continue
        return value


def read_parameter():
    print("Poisson Distribution Visualizer")
    lambd = prompt_positive_float("请输入参数 λ（>0，例如 3）: ")
    return lambd


def plot_poisson_distribution(lambd: float) -> None:
    spread = lambd + 4 * np.sqrt(lambd)  # mean + 4 std covers most mass
    max_k = max(10, int(np.ceil(spread)))
    k_values = np.arange(0, max_k + 1)
    probabilities = (lambd ** k_values / factorial(k_values)) * np.exp(-lambd)

    plt.figure(figsize=(10, 6))
    plt.bar(k_values, probabilities, color="skyblue")
    plt.xlabel("Count k")
    plt.ylabel("Probability P(X = k)")
    plt.title(f"Poisson Distribution: λ={lambd}")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    lambd = read_parameter()
    plot_poisson_distribution(lambd)


if __name__ == "__main__":
    main()
