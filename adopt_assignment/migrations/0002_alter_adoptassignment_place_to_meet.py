# Generated by Django 3.2.12 on 2022-03-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt_assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptassignment',
            name='place_to_meet',
            field=models.CharField(choices=[('서울 강동구청 반려동물팀', '서울 강동구청 반려동물팀'), ('인천 광역시 수의사회', '인천 광역시 수의사회'), ('대전 동물 보호 센터', '대전 동물 보호 센터'), ('세종 유기동물 보호센터', '세종 유기동물 보호센터'), ('대구 유기동물 보호 협회', '대구 유기동물 보호 협회'), ('부산 동물보호센터', '부산 동물보호센터'), ('광주 동물 보호소', '광주 동물 보호소'), ('울산 유기동물 보호센터', '울산 유기동물 보호센터'), ('제주 동물 보호센터', '제주 동물 보호센터'), ('속초시 유기동물 보호소', '속초시 유기동물 보호소')], default='서울 강동구청 반려동물팀', max_length=100),
        ),
    ]
