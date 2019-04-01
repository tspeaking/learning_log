from django.db import models

class Topic(models.Model):
    '''Topic that the user is learning'''
    topic = models.CharField(max_length=200)
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return topic'''
        return self.topic

class Entry(models.Model):
    '''Memo for a specific topic'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''Return memo'''
        return self.text[:50] + '...'