import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


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
    print("Step-by-step Monte Carlo Integration Demo")
    n_samples = prompt_int("请输入样本数量 n（50-2000，例如 200）: ", min_value=50, max_value=2000)
    seed = prompt_int("请输入随机种子（>=0，例如 7）: ", min_value=0)
    interval = prompt_int("请输入帧间隔毫秒（>=20，例如 80）: ", min_value=20)
    return n_samples, seed, interval


class MonteCarloAnimator:
    def __init__(self, n_samples: int, seed: int, interval_ms: int):
        self.a, self.b = 0.0, 1.0
        self.n_samples = n_samples
        self.interval_ms = interval_ms
        self.exact_value = np.e - 1.0
        self.rng = np.random.default_rng(seed)
        self.x_samples = self.rng.uniform(self.a, self.b, n_samples)
        self.y_samples = self.rng.uniform(0.0, np.e, n_samples)
        self.fx_samples = np.exp(self.x_samples)

        self.x_fine = np.linspace(self.a, self.b, 400)
        self.fx_fine = np.exp(self.x_fine)

        self.fig, (self.ax_hit, self.ax_mean) = plt.subplots(1, 2, figsize=(12, 5))
        self._setup_axes()

        self.hit_scatter = self.ax_hit.scatter([], [], color="green", s=25, alpha=0.7, label="Hits")
        self.miss_scatter = self.ax_hit.scatter([], [], color="red", s=25, alpha=0.5, label="Misses")
        self.sample_scatter = self.ax_mean.scatter([], [], color="purple", s=30, alpha=0.7, label="Samples")
        (self.mean_line,) = self.ax_mean.plot([], [], "tomato", linestyle="--", linewidth=2, label="Current mean")

        self.hit_text = self.ax_hit.text(
            0.02,
            0.98,
            "",
            transform=self.ax_hit.transAxes,
            va="top",
            bbox=dict(facecolor="white", alpha=0.85),
        )
        self.mean_text = self.ax_mean.text(
            0.02,
            0.98,
            "",
            transform=self.ax_mean.transAxes,
            va="top",
            bbox=dict(facecolor="white", alpha=0.85),
        )

        self.ax_hit.legend(loc="lower right")
        self.ax_mean.legend(loc="lower right")
        self.fig.suptitle("Incremental Estimates: Hit-or-Miss vs Mean Value", fontsize=14)
        self.fig.tight_layout(rect=[0, 0, 1, 0.96])

    def _setup_axes(self):
        # Hit-or-miss panel
        self.ax_hit.plot(self.x_fine, self.fx_fine, color="black", linewidth=2, label="f(x) = e^x")
        self.ax_hit.fill_between(self.x_fine, self.fx_fine, color="steelblue", alpha=0.2)
        self.ax_hit.set_xlim(self.a, self.b)
        self.ax_hit.set_ylim(0.0, np.e)
        self.ax_hit.set_xlabel("x")
        self.ax_hit.set_ylabel("y")
        self.ax_hit.set_title("Hit-or-Miss method")
        self.ax_hit.grid(alpha=0.3)

        # Mean method panel
        self.ax_mean.plot(self.x_fine, self.fx_fine, color="black", linewidth=2, label="f(x) = e^x")
        self.ax_mean.set_xlim(self.a, self.b)
        self.ax_mean.set_ylim(0.0, np.e)
        self.ax_mean.set_xlabel("x")
        self.ax_mean.set_ylabel("f(x)")
        self.ax_mean.set_title("Mean value method")
        self.ax_mean.grid(alpha=0.3)

    def init_artists(self):
        empty = np.empty((0, 2))
        self.hit_scatter.set_offsets(empty)
        self.miss_scatter.set_offsets(empty)
        self.sample_scatter.set_offsets(empty)
        self.mean_line.set_data([], [])
        self.hit_text.set_text("")
        self.mean_text.set_text("")
        return (
            self.hit_scatter,
            self.miss_scatter,
            self.sample_scatter,
            self.mean_line,
            self.hit_text,
            self.mean_text,
        )

    def update(self, frame: int):
        count = frame + 1
        x_current = self.x_samples[:count]
        y_current = self.y_samples[:count]
        fx_current = self.fx_samples[:count]
        hit_mask = y_current <= fx_current

        self.hit_scatter.set_offsets(np.column_stack((x_current[hit_mask], y_current[hit_mask])))
        self.miss_scatter.set_offsets(np.column_stack((x_current[~hit_mask], y_current[~hit_mask])))

        hit_estimate = (self.b - self.a) * np.e * hit_mask.mean()
        hit_error = abs(hit_estimate - self.exact_value)
        self.hit_text.set_text(
            f"Samples: {count}\n"
            f"Hits: {hit_mask.sum()}\n"
            f"Estimate = {hit_estimate:.6f}\n"
            f"Abs. error = {hit_error:.6f}"
        )

        self.sample_scatter.set_offsets(np.column_stack((x_current, fx_current)))
        mean_level = fx_current.mean()
        self.mean_line.set_data([self.a, self.b], [mean_level, mean_level])
        mean_estimate = (self.b - self.a) * mean_level
        mean_error = abs(mean_estimate - self.exact_value)
        self.mean_text.set_text(
            f"Samples: {count}\n"
            f"Mean f(x) = {mean_level:.5f}\n"
            f"Estimate = {mean_estimate:.6f}\n"
            f"Abs. error = {mean_error:.6f}"
        )

        return (
            self.hit_scatter,
            self.miss_scatter,
            self.sample_scatter,
            self.mean_line,
            self.hit_text,
            self.mean_text,
        )

    def run(self):
        # Keep a reference to the animation object to prevent garbage collection.
        self.ani = FuncAnimation(
            self.fig,
            self.update,
            frames=self.n_samples,
            init_func=self.init_artists,
            interval=self.interval_ms,
            blit=False,
            repeat=False,
        )
        plt.show()


def main():
    n_samples, seed, interval = read_parameters()
    animator = MonteCarloAnimator(n_samples, seed, interval)
    animator.run()


if __name__ == "__main__":
    main()
