#第11次作业：
1. 分发器改成 状态机实现
2. Paxos算法 python实现
    1. 比如 python dispatcher.py ls host1,host2,host3,host4,host5


##关于作业1：

###相关文件：
1. /nbNet/nbNetFramework.py
2. /nbNet/nbNetUtils.py
3. /dispath/rpc_Server.py
4. /dispath/rpcDiapatcher.py

##思路：

1. 修订原rpc_demo.py为rpc_Server.py，引入tempfile模块，将标准输出重定向到临时文件
2. 关于分发器改造成状态机：
    1. 继承nbNet类
    2. 重写 __init__函数：初始化主动发起类型的 网络连接； 
    3. 重写 setFd函数为initState，覆盖State起始状态为Write，覆盖need_read为0，初始化buff_write为传入的命令值
    4. 重写 write2read函数，在"writecomplete"时，初始化read相关状态，处理远端读取执行命令返回的 拼接数据报文
        1. sock_state.have_read = 0
        2. sock_state.need_read = 10
    5. 重写process函数，仅处理：
        1. 调用logic，打印返回并读取完毕的 数据
        2. 分发完成之后关闭连接 

##存在的问题：

    1. 即使读取完毕后，关闭对应的连接，所有连接都置closing了，分发器也不会退出

###启动服务器:执行命令的rpc server
python rpc_Server.py
###启动分发器:向部署了rpc_Server.py的主机分发命令
rpcDispatcher.py 'ls' 127.0.0.1,127.0.0.1