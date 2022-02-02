from django.db import models


class Ask(models.Model):
    by = models.CharField(max_length=200, default=None, null=True)
    s_id = models.IntegerField(default=None, null=True)
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    title = models.CharField(max_length=250, default=None, null=True)
    type = models.CharField(max_length=50, default=None, null=True)
    url = models.URLField(default=None, null=True)

    def __str__(self):
        return str(self.title)


class New(models.Model):
    by = models.CharField(max_length=200, default=None, null=True)
    s_id = models.IntegerField(default=None, null=True)
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    title = models.CharField(max_length=250, default=None, null=True)
    type = models.CharField(max_length=50, default=None, null=True)
    url = models.URLField(default=None, null=True)

    def __str__(self):
        return str(self.title)


class Job(models.Model):
    by = models.CharField(max_length=200, default=None, null=True)
    s_id = models.IntegerField(default=None, null=True)
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    title = models.CharField(max_length=250, default=None, null=True)
    type = models.CharField(max_length=20, default=None, null=True)
    url = models.URLField(default=None, null=True)

    def __str__(self):
        return str(self.title)


class Show(models.Model):
    by = models.CharField(max_length=200, default=None, null=True)
    s_id = models.IntegerField(default=None, null=True)
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    title = models.CharField(max_length=250, default=None, null=True)
    type = models.CharField(max_length=50, default=None, null=True)
    url = models.URLField(default=None, null=True)

    def __str__(self):
        return str(self.title)
