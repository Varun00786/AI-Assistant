import datetime
import winsound
def alarm(timing):
  
    alltime=str(datetime.datetime.now().strptime(timing,"%I:%M %p"))
    """"I means 0-12 in hours format 
    M means 0-60 minute format 
    p means its am or pm"""
    
    
    print(alltime)
    alltime=alltime[11:-3] #1900-01-01 23:56:00 o/p so to show only 23:56 it is used
    hours=alltime[0:2] #last is not used 1 is used in place of 2
    # hours.replace("00","0")
    hours=int(hours)
    print(hours)
    minutes=alltime[3:5]
    minutes=int(minutes)
    print(minutes)
    print(f"Done,alaram is set for {timing}")
   
    # print(f"h={H},m={M}")
    while True:
        H=(datetime.datetime.now().hour)
        M=(datetime.datetime.now().minute)
        if hours==H:
            if minutes==M:
                print("alarm is running")
                winsound.PlaySound('SystemExit',winsound.SND_LOOP)
            elif minutes<M:
                print("eror")
                break
            
# alarm("10:40 PM")