from django.urls import path


from .views import (StatusAPIView,
                    StatusAPIDetailView,
                    # StatusCreateAPIView,
                    # StatusDetailAPIView,
                    # StatusUpdateAPIView,
                    # StatusDeleteAPIView,
                    )

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:pk>/', StatusAPIDetailView.as_view()),

    # path('create/', StatusCreateAPIView.as_view()),

    # path('<int:pk>/', StatusDetailAPIView.as_view()),
    # path('<int:id>/', StatusDetailAPIView.as_view()),

    # path('<int:pk>/update/', StatusUpdateAPIView.as_view()),    
    # path('<int:pk>/delete/', StatusDeleteAPIView.as_view()),    
]

# Start with
# api/status/                   ==> List 
# api/status/create/            ==> Create
# api/status/<int:id>/          ==> Detail
# api/status/<int:id>/update/   ==> Update
# api/status/<int:id>/delete/   ==> Delete

# End with
# api/status/                   ==> List --> CRUD
# api/status/<int:id>/          ==> Detail --> CRUD

# Final
# api/status/                   ==> CRUD, List-Search(LS), List and Detail 