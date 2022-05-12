from django.db import models
from django.utils import timezone
from student.models import Student


class Room(models.Model) : 
  room_number = models.CharField("방이름", max_length=100) 
  
  def __str__(self) : 
    return self.room_number

class Reservation(models.Model) :
  date = models.DateField("예약날짜")
  start_time = models.CharField("예약시작시간", max_length=100)
  end_time = models.CharField("예약끝나는시간", max_length=100)
  title = models.TextField('용도', null = True)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  user = models.ForeignKey(Student, on_delete=models.CASCADE)
  user_cnt = models.IntegerField("사용인원")
  
  def __str__(self) : 
    return f'{self.date, self.start_time, "-", self.end_time, self.room, self.user.name}'
  

  