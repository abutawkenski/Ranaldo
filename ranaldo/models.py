from django.db import models


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    data = models.DateTimeField()
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=200)
    image = models.FileField(upload_to='about/')

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    time = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    education = models.CharField(max_length=200)
    body = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    time = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    education = models.CharField(max_length=200)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=200)
    python = models.IntegerField()
    last_week = models.IntegerField()
    last_month = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Skillss(models.Model):
    title = models.CharField(max_length=200)
    python = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Awards(models.Model):
    time = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    education = models.CharField(max_length=200)
    body = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.FileField(upload_to="project/")

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
