# Generated by Django 3.1.4 on 2020-12-27 18:22

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('moviesApp', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='film',
            name='Category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Action', 'Action'), ('Animation', 'Animation'), ('Adventure', 'Adventure'), ('Crime', 'Crime'), ('Comedy', 'Comedy'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('History', 'History'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Science-Fiction', 'Science-Fiction'), ('Tv-Movie', 'Tv Movie'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], max_length=162, null=True),
        ),
    ]
