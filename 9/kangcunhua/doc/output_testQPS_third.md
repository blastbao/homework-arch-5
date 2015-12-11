#output：第三次优化，加入性能分析的输出
```SHELL
>>study:/home/kang/arch-5/lession09/nbNet>python -m cProfile -s cumulative ./testQPS.py
100000 1449846207.64
200000 1449846217.86
300000 1449846228.01
400000 1449846238.63
500000 1449846248.63
600000 1449846258.79
700000 1449846269.2
800000 1449846279.43
900000 1449846289.36
1000000 1449846299.38
1100000 1449846309.29
1200000 1449846319.34
1300000 1449846329.35
1400000 1449846339.26
1500000 1449846349.17
1600000 1449846359.12
1700000 1449846369.04
1800000 1449846378.96
1900000 1449846388.98
2000000 1449846398.9
2100000 1449846408.82
2200000 1449846418.74
2300000 1449846428.77
2400000 1449846438.68
2500000 1449846448.59
2600000 1449846458.99
2700000 1449846468.89
2800000 1449846478.78
2900000 1449846488.71
3000000 1449846498.77
3100000 1449846508.69
3200000 1449846518.6
3300000 1449846528.56
3400000 1449846538.74
3500000 1449846549.05
3600000 1449846559.51
3700000 1449846569.61
3800000 1449846579.63
3900000 1449846589.78
4000000 1449846599.93
4100000 1449846610.13
4200000 1449846620.27
4300000 1449846630.26
4400000 1449846640.14
4500000 1449846650.15
4600000 1449846660.4
4700000 1449846670.7
4800000 1449846680.9
4900000 1449846691.0
5000000 1449846701.32
5100000 1449846711.75
5200000 1449846722.05
5300000 1449846732.39
5400000 1449846742.81
5500000 1449846753.17
5600000 1449846763.36
5700000 1449846773.68
5800000 1449846783.99
5900000 1449846794.41
6000000 1449846804.58
6100000 1449846815.1
6200000 1449846825.28
6300000 1449846835.38
6400000 1449846845.91
6500000 1449846856.21
6600000 1449846866.37
6700000 1449846876.3
6800000 1449846886.46
6900000 1449846896.43
^C         221558657 function calls (221557839 primitive calls) in 704.637 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001  704.637  704.637 testQPS.py:7(<module>)
        1   78.502   78.502  704.553  704.553 nbNetFramework.py:119(run)
 20769490   47.400    0.000  556.980    0.000 nbNetFramework.py:139(state_machine)
 13846326   41.744    0.000  319.768    0.000 nbNetFramework.py:196(read2process)
  6923162   38.639    0.000  189.812    0.000 nbNetFramework.py:223(write2read)
 13846326  100.070    0.000  181.195    0.000 nbNetFramework.py:54(read)
  6923163   56.581    0.000   96.829    0.000 nbNetFramework.py:174(process)
  6923164   35.333    0.000   84.300    0.000 nbNetFramework.py:23(setFd)
 20769490   69.070    0.000   69.070    0.000 {method 'poll' of 'select.epoll' objects}
  6923162   23.145    0.000   48.988    0.000 nbNetFramework.py:100(write)
55389090/55388941   48.274    0.000   48.275    0.000 {len}
 13846326   45.107    0.000   45.107    0.000 {method 'recv' of '_socket.socket' objects}
  6923171   22.673    0.000   36.389    0.000 socket.py:223(meth)
 13846325   35.658    0.000   35.658    0.000 {method 'modify' of 'select.epoll' objects}
  6923162   25.843    0.000   25.843    0.000 {method 'send' of '_socket.socket' objects}
  6923164   12.579    0.000   12.579    0.000 nbNetUtils.py:136(__init__)
  6923163   10.224    0.000   10.224    0.000 testQPS.py:22(logic)
  6923204    7.223    0.000    7.223    0.000 {getattr}
  6923167    6.493    0.000    6.493    0.000 {method 'fileno' of '_socket.socket' objects}
        1    0.003    0.003    0.075    0.075 nbNetFramework.py:8(<module>)
        1    0.001    0.001    0.069    0.069 nbNetUtils.py:8(<module>)
        1    0.002    0.002    0.069    0.069 inspect.py:25(<module>)
        1    0.001    0.001    0.052    0.052 tokenize.py:23(<module>)
        6    0.000    0.000    0.051    0.009 re.py:188(compile)
        6    0.000    0.000    0.051    0.009 re.py:226(_compile)
        6    0.000    0.000    0.051    0.008 sre_compile.py:493(compile)
        7    0.000    0.000    0.047    0.007 {map}
        6    0.000    0.000    0.025    0.004 sre_compile.py:478(_code)
        6    0.000    0.000    0.025    0.004 sre_parse.py:677(parse)
     56/6    0.001    0.000    0.025    0.004 sre_parse.py:301(_parse_sub)
    115/6    0.007    0.000    0.025    0.004 sre_parse.py:379(_parse)
    262/6    0.006    0.000    0.022    0.004 sre_compile.py:32(_compile)
        6    0.007    0.001    0.011    0.002 collections.py:288(namedtuple)
      115    0.001    0.000    0.009    0.000 sre_compile.py:178(_compile_charset)
        1    0.007    0.007    0.007    0.007 socket.py:45(<module>)
      115    0.004    0.000    0.007    0.000 sre_compile.py:207(_optimize_charset)
      735    0.002    0.000    0.007    0.000 sre_parse.py:201(get)
      904    0.004    0.000    0.006    0.000 sre_parse.py:182(__next)
     1185    0.004    0.000    0.005    0.000 sre_parse.py:130(__getitem__)
     3395    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
        6    0.000    0.000    0.003    0.001 sre_compile.py:359(_compile_info)
  377/123    0.002    0.000    0.003    0.000 sre_parse.py:140(getwidth)
        1    0.002    0.002    0.003    0.003 collections.py:1(<module>)
        1    0.001    0.001    0.002    0.002 pdb.py:3(<module>)
      718    0.001    0.000    0.002    0.000 sre_parse.py:195(match)
       30    0.001    0.000    0.002    0.000 {all}
      562    0.001    0.000    0.002    0.000 sre_parse.py:126(__len__)
       25    0.002    0.000    0.002    0.000 sre_compile.py:258(_mk_bitmap)
     1209    0.002    0.000    0.002    0.000 {isinstance}
      244    0.001    0.000    0.001    0.000 collections.py:332(<genexpr>)
      117    0.001    0.000    0.001    0.000 sre_compile.py:354(_simple)
      310    0.001    0.000    0.001    0.000 sre_parse.py:138(append)
        1    0.000    0.000    0.001    0.001 dis.py:1(<module>)
      609    0.001    0.000    0.001    0.000 {min}
       31    0.000    0.000    0.001    0.000 {method 'join' of 'str' objects}
        1    0.001    0.001    0.001    0.001 heapq.py:31(<module>)
        1    0.000    0.000    0.001    0.001 opcode.py:5(<module>)
        1    0.001    0.001    0.001    0.001 repr.py:1(<module>)
      214    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
      262    0.000    0.000    0.000    0.000 sre_parse.py:90(__init__)
       67    0.000    0.000    0.000    0.000 sre_parse.py:257(_escape)
      353    0.000    0.000    0.000    0.000 sre_compile.py:24(_identityfunction)
       54    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:148(__init__)
        1    0.000    0.000    0.000    0.000 daemon.py:8(<module>)
        1    0.000    0.000    0.000    0.000 bdb.py:1(<module>)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:185(accept2read)
      285    0.000    0.000    0.000    0.000 {ord}
       30    0.000    0.000    0.000    0.000 collections.py:358(<genexpr>)
        1    0.000    0.000    0.000    0.000 <string>:1(Attribute)
       30    0.000    0.000    0.000    0.000 collections.py:356(<genexpr>)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:32(accept)
      157    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       38    0.000    0.000    0.000    0.000 sre_parse.py:225(_class_escape)
        2    0.000    0.000    0.000    0.000 socket.py:185(__init__)
        1    0.000    0.000    0.000    0.000 socket.py:201(accept)
        1    0.000    0.000    0.000    0.000 socket.py:235(_fileobject)
      119    0.000    0.000    0.000    0.000 opcode.py:27(def_op)
      117    0.000    0.000    0.000    0.000 sre_parse.py:134(__setitem__)
       69    0.000    0.000    0.000    0.000 {time.time}
       38    0.000    0.000    0.000    0.000 sre_parse.py:83(closegroup)
       38    0.000    0.000    0.000    0.000 sre_parse.py:72(opengroup)
       91    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 os.py:35(_get_exports_list)
       89    0.000    0.000    0.000    0.000 {max}
        2    0.000    0.000    0.000    0.000 {dir}
        6    0.000    0.000    0.000    0.000 {repr}
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       19    0.000    0.000    0.000    0.000 tokenize.py:45(group)
        1    0.000    0.000    0.000    0.000 {method 'accept' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:38(decorated)
        6    0.000    0.000    0.000    0.000 sre_parse.py:178(__init__)
        1    0.000    0.000    0.000    0.000 socket.py:179(_socketobject)
        1    0.000    0.000    0.000    0.000 token.py:1(<module>)
       11    0.000    0.000    0.000    0.000 opcode.py:31(name_op)
        6    0.000    0.000    0.000    0.000 {_sre.compile}
       30    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
       29    0.000    0.000    0.000    0.000 {setattr}
       30    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
        1    0.000    0.000    0.000    0.000 functools.py:17(update_wrapper)
       12    0.000    0.000    0.000    0.000 sre_compile.py:472(isstring)
       38    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
       12    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       24    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 pdb.py:59(Pdb)
       26    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        1    0.000    0.000    0.000    0.000 pprint.py:35(<module>)
        1    0.000    0.000    0.000    0.000 {method 'bind' of '_socket.socket' objects}
        6    0.000    0.000    0.000    0.000 opcode.py:35(jrel_op)
        6    0.000    0.000    0.000    0.000 opcode.py:39(jabs_op)
        2    0.000    0.000    0.000    0.000 {method 'register' of 'select.epoll' objects}
        1    0.000    0.000    0.000    0.000 collections.py:26(OrderedDict)
        6    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        6    0.000    0.000    0.000    0.000 {sys._getframe}
        1    0.000    0.000    0.000    0.000 <string>:1(Traceback)
        1    0.000    0.000    0.000    0.000 cmd.py:46(<module>)
        1    0.000    0.000    0.000    0.000 <string>:1(Arguments)
        1    0.000    0.000    0.000    0.000 <string>:1(ModuleInfo)
        1    0.000    0.000    0.000    0.000 <string>:1(ArgInfo)
        1    0.000    0.000    0.000    0.000 <string>:1(ArgSpec)
       11    0.000    0.000    0.000    0.000 {range}
        1    0.000    0.000    0.000    0.000 {method 'listen' of '_socket.socket' objects}
        7    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 atexit.py:6(<module>)
        1    0.000    0.000    0.000    0.000 keyword.py:11(<module>)
        1    0.000    0.000    0.000    0.000 bdb.py:14(Bdb)
        1    0.000    0.000    0.000    0.000 posixpath.py:68(join)
        6    0.000    0.000    0.000    0.000 sre_parse.py:67(__init__)
        1    0.000    0.000    0.000    0.000 fnmatch.py:11(<module>)
        4    0.000    0.000    0.000    0.000 {hasattr}
        2    0.000    0.000    0.000    0.000 tokenize.py:47(maybe)
        1    0.000    0.000    0.000    0.000 cmd.py:55(Cmd)
        1    0.000    0.000    0.000    0.000 collections.py:390(Counter)
        1    0.000    0.000    0.000    0.000 tokenize.py:46(any)
        1    0.000    0.000    0.000    0.000 testQPS.py:18(__init__)
        1    0.000    0.000    0.000    0.000 pprint.py:84(PrettyPrinter)
        1    0.000    0.000    0.000    0.000 {method 'setblocking' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 {method 'setsockopt' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:20(nbNetBase)
        1    0.000    0.000    0.000    0.000 functools.py:39(wraps)
        2    0.000    0.000    0.000    0.000 repr.py:10(__init__)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:146(nbNet)
        1    0.000    0.000    0.000    0.000 repr.py:8(Repr)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:37(timeout)
        1    0.000    0.000    0.000    0.000 tokenize.py:179(Untokenizer)
        1    0.000    0.000    0.000    0.000 inspect.py:632(BlockFinder)
        1    0.000    0.000    0.000    0.000 inspect.py:630(EndOfBlock)
        1    0.000    0.000    0.000    0.000 testQPS.py:15(MyQPSServer)
        1    0.000    0.000    0.000    0.000 socket.py:167(_closedsocket)
        1    0.000    0.000    0.000    0.000 tokenize.py:146(TokenError)
        1    0.000    0.000    0.000    0.000 tokenize.py:148(StopTokenizing)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:33(TimeoutError)
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:134(STATE)
        1    0.000    0.000    0.000    0.000 bdb.py:449(Breakpoint)
        1    0.000    0.000    0.000    0.000 daemon.py:15(Daemon)
        1    0.000    0.000    0.000    0.000 bdb.py:614(Tdb)
        1    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.000    0.000 bdb.py:10(BdbQuit)
        1    0.000    0.000    0.000    0.000 pdb.py:18(Restart)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 {globals}
        1    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

```

