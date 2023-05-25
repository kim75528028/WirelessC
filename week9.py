import matplotlib.pyplot as plt
import numpy as np

data_size = 1000000
max_snr = 11 #dB
ber=[] # snr이 0,1,2,....,10dB로 변화할때 BIt Error Rate

for snr_db in range(0,max_snr):
    signal = np.random.randint(0,2,data_size)*2-1 #BPSK 완성
    noise_std=10**(-snr_db/20) #noise의 표준편차
    noise = np.random.randn(data_size)*noise_std/np.sqrt(2)
    rcv_signal = signal + noise
    dect_signal = (rcv_signal>0)*2-1
    num_error = np.sum(np.abs(signal-dect_signal))
    error_rate = num_error/data_size
    ber.append(error_rate)

snr = np.arange(0,max_snr)
plt.semilogy(snr,ber)
plt.show()