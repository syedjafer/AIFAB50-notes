from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

content = open("/home/iamsyedjafer/Documents/ML-Vault/data/ironman.txt", 'r').read()
stopwords = set(STOPWORDS)
custom_mask = np.array(Image.open('/home/iamsyedjafer/Documents/ML-Vault/data/img/i_bw.jpg'))
wc = WordCloud(background_color='black',stopwords=stopwords,
                mask=custom_mask, contour_color='yellow', contour_width=1)
wc.generate(content)
plt.figure( figsize=(20,10), facecolor='k')
plt.imshow(wc, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()