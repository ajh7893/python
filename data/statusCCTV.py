#지도 위에 표현해보기
import pandas as pd
import io
import folium

# CSV 파일 읽기
#file_path = input("CSV 파일의 경로를 입력하세요: ")  # 예: data.csv 또는 C:/folder/data.csv
file_path = 'C:\pythonDev\lean\data\statusCCTV.csv'
try:
    # 먼저 UTF-8로 시도
    cctv_csv = pd.read_csv(file_path) #C:\pythonDev\lean\data\유동인구데이터.csv
except UnicodeDecodeError:
    try:
        # UTF-8로 안되면 CP949로 시도
        cctv_csv = pd.read_csv(file_path, encoding='cp949')
    except UnicodeDecodeError:
        # CP949로도 안되면 EUC-KR로 시도
        cctv_csv = pd.read_csv(file_path, encoding='euc-kr',usecols=['년월','출발지역명','도착지역명','20대남성 유입인구'])

# data 프레임 NaN값 대체
cctv_csv = cctv_csv.fillna(0.0)

# x좌표(경도) y좌표(위도) 리스트로 만들기. 
x = []
y = []

for i in range(len(cctv_csv['위도'])):
    if cctv_csv['위도'][i] == 0.0 or cctv_csv['경도'][i] == 0.0:
        pass
    else:
        x.append(cctv_csv['경도'][i])
        y.append(cctv_csv['위도'][i])

map_osm = folium.Map(location=[y[20],x[20]], zoom_start=14)

for i in range(len(x)):
    folium.Marker([y[i],x[i]], popup='용산구 CCTV_%d'%i,
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
    

#범위지정
folium.CircleMarker(location=[y[20],x[20]], popup='용산구 CCTV',
                    radius=300, color='#3186cc',
                    fill_color='#3186cc').add_to(map_osm)    


#출력
map_osm
# HTML 파일로 저장
map_osm.save('cctv_map.html')
    