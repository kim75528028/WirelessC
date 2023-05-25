import numpy as np
import matplotlib.pyplot as plt
import ConvCodec as cc

data_size = 1024 # 1024개의 data bit
max_snr = range(1,10) # 최대 SNR 10db까지 실험
ber = []
for snr_db in max_snr:
    data = np.random.randint(0, 2, data_size) # 0과 1 데이터 1024개 (1024,)
    encoded_bit = cc.Encoder(data) # (2,1024) , 0과 1로 구성

    real_signal = encoded_bit[0, :] * 2 - 1  # -1과 1을 발생
    imag_signal = encoded_bit[1, :] * 2 - 1  # -1과 1을 발생

    qpsk_sym = (real_signal + 1j * imag_signal) / np.sqrt(2)
    ofdm_sym = np.fft.ifft(qpsk_sym) * np.sqrt(data_size) # 평균 파워 1이 되도록

    noise_std = 10 ** (-snr_db / 20)
    noise = np.random.randn(data_size+3) * noise_std / np.sqrt(2)
    rcv_signal = np.fft.fft(ofdm_sym) / np.sqrt(data_size) + noise

    real_detected_signal = np.array(((rcv_signal.real > 0) + 0)).reshape(1, data_size + 3)
    imag_detected_signal = np.array(((rcv_signal.imag > 0) + 0)).reshape(1, data_size + 3)

    dec_input = np.vstack([real_detected_signal, imag_detected_signal])
    #
    # real_error = np.sum(np.abs(real_signal - real_detected_signal)) / 2
    # imag_error = np.sum(np.abs(imag_signal - imag_detected_signal)) / 2
    #
    # total_error = real_error + imag_error
    # tmp_ber = total_error / (data_size * 2)

    decoded_bit = cc.ViterbiDecoder(dec_input)
    biterror = np.sum(np.abs(data - decoded_bit))
    ber.append(biterror / float(data_size))

    # print('-----', snr_db,'오류 정정 전 결과-----')
    print(np.sum(np.abs(dec_input - encoded_bit))) # 오류 정정 전 결과
    # print('-----', snr_db,'오류 정정 후 결과-----')
    print(np.sum(np.abs(data - decoded_bit))) # 오류 정정 후 결과
    print('-------------------------------------')

plt.semilogy(max_snr,ber)
plt.show()