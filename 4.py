def hello_fun(greeting):
    return'{} Function.'.format(greeting)
print(hello_fun('hello'))

def student_ingo(*args, **kwargs):
    print(args)
    print(kwargs)

courses=['maths','history','science']
info={'name':'saurabh','age':'20'}
student_ingo(courses,info)

student_ingo(*courses,**info)