
# coding: utf-8

# This assignment partially uses seminars and homeworks code from the course "Signal and Image Processing" by S. Lefkimmiatis at Skoltech.

# # HW 1

# # Before you start: please put your name in the name of this file.
# 
# ## The template is: "HW1_Alexander Kuleshov"

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from imageio import imread




# In[3]:


def show_image(input_image, input_title, cmap='gray'):
    fig, ax1 = plt.subplots(1, 1, figsize=(8,8))
    
    ax1.imshow(input_image, cmap=cmap)
    ax1.set_title(input_title)
    ax1.set_axis_off()
    
def show_images(input_image, input_title, output_image, output_title, cmap='gray'):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 35))
    
    ax1.imshow(input_image, cmap=cmap)
    ax1.set_title(input_title)
    ax1.set_axis_off()
    
    ax2.imshow(output_image, cmap=cmap)
    ax2.set_title(output_title)
    ax2.set_axis_off()


# ## Task 1. QR-Code

# The goal of this homework is to use Fourier transformations as well as denoising and sharpering techniques to recover original image.
# 
# We have QR code image, which is distorted too much to read it using phones.
# 
# You will try to recover it.

# In[4]:


img = imread('qr_code.jpg')/255

ft_img = np.fft.fft2(img)
mag = np.abs(np.fft.fftshift(ft_img))

show_images(img, 'Original image', 20*np.log10(mag**2 + 1), 'Power (dB)', cmap='gray')


# (1) Note that the image is distorted with noise. In this case we suggest you to make an assumption that noise consists of gaussian noise and some periodic structure. 
# 
# Plot first line of an image as 1d graph. You will see the noise we need to deal with.

# In[7]:


# plot it here
# ...
plt.plot(img[0])


# (2) Substruct this line from the image and look if it helps. 

# In[54]:


temp = np.array([np.array(img[0]) for i in range(300)])


# In[55]:


new_img = img - temp


# In[56]:


show_images(new_img, 'Original image', 20*np.log10(mag**2 + 1), 'Power (dB)', cmap='gray')


# (3) It should look a bit better, but still too much noise there. It seems that we added more noise by substructing with a noisy sinusoide. Create a sinosuide with same amplitute and frequency. It may be a good idea to look at it in Fourier domain.

# In[57]:


# go to Fourier domain. Try to reconstruct only the periodic signal to subtract it later.
plt.plot(img[0])


# In[133]:


fs = 300 
f = 2 
x = np.arange(fs)
y = [(np.sin(2*np.pi*f * (i/fs)))/2 + 0.5 for i in x]

plt.plot(y)


# In[128]:


temp = np.array([np.array(y) for i in range(300)])


# In[129]:


plt.plot(img[0] - y)


# In[142]:


fs = 300 
f = 2 
x = np.arange(fs)
y = [(-(np.sin(2*np.pi*f * (i/fs))))*0.1 + 0.02 for i in x]
plt.plot(y)


# In[143]:


temp_2 = np.array([np.array(y) for i in range(300)])


# In[144]:


new_img_2 = img - temp - temp_2


# In[145]:


show_images(new_img_2, 'Original image', 20*np.log10(mag**2 + 1), 'Power (dB)', cmap='gray')


# (4) Ok, it must seem much better now. Try to remove rest of the noise. Use gaussian filter (or any other filter you wish). Play with parameters in order to get better results.

# In[146]:


# put here gaussian filtering if necessary.
# you may use "from skimage.filters import gaussian" filter.
from skimage.filters import gaussian
new_img_3 = gaussian(new_img_2)


# In[147]:


show_images(new_img_3, 'Original image', 20*np.log10(mag**2 + 1), 'Power (dB)', cmap='gray')


# (5) If you did all steps carefully, the image must be already scanable. If not, you may use any sharpening techniques to increase the contrast. For example, Laplacian operator and/or histogram rescaling.

# In[148]:


from skimage.exposure import equalize_hist, adjust_gamma, adjust_log
from skimage import img_as_ubyte


# In[149]:


contrast_correction = equalize_hist(new_img_3)
contrast_correction = img_as_ubyte(contrast_correction, force_copy=False)


# In[150]:


show_images(contrast_correction, 'Original image', 20*np.log10(mag**2 + 1), 'Power (dB)', cmap='gray')


import scipy.misc
scipy.misc.toimage(contrast_correction, cmin=0.0, cmax=...).save('results/outfile_img_test.jpg')

# (6) Can your phone read the QR-code now? If yes, just follow the message. Be sure that the readable qr-code image is in this notebook.

# Good job! 
# You did the task successfully.
# Finish the second task, check your code, clean it and submit to Canvas.
# 
# We wish you successes in all undertakings.
# 
# Best wishes,
# Intro to Image Processing mentors

# ## Task 2. Histogram Equalizer

# * Implement the function that would equalize the image histogram. Any kind of stretching can be used. 
# 
# * Test your function on the grayscale "Lena" image and colored "Barbara".
# 
# * Compare qualitatively mappings of equalizing histogram of colored "Barbara" image both **channelwisely** and **processing the image without taking into account different channels**. 

# _Message for outstandingly gifted boys and girls: **take the function "equalize hist" from skimage.exposure is prohibited!**_

# In[160]:


lena = imread('./lena.bmp') # .astype(np.float64)/255
barbara = imread('./barbara.png')
show_images(lena, 'Lena', barbara, 'Barbara')


# In[196]:


def equalize_hist(img):
    hist,bins = np.histogram(img.flatten(), 256, [0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255 /(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    equalized_img = cdf[img]
    return equalized_img


# In[197]:


plt.imshow(equalize_hist(lena))


# In[198]:


plt.imshow(lena)


# In[199]:


plt.imshow(barbara)


# In[200]:


plt.imshow(equalize_hist(barbara))



