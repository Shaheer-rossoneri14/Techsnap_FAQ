from django.db import models

topic_choices = [
    ("Account", "Account"),
    ("Enrollment", "Enrollment"),
    ("Communication", "Communication"),
    ("Certification", "Certification"),
    ("Others", "Others"),
]

# Create your models here.
class FAQ(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length = 100, choices = topic_choices, default="Others")
    question = models.TextField()
    answer = models.TextField()


