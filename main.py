# main.py

from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide
from power import power
from sqrt import sqrt
from logarithm import logarithm
from trigonometry import sine, cosine, tangent

def main():
    a = 10
    b = 5

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
    print(f"{a} ^ {b} = {power(a, b)}")
    print(f"sqrt({a}) = {sqrt(a)}")
    print(f"log({a}) = {logarithm(a)}")
    print(f"log({a}, 10) = {logarithm(a, 10)}")
    print(f"sin(30) = {sine(30)}")
    print(f"cos(60) = {cosine(60)}")
    print(f"tan(45) = {tangent(45)}")

if __name__ == "__main__":
    main()
