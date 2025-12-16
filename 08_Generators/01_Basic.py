def my_generator():
    for i in range(5):
        yield i
gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
for i  in gen:
    print(i)

#list use large amount of memory while generator (gen)use memory when it need