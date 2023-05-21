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
        self.play(title.animate.to_edge(UP))
        
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
(e.g. moving from a state of rest), i.e., to accelerate.""", 
            font_size=24, slant=ITALIC).next_to(title, DOWN)
        self.play(Transform(definition, definition_up))

        box_left  = Square (color=GREY).move_to(2 * LEFT)
        box_right = box_left.copy().move_to(2 * RIGHT)
        box_down  = box_right.copy().move_to(5.5 * DOWN + 2 * RIGHT)
        arrow     = Arrow  (start=0 * LEFT, end=4 * RIGHT, color=GREY).move_to(2 * DOWN)
        arrow_hide = arrow.copy().set(z_index=100)
        self.play(Create(box_left))
        self.play(
            Transform(box_left, box_right, run_time=2), 
            AnimationGroup(
                AnimationGroup(Create(arrow), 
                Create(arrow_hide)), 
                arrow_hide.animate.set(color=BLACK), 
                lag_ratio=1, 
                run_time=2
            )
        );
        self.remove(arrow, arrow_hide)
        arrow = Arrow (start=0 * UP, end=2 * DOWN, color=GREY)
        arrow_hide = arrow.copy().set(z_index=100)
        self.play(
            Transform(box_left, box_down, run_time=2), 
            AnimationGroup(
                AnimationGroup(Create(arrow), 
                Create(arrow_hide)), 
                arrow_hide.animate.set(color=BLACK), 
                lag_ratio=1, 
                run_time=2
            )
        );
        self.remove(arrow, arrow_hide)

        f_ma    = MathTex (r"F=ma=m\frac{d^s}{dt^2}", font_size=128).next_to(definition_up, DOWN)
        caption = Text ("Force = mass × acceleration").next_to(f_ma, DOWN)
        f_ma.add(caption)
        self.play(Uncreate(box_left, arrow, arrow_hide), Write(f_ma))
        self.wait(1)

        self.play(f_ma.animate.scale(0.5))
        note = Text ("""
Note: Weight is mass already considering acceleration due to gravity, 
so it can be used in place of force.""", 
            font_size=24).next_to(f_ma, 4 * DOWN)
        self.play(Write(note))
        self.wait(1)
        FadeOutAll(self)

class Work(Scene):
    def construct(self):
        title = Text ("Work")
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = Text ("""
The energy transferred to or from an object 
via the application of force along a displacement.""", 
            font_size=24, slant=ITALIC).add(Text ("""
It can be thought of as the total 
effort required to perform a task - 
the total force required to push and pull an object.
""", font_size=24).move_to(DOWN))
        self.play(Write(definition))
        self.wait(1)
        definition_up = Text ("""
The energy transferred to or from an object 
via the application of force along a displacement.""", 
            font_size=24, slant=ITALIC).add(Text ("""
It can be thought of as the total effort required to perform a task - 
the total force required to push and pull an object.""", 
            font_size=24).move_to(DOWN)).next_to(title, DOWN)
        self.play(Transform(definition, definition_up))

        w_fd    = MathTex ("W=Fd", font_size=128)
        caption = Text ("When force is constant.").next_to(w_fd, DOWN)
        w_fd.add(caption)
        self.play(Write(w_fd))
        self.wait(1)

        self.play(w_fd.animate.scale(0.5).next_to(definition_up, DOWN))
        w_int_fdx  = MathTex (r"W=\int_a^b f(x) dx", font_size=128)
        caption_dx = Text ("""
When force varies as a continuous 
function with respect to position.""").next_to(w_int_fdx, DOWN)
        w_int_fdx.add(caption_dx)
        self.play(FadeOut(definition, w_fd), Write(w_int_fdx))
        self.wait(1)

        self.play(FadeIn(definition_up, w_fd), w_int_fdx.animate.scale(0.5).next_to(w_fd, DOWN))
        self.wait(1)

        FadeOutAll(self)

class Hookes_Law(Scene):
    def construct(self):
        title = Text ("Hooke's Law")
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
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

        f_kx    = MathTex ("f(x)=kx", font_size=128)
        caption = Text ("""
The force required to maintain 
a spring stretched x units 
beyond its natural length.""", t2s={'x':ITALIC}).next_to(f_kx, DOWN)
        self.play(Write(f_kx))
        self.wait(1)

        self.play(FadeOut(f_kx))
        eqs = [
            MathTex ("f(", "0",   ")", "=", "8",  "*",   "0", "=", "0"), 
            MathTex ("f(", "10",  ")", "=", "16", "*",  "10", "=", "160"), 
            MathTex ("f(", "-10", ")", "=", "32", "*", "-10", "=", "-320")
        ]
        springs = [
            ImageMobject ("springs/Spring.png", z_index=-100), 
            ImageMobject ("springs/SpringEx.png", z_index=-100), 
            ImageMobject ("springs/SpringCmp.png", z_index=-100)
        ]
        for i in springs: i.move_to(1.5 * DOWN)
        self.play(Write(eqs[0]), SpiralIn(springs[0]))
        self.wait(0.5)
        self.play(TransformMatchingTex(eqs[0], eqs[1]), Transform(springs[0], springs[1]))
        self.wait(0.5)
        self.play(TransformMatchingTex(eqs[1], eqs[2]), Transform(springs[0], springs[2]))
        self.wait(1)
        self.play(FadeOut(eqs[2]), springs[0].animate.shift(10 * LEFT), FadeIn(f_kx))

        self.play(f_kx.animate.scale(0.5).next_to(definition_up, DOWN))
        note = Text ("""
Note: k is the spring constant, which varies depending on the spring, 
and is always positive.""", 
            font_size=24, 
            t2s={'k':ITALIC}
        )
        self.play(Write(note))
        self.wait(1)

        FadeOutAll(self)

class Example_Work_Gravity(Scene):
    def construct(self):
        title     = Text ("Example - Work from Gravity").move_to(3 * UP)
        self.play(Write(title), runtime=1)

        problem_1 = Text ("""
How much work is done in lifting a 1.2 kg book off the floor 
to put it on a desk that is 0.7 m high? 
The acceleration due to gravity is g = 9.8 (m/s²).""", font_size=24, t2s={'[138:139]':ITALIC})
        problem_1.next_to(title, 1.5 * DOWN)
        self.play(Write(problem_1))
        self.wait(1)
        eq_1 = r"F=mg=(1.2)(9.8)=11.76 \textrm{N}"
        eq_2 = r"W=Fd=(11.76)(0.7)\approx8.2 \textrm{J}"
        solution_1 = MathTex (eq_1).add(MathTex (eq_2).move_to(DOWN))
        solution_1.next_to(problem_1, DOWN)
        self.play(Write(solution_1))
        self.wait(1)
        sol_1 = MathTex (eq_1 + ", " + eq_2).next_to(problem_1, DOWN)
        self.play(TransformMatchingTex(solution_1, sol_1))

        problem_2 = Text ("How much work is done in lifting a 20 lb weight 6 ft off the ground?", font_size=24).next_to(sol_1, 2 * DOWN)
        self.play(Write(problem_2))
        self.wait(1)
        eq_1 = r"F=20 \textrm{lb}"
        eq_2 = r"W=(20)(6)=120 \textrm{lb-ft}\approx163.2 \textrm{J}"
        solution_2 = MathTex (eq_1).add(MathTex (eq_2).move_to(DOWN))
        solution_2.next_to(problem_2, DOWN)
        self.play(Write(solution_2))
        self.wait(1)
        sol_2 = MathTex (eq_1 + ", " + eq_2).next_to(problem_2, DOWN)
        self.play(TransformMatchingTex(solution_2, sol_2))
        self.wait(1)

        FadeOutAll(self)
