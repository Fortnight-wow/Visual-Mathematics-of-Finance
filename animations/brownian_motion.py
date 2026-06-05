from manim import *
import numpy as np


class BrownianMotion(Scene):
    def construct(self):
        title = Title('Brownian Motion')
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-4, 4, 1],
            axis_config={'include_numbers': True},
        )

        labels = axes.get_axis_labels('Time', 'Position')
        self.play(Create(axes), Write(labels))

        rng = np.random.default_rng(42)

        for _ in range(5):
            x = np.linspace(0, 10, 250)
            increments = rng.normal(0, 0.15, len(x))
            y = np.cumsum(increments)
            y = y / np.max(np.abs(y)) * 3

            path = VMobject()
            points = [axes.c2p(xi, yi) for xi, yi in zip(x, y)]
            path.set_points_as_corners(points)

            self.play(Create(path), run_time=1.5)

        note = Text(
            'Uncertainty grows as time passes',
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(note))
        self.wait(2)
