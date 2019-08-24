# coding:utf-8
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54000, 55323, 57500, 58000, 60000, 65000]
# plt.plot(x_data,y_data)
ln1 = plt.plot(x_data, y_data, color='red', linestyle='-.', label='python')
plt.plot(x_data, y_data2, color='green', label='疯狂java')
plt.legend(loc='best')
plt.xlabel('年份')
plt.ylabel('销量')
plt.title('图书销量趋势图')
plt.show()
