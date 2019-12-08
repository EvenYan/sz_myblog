from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


black_ip_list = ["192.168.159.128", '192.168.159.1']

class BlockIPMiddleware(MiddlewareMixin):
    def process_request(self, request):

        print("执行了BlockIPMiddleware中的process_request方法！")
        # return HttpResponse("你的IP被限制了！")
        ip = request.META.get("REMOTE_ADDR")
        print(ip)
        if ip in black_ip_list:
            return HttpResponse("你的IP被限制")

class MyMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        print("执行了Middleware1中的process_request方法！")
        # return HttpResponse("你的IP被限制了！")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print("执行了Middleware1中的process_view方法！")

    def process_response(self, request, response):
        print("执行了Middleware1中的process_response方法！")
        return response

    def process_exception(self, request, exception):
        print("执行了Middleware1中的process_exception方法！")


    def process_template_response(self, request, response):
        print("执行了Middleware1中的process_template_response方法！")
        return response


class MyMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print("执行了Middleware2中的process_request方法！")
        # return HttpResponse("你的IP被限制了！")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print("执行了Middleware2中的process_view方法！")

    def process_response(self, request, response):
        print("执行了Middleware2中的process_response方法！")
        return response

    def process_exception(self, request, exception):
        print("执行了Middleware2中的process_exception方法！")


    def process_template_response(self, request, response):
        print("执行了Middleware2中的process_template_response方法！")
        return response





