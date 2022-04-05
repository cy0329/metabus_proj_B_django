from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfraCategory',
            fields=[
                ('category_name', models.CharField(choices=[('동물병원', '동물병원'), ('동물용품 상점', '동물병원 상점'), ('반려동물미용', '반려동물미용'), ('펫호텔', '펫호텔')], db_index=True, max_length=30, primary_key=True, serialize=False, verbose_name='분류')),
            ],
        ),
        migrations.CreateModel(
            name='AroundInfra',
            fields=[
                ('infra_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('infra_address', models.TextField()),
                ('infra_call', models.CharField(max_length=13, null=True)),
                ('category_name', models.ForeignKey(default='동물병원', on_delete=django.db.models.deletion.CASCADE, to='around_infra.infracategory', verbose_name='분류')),
            ],
            options={
                'ordering': ['-infra_name'],
            },
        ),
    ]
