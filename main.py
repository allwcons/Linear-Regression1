from LinearRegression import LinearRegression

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

model = LinearRegression()
model.fit(x,y)
result = model.predict([10])
print(result)
