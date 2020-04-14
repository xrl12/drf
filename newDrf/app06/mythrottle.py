from rest_framework.throttling import SimpleRateThrottle

class VisitThrottle(SimpleRateThrottle):
    scope = '未认证用户'
    def get_cache_key(self, request, view):
        print(self.get_ident(request))
        return self.get_ident(request)

class UserThrottle(SimpleRateThrottle):
    scope = '认证用户'   #会在setting里面用到
    def get_cache_key(self, request, view):
        print(request.user.id)
        return request.user  #返回用户的id