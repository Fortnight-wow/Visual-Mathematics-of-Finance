from manim import *


class DeltaHedging(Scene):
    def construct(self):
        title = Title("Delta Hedging")
        self.play(Write(title))

        intro = Text(
            "A small stock position can offset option risk.",
            font_size=28,
        ).to_edge(UP)
        self.play(Write(intro))

        option_box = RoundedRectangle(corner_radius=0.2, width=3.0, height=1.2)
        option_label = Text("Long Call Option", font_size=28).move_to(option_box.get_center())

        stock_box = RoundedRectangle(corner_radius=0.2, width=3.0, height=1.2)
        stock_box.next_to(option_box, DOWN, buff=1.0)
        stock_label = Text("Short / Long Stock Hedge", font_size=26).move_to(stock_box.get_center())

        arrow = Arrow(option_box.get_bottom(), stock_box.get_top(), buff=0.1)
        hedge_text = MathTex(r"\Delta = \frac{\partial V}{\partial S}").next_to(arrow, RIGHT, buff=0.5)

        self.play(Create(option_box), Write(option_label))
        self.play(Create(stock_box), Write(stock_label))
        self.play(Create(arrow), Write(hedge_text))
        self.wait(1)

        balance = MathTex(
            r"d\Pi = dV - \Delta\,dS"
        ).to_edge(DOWN)
        self.play(Write(balance))
        self.wait(1)

        rebalance = Text(
            "When stock price changes, the hedge is updated.",
            font_size=26,
        ).next_to(balance, UP, buff=0.5)
        self.play(Write(rebalance))
        self.wait(1)

        stock_up = MathTex(r"S \uparrow \,\Rightarrow\, \Delta \uparrow").shift(RIGHT * 3.2)
        stock_down = MathTex(r"S \downarrow \,\Rightarrow\, \Delta \downarrow").shift(LEFT * 3.2)
        self.play(Write(stock_up), Write(stock_down))
        self.wait(1)

        summary = Text(
            "The goal is to make the portfolio locally risk-free.",
            font_size=28,
        ).to_edge(DOWN)
        self.play(Transform(balance, summary))
        self.wait(2)
