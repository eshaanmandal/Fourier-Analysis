import numpy as np

class Compress:
    ''' Python class from compressing images using FFT method. It requires the numpy library installed'''
    def __init__(self):
        return
    def img_compress(self,image,grayscale=False,size=0.8):
        ''' Compresses an RGB image '''
        if not grayscale:
            times = 3
            channels = [image[:,:,0], image[:,:,1], image[:,:,2]]
        else:
            times = 1
            channels = [image]

        for i in range(times):
            print(f'compressing channel {i+1}')
            fft_img = np.fft.fft2(channels[i])
            lin_img = np.sort(np.abs(np.reshape(fft_img,-1)))[::-1]
            threshold = np.floor(len(lin_img)*size)-1
            mask = np.abs(fft_img) > lin_img[int(threshold)]
            c_fft = (mask * fft_img)
            if grayscale:
                image = np.real(np.fft.ifft2(c_fft))
                break
            image[:,:,i] = np.real(np.fft.ifft2(c_fft))

        return image









