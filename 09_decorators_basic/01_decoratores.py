def my_decoratore(func):
    def wrapper():
        print("Before Function runs")
        func()
        print("After function runs")
    return wrapper
@my_decoratore
def greet():
    print("Hello from decoratores from chai class")

greet()



 