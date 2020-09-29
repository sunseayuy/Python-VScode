import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx') # 加载要处理的工作簿
sheet = wb['Sheet1']