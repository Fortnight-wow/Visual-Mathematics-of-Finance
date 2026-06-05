from manim import *
import numpy as np


class GeometricBrownianMotion(Scene):
    def construct(self):
        title = Title('Geometric Brownian Motion')
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 250, 50],
            axis_config={'include_numbers': True},
        )

        labels = axes.get_axis_labels('Time', 'Stock Price')
        self.play(Create(axes), Write(labels))

        explanation = Text(
            'Unlike Brownian Motion, stock prices remain positive.',
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(explanation))

        rng = np.random.default_rng(42)

        for _ in range(5):
            steps = 250
            dt = 10 / steps
            mu = 0.10
            sigma = 0.25

            prices = [100]

            for _ in range(steps):
                z = rng.normal()
                next_price = prices[-1] * np.exp(
                    (mu - 0.5 * sigma**2) * dt / 10
                    + sigma * np.sqrt(dt / 10) * z
                )
                prices.append(next_price)

            x = np.linspace(0, 10, len(prices))

            curve = VMobject()
            curve.set_points_as_corners(
                [axes.c2p(xi, yi) for xi, yi in zip(x, prices)]
            )

            self.play(Create(curve), run_time=1.5)

        final_note = Text(
            'Volatility increases uncertainty while preserving positivity.',
            font_size=26
        ).to_edge(UP)

        self.play(Write(final_note))
        self.wait(2)
