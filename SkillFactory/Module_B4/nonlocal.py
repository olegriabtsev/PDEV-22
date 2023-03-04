def get_my_func():
    def hello_world():
        print("Hello")

    return hello_world


hello_world_func = get_my_func()  # получить функцию в качестве результата

print(type(hello_world_func))  # <class 'function'>
hello_world_func()  # Hello
