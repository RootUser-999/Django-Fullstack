from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="page_owner"
    )
    page_title = models.CharField(max_length=100)
    page_content = models.TextField()
    page_date_posted = models.DateTimeField(auto_now_add=True)

    page_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pages_authored"
    )

    def __str__(self):
        return self.page_title


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_date_posted = models.DateTimeField(auto_now_add=True)

    post_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts_authored"
    )

    def __str__(self):
        return self.post_title


class Song(models.Model):
    user = models.ManyToManyField(
        User,
        related_name="songs"
    )

    song_title = models.CharField(max_length=100)
    song_content = models.TextField()
    song_date_posted = models.DateTimeField(auto_now_add=True)

    song_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="songs_authored"
    )

    def __str__(self):
        return self.song_title

    def write(self):
        return ",".join(str(user) for user in self.user.all())