from manimlib import *

class demo(Scene):
    def setup(self):
        # ��ʼ������
        axes = ThreeDAxes()
        self.add(axes)
        sphere = Sphere().move_to(axes.coords_to_point(3, 2, 2))
        self.add(sphere)

    def construct(self) -> None:
        # ��ȡ���֡������
        camera = self.camera.frame
        self.wait()
        # ʹ����Ԫ����ת��ŷ����ת�������⵽�����������
        self.play(camera.animate.set_orientation(Rotation([0.8, 0.2, 0.1, 0.9])))
        self.wait()