from manim import *


class BlackScholesPDE(Scene):
    def construct(self):
        title = Title("Black-Scholes PDE")
        self.play(Write(title))

        intro = Text(
            "After Ito's Lemma, the option pricing equation appears.",
            font_size=28,
        ).to_edge(UP)
        self.play(Write(intro))

        bs = MathTex(
            r"\frac{\partial V}{\partial t}",
            r"+",
            r"\frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}",
            r"+",
            r"rS\frac{\partial V}{\partial S}",
            r"-",
            r"rV",
            r"= 0",
        )
        bs.scale(0.95).move_to(ORIGIN)

        self.play(Write(bs))
        self.wait(1)

        term1 = SurroundingRectangle(bs[0], color=BLUE, buff=0.15)
        term2 = SurroundingRectangle(bs[2], color=GREEN, buff=0.15)
        term3 = SurroundingRectangle(bs[4], color=YELLOW, buff=0.15)
        term4 = SurroundingRectangle(bs[6], color=RED, buff=0.15)

        labels = VGroup(
            Text("time decay", font_size=24),
            Text("diffusion", font_size=24),
            Text("drift", font_size=24),
            Text("discounting", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(RIGHT)

        self.play(
            Create(term1),
            Create(term2),
            Create(term3),
            Create(term4),
            Write(labels),
        )
        self.wait(1)

        explanation = Text(
            "Hedging removes risk, leaving a pricing equation instead of a return equation.",
            font_size=26,
        ).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        self.play(FadeOut(term1), FadeOut(term2), FadeOut(term3), FadeOut(term4), FadeOut(labels), FadeOut(explanation))

        derivation = MathTex(
            r"\text{Ito's Lemma} \;\rightarrow\; \text{Delta Hedge} \;\rightarrow\; \text{Risk-neutral pricing}"
        )
        derivation.scale(0.8).to_edge(DOWN)
        self.play(Write(derivation))
        self.wait(2)
