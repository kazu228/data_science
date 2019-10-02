import random
from math   import *
# モンテカルロ法

whole = 2 ** 20	
k = 0.0			# 半径1未満の件数を格納する

for i in range(whole):

	x = random.random() # 値域[0.0, 1.0)のランダムな数を生成

	y = random.random() # 値域[0.0, 1.0)のランダムな数を生成

	if ( x**2 + y**2 < 1 ):

		k += 1
result = k / whole 
total = 0.5 * 0.5* 3.14
print("一辺が1の正方形の内側にある円の面積は、" + str(total) + "である。")
print("一辺が1の正方形の内側にある円の面積は、" + str(result) + "である。")