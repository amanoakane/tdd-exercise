from django.db import models

class Entry(models.Model):
    entry_text = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self) -> str:
        return f"{self.entry_text}"


class Puzzle(models.Model):
    title = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=False)
    byline = models.CharField(max_length=255, null=False)
    publisher = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.publisher}, {str(self.date)}"


class Clue(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    clue_text = models.CharField(max_length=512, null=False)
    theme = models.BooleanField(default=False)

    def __str__(self):
        return f"Entry: {self.entry.entry_text}, Clue: {self.clue_text}"