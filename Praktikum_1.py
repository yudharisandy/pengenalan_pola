"""
    Nama  : Yudha Putra Arisandy
    NIM   : G6501211035
    
1. Vektor
Deklarasi variabel diawali dengan
Vektor dapat dituliskan dengan dan tanpa bantuan libarary 
"""

#vektor python numpy with range value
import numpy as np
print("vektor default python\n")
a = np.arange(1,20,1)
b = np.arange(1,20,2)

import numpy as np
print (" \n vektor via numpy \n")

# vektor via numpy 
c = np.array ([1,2,3,4,5])
d = np.array ([1.5, 2.5, 5, 6, 7])

print(a)
print(b)
print(a.ndim)
print(a.shape)


"""
2. Matrix
Matriks adalah basic 2D table dari data dan dapat berisi nilai numerik 
dan/atau karakter. Dapat dibuat dengan cara sederhana dengan membuat 
urutan dari vektor, mengubah dari vektor atau membaca dari file 
"""
# mengubah dari 1D menjadi matrik 2D 
a = np.arange(1,21,1)
c = a.reshape((4,5))
print(c)

"""
3. List
List merupakan merupakan representasi struktur data yang dapat 
menyimpan data dengan nilai numerik, karakter, dan lain-lain secara bersamaan"""

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)

""" 
4. data.Frame
Data frame adalah spesialisasi dari tipe list untuk menyimpan vektor ke dalam 
bentuk frame (menyerupai basis data). Kelebihan dibandingkan matriks adalah dapat 
dimanipulasi dalam berbagai bentuk dan car
"""

#data frame
import pandas as pd
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                        columns=['a', 'b', 'c'])

print(df)