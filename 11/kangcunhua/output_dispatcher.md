#rpcDispatcher.py 输出

```log

>>study:/home/kang/arch-5/rebootMon/dispatch>python rpcDispatcher.py 'ls' 127.0.0.1,127.0.0.1
hosts: ['127.0.0.1', '127.0.0.1']
=======hs=====: 127.0.0.1 ====p==== 9999
=======hs=====: 127.0.0.1 ====p==== 9999
132 
 - state of fd: 4
154 
 - current state of fd: 4
155  - - state: write
156  - - have_read: 0
157  - - need_read: 0
158  - - have_write: 0
159  - - need_write: 12
160  - - buff_write: 0000000002ls
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7ffd5213b130>
165  - - popen_pipe:   0
132 
 - state of fd: 5
154 
 - current state of fd: 5
155  - - state: write
156  - - have_read: 0
157  - - need_read: 0
158  - - have_write: 0
159  - - need_write: 12
160  - - buff_write: 0000000002ls
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7ffd5213b1a0>
165  - - popen_pipe:   0
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(135)run()
-> epoll_list = self.epoll_sock.poll()
(Pdb) c
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7ffd527a0518>, 5: <nbNet.nbNetUtils.STATE instance at 0x7ffd527a3d88>}
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(64)write2read()
-> try:
(Pdb) c
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7ffd52790560>, 5: <nbNet.nbNetUtils.STATE instance at 0x7ffd527a3d88>}
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(64)write2read()
-> try:
(Pdb) c
132 
 - state of fd: 4
154 
 - current state of fd: 4
155  - - state: read
156  - - have_read: 0
157  - - need_read: 10
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7ffd5213b130>
165  - - popen_pipe:   0
132 
 - state of fd: 5
154 
 - current state of fd: 5
155  - - state: read
156  - - have_read: 0
157  - - need_read: 10
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7ffd5213b1a0>
165  - - popen_pipe:   0
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(134)run()
-> pdb.set_trace()
(Pdb) c
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7ffd52790560>, 5: <nbNet.nbNetUtils.STATE instance at 0x7ffd527a6d40>}
header_said_need_read 47
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7ffd52790560>, 5: <nbNet.nbNetUtils.STATE instance at 0x7ffd527a6d40>}
header_said_need_read 47
134 
 - state of fd: 4
154 
 - current state of fd: 4
155  - - state: read
156  - - have_read: 10
157  - - need_read: 47
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7ffd5213b130>
165  - - popen_pipe:   0
134 
 - state of fd: 5
154 
 - current state of fd: 5
155  - - state: read
156  - - have_read: 10
157  - - need_read: 47
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7ffd5213b1a0>
165  - - popen_pipe:   0
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(135)run()
-> epoll_list = self.epoll_sock.poll()
(Pdb) c
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7ffd52790560>, 5: <nbNet.nbNetUtils.STATE instance at 0x7ffd527a6d40>}
=========d_in start=========
4 === ==fd== 5 ==fd== rpcDispatcher.py
rpc_Server.py
=========d_in end=========

===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7ffd52790560>, 5: <nbNet.nbNetUtils.STATE instance at 0x7ffd527a6d40>}
=========d_in start=========
5 === ==fd== 6 ==fd== rpcDispatcher.py
rpc_Server.py
=========d_in end=========

135 
 - state of fd: 4
154 
 - current state of fd: 4
155  - - state: read
156  - - have_read: 57
157  - - need_read: 0
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  ==fd== 5 ==fd== rpcDispatcher.py
rpc_Server.py

162  - - sock_obj:   <socket._socketobject object at 0x7ffd5213b130>
165  - - popen_pipe:   0
135 
 - state of fd: 5
154 
 - current state of fd: 5
155  - - state: read
156  - - have_read: 57
157  - - need_read: 0
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  ==fd== 6 ==fd== rpcDispatcher.py
rpc_Server.py

162  - - sock_obj:   <socket._socketobject object at 0x7ffd5213b1a0>
165  - - popen_pipe:   0
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(134)run()
-> pdb.set_trace()
(Pdb) c
c
^[[A^[[A^\Quit (core dumped)
>>study:/home/kang/arch-5/rebootMon/dispatch>rz -y
z waiting to receive.**B0100000023be50
>>study:/home/kang/arch-5/rebootMon/dispatch>python rpcDispatcher.py 'ls' 127.0.0.1,127.0.0.1
hosts: ['127.0.0.1', '127.0.0.1']
=======hs=====: 127.0.0.1 ====p==== 9999
=======hs=====: 127.0.0.1 ====p==== 9999
134 
 - state of fd: 4
154 
 - current state of fd: 4
155  - - state: write
156  - - have_read: 0
157  - - need_read: 0
158  - - have_write: 0
159  - - need_write: 12
160  - - buff_write: 0000000002ls
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7f9303570130>
165  - - popen_pipe:   0
134 
 - state of fd: 5
154 
 - current state of fd: 5
155  - - state: write
156  - - have_read: 0
157  - - need_read: 0
158  - - have_write: 0
159  - - need_write: 12
160  - - buff_write: 0000000002ls
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7f93035701a0>
165  - - popen_pipe:   0
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(137)run()
-> epoll_list = self.epoll_sock.poll()
(Pdb) c
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7f9303bd32d8>, 5: <nbNet.nbNetUtils.STATE instance at 0x7f9303bd5560>}
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(64)write2read()
-> try:
(Pdb) c
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7f9303bc50e0>, 5: <nbNet.nbNetUtils.STATE instance at 0x7f9303bd5560>}
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(64)write2read()
-> try:
(Pdb) c
134 
 - state of fd: 4
154 
 - current state of fd: 4
155  - - state: read
156  - - have_read: 0
157  - - need_read: 10
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7f9303570130>
165  - - popen_pipe:   0
134 
 - state of fd: 5
154 
 - current state of fd: 5
155  - - state: read
156  - - have_read: 0
157  - - need_read: 10
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7f93035701a0>
165  - - popen_pipe:   0
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(136)run()
-> pdb.set_trace()
(Pdb) c
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7f9303bc50e0>, 5: <nbNet.nbNetUtils.STATE instance at 0x7f9303bdbd88>}
header_said_need_read 47
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7f9303bc50e0>, 5: <nbNet.nbNetUtils.STATE instance at 0x7f9303bdbd88>}
header_said_need_read 47
136 
 - state of fd: 4
154 
 - current state of fd: 4
155  - - state: read
156  - - have_read: 10
157  - - need_read: 47
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7f9303570130>
165  - - popen_pipe:   0
136 
 - state of fd: 5
154 
 - current state of fd: 5
155  - - state: read
156  - - have_read: 10
157  - - need_read: 47
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7f93035701a0>
165  - - popen_pipe:   0
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(137)run()
-> epoll_list = self.epoll_sock.poll()
(Pdb) c
===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7f9303bc50e0>, 5: <nbNet.nbNetUtils.STATE instance at 0x7f9303bdbd88>}
=========d_in start=========
4 === ==fd== 5 ==fd== rpcDispatcher.py
rpc_Server.py
=========d_in end=========

===self.conn_state:=== {4: <nbNet.nbNetUtils.STATE instance at 0x7f9303bc50e0>, 5: <nbNet.nbNetUtils.STATE instance at 0x7f9303bdbd88>}
=========d_in start=========
5 === ==fd== 6 ==fd== rpcDispatcher.py
rpc_Server.py
=========d_in end=========

137 
 - state of fd: 4
154 
 - current state of fd: 4
155  - - state: closing
156  - - have_read: 57
157  - - need_read: 0
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  ==fd== 5 ==fd== rpcDispatcher.py
rpc_Server.py

162  - - sock_obj:   <socket._socketobject object at 0x7f9303570130>
165  - - popen_pipe:   0
137 
 - state of fd: 5
154 
 - current state of fd: 5
155  - - state: closing
156  - - have_read: 57
157  - - need_read: 0
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  ==fd== 6 ==fd== rpcDispatcher.py
rpc_Server.py

162  - - sock_obj:   <socket._socketobject object at 0x7f93035701a0>
165  - - popen_pipe:   0
> /home/kang/arch-5/rebootMon/dispatch/rpcDispatcher.py(136)run()
-> pdb.set_trace()
(Pdb) c

```
