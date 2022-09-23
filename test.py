from manimlib import *

class PointWithTrace(Scene):
    def construct(self):
        # 创建一个空物体
        path = VMobject()
        # 创建一个点
        dot = Dot()
        # 定义路径关键点
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        # 定义路径更新函数
        def update_path(path):
            # copy原路径
            previous_path = path.copy()
            # 增加新的点
            previous_path.add_points_as_corners([dot.get_center()])
            # 更新当前巨鲸
            path.become(previous_path)
        #将更新函数加入到路径中
        path.add_updater(update_path)
        #将路径与点加入到场景中
        self.add(path, dot)
        # 让dot做圆周运动
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()
        # 让dot 做线性运动
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()


if __name__ == "__main__":
    from os import system

    system("manimgl {} PointWithTrace -c black".format(__file__))