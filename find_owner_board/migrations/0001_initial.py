# Generated by Django 3.2.12 on 2022-04-04 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import find_owner_board.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FindOwnerBoard',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('find_board_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('content', models.TextField()),
                ('animal_type', models.CharField(max_length=10)),
                ('breed', models.CharField(max_length=18)),
                ('size', models.CharField(max_length=10)),
                ('animal_tag', models.CharField(max_length=30)),
                ('find_location', models.CharField(max_length=50)),
                ('find_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-find_board_no'],
            },
        ),
        migrations.CreateModel(
            name='FindOwnerBoardImage',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('find_image_no', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', validators=[find_owner_board.models.validate_image])),
                ('find_board_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_image', to='find_owner_board.findownerboard')),
            ],
            options={
                'ordering': ['-find_image_no'],
            },
        ),
        migrations.CreateModel(
            name='FindOwnerBoardComment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('find_comment_no', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField()),
                ('find_board_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='find_owner_board.findownerboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['find_comment_no'],
            },
        ),
    ]
