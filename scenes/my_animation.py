from manim import *
import numpy as np

# User requested portrait configuration
# (Reels/Shorts format)
config.frame_size = (700, 1000)
config.frame_width = 8

class HeartEquationAnimated(Scene):
    def construct(self):
        # Setting background color to black matching video
        self.camera.background_color = BLACK

        # --- Part 1: Main Graph Animation ---

        # 1. Setup Axes - Scaled and shifted down to accommodate portrait frame
        # and prevent labels going off-screen
        axes = Axes(
            x_range=[-2.5, 2.5, 1], # x range from -2.5 to 2.5
            y_range=[-2.5, 3.5, 1], # y range from -2.5 to 3.5
            axis_config={"include_numbers": False, "color": WHITE},
        ).scale(0.8).shift(DOWN * 0.5)

        # 2. Setup ValueTracker for 'k' variable
        # Initializing k to a very small positive number to avoid zero-division issues
        k_tracker = ValueTracker(0.01)

        # 3. Setup Texts (Matching red/pink color in video)
        # Manim uses LaTeX for MathTex. The equation is from the video.
        title = Text("Heart Equation", color=RED_B).next_to(axes, DOWN, buff=0.5)
        equation = MathTex(
            r"y = x^{\frac{2}{3}} + 0.9 \sin(kx)\sqrt{3 - x^2}",
            color=RED_B
        ).next_to(title, DOWN, buff=0.3).scale(0.9)
        
        # Dynamic 'k=' text that updates every frame
        k_label_text = always_redraw(
            lambda: MathTex(
                f"k = {k_tracker.get_value():.2f}",
                color=RED_B
            ).next_to(equation, DOWN, buff=0.3)
        )

        # Add all elements to scene except the changing graph
        self.add(axes, title, equation, k_label_text)

        # 4. Define and Setup Dynamic Graph
        # always_redraw will re-render the graph when k_tracker changes.
        heart_plot = always_redraw(
            lambda: axes.plot(
                # Mathematical equation from video, using numpy for efficiency.
                # np.cbrt handles negative x properly for absolute value.
                # np.clip handles potential precision errors near the square root boundary.
                lambda x: np.cbrt(x**2) + 0.9 * np.sin(k_tracker.get_value() * x) * np.sqrt(np.clip(3 - x**2, 0, None)),
                x_range=[-np.sqrt(3), np.sqrt(3)],
                color=RED_B,
                use_smoothing=True
            )
        )
        # Adding the initial plot (appearing as lines close to axes)
        self.add(heart_plot)

        # 5. Execute Animation: Increase 'k' value
        # Running linear k value increase from 0 to 100 over 10 seconds.
        # This creates the transition from straight lines to the heart shape.
        self.play(k_tracker.animate.set_value(100), run_time=10, rate_func=linear)
        self.wait(1)

        # Fade out everything from this part
        self.play(
            FadeOut(heart_plot),
            FadeOut(axes),
            FadeOut(title),
            FadeOut(equation),
            FadeOut(k_label_text)
        )
        self.wait(0.5)

        # --- Part 2: Outro (Credits) ---

        # 6. Setup Outro Text
        outro_main = Text("Created By", font_size=36, color=WHITE)
        outro_name = Text("Priya Ranjan Samal", font_size=48, color=RED_B)
        
        # Arrange name below main text
        credits_vgroup = VGroup(outro_main, outro_name).arrange(DOWN, buff=0.4)

        # Play outro animation
        self.play(Write(credits_vgroup), run_time=2.5)
        self.wait(2)
