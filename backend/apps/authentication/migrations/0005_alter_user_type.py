# Generated by Django 4.2.6 on 2023-11-01 16:18

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=model_utils.fields.StatusField(choices=[('user', 'user'), ('creator', 'creator')], default='user', max_length=100, no_check_for_status=True, verbose_name='User Type'),
        ),
    ]
