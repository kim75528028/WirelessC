import matplotlib.pyplot as plt
import numpy as np

N_sc = 200
max_snr = 10
ber = []

for snr_db in range (0,max_snr):
    real_sig = np.random.randint(0,2,N_sc)*2-1
    imag_sig = np.random.randint(0,2,N_sc)*2-1
    qpsk = (real_sig + 1j * imag_sig)/np.sqrt(2)
    #print(np.sum(np.abs(qpsk) ** 2) / N_sc)
    ofdm = np.fft.ifft(qpsk)*np.sqrt(N_sc)
    #print(np.sum(np.abs(ofdm) ** 2) / N_sc)


    noise_std = 10**(-snr_db/20)
    noise = (np.random.randn(N_sc) + 1j * np.random.randn(N_sc))/np.sqrt(2)
    noise = noise * noise_std

    rcv_sig = ofdm + noise
    #print(np.sum(np.abs(rcv_sig)**2)/N_sc)

    rcv_sig = np.fft.fft(rcv_sig)/np.sqrt(N_sc)
    #print(np.sum(np.abs(rcv_sig)**2)/N_sc)
    real_dec = (rcv_sig.real>0)*2-1
    imag_sig = (rcv_sig.imag>0)*2-1

    real_error = np.sum(np.abs(real_sig-real_dec))/2
    imag_error = np.sum(np.abs(imag_sig-real_dec))/2

    total_error = real_error+imag_error
    tmp_ber = total_error/(N_sc*2)
    ber.append(tmp_ber)

snr = np.arange(0,max_snr)
plt.semilogy(snr,ber)
plt.show()