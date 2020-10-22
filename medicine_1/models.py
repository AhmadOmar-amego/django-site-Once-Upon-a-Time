from django.db import models
from django.contrib.auth.models import Permission, User
from django_pandas.managers import DataFrameManager


import datetime
class Medicine(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    medicine_title = models.CharField(max_length=100)
    description_medicine = models.TextField(blank=True , null =True)
    description_medicine = models.TextField(blank=True, null=True)
    place_of_medicine=models.CharField(max_length=500)
    genre = models.CharField(max_length=100,blank=True , null =True)
    logo_medicine = models.FileField(default='')
    company = models.TextField(max_length=50, default='UnKnown',blank=True, null=True)
    date_of_launch_medicine=models.DateTimeField(auto_now_add= True, blank=True)
    is_book=models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    comment_term1 = models.TextField(blank=True , null =True)
    # the additions after we change it to book site
    author=models.TextField(max_length=50, default='UnKnown',blank=True, null=True)
    date_of_launch_book=models.TextField(blank=True , null =True)
    language_of_book = models.TextField(default='UnKnown',max_length=100,blank=True , null =True)
    number_of_pages=models.TextField(max_length=50, default='UnKnown',blank=True, null=True)
    email_user=models.EmailField(null =True, blank=True)
    simple_desciption = models.TextField(blank=True, null=True)
    rating_book=models.TextField(blank=True, null=True)
    save_rate=models.TextField(blank=True, null=True)
    # for god sake
    is_booker = models.ManyToManyField(User, blank=True, related_name='is_booker')
    text_comment = models.TextField(blank=True, null=True)
    label_comment=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.medicine_title

BOOK_CHOICES=(
    ('Book','Book'),
    ('UnBook','UnBook'),
)


class BookingSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    value = models.CharField(choices=BOOK_CHOICES , default = 'Book', max_length = 8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user}-{self.medicine}-{self.value}"




class Patientrating(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    Pathological_case=models.CharField(max_length=100)
    review= models.CharField(max_length=500)
    rating =models.PositiveSmallIntegerField()
    date_of_review=models.DateTimeField(auto_now_add=True,auto_now=False)
    usefulCount=models.PositiveSmallIntegerField()


class CommentReview(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='comme')
    review= models.CharField(max_length=500)
    rating =models.CharField(max_length=500)

    def __str__(self):
        return self.review


class Descriptionofmed(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    Indications = models.TextField(blank=True , null =True)




class DrugDataset(models.Model):
    userid = models.CharField(max_length=200)
    drugName = models.CharField(max_length=200)
    condition= models.CharField(max_length=500)
    review = models.CharField(max_length=1000)
    rating =  models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    usefulCount = models.CharField(max_length=100)

    objects = DataFrameManager()

    def __str__(self):
        return self.drugName
    def __unicode__(self):
        return "%s, %s (%s)" % (self.drugName, self.condition, self.review, self.rating, self.date ,self.usefulCount)
        class Meta:
            ordering = ['drugName']


from django.utils import timezone

class Comment(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Test1(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

