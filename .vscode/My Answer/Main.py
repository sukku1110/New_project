#File - main.py

from Question1 import Class1
from Question2 import Class2
from inputs.variables import line,input

def main():

    'Object creation and function call of Class1'
    object1=Class1()
    object1.function1(line)

    'Object creation and function call of Class2'
    object2=Class2()
    object2.password_compliance(input)

if __name__ == "__main__":
    main()