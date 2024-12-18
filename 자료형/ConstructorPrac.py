class Person:

    #생성자 
    # self는 나 자신을 가리키는 참조 java에선 this

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"제 이름은 {self.name}이고, {self.age}살입니다.")



if __name__ == '__main__':
    # 객체 생성
    person1 =Person("철수",25)
    person1.introduce()