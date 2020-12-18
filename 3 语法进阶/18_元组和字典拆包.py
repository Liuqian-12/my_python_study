def demo(*args, **kwargs):
    print(args)
    print(kwargs)

gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "xiaoming", "age": 18}

# demo(gl_nums, gl_xiaoming)
demo(*gl_nums, **gl_xiaoming)

