from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
   date_of_birth = models.CharField(null=True, blank=True, default=None, max_length=55)
   blood_group = models.CharField(null=True, blank=True, default=None, max_length=55)
   gender = models.CharField(null=True, blank=True, default=None, max_length=55)
   home_town = models.CharField(null=True, blank=True, default=None, max_length=55)
   Current_City = models.CharField(null=True, blank=True, default=None, max_length=55)

   about_me = models.TextField(null=True, blank=True, default=None)

   skill_name = models.TextField(null=True, blank=True, default=None)

   department = models.CharField(null=True, blank=True, default=None, max_length=55)
   sust_reg_no = models.CharField(null=True, blank=True, default=None, max_length=55)
   session = models.CharField(null=True, blank=True, default=None, max_length=55)
   cur_semester = models.CharField(null=True, blank=True, default=None, max_length=55)

   contact_no = models.CharField(null=True, blank=True, default=None, max_length=55)
   Linkedin_link = models.CharField(null=True, blank=True, default=None, max_length=55)
   Github_Link = models.CharField(null=True, blank=True, default=None, max_length=55)

   height = models.CharField(null=True, blank=True, default=None, max_length=55)
   weight = models.CharField(null=True, blank=True, default=None, max_length=55)

   MSc_Institute_name = models.CharField(null=True, blank=True, default=None, max_length=55)
   MSc_Institute_Country = models.CharField(null=True, blank=True, default=None, max_length=55)
   MSc_start_date = models.CharField(null=True, blank=True, default=None, max_length=55)
   MSc_end_date = models.CharField(null=True, blank=True, default=None, max_length=55)

   Phd_Institute_name = models.CharField(null=True, blank=True, default=None, max_length=55)
   Phd_Institute_Country = models.CharField(null=True, blank=True, default=None, max_length=55)
   Phd_start_date = models.CharField(null=True, blank=True, default=None, max_length=55)
   Phd_end_date = models.CharField(null=True, blank=True, default=None, max_length=55)

   photos = models.FileField(null=False,blank=False,default=None,upload_to='images/')

   def __str__(self):
      return self.email

class Paper(models.Model):
   alumni_id=models.AutoField(null=False,blank=False,default=None,primary_key=True)
   user_id = models.ForeignKey(CustomUser,default=1,on_delete=models.CASCADE)
   Research_area = models.CharField(null=True, blank=True, default=None, max_length=55)
   Published_Paper = models.CharField(null=True, blank=True, default=None, max_length=55)
   Published_Journal = models.CharField(null=True, blank=True, default=None, max_length=55)

class Job(models.Model):
   job_id = models.AutoField(null=False, blank=False, default=None, primary_key=True)
   user_id = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
   Job_Institute_or_Company = models.CharField(null=True, blank=True, default=None, max_length=55)
   Address = models.CharField(null=True, blank=True, default=None, max_length=55)
   Job_Position = models.CharField(null=True, blank=True, default=None, max_length=55)
   Job_start_date = models.CharField(null=True, blank=True, default=None, max_length=55)
   Job_end_date = models.CharField(null=True, blank=True, default=None, max_length=55)
