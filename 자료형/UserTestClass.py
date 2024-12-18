class UserTestClass:
    name = "클래스 연습"

    def testFunc1(self):
        print("test func1")

    # 함수 안에 함수 부르기
    def testFunc2(self):
        print("test func2")
        self.testFunc1()


if __name__ == '__main__':
    #객체 생성
    testClass = UserTestClass()
    # 클래스내 전역변수 사용
    print('전역변수: '+testClass.name)
    #메서드  
    testClass.testFunc2()