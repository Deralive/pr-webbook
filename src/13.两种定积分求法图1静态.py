import numpy as np
import matplotlib.pyplot as plt


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


def read_parameters():
    print("Monte Carlo Integration (Hit-or-Miss vs Mean)")
    n_samples = prompt_int("请输入样本数量 n（>=10，例如 500）: ", min_value=10)
    seed = prompt_int("请输入随机种子（>=0，例如 42）: ", min_value=0)
    return n_samples, seed


def monte_carlo_comparison(n_samples: int, seed: int) -> None:
    a, b = 0.0, 1.0
    exact_value = np.e - 1.0
    rng = np.random.default_rng(seed)

    x_samples = rng.uniform(a, b, n_samples)
    y_samples = rng.uniform(0.0, np.e, n_samples)
    fx_samples = np.exp(x_samples)
    hit_mask = y_samples <= fx_samples

    hit_estimate = (b - a) * np.e * hit_mask.mean()
    mean_estimate = (b - a) * fx_samples.mean()
    hit_error = abs(hit_estimate - exact_value)
    mean_error = abs(mean_estimate - exact_value)

    x_fine = np.linspace(a, b, 400)
    fx_fine = np.exp(x_fine)

    fig, (ax_hit, ax_mean) = plt.subplots(1, 2, figsize=(12, 5))

    # Hit-or-miss (area sampling)
    ax_hit.plot(x_fine, fx_fine, color="black", linewidth=2, label="f(x) = e^x")
    ax_hit.fill_between(x_fine, fx_fine, color="steelblue", alpha=0.25, label=f"Exact area = {exact_value:.4f}")
    ax_hit.scatter(x_samples[hit_mask], y_samples[hit_mask], color="green", s=15, alpha=0.7, label=f"Hits: {hit_mask.sum()}")
    ax_hit.scatter(x_samples[~hit_mask], y_samples[~hit_mask], color="red", s=15, alpha=0.5,
                   label=f"Misses: {n_samples - hit_mask.sum()}")
    ax_hit.set_xlim(a, b)
    ax_hit.set_ylim(0.0, np.e)
    ax_hit.set_xlabel("x")
    ax_hit.set_ylabel("y")
    ax_hit.set_title(f"Hit-or-Miss Method (n={n_samples})")
    ax_hit.grid(alpha=0.25)
    ax_hit.legend(loc="upper left", fontsize=9)
    ax_hit.text(
        0.02,
        0.02,
        f"Estimate = {hit_estimate:.6f}\n"
        f"Exact = {exact_value:.6f}\n"
        f"Abs. error = {hit_error:.6f}\n"
        f"Rel. error = {hit_error / exact_value * 100:.2f}%",
        transform=ax_hit.transAxes,
        bbox=dict(facecolor="white", alpha=0.85),
        fontsize=9,
    )

    # Mean value method
    ax_mean.plot(x_fine, fx_fine, color="black", linewidth=2, label="f(x) = e^x")
    ax_mean.scatter(x_samples, fx_samples, color="purple", s=15, alpha=0.6, label="Sampled f(x)")
    mean_level = fx_samples.mean()
    ax_mean.axhline(mean_level, color="tomato", linestyle="--", linewidth=2, label=f"Sample mean = {mean_level:.4f}")
    ax_mean.fill_between([a, b], mean_level, color="tomato", alpha=0.25,
                         label=f"Approx. area = {mean_estimate:.4f}")
    ax_mean.set_xlim(a, b)
    ax_mean.set_ylim(0.0, np.e)
    ax_mean.set_xlabel("x")
    ax_mean.set_ylabel("f(x)")
    ax_mean.set_title(f"Mean Value Method (n={n_samples})")
    ax_mean.grid(alpha=0.25)
    ax_mean.legend(loc="upper left", fontsize=9)
    ax_mean.text(
        0.02,
        0.02,
        f"Estimate = {mean_estimate:.6f}\n"
        f"Exact = {exact_value:.6f}\n"
        f"Abs. error = {mean_error:.6f}\n"
        f"Rel. error = {mean_error / exact_value * 100:.2f}%",
        transform=ax_mean.transAxes,
        bbox=dict(facecolor="white", alpha=0.85),
        fontsize=9,
    )

    fig.suptitle("Comparison of Two Monte Carlo Integration Methods", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()

    print("----- Numerical Summary -----")
    print(f"Hit-or-miss estimate : {hit_estimate:.6f} (abs error = {hit_error:.6f})")
    print(f"Mean-value estimate  : {mean_estimate:.6f} (abs error = {mean_error:.6f})")
    print(f"Exact integral value : {exact_value:.6f}")


def main():
    n_samples, seed = read_parameters()
    monte_carlo_comparison(n_samples, seed)


if __name__ == "__main__":
    main()
