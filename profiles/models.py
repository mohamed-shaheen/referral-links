from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommended_profile', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username}-{self.code}"

    def  get_recommended_profiles(self):
        qs = Profile.objects.filter(recommended_by__exact = self.user)
        #my_recs = [p for p in qs if p.recommended_by == self.user]

        # my_recs = []
        # for profile in qs:
        #     if profile.recommended_by == self.user:
        #         my_recs.append(profile)
        return qs
    def save(self, *args, **kwargs):
        if self.code =="":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)
