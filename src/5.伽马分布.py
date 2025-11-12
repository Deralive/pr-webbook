import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma as gamma_func


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
    print("Gamma Distribution Visualizer")
    alpha = prompt_positive_float("请输入形状参数 α（>0，例如 2）: ")
    lambd = prompt_positive_float("请输入尺度参数 λ（>0，例如 1）: ")
    return alpha, lambd


def plot_gamma_distribution(alpha: float, lambd: float) -> None:
    mean = alpha / lambd
    std = np.sqrt(alpha) / lambd
    x_max = max(5.0, mean + 5 * std)
    x = np.linspace(0, x_max, 1000)
    pdf = (lambd ** alpha * x ** (alpha - 1) * np.exp(-lambd * x)) / gamma_func(alpha)
    pdf[x < 0] = 0

    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf, color="skyblue", linewidth=2)
    plt.xlabel("Random variable X")
    plt.ylabel("Density f(X)")
    plt.title(f"Gamma Distribution: α={alpha}, λ={lambd}")
    plt.grid(True, alpha=0.3)
    plt.xlim(0, x_max)
    plt.ylim(0, max(0.1, pdf.max() * 1.2))
    plt.tight_layout()
    plt.show()


def main():
    alpha, lambd = read_parameters()
    plot_gamma_distribution(alpha, lambd)


if __name__ == "__main__":
    main()
