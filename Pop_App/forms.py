from django import forms

class PopEntryForm(forms.Form):
    character = forms.CharField()
    pop_type = forms.ChoiceField(choices=[
        ('pop', 'Pop!'),
        ('pop_games', 'Pop! Games'),
        ('pop_marvel', 'Pop! Marvel'),
        ('pop_heroes', 'Pop! Heroes'),
        ('pop_animation', 'Pop! Animation'),
        ('pop_wwe', 'Pop! WWE'),
        ('pop_movies', 'Pop! Movies'),
        ('pop_television', 'Pop! Television'),
        ('other', 'Other'),
    ])
    series = forms.CharField()
    series_number = forms.IntegerField()
    special_edition = forms.CharField()


