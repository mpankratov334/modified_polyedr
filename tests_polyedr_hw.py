from pytest import approx
from common.r3 import R3
from polyedr_hw import Polyedr
from common.tk_drawer import TkDrawer as tk


class TestPolyedr_hw:

    def test_1(self):
        tk1 = tk()
        ccc = Polyedr("data/ccc.geom")
        ccc.draw(tk1)
        tk1.close()
        assert  ccc.sum / ccc.c == 30

    def test_2(self):
        tk3 = tk()
        polyedr = Polyedr("data/cube.geom")
        polyedr.draw(tk3)
        tk3.close()
        assert polyedr.sum / polyedr.c == 0

    def test_3(self):
        tk5 = tk()
        polyedr = Polyedr("data/box.geom")
        polyedr.draw(tk5)
        tk5.close()
        assert polyedr.sum / polyedr.c == 0

    def test_4(self):
        tk7 = tk()
        polyedr = Polyedr("data/pyramid_top.geom")
        polyedr.draw(tk7)
        tk7.close()
        assert 29.0175 < polyedr.sum / polyedr.c < 29.018


    def test_5(self):
        tk10 = tk()
        polyedr = Polyedr("data/small_pyramid.geom")
        polyedr.draw(tk10)
        tk10.close()
        assert polyedr.sum / polyedr.c == 0
