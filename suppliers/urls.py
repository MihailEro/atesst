from django.urls import path

from suppliers.views import ParticipantListAPIView, ParticipantDetailAPIView, ParticipantCreateAPIView, \
    ParticipantUpdateAPIView, ParticipantDestroyAPIView, MyTokenObtainPairView

app_name = 'suppliers'

urlpatterns = [
    path('participant/', ParticipantListAPIView.as_view(), name='participant_list'),
    path('participant/<int:pk>', ParticipantDetailAPIView.as_view(), name='participant_detail'),
    path('participant/create/', ParticipantCreateAPIView.as_view(), name='participant_create'),
    path('participant/update/<int:pk>', ParticipantUpdateAPIView.as_view(), name='participant_update'),
    path('participant/delete/<int:pk>', ParticipantDestroyAPIView.as_view(), name='participant_delete'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
