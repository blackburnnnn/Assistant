#ans41答案.py
"""
评分标准
输入语句正确（3分）
循环处理正确（3分）
边框输出正确（2分）
*数目正确（2分）
正确换行（2分）
正确运行结果（3分）

"""


rows=int(input('请输入行数：'))
if rows%2==0:
    rows+=1
for i in range(1, rows+1):
    if i != 1 and i != rows:
        for k in range(0, int(rows/2)):
            print(" ", end="")
        print("*")
    else:
        for k in range(0, rows):
            print("*", end="")
        print()    
    
