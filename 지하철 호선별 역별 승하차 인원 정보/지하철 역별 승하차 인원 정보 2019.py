import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc 

# 한글 파일 깨짐 수정 코드	
rc('font', family='AppleGothic') 		
plt.rcParams['axes.unicode_minus'] = False 

data = pd.read_csv("/Users/minsung/Documents/2학년 1학기/과학적분석및발표/IC-PBL/지하철 호선별 역별 승하차 인원 정보/서울시 지하철호선별 역별 승하차 인원 정보 2019.csv", encoding='cp949')

station_data = data.groupby('역명').sum()

x = station_data.index
y1 = station_data['승차총승객수']
y2 = station_data['하차총승객수']

plt.title("2019 역별 승하차 인원 정보")
plt.plot(x, y1, label='승차')
plt.plot(x, y2, label='하차')
plt.legend()
plt.xticks(rotation=90)
plt.show()
