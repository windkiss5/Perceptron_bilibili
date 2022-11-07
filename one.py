from manimlib import *
import numpy as np
from numpy import linspace, square


def moon2Data(datanum):
    x1 = linspace(-3, 3, datanum)
    noise = np.random.randn(datanum) * 0.15
    y1 = -square(x1) / 3 + 4.5 + noise
    class_1 = np.array([[_x + 3, _y + 2] for _x, _y in zip(x1, y1)])

    x2 = linspace(0, 6, datanum)
    noise = np.random.randn(datanum) * 0.15
    y2 = square(x2 - 3) / 3 + 0.5 + noise
    class_2 = np.array([[_x + 3, _y] for _x, _y in zip(x2, y2)])

    return class_1, class_2

# 创建二维坐标系，并在(1,1)处创建一个蓝色的点

class demo(Scene):
    CONFIG = {"x_axis_label": "$x$"}
    def construct(self):
        # ---------------------------- #
        # 绘制坐标系
        # ---------------------------- #
        axe1 = Axes((-3, 10), (-3, 8),
                    x_axis_config={
                        "numbers_to_include": np.arange(-1, 10.01, 1),
                        "numbers_with_elongated_ticks": np.arange(-1, 8.01, 1),
                    }
                    )
        # print("!!!!!!!!!!!!!!!!!!!!!!!!111111111")
        # print(axe1.get_axis_labels())
        # axe1.add_c(
        #     font_size=20,
        #     num_decimal_places=1
        # )
        axe1.add(axe1.get_axis_labels())
        axe1.set_color(WHITE)
        # 播放坐标系生成
        self.play(ShowCreation(axe1), run_time=1.5)

        # ---------------------------- #
        # 按高斯分布生成数据
        # ---------------------------- #
        num = 50
        # 类别 1 -> label=-1
        class_1 = np.random.normal(loc=7.3, scale=0.7, size=(num, 2))
        # 类别 2 -> label=1
        class_2 = np.random.normal(loc=1.9, scale=0.9, size=(num, 2))

        # self.add(axe1, dot_cloud_1)
        pointCloud = VGroup()
        for i in range(num):
            dot_1 = Dot(point=axe1.c2p(class_1[i][0], class_1[i][1]), color=BLUE)
            dot_2 = Dot(point=axe1.c2p(class_2[i][0], class_2[i][1]), color=RED_B)
            pointCloud.add(dot_1, dot_2)

        self.play(ShowCreation(pointCloud), run_time=1.5)
        self.wait()

        # ---------------------------- #
        # 绘制多个超平面演示
        # ---------------------------- #
        line = axe1.get_graph(
            lambda x: -x + 7.5,
            color=YELLOW_B,
        )
        self.play(ShowCreation(line), run_time=0.5)
        self.wait()

        self.play(FadeOut(line), run_time = 0.5)

        line = axe1.get_graph(
            lambda x: -3 * x + 16.5,
            color=YELLOW_B,
        )
        self.play(ShowCreation(line), run_time=0.5)
        self.wait()

        self.play(FadeOut(line), run_time = 0.5)

        line = axe1.get_graph(
            lambda x: -0.35 * x + 6.5,
            color=YELLOW_B,
        )
        self.play(ShowCreation(line), run_time=0.5)
        self.wait()

        self.play(FadeOut(line), run_time = 0.5)

        line = axe1.get_graph(
            lambda x: -9 * x + 50.0,
            color=YELLOW_B,
        )
        self.play(ShowCreation(line), run_time=0.5)
        self.wait()

        # ---------------------------- #
        # 重绘(不可使用感知机的情况)
        # ---------------------------- #
        self.play(FadeOut(pointCloud), FadeOut(line), run_time = 0.5)

        # 生成新的样本
        class_1, class_2 = moon2Data(num)
        pointCloud_2 = VGroup()
        pointCloud_2.clear_points()
        pointCloud_2.remove()
        for i in range(num):
            dot_1 = Dot(point=axe1.c2p(class_1[i][0], class_1[i][1]), color=BLUE)
            dot_2 = Dot(point=axe1.c2p(class_2[i][0], class_2[i][1]), color=RED_B)
            pointCloud_2.add(dot_1, dot_2)
        self.play(ShowCreation(pointCloud_2), run_time=1)

        # 贝塞尔曲线
        points = [[-1, 0, 0],
                  [3, 13, 0],
                  [6, -8, 0],
                  [10, 10, 0]
                  ]

        points = np.array([axe1.coords_to_point(*_p) for _p in points])
        arc1 = TipableVMobject()
        arc1.add_cubic_bezier_curve(*points)
        arc1.set_color(YELLOW_B)
        self.play(ShowCreation(arc1))

        # ------------------------------------------------ #
        self.play(FadeOut(arc1), FadeOut(pointCloud_2), FadeOut(axe1))

if __name__ == "__main__":
    from os import system

    system("manimgl {} demo -c black".format(__file__))