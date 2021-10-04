import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude

class MyWordCloud:
    def __init__(self, content_location, out_location, mask_image=None):
        self.content_location = content_location
        self.out_location = out_location
        self.mask_image = mask_image
        self.__stopwords = set(STOPWORDS)
    
    def add_stop_words(self, words):
        try:
            self.__stopwords.update(words)
        except Exception as ex:
            raise ex
    
    def get_stop_words(self):
        return self.__stopwords

    def generate_image(self):
        try:
            # Reading File Content
            _content_file_obj = open(self.content_location, 'r')
            _content = _content_file_obj.read()
            _content_file_obj.close()

            # Reading Mask
            if self.mask_image:
                image = np.array(Image.open(self.mask_image))
                _image_mask = image.copy()
                # dimension = 2
                # image[_image_mask.sum(axis=dimension-2) == 0] = 255

                # edges = np.mean([gaussian_gradient_magnitude(image[:, :, i] / 255., 2) for i in range(dimension)], axis=0)
                # _image_mask[edges > .1] = 255
            else:
                _image_mask = None
            
            _wc = WordCloud(background_color='black',
                            mask=_image_mask, stopwords=self.get_stop_words())
            
            _wc.generate(_content)

            fig = plt.figure()
            
            plt.imshow(_wc, interpolation='bilinear')
            plt.axis('off')
            plt.show()
        except Exception as ex:
            raise ex

_content_location = r"/home/iamsyedjafer/Documents/ML-Vault/data/tamil_nadu.txt"
_out_location = r"/home/iamsyedjafer/Documents/ML-Vault/Tryouts"
_mask_image = r"/home/iamsyedjafer/Documents/ML-Vault/data/img/heart.png"

mwc = MyWordCloud(content_location=_content_location,
                    out_location=_out_location,
                    mask_image=_mask_image)
mwc.generate_image()