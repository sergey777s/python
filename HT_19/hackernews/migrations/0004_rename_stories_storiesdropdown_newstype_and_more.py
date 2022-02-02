# Generated by Django 4.0.1 on 2022-02-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0003_ask_by_ask_descendants_ask_kids_ask_score_ask_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storiesdropdown',
            old_name='stories',
            new_name='newsType',
        ),
        migrations.RemoveField(
            model_name='ask',
            name='descendants',
        ),
        migrations.RemoveField(
            model_name='ask',
            name='kids',
        ),
        migrations.RemoveField(
            model_name='new',
            name='kids',
        ),
        migrations.RemoveField(
            model_name='show',
            name='descendants',
        ),
        migrations.RemoveField(
            model_name='show',
            name='kids',
        ),
        migrations.AddField(
            model_name='ask',
            name='s_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='ask',
            name='url',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='s_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='new',
            name='s_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='show',
            name='s_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='ask',
            name='by',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ask',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ask',
            name='score',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ask',
            name='text',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ask',
            name='time',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ask',
            name='title',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='ask',
            name='type',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='by',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='job',
            name='score',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='text',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='time',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='by',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='new',
            name='score',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='text',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='time',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='type',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='url',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='by',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='show',
            name='score',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='text',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='time',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='type',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='url',
            field=models.URLField(default=None, null=True),
        ),
    ]
