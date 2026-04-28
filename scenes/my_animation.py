from manim import *
import numpy as np

class HeartEquation(Scene):
    def construct(self):
        # 1. Setup Axes
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=7,
            y_length=7,
            axis_config={"include_numbers": False}
        ).scale(0.8).shift(UP * 1.2)

        # 2. Setup ValueTracker for 'k'
        k = ValueTracker(0)

        # 3. Setup Text Elements
        # Using RED_B to match the pinkish-red tone from the video
        title = Text("Heart Equation", color=RED_B, font="serif").next_to(axes, DOWN, buff=0.4)
        
        # The mathematical equation
        eq = MathTex(
            r"y = x^{\frac{2}{3}} + 0.9 \sin(kx)\sqrt{3 - x^2}"
        ).next_to(title, DOWN, buff=0.3)
        
        # Dynamic text that updates as 'k' changes
        k_text = always_redraw(
            lambda: MathTex(f"k = {k.get_value():.2f}").next_to(eq, DOWN, buff=0.3)
        )

        self.add(axes, title, eq, k_text)

        # 4. Setup Dynamic Graph
        # always_redraw ensures the graph updates on every frame while k changes
        heart_graph = always_redraw(
            lambda: axes.plot(
                lambda x: np.cbrt(x**2) + 0.9 * np.sin(k.get_value() * x) * np.sqrt(np.clip(3 - x**2, 0, None)),
                x_range=[-np.sqrt(3), np.sqrt(3), 0.002], # Small step size to render high-frequency sine waves smoothly
                color=RED_B
            )
        )
        self.add(heart_graph)

        # 5. Animate the value of 'k' from 0 to 100 over 10 seconds
        self.play(k.animate.set_value(100), run_time=10, rate_func=linear)
        self.wait(1)

        # 6. Fade everything out for the outro
        self.play(
            FadeOut(title),
            FadeOut(eq),
            FadeOut(k_text),
            FadeOut(heart_graph),
            FadeOut(axes)
        )

        # 7. Add Credits
        credit_1 = Text("Created By", font_size=36)
        credit_2 = Text("Priya Ranjan Samal", font_size=48)
        
        # Arrange groups them so the name is directly below "Created By"
        credits = VGroup(credit_1, credit_2).arrange(DOWN, buff=0.5)

        self.play(Write(credits))
        self.wait(2)
