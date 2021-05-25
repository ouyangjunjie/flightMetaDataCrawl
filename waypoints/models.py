from djongo import models

# Create your models here.
# {
#     "cityChineseName": "北京",
#     "cityEnglishName": "Beijing",
#     "airportChineseName": "北京首都国际机场",
#     "airportEnglishName": "Beijing Capital International Airport",
#     "airportCode": "PEK",
#     "countryCode": "CN",
#     "icao": "ZBAA",
#     "iata": "PEK",
#     "status": "运营中",
#     "startTime": "1958",
#     "flightLevel": "4F",
#     "latitude": 40.0448,
#     "longitude": 116.3504,
#     "timeZone": "UTC+8"
# }


class WayPoint(models.Model):
    cityChineseName = models.CharField(verbose_name="城市中文名", max_length=256)
    cityEnglishName = models.CharField(verbose_name="城市英文名", max_length=256)
    airportChineseName = models.CharField(verbose_name="机场中文名", max_length=256)
    airportEnglishName = models.CharField(verbose_name="机场英文名", max_length=256)
    airportCode = models.CharField(verbose_name="机场三字码", max_length=256)
    countryCode = models.CharField(verbose_name="国家二字码", max_length=256)
    icao = models.CharField(verbose_name="国际四字码", max_length=256)
    iata = models.CharField(verbose_name="三字码", max_length=256)
    status = models.CharField(verbose_name="机场状态", max_length=256)
    startTime = models.CharField(verbose_name="开始运营时间", max_length=256)
    flightLevel = models.CharField(verbose_name="机场等级", max_length=256)
    latitude = models.CharField(verbose_name="纬度", max_length=256)
    longitude = models.CharField(verbose_name="经度", max_length=256)
    timeZone = models.CharField(verbose_name="时区", max_length=6)

    def __str__(self):
        return "{}:{}..".format(self.id, self.paragraph[:15])

    class Meta:
        verbose_name = '航点'
        verbose_name_plural = verbose_name

