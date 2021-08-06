from django.db import models




IN_STORE = (
    ("YES", "Yes"),
    ("NO", "No"),
)
class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    in_store = models.CharField(choices=IN_STORE, default="NO", max_length=3)
    isbn_number = models.CharField(max_length=13)
    pub_date = models.DateField()
    
    def __str__(self):
        return self.name
