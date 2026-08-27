from django.db import models

class TemperatureRecord(models.Model):
    myid = models.AutoField(primary_key=True)  # 將 id 改為 myid
    sensor_id = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'myapp_temperature_db'
