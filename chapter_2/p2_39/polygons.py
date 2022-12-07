"""
Develop an inheritance hierarchy based upon a Polygon class that has
abstract methods area( ) and perimeter( ). Implement classes Triangle,
Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
class, with the obvious meanings for the area( ) and perimeter( ) methods.
Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectan-
gle, and Square, that have the appropriate inheritance relationships. Fi-
nally, write a simple program that allows users to create polygons of the
various types and input their geometric dimensions, and the program then
outputs their area and perimeter. For extra effort, allow users to input
polygons by specifying their vertex coordinates and be able to test if two
such polygons are similar.
"""

from abc import abstractmethod, ABCMeta
from math import sqrt, pow


class Polygon(metaclass=ABCMeta):
    """Abstract base class for polygons"""

    @abstractmethod
    def __init__(self, nsides: int, a: float) -> None:
        self.nside = nsides
        self.side_length = a
        return None

    def __repr__(self) -> str:
        """returns a string representation for Polygon class"""
        return "Polygon Object"

    def __str__(self) -> str:
        """returns a string representation as a string"""
        return "Polygon"

    @abstractmethod
    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        ans = self.nside * self.side_length
        print(f"The perimeter of {self} is {ans:.2f}")
        return ans


class Triangle(Polygon):
    """General triangle object can be used to determine the area and perimeter of a triangle if all sides are known."""

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def __repr__(self) -> str:
        return "Triangle Object"

    def __str__(self) -> str:
        return "Triangle"

    def area(self) -> float:
        s = (1 / 2) * (self.side_a + self.side_b + self.side_c)
        ans = sqrt(s * ((s - self.side_a) * (s - self.side_b) * (s - self.side_c)))
        print(f"The area of {self} is {ans:.2f}")
        return ans

    def perimeter(self) -> float:
        ans = self.side_a + self.side_b + self.side_c
        print(f"The perimeter of {self} is {ans:.2f}")
        return ans


class Quadrilateral(Polygon):
    """Equations for general quadrilateral"""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width
        return None

    def __repr__(self) -> str:
        return "Quadrilateral Object"

    def __str__(self) -> str:
        return "Quadrilateral"

    def area(self) -> float:
        ans = self.length * self.width
        print(f"The area of {self} is {ans:.2f}", sep=" ")
        return ans

    def perimeter(self) -> float:
        ans = (self.length * 2) + (self.width * 2)
        print(f"The perimeter of {self} is {ans:.2f}")
        return ans


class Pentagon(Polygon):
    """Equations for general pentagon"""

    def __init__(self, nsides: int, a: float) -> None:
        super().__init__(nsides, a)

    def __repr__(self) -> str:
        return "Pentagon Object"

    def __str__(self) -> str:
        return "Pentagon"

    def area(self) -> float:
        return (1 / 4) * sqrt(5 * (5 + (2 * sqrt(5)))) * pow(self.side_length, 2)

    def perimeter(self) -> float:
        return super().perimeter()


class Hexagon(Polygon):
    """Equations for general hexagon"""

    def __init__(self, nsides: int, a: float) -> None:
        super().__init__(nsides, a)
        return None

    def __repr__(self) -> str:
        return "Hexagon Object"

    def __str__(self) -> str:
        return "Hexagon"

    def area(self) -> float:
        return ((3 * sqrt(3)) / 2) * pow(self.side_length, 2)


class Octagon(Polygon):
    """Equations for general octagon"""

    def __init__(self, nsides: int, a: float) -> None:
        super().__init__(nsides, a)
        return None

    def __repr__(self) -> str:
        return "Octagon Object"

    def __str__(self) -> str:
        return "Octagon"

    def area(self) -> float:
        return 2 * (1 + sqrt(2)) * pow(self.side_length, 2)


class Square(Quadrilateral):
    """Equations for a square"""

    def __init__(self, *arg) -> None:
        if len(arg) == 2:
            width, length = arg
            super().__init__(length, width)
        elif len(arg) == 1:
            width = arg[-1]
            length = width
            super().__init__(length, width)

    def __repr__(self) -> str:
        return "Square Object"

    def __str__(self) -> str:
        return "Square"

    def area(self) -> float:
        return super().area()

    def perimeter(self) -> float:
        return super().perimeter()


class IsoscelesTriangle(Triangle):
    """
    Equations for an Isocelees Triangle
    The triangle is coerced into a form so that
    Heron's area formula can be used
    """

    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height
        self.a = sqrt(pow(base / 2, 2) + pow(height, 2))
        super().__init__(self.base, self.a, self.a)
        return None

    def __repr__(self) -> str:
        return "IsoscelesTriangle Object"

    def __str__(self) -> str:
        return "IsoscelesTriangle"

    def area(self) -> float:
        return super().area()

    def perimeter(self) -> float:
        return super().perimeter()


class EquilateralTriangle(Triangle):
    """
    Equations for an Equilateral Triangle
    The triangle is coerced into a form so that
    Heron's area formula can be used
    """

    def __init__(self, length: float) -> None:
        super().__init__(length, length, length)
        return None

    def __repr__(self) -> str:
        return "EquilateralTriangle Object"

    def __str__(self) -> str:
        return "EquilateralTriangle"

    def area(self) -> float:
        return super().area()

    def perimeter(self) -> float:
        return super().perimeter()


if __name__ == "__main__":
    square = Square(3)
    square.area()
    square.perimeter()
