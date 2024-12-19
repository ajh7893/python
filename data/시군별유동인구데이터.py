#시군별 유동인구 데이터 
# 지역별 / 연령별 방문객 순위는?

import pandas as pd
import numpy

# CSV 파일 읽기
#file_path = input("CSV 파일의 경로를 입력하세요: ")  # 예: data.csv 또는 C:/folder/data.csv
file_path = 'C:\pythonDev\lean\data\시군별유동인구데이터.csv'
try:
    # 먼저 UTF-8로 시도
    df = pd.read_csv(file_path) #C:\pythonDev\lean\data\유동인구데이터.csv
except UnicodeDecodeError:
    try:
        # UTF-8로 안되면 CP949로 시도
        df = pd.read_csv(file_path, encoding='cp949',usecols=['년월','출발지역명','도착지역명','20대남성 유입인구'])
    except UnicodeDecodeError:
        # CP949로도 안되면 EUC-KR로 시도
        df = pd.read_csv(file_path, encoding='euc-kr',usecols=['년월','출발지역명','도착지역명','20대남성 유입인구'])

# 컬럼 목록 출력
print("\n=== 컬럼 목록 ===")
for col in df.columns:
    print(col)

# 데이터 미리보기
print("\n=== 데이터 미리보기 ===")
print(df.head())
print(df)
data_array = df.to_numpy()