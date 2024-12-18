# 클래스
class classPractice:
    name = "클래스 연습"

    def printTest(self):
        print("클래스 연습")

    # 소멸자
    def __del__(self):
        print("클래스 소멸자 호출")


if __name__ == '__main__':
    #클래스 생성 
    classPrac = classPractice()
    #메서드 호출
    classPrac.printTest()
    print(classPrac)

    del classPrac
    print(classPrac)