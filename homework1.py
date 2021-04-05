import numpy as np
import matplotlib.pyplot as plt
def y(x):
    y= (5 / 4 + np.cos(x)) ** 0.5 + (5 / 4 - np.cos(x))**0.5
    return y
def dy(x):
    dy =0.5*np.sin(x)*(((5/4)-np.cos(x))**(-0.5)-((5/4)+np.cos(x))**(-0.5))
    return dy
"各个作业内容只需要对下方的x与alpha值进行修改即可得出答案，这里给出课件实例图片的代码"
x = 2 #x可分别取1,2,3,4
alpha = 0.2
x_result=[x]
for i in range(100):
    x = x-alpha*dy(x)
    x_result.append(x)

print(x_result)
print(y(x_result))

plt.plot(x_result)
plt.plot(y(x_result))
plt.show()
"由于初始x不同，因此x，y的最终结果不同"