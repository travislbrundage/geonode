from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('services', '0003_missing_service_fields')
    ]

    operations = [
        migrations.AddField(
            model_name='WebServiceRegistrationJob',
            name='result',
            field=models.TextField(blank=True, null=True),
        )
    ]