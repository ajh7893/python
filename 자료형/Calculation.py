class Calculation:
    name = "calculation class"

    def __init__(self):
        print("연산 클래스 생성자 호출")

    def execPlus(self,num1,num2):
        return num1 + num2
    
    def execMinus(self,num1,num2):
        return num1 - num2
    
    def execMultiply(self,num1,num2):
        return num1 * num2
    
    def execDivide(self,num1,num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("can not divide by 0")
            return 0
        
    def executeCalculation(self):
        print("input num1")
        num1 = float(input())
        print("operator")
        operator =input()
        print("input num2")
        num2 = float(input())

        if operator == "+":
            result = self.execPlus(num1,num2)
        elif operator == "-":
            result = self.execMinus(num1,num2)
        elif operator == "*":
            result = self.execMultiply(num1,num2)
        elif operator == "/":
            result = self.execDivide(num1,num2)
        else:
            print("Error")

        print(result)
        return num1, operator, num2    
    
    def __del__(self):
        print("소멸")

if __name__ == '__main__':
    cal = Calculation()
    num1, operator, num2 = cal.executeCalculation()
    cal.__del__