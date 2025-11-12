import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def prompt_distribution() -> str:
    options = {
        "1": "chi2",
        "2": "uniform",
        "3": "exponential",
        "4": "poisson",
    }
    prompt = (
        "请选择基准分布（输入数字）：\n"
        "1. Chi-square distribution (df=2)\n"
        "2. Uniform distribution on [0, 1]\n"
        "3. Exponential distribution (rate=1)\n"
        "4. Poisson distribution (λ=2)\n"
        "你的选择: "
    )
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return options[choice]
        print("请输入 1-4 的数字。")


def read_parameters():
    print("CLT Demo: Comparing sums with different sample sizes")
    dist_key = prompt_distribution()
    return dist_key


def build_pdf(dist_key: str, n: int, x: np.ndarray):
    if dist_key == "chi2":
        return stats.chi2.pdf(x, df=n * 2)
    elif dist_key == "uniform":
        mean = 0.5 * n
        std = np.sqrt(n / 12)
        return stats.norm.pdf(x, loc=mean, scale=max(std, 1e-8))
    elif dist_key == "exponential":
        return stats.gamma.pdf(x, a=n, scale=1)
    else:  # poisson
        mean = 2 * n
        std = np.sqrt(2 * n)
        return stats.norm.pdf(x, loc=mean, scale=max(std, 1e-8))


def determine_range(dist_key: str, n_values):
    if dist_key == "chi2":
        x_min = 0
        x_max = max(12, 4 * max(n_values))
    elif dist_key == "uniform":
        mean = 0.5 * max(n_values)
        std = np.sqrt(max(n_values) / 12)
        x_min = mean - 6 * std
        x_max = mean + 6 * std
    elif dist_key == "exponential":
        x_min = 0
        x_max = max(12, 5 * max(n_values))
    else:  # poisson
        mean = 2 * max(n_values)
        std = np.sqrt(2 * max(n_values))
        x_min = mean - 6 * std
        x_max = mean + 6 * std
    return x_min, x_max


def plot_comparison(dist_key: str):
    n_values = [1, 5, 10, 30]
    x_min, x_max = determine_range(dist_key, n_values)
    x = np.linspace(x_min, x_max, 1200)

    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes = axes.flatten()

    for ax, n in zip(axes, n_values):
        pdf = build_pdf(dist_key, n, x)
        ax.plot(x, pdf, "b-", linewidth=2, label=f"n = {n}")
        ax.set_xlabel("x")
        ax.set_ylabel("Density")
        ax.set_title(f"Sum of {n} variables")
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(bottom=0)
        ax.grid(True, alpha=0.3)
        ax.legend()

    dist_label = {
        "chi2": "chi-square(2)",
        "uniform": "uniform[0,1]",
        "exponential": "exponential(1)",
        "poisson": "poisson(λ=2)",
    }[dist_key]

    fig.suptitle(f"CLT Illustration: summing {dist_label} variables", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


def main():
    dist_key = read_parameters()
    plot_comparison(dist_key)


if __name__ == "__main__":
    main()
