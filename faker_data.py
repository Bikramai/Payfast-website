from src.accounts.models import User
from faker import Faker
import datetime
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from src.api.models import AlertMessage

fake = Faker()


def initialization(init=True, mid=True, end=True):

    if init:
        create_users()


def create_users():
    print()
    print("----- BUILDING USERS STARTED  ------")

    user_names = [
        'u1', 'u2', 'u3', 'user1', 'user2', 'user3', 'user4', 'user5',
        'user6', 'user7', 'user8', 'user9', 'user10'
    ]

    for name in user_names:
        if not User.objects.filter(username=name):
            user = User.objects.create_user(username=name, email=f'{name}@exarth.com', password='poiuyt098765',
                                            phone_number='03000000000')
            user.first_name = fake.first_name()
            user.last_name = fake.last_name()
            user.phone_number = fake.phone_number()
            user.save()

            print(f"  -- User {user.username} Created")
        else:
            print(f"  -- User {name} already exists.")

    print("----- BUILDING USERS FINISHED ------")
