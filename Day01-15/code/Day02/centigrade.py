"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

print('评分系统')
sc = float(input('please input score: '))
sum = sc * 0.3 + (sc + 5) * 0.7
print('totole %.2f --' % sum)
