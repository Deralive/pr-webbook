import numpy as np
import matplotlib.pyplot as plt


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("请输入有效的小数。")


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


def read_parameters():
    print("Normal Distribution Visualizer")
    mean = prompt_float("请输入均值 μ（例如 0）: ")
    variance = prompt_positive_float("请输入方差 σ^2（>0，例如 1）: ")
    return mean, variance


def plot_normal_distribution(mean: float, variance: float) -> None:
    std_dev = np.sqrt(variance)
    span = max(1.0, 4 * std_dev)  # cover most of the density even when mean/variance shift
    x_min = mean - span
    x_max = mean + span
    x = np.linspace(x_min, x_max, 1000)
    y = (1 / (np.sqrt(2 * np.pi * variance))) * np.exp(-(x - mean) ** 2 / (2 * variance))

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color="skyblue", linewidth=2)
    plt.xlabel("Random variable X")
    plt.ylabel("Density f(X)")
    plt.title(f"Normal Distribution: mean={mean}, variance={variance}")
    plt.grid(True, alpha=0.3)
    plt.xlim(x_min, x_max)
    plt.ylim(0, max(0.1, y.max() * 1.2))
    plt.tight_layout()
    plt.show()


def main():
    mean, variance = read_parameters()
    plot_normal_distribution(mean, variance)


if __name__ == "__main__":
    main()
