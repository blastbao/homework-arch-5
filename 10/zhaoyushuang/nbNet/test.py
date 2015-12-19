import time 

m_data=[
{"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795},
{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246805},
{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246815},
{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246825},
{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246835},
{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246875},
{"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246885},
]

for index in m_data:
    print index
    time.sleep(1)
