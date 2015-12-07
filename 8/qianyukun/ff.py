#!/usr/bin/env python
# conding = utf-8
import json
import conf
from nbNetFramework import nbNet

alarmStatus = {}
def ff(d_in):
    mon_data = json.loads(d_in)
    for rule in conf.ff_conf:
        monKey, operator, value, alarmRecv = rule
        monName = monKey + operator + str(value)
        eval_function = str(mon_data[monKey]) + operator + str(value)
        ff_result = eval(eval_function)
        if ff_result:
            alrm_times = alarmStatus.get(monName,0)
            alarmStatus[monName] = alrm_times + 1
            if alrm_times >= 2:
                print "Alarm", eval_function, alarmRecv
        else:
            if alarmStatus.get(monName,0) >= 2:
                print "Recover", eval_function, alarmRecv
            alarmStatus[monName] = 0
if __name__ == '__main__':
    def logic(d_in):
        ff(d_in)
        return("OK")
    ffD = nbNet('0.0.0.0', 50002, logic)
    ffD.run()