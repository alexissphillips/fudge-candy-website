from django.contrib import admin
from .models import AboutFudgeKettle 
from .models import Candy
# To make our model visible on the admin page, 
# we need to register the model with admin.site.register(class name)
admin.site.register(AboutFudgeKettle)
admin.site.register(Candy)




