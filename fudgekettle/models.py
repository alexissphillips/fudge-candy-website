from django.db import models

# Create your models here.
class AboutFudgeKettle(models.Model):
    # CharField stores short text= UN, titles, product names, categories, tags
    title = models.CharField(max_length=200)


    # TextField = no max length for large blocks of text 
    text= models.TextField()

    #this makes the objects much easier to identify in the django admin 
    # when trying to upload information into the text field of the About 
    # section, I got an error saying there is no 'name' attribute field in
    # the model therefore, it is not defined. so the returned string will be 
    # title because it has been defined 
    def __str__(self):
        return self.title

# The class for the candy will be seperate from the about model because they hold different information
class Candy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    #images require the pillow library 
    #stores the image associated with candy
    image = models.ImageField(upload_to= 'candy/')

    # a fixed precision decimal number represented in python by a Decimal instance
    #it validates the input using DecimalValidator 
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
            return self.name