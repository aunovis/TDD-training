import sys

from stringcalculator import StringCalculator


if __name__ == "__main__":
    if len(sys.argv) > 1:
        calc = StringCalculator()
        sum = calc.add(sys.argv[1])
        print(sum)
