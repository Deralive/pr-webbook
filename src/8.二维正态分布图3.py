import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (needed for 3D plotting)
from scipy.stats import multivariate_normal, norm


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("请输入有效的数字。")


def prompt_positive_float(message: str) -> float:
    while True:
        value = prompt_float(message)
        if value > 0:
            return value
        print("该参数必须大于 0。")


def prompt_rho(message: str) -> float:
    while True:
        value = prompt_float(message)
        if -0.99 < value < 0.99:
            return value
        print("相关系数需要在 (-0.99, 0.99) 范围内。")


def read_parameters():
    print("Projection of Bivariate Normal onto X-Z plane (Y=0)")
    mu_x = prompt_float("请输入 μ_x（例如 0）: ")
    mu_y = prompt_float("请输入 μ_y（例如 0）: ")
    sigma_x = prompt_positive_float("请输入 σ_x（>0，例如 1）: ")
    sigma_y = prompt_positive_float("请输入 σ_y（>0，例如 1.2）: ")
    rho = prompt_rho("请输入相关系数 ρ（-0.99 到 0.99，例如 0.6）: ")
    return mu_x, mu_y, sigma_x, sigma_y, rho


def build_grid(mu_x, mu_y, sigma_x, sigma_y):
    span_x = max(4 * sigma_x, 6.0)
    span_y = max(4 * sigma_y, 6.0)
    x = np.linspace(mu_x - span_x, mu_x + span_x, 120)
    y = np.linspace(mu_y - span_y, mu_y + span_y, 120)
    X, Y = np.meshgrid(x, y)
    return x, y, X, Y


def plot_projection(mu_x, mu_y, sigma_x, sigma_y, rho):
    cov = [
        [sigma_x ** 2, rho * sigma_x * sigma_y],
        [rho * sigma_x * sigma_y, sigma_y ** 2],
    ]
    x, y, X, Y = build_grid(mu_x, mu_y, sigma_x, sigma_y)
    pos = np.dstack((X, Y))
    Z = multivariate_normal.pdf(pos, mean=[mu_x, mu_y], cov=cov)

    # Projection onto Y=mu_y plane (shift to zero-centered axis for clarity)
    y_proj = mu_y
    slice_points = np.dstack((x, np.full_like(x, y_proj)))
    z_slice = multivariate_normal.pdf(slice_points, mean=[mu_x, mu_y], cov=cov).flatten()

    # Theoretical 1D marginal over X
    x_marginal = norm.pdf(x, loc=mu_x, scale=sigma_x)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")

    # Main surface
    ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.7, linewidth=0, antialiased=True)

    # Projection plane (Y = mu_y)
    xx, zz = np.meshgrid(x, np.linspace(0, Z.max(), 30))
    yy = np.full_like(xx, y_proj)
    ax.plot_surface(xx, yy, zz, color="gray", alpha=0.15, shade=False)
    ax.text(
        mu_x + 3,
        y_proj,
        Z.max() * 0.8,
        "Plane Y = μ_y",
        color="gray",
    )

    # Slice curve (actual projection)
    ax.plot(
        x,
        np.full_like(x, y_proj),
        z_slice,
        "r-",
        linewidth=3,
        label="Slice at Y = μ_y",
    )

    # Theoretical marginal curve (scaled to overlay)
    scale = z_slice.max() / max(x_marginal.max(), 1e-12)
    ax.plot(
        x,
        np.full_like(x, y_proj),
        x_marginal * scale,
        "b--",
        linewidth=2,
        label="Theoretical marginal (scaled)",
    )

    # Vertical projection lines
    sample_x = np.linspace(mu_x - 3 * sigma_x, mu_x + 3 * sigma_x, 9)
    for xi in sample_x:
        z_proj = multivariate_normal.pdf([xi, y_proj], mean=[mu_x, mu_y], cov=cov)
        ax.plot([xi, xi], [y_proj, y_proj], [0, z_proj], "k--", alpha=0.3)

    ax.set_title("Projection of Bivariate Normal onto X-Z plane (Y fixed)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Density")
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(y.min(), y.max())
    ax.set_zlim(0, Z.max() * 1.1)
    ax.legend(loc="upper right")
    ax.view_init(elev=30, azim=45)
    plt.tight_layout()
    plt.show()


def main():
    params = read_parameters()
    plot_projection(*params)


if __name__ == "__main__":
    main()
