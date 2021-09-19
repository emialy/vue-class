from rest_framework import viewsets

from collect.models import Collect
from collect.serializers import CollectSerializer
from rest_framework.decorators import action
from comment.permissions import IsOwnerOrReadOnly


class CollectViewSet(viewsets.ModelViewSet):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer


#     @action(methods=['post'], detail=False)
#     def create(self, request):
#            # 获取用户ID
#         article.id = request.data.get('grade')  # 获取年级
#         Class_message = Collect.objects.filter(number=number, grade=grade)
#         if Class_message:
#             return_message = '班级已存在！'
#         else:
#            Collect.objects.create(number=number, grade=grade)  # 保存数据
#             return_message = '班级保存成功！'
#         content = {'result': return_message}
#         return Response(content)
#
#
# # drf_post.html的视图
# def drf_post(request):
#     return render(request, '')
def perform_create(self, serializer):
    serializer.save(author=self.request.user)
