from manimlib import *

class text(Scene):
    def construct(self):
        text = Tex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        self.wait()

if __name__ == "__main__":
    from os import system

    system("manimgl {} text -c black".format(__file__))