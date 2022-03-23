
"""
中间件的作用：每次请求和响应的时候都会调用
中间件的定义

中间件的使用： 我们可以判断每次请求中是否携带了cookie中某种信息
"""
from django.http import HttpResponse
def simple_middleware(get_response):

    # 这里是 中间件第一次调用执行的地方
    def middleware(request):
        username = request.COOKIES.get('username')
        if username is None:
            print('username is None')
            return HttpResponse('哥们，你没有登录')
        # 这里是请求前
        print('before request')
        response = get_response(request)
        #这里就是 响应后/请求后
        print('after request/response')

        return response

    return middleware
