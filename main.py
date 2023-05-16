from manim import *

def FadeOutAll(scene : Scene):
    scene.play(*[FadeOut(i) for i in scene.mobjects])

class Title(Scene):
    def construct(self):
        title    = Text ("Work")
        subtitle = Text ("Chapter 6.4", font_size=24).next_to(title, DOWN)
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)
        FadeOutAll(self)

class Force(Scene):
    def construct(self):
        title = Text ("Force")
        self.play(Write(title))
        self.play(title.animate.shift(3 * UP))
        
        definition = Text ("""
An influence that causes the 
motion of an object with mass 
to change its velocity 
(e.g. moving from a state of rest), 
i.e., to accelerate.""", font_size=24, slant="ITALIC")
        self.play(Write(definition))
        self.wait(1)
        definition_up = Text ("""
An influence that causes the motion of an object with mass to change its velocity 
(e.g. moving from a state of rest), i.e., to accelerate.""", font_size=24, slant="ITALIC").next_to(title, DOWN)
        self.play(Transform(definition, definition_up))

        box   = Square (color=GREY).move_to(2 * LEFT)
        arrow = Arrow  (start=0 * LEFT, end=4 * RIGHT, color=GREY).move_to(2 * DOWN)
        self.play(Create(box), runtime=1)
        self.play(box.animate.shift(4 * RIGHT), Create(arrow));
        self.play(Uncreate(arrow), runtime=1)
        arrow = Arrow (start=0 * UP, end=2 * DOWN, color=GREY)
        self.play(box.animate.shift(6 * DOWN), Create(arrow))
        self.play(Uncreate(box), Uncreate(arrow))

        f_ma = MathTex (r"F=ma=m\frac{d^s}{dt^2}", font_size=128).add(Text ("Force = mass x acceleration").move_to(2 * DOWN))
        self.play(Write(f_ma))
        self.wait(1)

        self.play(f_ma.animate.scale(0.5).shift(UP))
        note = Text ("Note: Weight is mass already considering acceleration due to gravity, \nso it can be used in place of force.", font_size=24).move_to(2 * DOWN)
        self.play(Write(note))
        self.wait(1)
        FadeOutAll(self)
