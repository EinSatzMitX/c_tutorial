from manim import *
import palette as G

config.background_color = G.BG
Text.set_default(color=G.FG)
MathTex.set_default(color=G.FG)   
Square.set_default(fill_opacity=0.0, stroke_color=G.BLUE)

# Some global vvariables
ft_size=24
ft_size_mid=30
ft_size_large=36
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



        self.play(FadeIn(c))
        self.wait(3)
        self.play(FadeOut(c))


        self.wait(5)

        contents_t = Text("Contents", font_size=ft_size_large, font=ft).to_edge(UP)
        contents_t.set_color(G.ORANGE)
        what_is_c_t = Text("What is C?", font_size=ft_size, font=ft).next_to(contents_t, DOWN*4)
        why_c_t = Text("Why should you learn C?", font_size=ft_size, font=ft).next_to(what_is_c_t, DOWN*2)
        requirements_t = Text("What programs are required for the tutorial series?", font_size=ft_size, font=ft).next_to(why_c_t, DOWN*2)
        writing_c_t = Text("Writing your own program in C", font_size=ft_size, font=ft).next_to(requirements_t, DOWN*2)


        self.play(FadeIn(contents_t), FadeIn(what_is_c_t), FadeIn(why_c_t), FadeIn(requirements_t), FadeIn(writing_c_t))
        self.wait(5)
        self.play( FadeOut(why_c_t), FadeOut(requirements_t), FadeOut(writing_c_t))

        what_is_c_big_t = Text(
            "What is C?",
            font_size=ft_size_large,  # or whatever larger size you want
            font=ft,
            color=G.ORANGE             # already orange
        ).move_to(contents_t.get_center())  # position where "Contents" was

        # animate: fade out old title, transform "What is C?" into the bigger orange one
        self.play(
            FadeOut(contents_t),
            ReplacementTransform(what_is_c_t, what_is_c_big_t)
        )
        self.wait(2)

        founded_t = Text("Developed in 1972, by Dennis Ritchie and Ken Thompson", font_size=ft_size, font=ft).next_to(what_is_c_big_t, DOWN*4)

        founders_i = ImageMobject("assets/C_founders.png")
        founders_i.set_resampling_algorithm(RESAMPLING_ALGORITHMS["linear"])
        founders_i.scale(2)
        founders_i.next_to(founded_t, DOWN*2)


        self.play(FadeIn(founded_t), FadeIn(founders_i))
        self.wait(2)
        self.play(
                founded_t.animate.shift(UP * 0.75).scale(0.6),
                founders_i.animate.shift(UP * 1.5).scale(0.6)
        )
        self.wait(2)


        uses_cases_t = Text("Use Cases:", font_size=ft_size_mid, font=ft, color=G.YELLOW).next_to(founders_i, DOWN*2)
        embedded_systems_t = Text("Embedded Systems", font_size=ft_size, font=ft).next_to(uses_cases_t, DOWN*2)
        embedded_systems_i = ImageMobject("assets/embedded_systems.jpg")
        embedded_systems_i.set_resampling_algorithm(RESAMPLING_ALGORITHMS["linear"])
        embedded_systems_i.scale(0.25)
        embedded_systems_i.next_to(embedded_systems_t, DOWN*2)

        self.play(FadeIn(uses_cases_t))
        self.play(FadeIn(embedded_systems_t), FadeIn(embedded_systems_i))

        self.wait(2)

        self.play(embedded_systems_t.animate.shift(LEFT*2), embedded_systems_i.animate.shift(LEFT*2))


        os_t = Text("Operating Systems", font_size=ft_size, font=ft).next_to(embedded_systems_t, RIGHT*4)
        tux_i = ImageMobject("assets/Tux.png")
        tux_i.set_resampling_algorithm(RESAMPLING_ALGORITHMS["linear"])
        tux_i.scale(0.25)
        tux_i.next_to(os_t, DOWN*2)

        self.play(FadeIn(os_t), FadeIn(tux_i))
        
        self.wait(3)

        self.play(FadeOut(founded_t), FadeOut(founders_i), FadeOut(uses_cases_t), FadeOut(embedded_systems_t), FadeOut(embedded_systems_i), FadeOut(os_t), FadeOut(tux_i))

        self.wait(2)

        # Now talk about the pros of C

        pros_t = Text("Pros", font=ft, font_size = ft_size_mid, color=G.GREEN).next_to(what_is_c_big_t, DOWN * 6)

        self.play(FadeIn(pros_t))

        clear_t = Text("Readability", font=ft, font_size=ft_size).next_to(pros_t, DOWN*2.5)
        speed_t = Text("Execution speed", font=ft, font_size=ft_size).next_to(clear_t, DOWN*1.5)
        abstract_t = Text("Abstracts Machine Code", font=ft, font_size=ft_size).next_to(speed_t, DOWN*1.5)

        self.play(FadeIn(clear_t))
        self.wait(1)
        self.play(FadeIn(speed_t))
        self.wait(1)
        self.play(FadeIn(abstract_t))
        self.wait(1)
        self.play(pros_t.animate.shift(LEFT*4), speed_t.animate.shift(LEFT*4), clear_t.animate.shift(LEFT*4), abstract_t.animate.shift(LEFT*4))

        self.wait(2)
        # Now the cons
        cons_t = Text("Cons", font=ft, font_size = ft_size_mid, color=G.RED).next_to(what_is_c_big_t, DOWN* 6+ RIGHT*4)
        self.play(FadeIn(cons_t))
        self.wait(1)

        error_t = Text("Error Prone", font=ft, font_size=ft_size).next_to(cons_t, DOWN*2.5)
        mmm_t = Text("Manual Memory Management", font=ft, font_size=ft_size).next_to(error_t, DOWN*1.5)
        exception_t = Text("Lack of Exception Handling", font=ft, font_size=ft_size).next_to(mmm_t, DOWN*1.5)

        self.play(FadeIn(error_t))
        self.wait(1)
        self.play(FadeIn(mmm_t))
        self.wait(1)
        self.play(FadeIn(exception_t))
        self.wait(1)

        self.wait(2)

        # Why should I learn C ?
        self.play(FadeOut(pros_t), FadeOut(cons_t), FadeOut(error_t), FadeOut(mmm_t), FadeOut(exception_t), FadeOut(clear_t), FadeOut(speed_t), FadeOut(abstract_t))

        why_c_big_t = Text(
            "Why should you learn C?",
            font_size=ft_size_large,  # or whatever larger size you want
            font=ft,
            color=G.ORANGE             # already orange
        ).move_to(what_is_c_big_t.get_center())  # position where "Contents" was

        self.play(ReplacementTransform(what_is_c_big_t, why_c_big_t))



        self.wait(2)