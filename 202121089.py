import numpy as np

std = np.sqrt(0.5)
N = 100000
snr = [0,1,2,3,4,5,6,7,8,9,10]
noise_list = []
for snr_db in snr:
    sig = np.random.randint(2,size=N)*2-1
    noise = std*np.random.randn(N)
    noise_power = 10**(-snr_db/20)

    rcv_sig = sig+noise
    dec_sig = (rcv_sig>0)*2-1
    error = np.sum(np.abs(sig - dec_sig) / 2) / N
    print(error)
    print('--------------------------')
