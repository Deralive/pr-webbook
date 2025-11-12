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


def read_parameters():
    print("超几何分布可视化")
    while True:
        N = prompt_int("请输入总体大小 N（>=1，例如 50）: ", min_value=1)
        K = prompt_int("请输入成功元素个数 K（0 到 N，例如 10）: ", min_value=0, max_value=N)
        n = prompt_int("请输入抽样次数 n（1 到 N，例如 5）: ", min_value=1, max_value=N)

        if n > N:
            print("抽样次数 n 不能大于 N，请重新输入。\n")
            continue
        if K > N:
            print("成功元素个数 K 不能大于 N，请重新输入。\n")
            continue
        # valid set
        return N, K, n


def hypergeometric_pmf(N: int, K: int, n: int):
    k_min = max(0, n - (N - K))
    k_max = min(n, K)
    k_values = np.arange(k_min, k_max + 1)
    numerator = comb(K, k_values) * comb(N - K, n - k_values)
    denominator = comb(N, n)
    probabilities = numerator / denominator
    return k_values, probabilities


def plot_distribution(N: int, K: int, n: int):
    k_values, probabilities = hypergeometric_pmf(N, K, n)

    plt.figure(figsize=(10, 6))
    plt.bar(k_values, probabilities, color="skyblue")
    plt.xlabel("Number of successes k")
    plt.ylabel("Probability P(X = k)")
    plt.title(f"Hypergeometric Distribution: N={N}, K={K}, n={n}")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    N, K, n = read_parameters()
    plot_distribution(N, K, n)


if __name__ == "__main__":
    main()
