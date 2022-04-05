import adopt_assignment.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('streetanimal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptAssignment',
            fields=[
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('assignment_no', models.AutoField(primary_key=True, serialize=False)),
                ('adopter_name', models.CharField(db_index=True, max_length=30)),
                ('monthly_income', models.IntegerField()),
                ('residential_type', models.CharField(choices=[('아파트', '아파트'), ('빌라', '빌라'), ('주택', '주택'), ('원룸', '원룸'), ('오피스텔', '오피스텔')], default='아파트', max_length=50)),
                ('have_pet_or_not', models.BooleanField()),
                ('date_to_meet', models.DateField()),
                ('status', models.CharField(choices=[('신청', '신청'), ('심사 중', '심사 중'), ('수락', '수락'), ('교육 중', '교육 중'), ('입양 완료', '입양 완료'), ('거절', '거절')], db_index=True, default='신청', max_length=30)),
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='streetanimal.animal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-assignment_no'],
            },
        ),
        migrations.CreateModel(
            name='AdoptAssignmentHomeImage',
            fields=[
                ('home_image_no', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', validators=[adopt_assignment.models.validate_image])),
                ('assignment_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_image', to='adopt_assignment.adoptassignment')),
            ],
            options={
                'ordering': ['-home_image_no'],
            },
        ),
    ]
