import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc 

# 한글 파일 깨짐 수정 코드	
rc('font', family='AppleGothic') 		
plt.rcParams['axes.unicode_minus'] = False 

data = pd.read_csv("/Users/minsung/Documents/2학년 1학기/과학적분석및발표/IC-PBL/서울시 지하철호선별 역별 승하차 인원 정보 2020.csv", encoding='cp949')

data = data[['노선명', '승차총승객수', '하차총승객수']]
data['총승객수'] = data['승차총승객수'] + data['하차총승객수']

grouped_data = data.groupby('노선명')['총승객수'].sum().reset_index()

x = grouped_data['노선명']
y = grouped_data['총승객수']

plt.bar(x, y)
plt.xticks(rotation=90)
plt.xlabel('노선명')
plt.ylabel('승차총승객수+하차총승객수')
plt.show()
