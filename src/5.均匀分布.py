import numpy as np
import matplotlib.pyplot as plt


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("请输入有效的小数。")


def read_parameters():
    print("Uniform Distribution Visualizer")
    while True:
        a = prompt_float("请输入下限 a（可为负，例如 0）: ")
        b = prompt_float("请输入上限 b（需大于 a，例如 1）: ")
        if b <= a:
            print("必须满足 b > a，请重新输入。\n")
            continue
        return a, b


def plot_uniform_distribution(a: float, b: float) -> None:
    width = b - a
    margin = max(width * 0.1, 1.0)
    x_min = a - margin
    x_max = b + margin
    x = np.linspace(x_min, x_max, 1000)
    pdf = np.zeros_like(x)
    mask = (x >= a) & (x <= b)
    pdf[mask] = 1 / (b - a)

    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf, color="skyblue", linewidth=2)
    plt.fill_between(x, pdf, where=mask, color="skyblue", alpha=0.3)
    plt.axvline(x=a, color="gray", linestyle="--", alpha=0.7)
    plt.axvline(x=b, color="gray", linestyle="--", alpha=0.7)
    plt.xlabel("Random variable X")
    plt.ylabel("Density f(X)")
    plt.title(f"Uniform Distribution U({a}, {b})")
    plt.grid(True, alpha=0.3)
    plt.xlim(x_min, x_max)
    plt.ylim(0, max(pdf.max() * 1.2, 0.2))
    plt.tight_layout()
    plt.show()


def main():
    a, b = read_parameters()
    plot_uniform_distribution(a, b)


if __name__ == "__main__":
    main()
