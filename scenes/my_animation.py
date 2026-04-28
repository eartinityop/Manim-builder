from manim import *

class CalculateCircleArea(Scene):
    def construct(self):
        # Explicitly set the background color to black (default in Manim)
        self.camera.background_color = BLACK

        # --- 1. Define the Shapes and Text ---
        
        # Create the circle using a light blue hex code
        light_blue = "#ADD8E6"
        circle = Circle(radius=2.0, color=light_blue)
        circle.set_fill(light_blue, opacity=0.0) # Start transparent
        circle.move_to(LEFT * 2)

        # Create the radius line and label
        radius_line = Line(circle.get_center(), circle.get_right(), color=WHITE)
        r_label = MathTex("r").next_to(radius_line, UP, buff=0.2)

        # Create the titles and formulas
        title_text = Text("Area of a Circle", font_size=36).move_to(RIGHT * 3 + UP * 1)
        formula_math = MathTex("A = \pi r^2", font_size=54).next_to(title_text, DOWN, buff=0.5)

        # --- 2. Animation Sequence ---
        
        # Animate drawing the circle's perimeter
        self.play(Create(circle), run_time=1.5)
        self.wait(0.5)

        # Draw the radius line and label
        self.play(Create(radius_line))
        self.play(Write(r_label))
        self.wait(0.5)

        # Write out the formulas on the right side
        self.play(Write(title_text))
        self.play(Write(formula_math))
        self.wait(1)

        # Highlight the concept by filling the circle and indicating the formula
        self.play(
            circle.animate.set_fill(light_blue, opacity=0.5),
            Indicate(formula_math, color=YELLOW),
            run_time=1.5
        )
        self.wait(2)
