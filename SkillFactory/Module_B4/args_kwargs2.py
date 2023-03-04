def my_fun(arg1, *args):
    print('First argument :', arg1)
    for i in args:
        print('Next argument through *args: ', i)


my_fun('Hello', 'Welcome', 'to', 'Unit4')
print('---')


def my_fun2(**kwargs):
    for key, value in kwargs.items():
        print('%s == %s' % (key, value))


my_fun2(first='Geeks', seconds='for', third='Geeks')
print('---')


def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')
