from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', team='Test Team', type='Run', duration=10)
        self.assertEqual(str(activity), 'testuser - Run')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=50)
        self.assertEqual(str(lb), 'Test Team: 50')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushup', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushup')
