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
i.e., to accelerate.""", font_size=24, slant=ITALIC)
        self.play(Write(definition))
        self.wait(1)
        definition_up = Text ("""
An influence that causes the motion of an object with mass to change its velocity 
(e.g. moving from a state of rest), i.e., to accelerate.""", font_size=24, slant=ITALIC).next_to(title, DOWN)
        self.play(Transform(definition, definition_up))

        box   = Square (color=GREY).move_to(2 * LEFT)
        arrow = Arrow  (start=0 * LEFT, end=4 * RIGHT, color=GREY).move_to(2 * DOWN)
        self.play(Create(box), runtime=1)
        self.play(box.animate.shift(4 * RIGHT), Create(arrow));
        self.play(Uncreate(arrow), runtime=1)
        arrow = Arrow (start=0 * UP, end=2 * DOWN, color=GREY)
        self.play(box.animate.shift(6 * DOWN), Create(arrow))
        self.play(Uncreate(box), Uncreate(arrow))

        f_ma = MathTex (r"F=ma=m\frac{d^s}{dt^2}", font_size=128).add(Text ("Force = mass × acceleration").move_to(2 * DOWN))
        self.play(Write(f_ma))
        self.wait(1)

        self.play(f_ma.animate.scale(0.5).shift(UP))
        note = Text ("Note: Weight is mass already considering acceleration due to gravity, \nso it can be used in place of force.", font_size=24).move_to(2 * DOWN)
        self.play(Write(note))
        self.wait(1)
        FadeOutAll(self)

class Work(Scene):
    def construct(self):
        title = Text ("Work")
        self.play(Write(title))
        self.play(title.animate.shift(3 * UP))

        definition = Text ("""
The energy transferred to or from an object 
via the application of force along a displacement.""", font_size=24, slant=ITALIC).add(Text ("""
It can be thought of as the total 
effort required to perform a task - 
the total force required to push and pull an object.
""", font_size=24).move_to(DOWN))
        self.play(Write(definition))
        self.wait(1)
        definition_up = Text ("""
The energy transferred to or from an object 
via the application of force along a displacement.""", font_size=24, slant=ITALIC).add(Text ("""
It can be thought of as the total effort required to perform a task - 
the total force required to push and pull an object.""", font_size=24).move_to(DOWN)).next_to(title, DOWN)
        self.play(Transform(definition, definition_up))

        w_fd = MathTex ("W=Fd", font_size=128).add(Text ("When force is constant.").move_to(2 * DOWN))
        self.play(Write(w_fd))
        self.wait(1)

        self.play(w_fd.animate.scale(0.5).shift(0.5 * UP))
        w_int_fdx = MathTex (r"W=\int_a^b f(x) dx", font_size=128)
        w_int_fdx.add(Text ("""
When force varies as a continuous 
function with respect to position.""").move_to(2.5 * DOWN))
        w_int_fdx.move_to(DOWN)
        self.play(FadeOut(w_fd), Write(w_int_fdx))
        self.wait(1)

        self.play(FadeIn(w_fd), w_int_fdx.animate.scale(0.5).move_to(2.5 * DOWN))
        self.wait(1)

        FadeOutAll(self)

class Hookes_Law(Scene):
    def construct(self):
        title = Text ("Hooke's Law")
        self.play(Write(title))
        self.play(title.animate.shift(3 * UP))
        definition = Text ("""
The force needed to extend or compress 
a spring by some distance scales linearly 
with respect to that distance.""", font_size=24, slant=ITALIC)
        self.play(Write(definition))
        self.wait(1)
        definition_up = Text ("""
The force needed to extend or compress a spring by some distance 
scales linearly with respect to that distance.""", font_size=24, slant=ITALIC).next_to(title, DOWN)
        self.play(Transform(definition, definition_up))

        f_kx = MathTex ("f(x)=kx", font_size=128).add(Text ("""
The force required to maintain 
a spring stretched x units 
beyond its natural length""", t2s={'x':ITALIC}).move_to(2 * DOWN))
        self.play(Write(f_kx))
        self.wait(1)

        self.play(f_kx.animate.scale(0.5).shift(UP))
        note = Text ("Note: k is the spring constant, which varies depending on the spring.", font_size=24, t2s={'k':ITALIC}).move_to(2 * DOWN)
        self.play(Write(note))
        self.wait(1)

        FadeOutAll(self)
