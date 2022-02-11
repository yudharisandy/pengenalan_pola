"""
Praktikum 2

    Nama  : Yudha Putra Arisandy
    NIM   : G6501211035

Buat file dengan header, misalkan terdiri dari Nama Pasisen, Umur, Penyakit, 
Gender seperti pada tabel berikut dan simpan kedalam format CSV dan Text 
(Tab delimeter)
"""    
#Kemudian lakukan pembacaan untuk file tersebut:

# Membaca data dari file dengan format CSV
import pandas as pd
data = pd.read_csv("data/data.csv", sep=";")
print(data)
print('----------------------------')

# Membaca data dari file dengan format text (delimeter)
print("\n read text data with tab delimiter")
with open ('data/data.txt') as data:
    print(data.read())  
print('----------------------------')

# Membaca data dari URL
f = pd.read_csv('http://www.exploredata.net/ftp/Spellman.csv')
print(f)
print('----------------------------')

#Membaca file dan menyajikan dalam bentuk grafik. 
#Untuk dapat menyajikan dalam bentuk grafik terlebih dahulu 
#melakukan instalasi paket matplotlib. 
import numpy as sp
traffic = sp.genfromtxt("data/web_traffic.txt",delimiter='\t')
print(traffic[:10])
print(traffic.shape)

x = traffic[:,0]
y = traffic[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.title("Web traffic last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")

plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()

# Operasi image pada Python 
# Instalasi paket open cv
# pip install opencv-contrib-python 

# pilihan load image (contoh logo ipb)
import matplotlib.pyplot as plt
import cv2
import numpy as np

print("read images using opencv")
five = cv2.imread("data/5.png")
print(five.shape)
print(five.size)
plt.imshow(five)
cv2.waitKey(0)

# konversi image
import cv2
babon = cv2.imread("data/babon.jpg")
babon_gray = cv2.cvtColor(babon, cv2.COLOR_BGR2GRAY)
plt.imshow(babon) 
plt.imshow(babon_gray)

# mengambil nilai matriksnya
# acces pixel of images per postion 
pixels = five[100,100]
print(pixels)
