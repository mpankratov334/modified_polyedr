from pytest import approx
from math import sqrt
from shadow.polyedr import Polyedr, DEFAULT_ANGLE
import os


def length(poly):
    leng = 0
    for e in poly.edges:
        for f in poly.facets:
            e.shadow(f)
        if not e.gaps and not e.is_in_default_square(poly.c):
            angle = e.h_angle()
            if angle <= DEFAULT_ANGLE:
                sqx = (e.fin.x - e.beg.x) ** 2
                sqy = (e.fin.y - e.beg.y) ** 2
                sqz = (e.fin.z - e.beg.z) ** 2
                leng += sqrt(sqx + sqy + sqz)
    return leng/poly.c


class TestModification:

    # Ребро закрыто плоскостью и её центр лежит внутри квадрата
    # угол с горизонтальной плоскостью равен нулю
    def test1(self):
        current_directory = os.getcwd()
        file = os.path.join(os.path.dirname(current_directory), "data", "test1.geom")
        poly = Polyedr(file)
        assert length(poly) == approx(0)

    # Ребро закрыто плоскостью её центр лежит вне квадрата
    # угол с горизонтальной плоскостью равен нулю
    def test2(self):
        current_directory = os.getcwd()
        file = os.path.join(os.path.dirname(current_directory), "data", "test2.geom")
        poly = Polyedr(file)
        assert length(poly) == approx(5)

    # Ребро закрыто плоскостью её центр лежит вне квадрата
    # угол с горизонтальной плоскостью
    # приблизительно равен 45 градусам (больше pi/7)
    def test3(self):
        current_directory = os.getcwd()
        file = os.path.join(os.path.dirname(current_directory), "data", "test3.geom")
        poly = Polyedr(file)
        assert length(poly) == approx(0)

    # Ребро частично закрыто плоскостью
    # её центр лежит вне квадрата
    # угол с горизонтальной плоскостью равен нулю
    def test4(self):
        current_directory = os.getcwd()
        file = os.path.join(os.path.dirname(current_directory), "data", "test4.geom")
        poly = Polyedr(file)
        assert length(poly) == approx(0)

    # Ребро не закрыто плоскостью
    # её центр лежит вне квадрата
    # угол с горизонтальной плоскостью равен нулю
    def test5(self):
        current_directory = os.getcwd()
        file = os.path.join(os.path.dirname(current_directory), "data", "test5.geom")
        poly = Polyedr(file)
        assert length(poly) == approx(0)