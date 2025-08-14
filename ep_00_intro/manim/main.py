from manim import *
import palette as G

config.background_color = G.BG
Text.set_default(color=G.FG)
MathTex.set_default(color=G.FG)   
Square.set_default(fill_opacity=0.0, stroke_color=G.BLUE)

# Some global vvariables
ft_size=24
ft = "JetBrainsMono Nerd Font"


class DefaultTemplate(Scene):
    def construct(self):
        stickman = ImageMobject("assets/stickman_gestures1.png")
        stickman.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        stickman.scale(6)

        stickman_exclam = ImageMobject("assets/stickman_gestures2.png")
        stickman_exclam.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        stickman_exclam.scale(6)
        stickman_exclam.next_to(stickman)

        stickman_question = ImageMobject("assets/stickman_gestures3.png")
        stickman_question.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        stickman_question.scale(6)
        stickman_question.next_to(stickman_exclam)

        teacher = ImageMobject("assets/teacher_gestures1.png")
        teacher.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        teacher.scale(8)
        teacher.next_to(stickman_question)

        teacher_point = ImageMobject("assets/teacher_gestures2.png")
        teacher_point.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        teacher_point.scale(8)
        teacher_point.next_to(teacher)

        c = ImageMobject("assets/C_Programming_Language.png")
        c.set_resampling_algorithm(RESAMPLING_ALGORITHMS["linear"])
        c.scale(0.5)
        c.next_to(stickman, DOWN)


        self.add(stickman)
        self.add(stickman_exclam)
        self.add(stickman_question)
        self.add(teacher)
        self.add(teacher_point)
        square = Square()
        self.play(Create(square), FadeIn(c))
        self.wait(3)
