from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllSecurityCenter',
            fields=[
                ('center_name', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('center_call', models.CharField(max_length=14)),
                ('center_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('announce_no', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('kind_of_animal', models.CharField(max_length=40)),
                ('breed', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('sex', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=40)),
                ('weight', models.CharField(max_length=30)),
                ('place_of_discovery', models.TextField()),
                ('date_time_of_receipt', models.TextField()),
                ('neutering', models.CharField(max_length=30)),
                ('info', models.TextField()),
                ('competent_organization', models.TextField()),
                ('protect_status', models.CharField(max_length=18)),
                ('image_url1', models.TextField()),
                ('image_url2', models.TextField(null=True)),
                ('image_url3', models.TextField(null=True)),
                ('center_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streetanimal.allsecuritycenter')),
            ],
            options={
                'ordering': ['-announce_no'],
            },
        ),
    ]
