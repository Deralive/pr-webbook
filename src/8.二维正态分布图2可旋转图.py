import numpy as np
import matplotlib.pyplot as plt
# 导入 3D 绘图工具
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from scipy.stats import multivariate_normal
from matplotlib import cm


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("请输入有效的数字。")


def prompt_positive_float(message: str) -> float:
    while True:
        value = prompt_float(message)
        if value <= 0:
            print("该参数必须大于 0。")
            continue
        return value


def prompt_rho(message: str) -> float:
    while True:
        value = prompt_float(message)
        if -0.99 < value < 0.99:
            return value
        print("相关系数需要在 (-0.99, 0.99) 范围内。")


def read_parameters():
    print("Interactive Bivariate Normal Surface")
    mu_x = prompt_float("请输入 μ_x（例如 0）: ")
    mu_y = prompt_float("请输入 μ_y（例如 0）: ")
    sigma_x = prompt_positive_float("请输入 σ_x（>0，例如 1）: ")
    sigma_y = prompt_positive_float("请输入 σ_y（>0，例如 1）: ")
    rho = prompt_rho("请输入相关系数 ρ（-0.99 到 0.99，例如 0.5）: ")
    return mu_x, mu_y, sigma_x, sigma_y, rho


def compute_surface(mu_x, mu_y, sigma_x, sigma_y, rho):
    cov = [
        [sigma_x ** 2, rho * sigma_x * sigma_y],
        [rho * sigma_x * sigma_y, sigma_y ** 2],
    ]

    span_x = max(3 * sigma_x, 4.0)
    span_y = max(3 * sigma_y, 4.0)
    x = np.linspace(mu_x - span_x, mu_x + span_x, 150)
    y = np.linspace(mu_y - span_y, mu_y + span_y, 150)
    X, Y = np.meshgrid(x, y)
    pos = np.dstack((X, Y))
    Z = multivariate_normal.pdf(pos, mean=[mu_x, mu_y], cov=cov)
    return X, Y, Z


def plot_surface(X, Y, Z, mu_x, mu_y, sigma_x, sigma_y, rho):
    fig = plt.figure(figsize=(9, 7))
    # 使用 fig.add_subplot 配合 projection='3d' 创建 3D 坐标轴
    ax = fig.add_subplot(111, projection='3d')

    # 绘制 3D 曲面图
    ax.plot_surface(
        X, Y, Z,
        cmap=cm.viridis,
        linewidth=0,
        antialiased=False,
        alpha=0.85  # 设置透明度
    )

    # 设置标题和标签
    ax.set_title(f"3D Bivariate Normal Surface (μx={mu_x}, μy={mu_y}, ρ={rho})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Density")

    # 调整视角
    ax.view_init(elev=30, azim=45)

    plt.tight_layout()
    plt.show()


def main():
    mu_x, mu_y, sigma_x, sigma_y, rho = read_parameters()
    X, Y, Z = compute_surface(mu_x, mu_y, sigma_x, sigma_y, rho)
    plot_surface(X, Y, Z, mu_x, mu_y, sigma_x, sigma_y, rho)


if __name__ == "__main__":
    main()