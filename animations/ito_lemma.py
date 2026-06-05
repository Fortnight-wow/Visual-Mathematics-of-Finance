from manim import *


class ItoLemma(Scene):
    def construct(self):
        title = Title("Ito's Lemma")
        self.play(Write(title))

        intro = Text(
            "A small change in the input creates a predictable change in the output.",
            font_size=28,
        ).to_edge(UP)
        self.play(Write(intro))

        drift_diffusion = MathTex(
            r"dS_t = \mu S_t\,dt + \sigma S_t\,dW_t"
        )
        drift_diffusion.move_to(ORIGIN)

        self.play(Write(drift_diffusion))
        self.wait(1)

        self.play(drift_diffusion.animate.shift(UP * 1.5))

        lemma = MathTex(
            r"df(S_t,t)",
            r"=",
            r"\frac{\partial f}{\partial t}dt",
            r"+",
            r"\frac{\partial f}{\partial S}dS_t",
            r"+",
            r"\frac{1}{2}\frac{\partial^2 f}{\partial S^2}(dS_t)^2"
        )
        lemma.scale(0.85).next_to(drift_diffusion, DOWN, buff=0.8)

        self.play(Write(lemma))
        self.wait(1)

        box = SurroundingRectangle(lemma[6], color=YELLOW, buff=0.15)
        note = Text(
            "This extra term is the key difference from ordinary calculus.",
            font_size=26,
        ).to_edge(DOWN)

        self.play(Create(box), Write(note))
        self.wait(2)

        self.play(FadeOut(box), FadeOut(note))

        replacement = MathTex(
            r"df = \left(\frac{\partial f}{\partial t} + \mu S\frac{\partial f}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 f}{\partial S^2}\right)dt"
            r"+ \sigma S\frac{\partial f}{\partial S} dW_t"
        )
        replacement.scale(0.85).move_to(lemma.get_center())

        self.play(TransformMatchingTex(lemma, replacement))

        closing = Text(
            "Randomness changes the calculus itself.",
            font_size=28,
        ).to_edge(DOWN)
        self.play(Write(closing))
        self.wait(2)
