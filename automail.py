import yagmail
import os
import datetime
import csv
import warnings
warnings.filterwarnings('ignore')
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("preethiba1912@gmail.com", "jcff iumc sbeo vyto")

#sent the mail
with open("Attendance_2022-06-07_21-59-57.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for Id,Name,Date,Time,mail in reader:
        yag.send(
        to= mail[2:len(list(mail))-2],
        subject=sub, # email subject
        attachments= filename  # file attached
        )
        print(f'sent to {Name}')
print("Email Sent!")