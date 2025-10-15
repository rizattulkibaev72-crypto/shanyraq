from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
    THEMES = [
        ('relationships', 'Отношения 💞'),
        ('burnout', 'Выгорание 🔥'),
        ('boundaries', 'Границы 🧱'),
        ('self', 'Саморазвитие 🌿'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    time_to_complete = models.PositiveIntegerField(default=5)
    questions_count = models.PositiveIntegerField(default=0)
    theme = models.CharField(max_length=30, choices=THEMES, default='self')

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    score_a = models.IntegerField(default=1)
    score_b = models.IntegerField(default=2)
    score_c = models.IntegerField(default=3)
    def __str__(self):
        return self.text


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    result_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.test.title} ({self.score})"
