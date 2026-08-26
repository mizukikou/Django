from django.db import models

class TemperatureRecord(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_id = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'myapp_temperature_db'
