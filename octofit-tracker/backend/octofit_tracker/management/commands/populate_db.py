from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        # Use Djongo's MongoDB client to drop collections for a clean reset
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']
        db['octofit_tracker_team'].drop()
        db['octofit_tracker_user'].drop()
        db['octofit_tracker_activity'].drop()
        db['octofit_tracker_workout'].drop()
        db['octofit_tracker_leaderboard'].drop()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Create Users (Superheroes)
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_leader=True),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_leader=True),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date=date.today())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400, date=date.today())
        Activity.objects.create(user=users[3], type='Swimming', duration=60, calories=500, date=date.today())

        # Create Workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes', difficulty='Hard')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility', difficulty='Medium')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=1200, rank=1)
        Leaderboard.objects.create(team=dc, total_points=1100, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
