# # def test():
# #     y = 5   # local variable
# #     print(y)

# # test()

# y = 5 #Global
# def test():
#     print(y)
# test()
# print(y)   # (y is Global Now)


import matplotlib.pyplot as plt
categories = ["A","B","c","d","e"]
values = [25,40,80,100,10]

plt.bar(categories,values)
plt.title("bar chart")
plt.ylabel("categories")
plt.ylabel("values")
plt.show()