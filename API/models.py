from django.db import models
import uuid

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField()
    email = models.TextField(default=None)


    def create(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
        self.save()

    def __repr__(self):
        return str({"id": self.id, "username": self.username, "email": self.email})

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()


    def create(self, id, name):
        self.id = id
        self.name = name
        self.save()

    def __repr__(self):
        return str({"id": self.id, "name": self.name})

class Times(models.Model):
    id = models.AutoField(primary_key=True)
    time_start = models.BigIntegerField()
    time_finish = models.BigIntegerField()
    event = models.IntegerField()

    def create(self, id, time_start, time_finish, event):
        self.id = id
        self.time_finish = time_finish
        self.time_start = time_start
        self.event = event
        self.save()

    def __repr__(self):
        return str({"id": self.id,
        "time_start": self.time_start,
        "time_finish": self.time_finish,
        "event": self.event})
