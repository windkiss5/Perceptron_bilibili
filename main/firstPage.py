import numpy as np
from manimlib import *
from numpy import linspace, square
from sklearn import datasets

def moon2Data(num):
    data, _ = datasets.make_moons(n_samples=num * 2,noise=0.1,random_state=8, shuffle=False)

    data_1 = data[0: num] * 4.5
    data_1[:, 0] -= 1
    data_1[:, 1] += 0.8

    data_2 = data[num: num * 2] * 4.5
    data_2[:, 1] -= 0.6

    return data_1, data_2

class demo(ThreeDScene):
    def construct(self):
        # ------------------------- 画坐标轴 ------------------------------ #
        frame: CameraFrame = self.camera.frame
        frame.set_euler_angles(
            theta=-90 * DEGREES,
            phi=0 * DEGREES,
            gamma=90 * DEGREES
        )
        axes = ThreeDAxes((-10, 10), (-8, 8), (-6, 6),
                          height = 6,
                          width = 10,
                          depth = 6,
                          include_tip=True,
                          axis_config={
                              "include_tip": True,
                          },
                          # x_axis_config={"include_number":True, "x": np.arange(-3.01, 10.01, 1)},
                          # y_axis_config={"include_number":True, "y": np.arange(-3.01, 8.01, 1)},
                          # z_axis_config={"include_number":True, "z": np.arange(-3.01, 6.01, 1)}
                          )
        axes.add(axes.get_axis_label(label_tex="x", axis=axes.get_x_axis(), edge=RIGHT, direction=DL))
        axes.add(axes.get_axis_label(label_tex="y", axis=axes.get_y_axis(), edge=UP, direction=DR))
        # axes.add(axes.get_axis_label(label_tex="z", axis=axes.get_z_axis(), edge=OUT, direction=OUT))
        # self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("This is a 3D text")
        # self.add_fixed_in_frame_mobjects(text3d)
        # text3d.to_corner(UL)
        self.add(axes)
        self.play(ShowCreation(axes), run_time=3)
        self.wait()

        # --------------------------- 散点图 ---------------------------- #
        # ---------------------------- #
        # 按高斯分布生成数据
        # ---------------------------- #
        num = 50
        # 类别 1 -> label=-1
        class_1 = np.random.normal(loc=4.3, scale=1.5, size=(num, 3))
        print(class_1.shape)
        # 类别 2 -> label=1
        class_2 = np.random.normal(loc=-3.9, scale=1.5, size=(num, 3))

        pointCloud = VGroup()

        dot_1 = []
        dot_2 = []
        for i in range(num):
            dot_1.append(axes.c2p(class_1[i][0], class_1[i][1], class_1[i][2]))
            dot_2.append(axes.c2p(class_2[i][0], class_2[i][1], class_2[i][2]))

        dot_cloud_1 = DotCloud(
            points=dot_1,
            color=BLUE,
            opacity=0.8,
            radius=0.1
        )

        dot_cloud_2 = DotCloud(
            points=dot_2,
            color=RED,
            opacity=0.8,
            radius=0.13
        )
        # print("----------------")
        # print(class_1[0][0], class_1[0][1], class_1[0][2])
        # print(type(axes.c2p(class_1[0][0], class_1[0][1], class_1[0][2])))
        # for i in range(num):
        #     dot_1 = DotCloud(point=axes.c2p(class_1[i][0], class_1[i][1], class_1[i][2]), color=BLUE)
        #     dot_2 = DotCloud(point=axes.c2p(class_2[i][0], class_2[i][1], class_2[i][2]), color=RED_B)
        #     pointCloud.add(dot_1, dot_2)

        self.play(ShowCreation(dot_cloud_1), ShowCreation(dot_cloud_2), run_time=1.5)
        self.wait()

        # ------------------------------------------ #
        # 超平面
        # ------------------------------------------ #
        # S1 = ParametricSurface(
        #     uv_func=lambda x, y: [x, -x, y],
        #     u_range=(-6, 6),
        #     v_range=(-3, 3),
        #     color=YELLOW_B
        # )
        # self.add(S1)

        # ---------------------------------------- #
        # line 1
        _start = axes.c2p(-2, 7, 4)
        _end = axes.c2p(3, -5, -2)
        line_1 = Line3D(
            start=_start,
            end=_end
        )
        self.add(line_1)
        self.play(ShowCreation(line_1))
        self.wait()

        # ---------------------------------------- #
        # line 2
        _start = axes.c2p(-7, 1.5, 4)
        _end = axes.c2p(9, 1.5, -2)
        line_2 = Line3D(
            start=_start,
            end=_end
        )
        self.add(line_2)
        self.play(FadeOut(line_1), ShowCreation(line_2))
        self.wait()

        # ---------------------------------------- #
        # line 3
        _start = axes.c2p(-5, 5, 4)
        _end = axes.c2p(9, -2, -2)
        line_3 = Line3D(
            start=_start,
            end=_end
        )
        self.add(line_3)
        self.play(FadeOut(line_2), ShowCreation(line_3))
        self.wait()
        self.play(FadeOut(line_3))
        # -------------------------------------------- #
        # 月牙数据
        # -------------------------------------------- #
        self.play(FadeOut(dot_cloud_1), FadeOut(dot_cloud_2))
        # 生成月牙数据
        moon_1, moon_2 = moon2Data(num)
        print(moon_1.shape)
        moon_dot_1 = []
        moon_dot_2 = []
        for i in range(num):
            moon_dot_1.append(axes.c2p(moon_1[i][0], moon_1[i][1], class_1[i][0]))
            moon_dot_2.append(axes.c2p(moon_2[i][0], moon_2[i][1], class_2[i][0]))
        moon_dot_cloud_1 = DotCloud(
            points=moon_dot_1,
            color=BLUE,
            opacity=0.8,
            radius=0.1
        )

        moon_dot_cloud_2 = DotCloud(
            points=moon_dot_2,
            color=RED,
            opacity=0.8,
            radius=0.13
        )

        self.play(ShowCreation(moon_dot_cloud_1), ShowCreation(moon_dot_cloud_2), run_time=1.5)
        self.wait()

        _key_point = np.array([[-6, -4, 1.5],
                                [0, 20, 1],
                                [3.5, -17.5, 1],
                                [8, 6, 0]])
        key_point = []
        for i in range(4):
            key_point.append(axes.c2p(_key_point[i][0], _key_point[i][1], _key_point[i][2]))
        moon_line = CubicBezier(key_point[0], key_point[1], key_point[2], key_point[3])

        self.play(ShowCreation(moon_line))
        self.wait()

        # -----------------------------------------------------------------
        #  旋转相机
        # 获取相机帧的引用
        camera = self.camera.frame
        self.wait()
        # 使用四元数旋转（欧拉旋转经常会检测到万向节锁死）
        self.play(camera.animate.set_orientation(Rotation([0.8, 0.2, 0.3, 1])))
        self.wait()

        # 隐藏曲线
        self.play(FadeOut(moon_line))
        # ------------------------------------------ #
        # 超平面
        # ------------------------------------------ #
        S1 = ParametricSurface(
            uv_func=lambda x, y: [x, y, -0.05*x+0.5-0.15*y],
            u_range=(-5, 5),
            v_range=(-5, 3),
            color=WHITE,
            opacity=0.6

        )
        self.play(ShowCreation(S1))
        self.wait()

        # 隐去
        self.play(FadeOut(S1), FadeOut(moon_dot_cloud_1), FadeOut(moon_dot_cloud_2), FadeOut(axes))


if __name__ == "__main__":
    from os import system

    system("manimgl {} FixedInFrameMObjectTest -c black".format(__file__))