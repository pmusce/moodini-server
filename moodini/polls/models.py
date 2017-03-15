from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.location_name


class Poll(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    people = models.SmallIntegerField()
    result = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return str(self.id)

    def generate_locations(self):
        i = 0
        for loc in Location.objects.all()[:5]:
            sloc = SelectedLocations(poll=self, location=loc, num=i)
            i = i + 1
            sloc.save()

    def is_closed(self):
        for loc in self.selectedlocations_set.all():
            if loc.choice_set.count() != self.people:
                return False
        return True

    def is_mood_selected(self):
        return self.selectedmood_set.count() == self.people


class SelectedLocations(models.Model):
    class Meta:
        unique_together = (('poll', 'num'),)

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    num = models.SmallIntegerField()

    def __unicode__(self):
        return str(self.poll) + ' - ' + str(self.num)


class SelectedMood(models.Model):
    class Meta:
        unique_together = (('poll', 'user'),)

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    mood = models.CharField(max_length=200)
    user = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.poll) + ' - ' + self.user + ' - ' + self.mood


class Choice(models.Model):
    location = models.ForeignKey(SelectedLocations, on_delete=models.CASCADE)
    vote = models.NullBooleanField()
    user = models.CharField(max_length=200)
