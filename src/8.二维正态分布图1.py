import numpy as np
import matplotlib.pyplot as plt
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
        if value <= -0.99 or value >= 0.99:
            print("相关系数需要在 (-0.99, 0.99) 范围内，以避免奇异协方差矩阵。")
            continue
        return value


def read_parameters():
    print("Bivariate Normal Visualization")
    mu_x = prompt_float("请输入 μ_x（例如 0）: ")
    mu_y = prompt_float("请输入 μ_y（例如 0）: ")
    sigma_x = prompt_positive_float("请输入 σ_x（>0，例如 1）: ")
    sigma_y = prompt_positive_float("请输入 σ_y（>0，例如 1）: ")
    rho = prompt_rho("请输入相关系数 ρ（-0.99 到 0.99，例如 0）: ")
    return mu_x, mu_y, sigma_x, sigma_y, rho


def compute_bivariate_pdf(mu_x, mu_y, sigma_x, sigma_y, rho):
    span_x = max(4 * sigma_x, 6.0)
    span_y = max(4 * sigma_y, 6.0)
    x = np.linspace(mu_x - span_x, mu_x + span_x, 150)
    y = np.linspace(mu_y - span_y, mu_y + span_y, 150)
    X, Y = np.meshgrid(x, y)

    rho_sq = rho ** 2
    sigma_x_sq = sigma_x ** 2
    sigma_y_sq = sigma_y ** 2
    denom = 2 * np.pi * sigma_x * sigma_y * np.sqrt(1 - rho_sq)
    diff_x = X - mu_x
    diff_y = Y - mu_y
    exponent = (
        (diff_x ** 2) / sigma_x_sq
        - 2 * rho * diff_x * diff_y / (sigma_x * sigma_y)
        + (diff_y ** 2) / sigma_y_sq
    )
    Z = np.exp(-exponent / (2 * (1 - rho_sq))) / denom
    return X, Y, Z, x, y


def plot_bivariate_normal(mu_x, mu_y, sigma_x, sigma_y, rho):
    X, Y, Z, x, y = compute_bivariate_pdf(mu_x, mu_y, sigma_x, sigma_y, rho)
    z_max = Z.max() * 1.05
    fig = plt.figure(figsize=(14, 6))

    # 3D surface
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    ax1.plot_surface(X, Y, Z, cmap=cm.viridis, alpha=0.85, rstride=2, cstride=2)
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_zlabel("Density")
    ax1.set_title(f"Joint PDF (μx={mu_x}, μy={mu_y})")
    ax1.set_xlim(x.min(), x.max())
    ax1.set_ylim(y.min(), y.max())
    ax1.set_zlim(0, z_max)
    ax1.view_init(elev=30, azim=45)

    # Contour
    ax2 = fig.add_subplot(1, 2, 2)
    contour = ax2.contour(X, Y, Z, 12, cmap=cm.viridis)
    ax2.clabel(contour, inline=True, fontsize=8)
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.set_title(f"Contours (ρ={rho}, σx={sigma_x}, σy={sigma_y})")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def main():
    params = read_parameters()
    plot_bivariate_normal(*params)


if __name__ == "__main__":
    main()
