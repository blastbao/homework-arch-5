#output：第一次优化，将状态改为元组存储
```SHELL
>>study:/home/kang/arch-5/lession09/nbNet>python -m cProfile -s cumulative ./testQPS.py
100000 1449835124.74
200000 1449835134.91
300000 1449835145.3
400000 1449835155.75
500000 1449835166.03
600000 1449835176.42
700000 1449835186.57
800000 1449835197.2
900000 1449835207.95
1000000 1449835218.77
1100000 1449835229.39
1200000 1449835239.89
1300000 1449835250.5
1400000 1449835261.42
1500000 1449835272.2
1600000 1449835283.28
1700000 1449835293.96
1800000 1449835304.51
1900000 1449835315.11
2000000 1449835326.13
2100000 1449835336.56
2200000 1449835347.46
2300000 1449835358.1
^C         73765614 function calls (73764796 primitive calls) in 249.570 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002  249.570  249.570 testQPS.py:7(<module>)
        1   27.260   27.260  249.490  249.490 nbNetFramework.py:119(run)
  6913896   16.177    0.000  194.238    0.000 nbNetFramework.py:139(state_machine)
  4609264   15.125    0.000  111.421    0.000 nbNetFramework.py:195(read2process)
  2304631   13.906    0.000   66.639    0.000 nbNetFramework.py:222(write2read)
  4609264   34.648    0.000   62.334    0.000 nbNetFramework.py:54(read)
  2304632   20.022    0.000   33.962    0.000 nbNetFramework.py:173(process)
  2304633   12.417    0.000   29.240    0.000 nbNetFramework.py:23(setFd)
  6913896   27.993    0.000   27.993    0.000 {method 'poll' of 'select.epoll' objects}
  2304631    8.227    0.000   17.246    0.000 nbNetFramework.py:100(write)
18440840/18440691   16.481    0.000   16.481    0.000 {len}
  4609264   15.378    0.000   15.378    0.000 {method 'recv' of '_socket.socket' objects}
  4609262   12.409    0.000   12.409    0.000 {method 'modify' of 'select.epoll' objects}
  2304640    7.686    0.000   12.390    0.000 socket.py:223(meth)
  2304631    9.019    0.000    9.019    0.000 {method 'send' of '_socket.socket' objects}
  2304633    4.433    0.000    4.433    0.000 nbNetUtils.py:136(__init__)
  2304632    3.609    0.000    3.609    0.000 testQPS.py:22(logic)
  2304673    2.518    0.000    2.518    0.000 {getattr}
  2304636    2.186    0.000    2.186    0.000 {method 'fileno' of '_socket.socket' objects}
        1    0.003    0.003    0.066    0.066 nbNetFramework.py:8(<module>)
        1    0.001    0.001    0.060    0.060 nbNetUtils.py:8(<module>)
        1    0.001    0.001    0.059    0.059 inspect.py:25(<module>)
        1    0.001    0.001    0.050    0.050 tokenize.py:23(<module>)
        6    0.000    0.000    0.050    0.008 re.py:188(compile)
        6    0.000    0.000    0.050    0.008 re.py:226(_compile)
        6    0.000    0.000    0.049    0.008 sre_compile.py:493(compile)
        7    0.000    0.000    0.047    0.007 {map}
        6    0.000    0.000    0.025    0.004 sre_parse.py:677(parse)
     56/6    0.001    0.000    0.024    0.004 sre_parse.py:301(_parse_sub)
        6    0.000    0.000    0.024    0.004 sre_compile.py:478(_code)
    115/6    0.007    0.000    0.024    0.004 sre_parse.py:379(_parse)
    262/6    0.006    0.000    0.021    0.004 sre_compile.py:32(_compile)
        1    0.012    0.012    0.012    0.012 socket.py:45(<module>)
      115    0.001    0.000    0.009    0.000 sre_compile.py:178(_compile_charset)
      115    0.004    0.000    0.007    0.000 sre_compile.py:207(_optimize_charset)
      735    0.002    0.000    0.006    0.000 sre_parse.py:201(get)
      904    0.004    0.000    0.006    0.000 sre_parse.py:182(__next)
        6    0.003    0.001    0.005    0.001 collections.py:288(namedtuple)
     1185    0.004    0.000    0.005    0.000 sre_parse.py:130(__getitem__)
     3395    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
  377/123    0.002    0.000    0.003    0.000 sre_parse.py:140(getwidth)
        6    0.000    0.000    0.003    0.001 sre_compile.py:359(_compile_info)
        1    0.001    0.001    0.002    0.002 pdb.py:3(<module>)
      718    0.001    0.000    0.002    0.000 sre_parse.py:195(match)
      562    0.001    0.000    0.002    0.000 sre_parse.py:126(__len__)
       25    0.002    0.000    0.002    0.000 sre_compile.py:258(_mk_bitmap)
     1209    0.002    0.000    0.002    0.000 {isinstance}
        1    0.001    0.001    0.002    0.002 collections.py:1(<module>)
      310    0.001    0.000    0.001    0.000 sre_parse.py:138(append)
      117    0.001    0.000    0.001    0.000 sre_compile.py:354(_simple)
       30    0.000    0.000    0.001    0.000 {all}
        1    0.000    0.000    0.001    0.001 dis.py:1(<module>)
      609    0.001    0.000    0.001    0.000 {min}
      244    0.001    0.000    0.001    0.000 collections.py:332(<genexpr>)
        1    0.000    0.000    0.001    0.001 opcode.py:5(<module>)
        1    0.001    0.001    0.001    0.001 repr.py:1(<module>)
      262    0.000    0.000    0.000    0.000 sre_parse.py:90(__init__)
       67    0.000    0.000    0.000    0.000 sre_parse.py:257(_escape)
       31    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 daemon.py:8(<module>)
        1    0.000    0.000    0.000    0.000 heapq.py:31(<module>)
      353    0.000    0.000    0.000    0.000 sre_compile.py:24(_identityfunction)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:184(accept2read)
        1    0.000    0.000    0.000    0.000 bdb.py:1(<module>)
      285    0.000    0.000    0.000    0.000 {ord}
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:32(accept)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:148(__init__)
       54    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
      214    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
      157    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 socket.py:201(accept)
      119    0.000    0.000    0.000    0.000 opcode.py:27(def_op)
       38    0.000    0.000    0.000    0.000 sre_parse.py:225(_class_escape)
        1    0.000    0.000    0.000    0.000 socket.py:235(_fileobject)
       38    0.000    0.000    0.000    0.000 sre_parse.py:83(closegroup)
       30    0.000    0.000    0.000    0.000 collections.py:358(<genexpr>)
       38    0.000    0.000    0.000    0.000 sre_parse.py:72(opengroup)
      117    0.000    0.000    0.000    0.000 sre_parse.py:134(__setitem__)
        1    0.000    0.000    0.000    0.000 os.py:35(_get_exports_list)
        2    0.000    0.000    0.000    0.000 socket.py:185(__init__)
       30    0.000    0.000    0.000    0.000 collections.py:356(<genexpr>)
       91    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       89    0.000    0.000    0.000    0.000 {max}
        2    0.000    0.000    0.000    0.000 {dir}
        1    0.000    0.000    0.000    0.000 <string>:1(Attribute)
        1    0.000    0.000    0.000    0.000 {method 'accept' of '_socket.socket' objects}
       19    0.000    0.000    0.000    0.000 tokenize.py:45(group)
       23    0.000    0.000    0.000    0.000 {time.time}
        1    0.000    0.000    0.000    0.000 socket.py:179(_socketobject)
        1    0.000    0.000    0.000    0.000 token.py:1(<module>)
       11    0.000    0.000    0.000    0.000 opcode.py:31(name_op)
        6    0.000    0.000    0.000    0.000 sre_parse.py:178(__init__)
       38    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
       29    0.000    0.000    0.000    0.000 {setattr}
        6    0.000    0.000    0.000    0.000 {_sre.compile}
       12    0.000    0.000    0.000    0.000 sre_compile.py:472(isstring)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:38(decorated)
        1    0.000    0.000    0.000    0.000 pdb.py:59(Pdb)
       26    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       30    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        6    0.000    0.000    0.000    0.000 opcode.py:35(jrel_op)
        6    0.000    0.000    0.000    0.000 opcode.py:39(jabs_op)
        6    0.000    0.000    0.000    0.000 {repr}
        1    0.000    0.000    0.000    0.000 pprint.py:35(<module>)
       30    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
        1    0.000    0.000    0.000    0.000 functools.py:17(update_wrapper)
       12    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        1    0.000    0.000    0.000    0.000 cmd.py:46(<module>)
       11    0.000    0.000    0.000    0.000 {range}
       24    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        2    0.000    0.000    0.000    0.000 {method 'register' of 'select.epoll' objects}
        1    0.000    0.000    0.000    0.000 atexit.py:6(<module>)
        1    0.000    0.000    0.000    0.000 {method 'bind' of '_socket.socket' objects}
        7    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 collections.py:26(OrderedDict)
        1    0.000    0.000    0.000    0.000 {method 'listen' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 bdb.py:14(Bdb)
        6    0.000    0.000    0.000    0.000 {sys._getframe}
        1    0.000    0.000    0.000    0.000 posixpath.py:68(join)
        6    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <string>:1(Traceback)
        1    0.000    0.000    0.000    0.000 <string>:1(ArgSpec)
        1    0.000    0.000    0.000    0.000 fnmatch.py:11(<module>)
        2    0.000    0.000    0.000    0.000 tokenize.py:47(maybe)
        1    0.000    0.000    0.000    0.000 <string>:1(ModuleInfo)
        1    0.000    0.000    0.000    0.000 <string>:1(Arguments)
        6    0.000    0.000    0.000    0.000 sre_parse.py:67(__init__)
        1    0.000    0.000    0.000    0.000 collections.py:390(Counter)
        1    0.000    0.000    0.000    0.000 cmd.py:55(Cmd)
        1    0.000    0.000    0.000    0.000 <string>:1(ArgInfo)
        4    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 keyword.py:11(<module>)
        1    0.000    0.000    0.000    0.000 {method 'setblocking' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:46(any)
        1    0.000    0.000    0.000    0.000 testQPS.py:18(__init__)
        2    0.000    0.000    0.000    0.000 repr.py:10(__init__)
        1    0.000    0.000    0.000    0.000 {method 'setsockopt' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 repr.py:8(Repr)
        1    0.000    0.000    0.000    0.000 pprint.py:84(PrettyPrinter)
        1    0.000    0.000    0.000    0.000 tokenize.py:179(Untokenizer)
        1    0.000    0.000    0.000    0.000 socket.py:167(_closedsocket)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:20(nbNetBase)
        1    0.000    0.000    0.000    0.000 functools.py:39(wraps)
        1    0.000    0.000    0.000    0.000 bdb.py:449(Breakpoint)
        1    0.000    0.000    0.000    0.000 daemon.py:15(Daemon)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:146(nbNet)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:37(timeout)
        1    0.000    0.000    0.000    0.000 testQPS.py:15(MyQPSServer)
        1    0.000    0.000    0.000    0.000 bdb.py:614(Tdb)
        1    0.000    0.000    0.000    0.000 tokenize.py:148(StopTokenizing)
        1    0.000    0.000    0.000    0.000 bdb.py:10(BdbQuit)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:33(TimeoutError)
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:134(STATE)
        1    0.000    0.000    0.000    0.000 inspect.py:632(BlockFinder)
        1    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 inspect.py:630(EndOfBlock)
        1    0.000    0.000    0.000    0.000 {globals}
        1    0.000    0.000    0.000    0.000 tokenize.py:146(TokenError)
        1    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.000    0.000 pdb.py:18(Restart)
        1    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
