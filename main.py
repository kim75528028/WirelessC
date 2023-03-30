import numpy as np
import matplotlib.pyplot as plt

m=0
std=2
min=3
max=20
dx=0.001
x=np.arange(min, max, dx)
g1=1/(np.sqrt(2*np.pi)*std)
g2=np.exp(-1*((x-m)**2)/(2*std**2))
gauss=g1*g2
m1=np.sum(gauss*dx) # 평균 구하기(평균=m)
print(m1) #이론상 평균

data_size=1000000
data=np.random.randn(data_size)*2  #가우스 랜덤 넘버 생성 , *2->표준편차를 2로 늘림
print(np.sum(data>3)/data_size) #랜덤 생성 후 평균