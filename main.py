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

        f_ma    = MathTex (r"F=ma=m\frac{d^2s}{dt^2}", font_size=128).next_to(definition_up, DOWN)
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

example_data = {
    "gravity":{
        "title":Text ("Work from Gravity"), 
        "notes":[
            MathTex (r"F=ma=m\frac{d^2s}{dt^2}"), 
            MathTex ("W=Fd")
        ], 
        "content":[
            Text ("""
How much work is done in lifting a 1.2 kg book off the floor to put it on a desk 
that is 0.7 m high? The acceleration due to gravity is g = 9.8 (m/s2).""", 
                t2s={'[138:139]':ITALIC}), 
            MathTex (r"F=mg=(1.2)(9.8)=11.76 \textrm{N}"), 
            MathTex (r"W=Fd=(11.76)(0.7)\approx8.2 \textrm{J}"), 
            Text ("How much work is done in lifting a 20 lb weight 6 ft off the ground?"), 
            MathTex (r"F=20 \textrm{lb}"), 
            MathTex (r"W=(20)(6)=120 \textrm{lb-ft}\approx163.2 \textrm{J}")
        ]
    }, 
    "variable":{
        "title":Text ("""
Work from a 
Variable Force"""), 
        "notes":[
            MathTex (r"W=\int_a^b f(x) dx")
        ], 
        "content":[
            Text ("""
When a particle is located a distance 
x feet from the origin, a force of x2+2x pounds acts on it. 
How much work is done in moving it from x=1 to x=3?""", t2s={'x':ITALIC}), 
            MathTex (r"W=\int_1^3 (x^2+2x) dx=\left.(\frac{1}{3}x^3+x^2)\right|_1^3=\frac{50}{3} \textrm{lb-ft}")
        ]
    }, 
    "spring":{
        "title":Text ("Work from a Spring"), 
        "notes":[
            MathTex ("f(x)=kx")
        ], 
        "content":[
            Text ("""
A force of 40 N is required to hold a spring 
that has been stretched from its natural length 
of 10 cm to a length of 15 cm. 
How much work is done in stretching the spring 
from 15 cm to 18 cm?"""), 
            MathTex (r"10 \textrm{cm}=0.1 \textrm{m}, 15 \textrm{cm}=0.15 \textrm{m}, x=0.05 \textrm{m}"), 
            MathTex (r"f(0.05)=40, 0.05k=40, k=800"), 
            MathTex (r"f(x)=800x"), 
            MathTex (r"W=\int_{0.05}^{0.08} (800x) dx=\left.400x^2\right|_{0.05}^{0.08}=1.56 \textrm{J}") # > 100 cols
        ]
    }, 
    "extra":{
        "title":Text ("Extra Example"), 
        "notes":[], 
        "content":[
            Text ("""
A 200 lb cable is 100 ft long and hangs vertically 
from the top of a tall building. 
How much work is required to lift the cable to the top of the building?"""), 
            Text ("""
- Each ft. of cable weighs 2 lb.
- The weight of a specific point on the cable can be expressed as 2dx.
- The distance each point travels increases with x.""", t2s={'[100:102]':ITALIC, 'x':ITALIC}), 
            MathTex (r"W=\int_{0}^{100} (2x) dx=\left.x^2\right|_{0}^{100}=10,000 \textrm{lb-ft}")
        ]
    }
}

def render_example(scene : Scene, id : str):
    data = example_data[id]
    title = data["title"]
    start = [Write (title.to_edge(UP))]
    notes = data["notes"]
    notes_len = len(data["notes"])
    for i in range(notes_len):
        note = notes[i]
        if i == 0:
            note.set(font_size=48).to_edge(UP).to_edge(RIGHT)
        else:
            note.set(font_size=48).next_to(notes[i - 1], DOWN)
        start.append(Write (note))
    scene.play(*start)
    bottom = title
    isTitle = True
    content = data["content"]
    for thing in content:
        if type(thing) == Text:
            thing.set(font_size=24)
        elif type(thing) == MathTex:
            thing.set(font_size=48)
        if isTitle:
            thing.next_to(bottom, 5 * DOWN)
            isTitle = False
        else:
            thing.next_to(bottom, DOWN)
        scene.play(Write (thing))
        scene.wait(1)
        bottom = thing
    FadeOutAll(scene)

class Example_Work_Gravity(Scene):
    def construct(self):
        render_example(self, "gravity")

class Example_Variable_Force(Scene):
    def construct(self):
        render_example(self, "variable")

class Example_Spring(Scene):
    def construct(self):
        render_example(self, "spring")

class Example_Extra(Scene):
    def construct(self):
        render_example(self, "extra")

class Homefun(Scene):
    def construct(self):
        title = Text ("Homefuns")
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        fun       = Text ("""
Page 458: #1, 2,  3,  7,  9, 12
Extras: #4, 8, 11, 13, 16, 20
    (Take a look at example 5 in the textbook for hints for #20.)""", font_size=24)
        self.play(Write(fun))
