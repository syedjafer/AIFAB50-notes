import cv2
source_image = "/home/iamsyedjafer/Documents/ML-Vault/data/img/i.jpg"
im_gray = cv2.imread(source_image, cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 127
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('/home/iamsyedjafer/Documents/ML-Vault/data/img/i_bw.jpg', im_bw)