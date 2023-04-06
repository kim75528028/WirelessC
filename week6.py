import numpy as np
import matplotlib.pyplot as plt

N = 100000 #데이터의 양
std = np.sqrt(0.1) # 노이즈에 곱하여 데시벨을 변화한다
sig = np.random.randint(2,size=N)*2-1 # 2보다 작은 랜덤값 N개 발생(0~1) 신호는 1과 -1 이기 때문에 2를 곱한후 1을 빼준다
noise = std*np.random.randn(N) #표준편차 1짜리인 노이즈를 N개 생성 , 평균 노이즈 파워 = 1

rcv_sig = sig+noise #sig에 noise를 섞음
dec_sig = (rcv_sig>0)*2-1
error = np.sum(np.abs(sig-dec_sig)/2)/N #오류가 생긴 부분을 찾기 sum = 오류의 갯수, /N = 오류확률

print(error*100) #오류 확률
#print(rcv_sig)


# plt.subplot(4,1,1)
# plt.stem(sig)
# plt.subplot(4,1,2)
# plt.stem(rcv_sig)
# plt.subplot(4,1,3)
# plt.stem(dec_sig)
# plt.show()

print(np.mean(noise**2)) #노이즈^2의 평균 거의 1
print(np.mean(noise)) #평균이 거의 0
