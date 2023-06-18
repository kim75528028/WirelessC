import matplotlib.pyplot as plt
import numpy as np
import ConvCodec as cc

data_size=128 #하나의 OFDM 심볼에 한번에 전송되는 QPSK 심볼의 수
max_snr=13 #최대 SNR 13db까지 실험
max_repeat = 10000
ber=[]

for snr_db in range(0,max_snr): # SNR을 높게 일단 설정
    total_error = 0
    for a in range(max_repeat):
        data = np.random.randint(0, 2, data_size)
        encoded_data = cc.Encoder(data)  # (131,2)
        real_data = encoded_data[0, :]
        imag_data = encoded_data[1, :]

        real_signal = real_data * 2 - 1  # -1과 1을 발생
        imag_signal = imag_data * 2 - 1  # -1과 1을 발생

        qpsk_sym = (real_signal + 1j * imag_signal) / np.sqrt(2)  # data_size 개의 QPSK
        ofdm_sym = np.fft.ifft(qpsk_sym) * np.sqrt(data_size)
        # ofdm_sym = np.fft.ifft(qpsk_sym) #QPSK 심볼 에너지가 data_size 배 감소한다.
        noise_std = 10 ** (-snr_db / 20)
        noise = np.random.randn(data_size+3) * noise_std / np.sqrt(2) + 1j * np.random.randn(
            data_size+3) * noise_std / np.sqrt(
            2)

        rcv_signal = np.fft.fft(ofdm_sym) / np.sqrt(data_size) + noise

        dec_real_signal = (rcv_signal.real > 0)
        dec_imag_signal = (rcv_signal.imag > 0)

        dec_signal = np.vstack([dec_real_signal, dec_imag_signal])

        rcv_data = cc.ViterbiDecoder(dec_signal)
        N_error = np.sum(np.abs(rcv_data - data))
        total_error = total_error + N_error
    ber.append(total_error / (data_size * max_repeat))


plt.subplot(2,2,1)
plt.plot(np.abs(qpsk_sym)**2)
plt.subplot(2,2,2)
plt.plot(np.abs(ofdm_sym)**2)
plt.subplot(2,2,3)
plt.scatter(ofdm_sym.real,ofdm_sym.imag)
plt.subplot(2,2,4)
plt.scatter(rcv_signal.real,rcv_signal.imag)

plt.show()