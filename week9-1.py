import matplotlib.pyplot as plt
import numpy as np

data_size = 1000000
max_snr = 14 #dB
ber=[] # snr이 0,1,2,....,10dB로 변화할때 BIt Error Rate

for snr_db in range(0,max_snr):
    real_signal = np.random.randint(0,2,data_size)*2-1 #실수 신호
    imag_signal = np.random.randint(0,2,data_size)*2-1 #허수 신호
    qpsk_signal = (real_signal + 1j * imag_signal)/np.sqrt(2)
    std = 10**(-snr_db/20)
    real_noise = np.random.randn(data_size)*std/np.sqrt(2) #실수 noise
    imag_noise = np.random.randn(data_size)*std/np.sqrt(2) #허수 noise
    noise = real_noise + 1j * imag_noise
    rcv_signal = qpsk_signal + noise
    real_dect_signal = (rcv_signal.real>0)*2-1 #실수 dect
    imag_dect_signal = (rcv_signal.imag>0)*2-1 #허수 dect
    real_error = np.sum(np.abs(real_signal - real_dect_signal)) / 2 #실수 error
    imag_error = np.sum(np.abs(imag_signal - imag_dect_signal)) / 2 #허수 error
    error_rate = (real_error + imag_error)/(2*data_size)
    ber.append(error_rate)

snr = np.arange(0,max_snr)
plt.semilogy(snr-3,ber)
# plt.scatter(rcv_signal.real,rcv_signal.imag)
plt.show()