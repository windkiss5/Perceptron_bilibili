from manimlib import *

class demo(Scene):
    def setup(self):
        # 初始化场景
        axes = ThreeDAxes()
        self.add(axes)
        sphere = Sphere().move_to(axes.coords_to_point(3, 2, 2))
        self.add(sphere)

    def construct(self) -> None:
        # 获取相机帧的引用
        camera = self.camera.frame
        self.wait()
        # 使用四元数旋转（欧拉旋转经常会检测到万向节锁死）
        self.play(camera.animate.set_orientation(Rotation([0.8, 0.2, 0.1, 0.9])))
        self.wait()