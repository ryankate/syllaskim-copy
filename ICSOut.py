import pandas
from ics import Calendar, Event
from datetime import timedelta


def saveToICS(assignment_date_list, f):
    c = Calendar()
    
    for i in range(len(assignment_date_list)):
        e = Event()
        e.name = assignment_date_list[i][0]
        #date = assignment_date_list[i][1].split('/')
        date = assignment_date_list[i][1].tz_localize('US/Central')

        e.begin = date
        e.duration = timedelta(hours=1)
        c.events.add(e)
        print(c.events)
     
    f.writelines(c)
    print(str(c))
