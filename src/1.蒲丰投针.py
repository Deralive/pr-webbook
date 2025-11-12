import numpy as np
import matplotlib.pyplot as plt


def prompt_positive_float(message: str) -> float:
    """Request a positive numeric value from stdin."""
    while True:
        try:
            value = float(input(message))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value <= 0:
            print("Value must be greater than zero.")
            continue
        return value


def read_parameters():
    print("Buffon's Needle Simulation (9 throws)")
    while True:
        l = prompt_positive_float("针的长度 l (比如5): ")
        d = prompt_positive_float("线的空间 d (最好大于线长度哦,比如8): ")
        if l >= d:
            print("Constraint violated: l must be smaller than d. Try again.\n")
            continue
        return l, d


def simulate_and_plot(l: float, d: float) -> None:
    x_min = 0.0
    x_max = d * 3
    y_min = -l
    y_max = l + d
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    axes = axes.flatten()
    cross_count = 0

    for idx, ax in enumerate(axes, start=1):
        phi = np.random.uniform(0, np.pi)
        x_center = np.random.uniform(d, d * 2)
        y_center = np.random.uniform(0, d)

        half_len = l / 2
        x1 = x_center - half_len * np.cos(phi)
        y1 = y_center - half_len * np.sin(phi)
        x2 = x_center + half_len * np.cos(phi)
        y2 = y_center + half_len * np.sin(phi)

        hit = False
        for j in range(4):
            if min(y1, y2) <= j * d <= max(y1, y2):
                hit = True
                cross_count += 1
                break

        ax.set_title(f"Trial {idx}")
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_aspect("equal")
        ax.axis("on")

        for j in range(4):
            ax.axhline(y=j * d, color="black", linestyle="-", linewidth=1)

        color = "red" if hit else "blue"
        ax.plot([x1, x2], [y1, y2], color, linewidth=2)
        ax.plot(x_center, y_center, "bo", markersize=5)

        arc_radius = l / 4
        arc_angles = np.linspace(0, phi, 100)
        arc_x = x_center + arc_radius * np.cos(arc_angles)
        arc_y = y_center + arc_radius * np.sin(arc_angles)
        ax.plot(arc_x, arc_y, "g-", linewidth=1)
        ax.text(x_center + arc_radius * 1.1,
                y_center + arc_radius * 0.3,
                r"$\phi$",
                fontsize=12)

        status_y = y_min + 0.1 * (y_max - y_min)
        ax.text(x_min + 0.1 * (x_max - x_min),
                status_y,
                f"Status: {'hit' if hit else 'miss'}",
                fontsize=10,
                bbox=dict(facecolor="white", alpha=0.8))

    plt.tight_layout()
    plt.show()

    theoretical_probability = (2 * l) / (np.pi * d)
    empirical_ratio = cross_count / 9
    print(f"Theoretical probability P = {theoretical_probability:.4f}")
    print(f"Empirical hit ratio = {empirical_ratio:.4f} ({cross_count}/9)")
def main():
    l, d = read_parameters()
    simulate_and_plot(l, d)


if __name__ == "__main__":
    main()
