import pandas

# pip install pandas

data = pandas.read_csv('records_discount.csv', delimiter=";")
print(data)
#     sku  exp_date   price
# 0    1     today  200.00
# 1    2     today  100.00
# 2    3  tomorrow   50.00
# 3    4     today   49.99
# 4    5     today  100.00

print(data.columns)  # Index(['sku', 'exp_date', 'price'], dtype='object')
print(data.values)
# [[1 'today' 200.0]
#  [2 'today' 100.0]
#  [3 'tomorrow' 50.0]
#  [4 'today' 49.99]
#  [5 'today' 100.0]]
