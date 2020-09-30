import openpyxl as xl
from openpyxl.chart import BarChart, Reference

wb = xl.load_workbook('venv/transactions.xlsx')  # 加载要处理的工作簿
sheet = wb['Sheet1']  # 表格1赋予sheet

#定位单元格的位置
cell = sheet['a1']
cell = sheet.cell(1, 1)
#显示单元格中内容 cell.value
print(cell.value)

#显示表有多少行
print(f'行数：{sheet.max_row}')

#将某一列乘0.9
for row in range(2, sheet.max_row + 1):
    #print(row)
    cell = sheet.cell(row, 3)
    print(cell.value)
    corrected_price = cell.value * 0.9
    #添加一行新列
    corrected_price_cell = sheet.cell(row, 4)  # 这个只是单元格
    corrected_price_cell.value = corrected_price  # 单元格值赋予

#添加图表
#使用应用类来添加对象范围
values = Reference(sheet,
          min_row=2,
          max_row=sheet.max_row,
          min_col=4,
          max_col=4)
#创建条形图类的实例
chart = BarChart()
chart.add_data(values)#图表添加数据
sheet.add_chart(chart,'e2')#表格添加条形图

wb.save('venv/transactions2.xlsx')
