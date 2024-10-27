# Generated by Django 3.2.23 on 2023-12-23 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation_app', '0003_delete_route_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='route_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=100)),
                ('from_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid', to='navigation_app.room_table')),
                ('to_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tid', to='navigation_app.room_table')),
            ],
        ),
    ]
