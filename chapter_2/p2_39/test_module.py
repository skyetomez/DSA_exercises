import polygons
import unittest


def setUpModule() -> None:
    print("Test module is set up.")
    return None


def tearDownModule():
    print("Test module is torn down.")
    pass


class TestTriangle(unittest.TestCase):
    """Test Module for the Triangle class"""

    def __str__(self) -> str:
        return "TestTriangle"

    def __repr__(self) -> str:
        return "Test Triangle Object"

    @classmethod
    def setUpClass(cls) -> None:
        cls.side_a = 2
        cls.side_b = 3
        cls.side_c = 4
        print(f"The class {cls} is setup")
        return None

    @classmethod
    def tearDownClass(cls) -> None:
        print(f"The class {cls} is torn down")
        return None

    def setUp(self) -> None:
        self.tri = polygons.Triangle(self.side_a, self.side_b, self.side_c)
        self.iso = polygons.IsoscelesTriangle(self.side_a, self.side_b)
        self.equi = polygons.EquilateralTriangle(self.side_a)
        return

    def test_area(self):
        self.assertAlmostEqual(self.tri.area(), 2.9, 2)
        self.assertAlmostEqual(self.iso.area(), 3, 2)
        self.assertAlmostEqual(self.equi.area(), 1.73, 2)
        return print("test complete")

    def test_perimeter(self):
        self.assertAlmostEqual(self.tri.perimeter(), 9, 2)
        self.assertAlmostEqual(self.iso.perimeter(), 8.32, 2)
        self.assertAlmostEqual(self.equi.perimeter(), 6, 2)


class TestQuadrilateral(unittest.TestCase):
    def __str__(self) -> str:
        return "TestQuadrilateral"

    def __repr__(self) -> str:
        return "TestQuadrilateral Object"

    @classmethod
    def setUpClass(cls) -> None:
        cls.length = 2
        cls.width = 3
        print(f"The class {cls} is setup")
        return None

    @classmethod
    def tearDownClass(cls) -> None:
        print(f"The class {cls} is torn down")
        return None

    def setUp(self) -> None:
        self.quad = polygons.Quadrilateral(self.length, self.width)
        self.squ = polygons.Square(self.width)
        return None

    def test_area(self) -> None:
        self.assertAlmostEqual(self.quad.area(), 6, 2)
        self.assertAlmostEqual(self.squ.area(), 9, 2)
        return None

    def test_perimeter(self) -> None:
        self.assertAlmostEqual(self.quad.perimeter(), 10, 2)
        self.assertAlmostEqual(self.squ.perimeter(), 12, 2)
        return None


class TestPolygon(unittest.TestCase):
    def __str__(self) -> str:
        return "Test Polygon"

    def __repr__(self) -> str:
        return "Test Triangle Object"

    @classmethod
    def setUpClass(cls) -> None:
        cls.side_length = 1
        print(f"The class {cls} is setup")
        return None

    @classmethod
    def tearDownClass(cls) -> None:
        print(f"The class {cls} is torn down")
        return None

    def setUp(self) -> None:
        self.pent = polygons.Pentagon(5, self.side_length)
        self.hex = polygons.Hexagon(6, self.side_length)
        self.oct = polygons.Octagon(8, self.side_length)
        return None

    def test_area(self) -> None:
        self.assertAlmostEqual(self.pent.area(), 1.72, 2)
        self.assertAlmostEqual(self.hex.area(), 2.6, 2)
        self.assertAlmostEqual(self.oct.area(), 4.83, 2)
        return None

    def test_perimeter(self) -> None:
        self.assertAlmostEqual(self.pent.perimeter(), 5, 2)
        self.assertAlmostEqual(self.hex.perimeter(), 6, 2)
        self.assertAlmostEqual(self.oct.perimeter(), 8, 2)
        return None
