#coding=utf-8


import sys

'''对运行时的错误信息进行了封装处理'''
def tryfun(printdebug=True):
    def inner1(f):
        def inner2(*args, **kwargs):
            try:
                res = f(*args, **kwargs)
            except Exception as err:
                if printdebug:
                    info = sys.exc_info()[2].tb_frame.f_back
                    temp = "filename:{}\nlines:{}\tfuncation:{}\terror:{}"
                    print(temp.format(info.f_code.co_filename, info.f_lineno, f.__name__, repr(err)))
                res = None

            return res

        return inner2
    return inner1








