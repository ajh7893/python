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

# 각점수는 국 영 수 순으로 한다. 
score = {"가은":[82,97,88], "나영":[92,87,82],"다래":[84,77,94]}
#학생별 평균. 
score1 =score["가은"]
print(sum(score1)/len(score1))
score2 =score["나영"]
print(sum(score2)/len(score2))
score3 =score["다래"]
print(sum(score3)/len(score3))

# 각 과목별  평균
score_list = list(score.values())
kor = score_list[0][0] + score_list[1][0] + score_list[2][0]
eng = score_list[0][1] + score_list[1][1] + score_list[2][1]
mat = score_list[0][2] + score_list[1][2] + score_list[2][2]

print(kor/3)
print(eng/3)
print(mat/3)