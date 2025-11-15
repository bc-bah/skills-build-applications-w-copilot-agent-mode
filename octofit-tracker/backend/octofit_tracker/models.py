from djongo import models
from bson import ObjectId

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', db_column='team_id', to_field='id')
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities', db_column='user_id', to_field='id')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories = models.IntegerField()
    date = models.DateField()

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    suggested_for = models.ManyToManyField(Team, related_name='workouts')

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards', db_column='team_id', to_field='id')
    total_points = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        ordering = ['rank']
