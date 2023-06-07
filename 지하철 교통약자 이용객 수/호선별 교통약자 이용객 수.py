import matplotlib.pyplot as plt

# 데이터 정의
line_names = ['Line1', 'Line2', 'Line3', 'Line4', 'Line5', 'Line6', 'Line7', 'Line8', 'Line9']
passenger_counts = [21366511, 54076749, 30485816, 29269418, 38029420, 19062335, 32759753, 11784410, 4492024]

# 그래프 그리기
plt.bar(line_names, passenger_counts)
plt.xlabel('line name')
plt.ylabel('Number of passengers')
plt.title('Number of passengers by subway line')

# 그래프 출력
plt.show()

