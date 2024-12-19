# 전처리 0값을 제거하자.
# 전처리 하는 이유는 데이터 생성이나 처리 과정에서 오류가 생길 수 있기 때문에.
import numpy

data = [16,18,17,18,0,19,20,22,21,0,21,22,0,0,0]
print(data)
data = [x for x in data if x != 0]
print(data)

numOfZeors = 0

for i in range(0,len(data)):
    if data[i] == 0:
        numOfZeors = numOfZeors +1
        print(numOfZeors)

for i in range(0,numOfZeors):
    data.remove(0)
    print(data)        

