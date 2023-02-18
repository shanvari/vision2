#2.1.1
img = cv2.imread('Camera Man.bmp',cv2.IMREAD_GRAYSCALE)
imshow(img)
#2.1.1
def histogram(img):
  hist = [0] * 256
  for i in range(len(img)):
    for j in range (len(img[0])):
      hist[img[i][j]] = hist[img[i][j]] + 1
  return hist
hist = histogram(img)

figure,(img1, img2) = plt.subplots(1, 2, figsize=(15, 6))
img1.plot(temp, hist)
img2.imshow(img)
 
#2.1.1.1
D = np.array(img / 3, dtype = 'uint8')
imshow(D)
 
#2.1.1.2
histD = histogram(D)

figure,(img1, img2) = plt.subplots(1, 2, figsize=(15, 6))
img1.plot(temp, hist_image)
img2.plot(temp, hist_imageD)
 
#2.1.1.3
def equalization(img):
    h, _ = np.histogram(img, 256, [0, 256])
    cdf = np.cumsum(h)
    cdf_norm = np.ma.masked_equal(cdf, 0)
    cdf_norm = (
        (cdf_norm - cdf_norm.min()) * 255 / (cdf_norm.max() - cdf_norm.min())
    )
    cdf_final = np.ma.filled(cdf_norm, 0).astype("uint8")
    img = cdf_final[img]
    return img
H = equalization(D)
plt.imshow(H)
plt.show()
 
#2.1.1.4
def lh_equalization(img,w):
    temp = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(w, w))
    cl1 = temp.apply(img)
    return cl1
L = lh_equalization(D,w=8)
plt.imshow(imageL,cmap="gray")
plt.show()
 
#2.1.1.5
hist_H = histogram(H)
hist_L = histogram(L)
figure,(a1, a2) = plt.subplots(1, 2, figsize=(15, 6))
a1.plot(temp, hist_H)
a2.plot(temp, hist_L)
plt.show()
#2.1.1.6
def log_transform(img):
    c = 255/(np.log(1 + np.max(img)))
    log_transformed = c * np.log(1 + img)
    log_transformed = np.array(log_transformed, dtype = np.uint8)
    return log_transformed
image_log_transform = log_transform(imageD)
plt.imshow(image_log_transform,cmap="gray")
plt.show()

def powerLaw_transform(img,gamma):
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
    return gamma_corrected
image_powerLaw_transform = powerLaw_transform(imageD,0.67)
plt.imshow(image_powerLaw_transform,cmap="gray")
plt.show()
 
hist_image_log_transform = histogram(image_log_transform)
hist_image_powerLaw_transform = histogram(image_powerLaw_transform)

figure,(ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
ax1.plot(temp, hist_image_log_transform)
ax2.plot(temp, hist_image_powerLaw_transform)
plt.show()
 
2.1.2
image_eq = histogram_equalization(image)
hist_image_eq = histogram(image_eq)
figure,((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
ax1.plot(temp, hist_image)
ax2.imshow(image,cmap="gray")
ax3.plot(temp, hist_image_eq)
ax4.imshow(image_eq,cmap="gray")
plt.show()
 


2.2.1
he1 = cv2.imread("images//2//HE1.jpg",0)
he2 = cv2.imread("images//2//HE2.jpg",0)
he3 = cv2.imread("images//2//HE3.jpg",0)
he4 = cv2.imread("images//2//HE4.jpg",0)

figure,((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
ax1.imshow(he1,cmap="gray")
ax2.imshow(he2,cmap="gray")
ax3.imshow(he3,cmap="gray")
ax4.imshow(he4,cmap="gray")
plt.show()
 

global histogram equalization:
def histogram_equalization(img):
    h, _ = np.histogram(img, 256, [0, 256])
    cdf = np.cumsum(h)
    cdf_norm = np.ma.masked_equal(cdf, 0)
    cdf_norm = (
        (cdf_norm - cdf_norm.min()) * 255 / (cdf_norm.max() - cdf_norm.min())
    )
    cdf_final = np.ma.filled(cdf_norm, 0).astype("uint8")
    img = cdf_final[img]
    return img
figure,((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
ax1.imshow(histogram_equalization(he1),cmap="gray")
ax2.imshow(histogram_equalization(he2),cmap="gray")
ax3.imshow(histogram_equalization(he3),cmap="gray")
ax4.imshow(histogram_equalization(he4),cmap="gray")
plt.show()
 
local histogram equalization:
def local_histogram_equalization(img,window):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(window, window))
    cl1 = clahe.apply(img)
    return cl1
window = 8
figure,((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
ax1.imshow(local_histogram_equalization(he1,window),cmap="gray")
ax2.imshow(local_histogram_equalization(he2,window),cmap="gray")
ax3.imshow(local_histogram_equalization(he3,window),cmap="gray")
ax4.imshow(local_histogram_equalization(he4,window),cmap="gray")
plt.show()
 
window = 32
figure,((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
ax1.imshow(local_histogram_equalization(he1,window),cmap="gray")
ax2.imshow(local_histogram_equalization(he2,window),cmap="gray")
ax3.imshow(local_histogram_equalization(he3,window),cmap="gray")
ax4.imshow(local_histogram_equalization(he4,window),cmap="gray")
plt.show()
 
window = 128
figure,((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
ax1.imshow(local_histogram_equalization(he1,window),cmap="gray")
ax2.imshow(local_histogram_equalization(he2,window),cmap="gray")
ax3.imshow(local_histogram_equalization(he3,window),cmap="gray")
ax4.imshow(local_histogram_equalization(he4,window),cmap="gray")
plt.show()

 
