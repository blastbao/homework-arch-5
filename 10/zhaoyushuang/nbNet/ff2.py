import sys,os,json,hashlib,time
import MySQLdb as mysql
import conf

sys.path.insert(1,os.path.join(sys.path[0],'..'))

from nbNetFramework import nbNet

alarmStatus={}
alarmItems={}
# dict : mon_key :{alarm_times:3,monitor_times:4}
# alarmItems = {
#   mon_key :[3,n]
# }

def ff(input):
    #load monitor data
    #mon_data=json.load(input)
    mon_data=input
    for rule in conf.ff_conf:
        #com monitor rule
        mon_key,operator,value,alarmRecv,alarm_times=rule 
        mon_name=mon_key+operator+str(value)
        #use the rule to check input data 
        eval_function = str(mon_data[mon_key])+operator+str(value)
        ff_result=eval(eval_function)
        
        if ff_result:
            alarmStatus[mon_name]=True
            # if alarmItems[mon_key] is null init 
            if not alarmItems.has_key(mon_key) :
                alarmItems[mon_key]=[alarm_times,0]

            alarmItems[mon_key][1]+=1
            
            # when over the max alarm times then alarm it. 
            if alarmItems[mon_key][1]>=alarm_times:
                print ("Alarm %s %s %s ." %( mon_key,eval_function,alarmRecv) )
        else:
            if (alarmStatus.get(mon_name,False)):
                alarmStatus[mon_name]=False
                alarmItems[mon_key][1]=0
                
                print ("Recover %s %s %s ." %( mon_key,eval_function,alarmRecv) )
    
    
def logic(input):
    ff(input)
    return ("ok")


def testMonitor2():    
    ffD=nbNet('0.0.0.0',9090,logic)
    ffD.run()


def testMonitor():

    m_data=[
    {"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795},
    {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246805},
    {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246815},
    {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246825},
    {"MemTotal": 15888, "MemUsage": 904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246835},
    {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246875},
    {"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246885},
    {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246875},
    {"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246885},
    ]

    for index in m_data:
        print index
        ff(index)
        time.sleep(1)
   
    print "over"
 
if __name__ == '__main__':
    testMonitor()


