# Online Exam Access: Allow or deny access to an online exam based on the current date and the exam's availability period.

from datetime import datetime

exam_date_and_time=datetime(2024, 7, 12, 15, 30, 45)
print(exam_date_and_time) 
current_time = datetime.now()

if current_time == exam_date_and_time:
    print("you can start your online exam")

elif current_time<exam_date_and_time:
    print("you are before time.Please wait for the exam began")

else:
    print("You can`t do online exam because time is passed") 