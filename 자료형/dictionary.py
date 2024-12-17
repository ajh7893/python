dictionary = {
    "list" : [1,23,4,], 1:"ONE","name":"CHoi", "age":30
}

print(dictionary)

dictionary["weight"] = 80

print(dictionary)

del dictionary['name']

print(dictionary)

dictionary["list"] = 80

print(dictionary)
print(dictionary.get(1))
print(dictionary.get('list'))


fruits = {"apple":1000,"banana":1500,"pineapple":2000}
# 1.가지고있는 과일의 목록을 출력하기
fruits_list = list(fruits.keys())
print(fruits_list)

# 2.모든 과일의 가격 합과 평균을 구하기
fruits_list = list(fruits.values())
print(fruits_list)
print(sum(fruits_list))
print(sum(fruits_list)/len(fruits_list))
