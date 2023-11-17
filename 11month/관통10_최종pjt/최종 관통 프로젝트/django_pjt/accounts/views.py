from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserProfileSerializer


# # profile 조회
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_profile_detail(request):
#     user = request.user
#     serializer = UserProfileSerializer(user)
#     return Response(serializer.data)



# def profile(request, user_pk):
#     User = get_user_model()
#     person = User.objects.get(pk=user_pk)
#     # user = request.user
#     context = {
#         'person' : person
#     }
#     return render(request, 'accounts/profile.html', context)


# # # @login_required
# # def follow(request, user_pk):
# #     if request.user.is_authenticated:
# #         User = get_user_model()
# #         you = User.objects.get(pk=user_pk)
# #         me = request.user
# #         if you != me:
# #             if you.followers.filter(pk=request.user.pk).exists():
# #                 you.followers.remove(me)
# #             else:
# #                 you.followers.add(me)
# #         return redirect("accounts:profile", you.pk)
# #     return redirect("accounts:login")