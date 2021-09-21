
from django.contrib import admin
<<<<<<< Updated upstream
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))

]
=======
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', include( 'accounts.urls' ) )
]
>>>>>>> Stashed changes
