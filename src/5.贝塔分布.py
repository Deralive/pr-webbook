import numpy as np
import matplotlib.pyplot as plt
from scipy.special import beta as beta_func


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
    print("Beta Distribution Visualizer")
    alpha = prompt_positive_float("请输入形状参数 α（>0，例如 2）: ")
    beta = prompt_positive_float("请输入形状参数 β（>0，例如 2）: ")
    return alpha, beta


def plot_beta_distribution(alpha: float, beta: float) -> None:
    x = np.linspace(0, 1, 1000)
    pdf = (x ** (alpha - 1) * (1 - x) ** (beta - 1)) / beta_func(alpha, beta)

    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf, color="skyblue", linewidth=2)
    plt.xlabel("Random variable X")
    plt.ylabel("Density f(X)")
    plt.title(f"Beta Distribution: α={alpha}, β={beta}")
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1)
    plt.ylim(0, max(3, pdf.max() * 1.1))
    plt.tight_layout()
    plt.show()


def main():
    alpha, beta = read_parameters()
    plot_beta_distribution(alpha, beta)


if __name__ == "__main__":
    main()
