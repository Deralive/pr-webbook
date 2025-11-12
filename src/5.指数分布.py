import numpy as np
import matplotlib.pyplot as plt


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
    print("Exponential Distribution Visualizer")
    lambd = prompt_positive_float("请输入参数 λ（>0，例如 1）: ")
    return lambd


def plot_exponential_distribution(lambd: float) -> None:
    x_max = max(10.0, 5.0 / lambd)
    x = np.linspace(0, x_max, 1000)
    pdf = lambd * np.exp(-lambd * x)
    x_threshold = 2
    exceed_prob = np.exp(-lambd * x_threshold)
    exceed_pct = exceed_prob * 100

    plt.figure(figsize=(12, 8))
    plt.plot(x, pdf, color="skyblue", linewidth=3, label=f"PDF (λ={lambd})")

    mask = x > x_threshold
    plt.fill_between(x[mask], pdf[mask], color="lightgreen", alpha=0.5,
                     label=f"P(X > {x_threshold}) = {exceed_pct:.1f}%")

    peak_y = lambd * np.exp(-lambd * (x_threshold + 0.5))
    plt.annotate(f"{exceed_pct:.1f}%",
                 xy=(x_threshold + 0.5, peak_y),
                 xytext=(x_threshold + 1.5, peak_y + 0.2),
                 arrowprops=dict(facecolor="black", shrink=0.05, width=1.5, headwidth=8),
                 fontsize=12)

    plt.xlabel("Time interval X")
    plt.ylabel("Density f(X)")
    plt.title("Exponential Distribution and Tail Probability")
    plt.grid(True, alpha=0.3)
    plt.xlim(0, x_max)
    plt.ylim(0, max(0.5, pdf.max() * 1.2))
    plt.legend()
    plt.figtext(0.15, 0.01,
                "Notes:\n"
                "1. Memoryless property: P(X>s+t | X>s) = P(X>t).\n"
                f"2. Shaded area represents P(X > {x_threshold}).",
                fontsize=10, bbox=dict(facecolor="white", alpha=0.85))
    plt.tight_layout(rect=[0, 0.08, 1, 0.97])
    plt.show()


def main():
    lambd = read_parameter()
    plot_exponential_distribution(lambd)


if __name__ == "__main__":
    main()
