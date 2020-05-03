# Generated by Django 3.0.5 on 2020-05-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recommender', '0004_auto_20200501_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_reputation_rank',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='art',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='biology',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='chemistry',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='chinese',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='citation_rank',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='cost_index',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='employer_reputation_rank',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='english',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty_student_rank',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='geogrophy',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='history',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='ielts',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='international_faculty_rank',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='international_student_percentage',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='international_student_rank',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='math',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='max_tution_fee',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='min_tution_fee',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='physics',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='politics',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='region',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='toefl',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='work_study',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
