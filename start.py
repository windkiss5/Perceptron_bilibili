import numpy as np
from manimlib import *


# 创建二维坐标系，并在(1,1)处创建一个蓝色的点

class demo(Scene):
    def construct(self):
        # ---------------------------- #
        # 绘制坐标系
        # ---------------------------- #
        axe1 = Axes((-1, 10), (-1, 8))
        axe1.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1
        )
        axe1.set_color(WHITE)
        # 播放坐标系生成
        self.play(ShowCreation(axe1), run_time=1.0)

        # ---------------------------- #
        # 按高斯分布生成数据
        # ---------------------------- #
        num = 50
        # 类别 1 -> label=-1
        class_1 = np.random.normal(loc=7.3, scale=0.7, size=(num, 2))
        label_1 = -1 * np.ones((num, 1))
        class_Label_1 = np.concatenate((class_1, label_1), axis=1)
        # 类别 2 -> label=1
        class_2 = np.random.normal(loc=1.9, scale=0.9, size=(num, 2))
        label_2 = np.ones((num, 1))
        class_Label_2 = np.concatenate((class_2, label_2), axis=1)

        # self.add(axe1, dot_cloud_1)
        pointCloud = VGroup()
        for i in range(num):
            dot_1 = Dot(point=axe1.c2p(class_1[i][0], class_1[i][1]), color=BLUE)
            dot_2 = Dot(point=axe1.c2p(class_2[i][0], class_2[i][1]), color=RED_B)
            pointCloud.add(dot_1, dot_2)
            self.add(axe1, dot_1)
            self.add(axe1, dot_2)

        self.play(ShowCreation(pointCloud), run_time=1)
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

        self.remove(line)

        line = axe1.get_graph(
            lambda x: -3 * x + 16.5,
            color=YELLOW_B,
        )
        self.play(ShowCreation(line), run_time=0.5)
        self.wait()

        self.remove(line)

        line = axe1.get_graph(
            lambda x: -0.35 * x + 6.5,
            color=YELLOW_B,
        )
        self.play(ShowCreation(line), run_time=0.5)
        self.wait()


        self.remove(line)

        line = axe1.get_graph(
            lambda x: -9 * x + 50.0,
            color=YELLOW_B,
        )
        self.play(ShowCreation(line), run_time=0.5)
        self.wait()


if __name__ == "__main__":
    from os import system

    system("manimgl {} demo -c black".format(__file__))