#output:调优前，原始代码的输出
```SHELL
>>study:/home/kang/arch-5/lession09/nbNet>python -m cProfile -s cumulative ./testQPS.py 
100000 1449823816.14
200000 1449823830.6
300000 1449823845.0
400000 1449823859.56
500000 1449823873.72
600000 1449823887.97
700000 1449823902.28
800000 1449823916.31
900000 1449823930.36
1000000 1449823944.35
1100000 1449823958.69
1200000 1449823973.07
1300000 1449823987.35
1400000 1449824002.03
1500000 1449824016.42
1600000 1449824030.57
1700000 1449824045.29
1800000 1449824059.79
1900000 1449824074.39
2000000 1449824088.53
2100000 1449824102.86
2200000 1449824117.27
2300000 1449824131.73
2400000 1449824146.12
2500000 1449824160.39
2600000 1449824174.83
2700000 1449824189.35
2800000 1449824203.87
2900000 1449824218.15
3000000 1449824232.59
^C         154111753 function calls (154110935 primitive calls) in 447.826 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001  447.826  447.826 testQPS.py:7(<module>)
        1   70.914   70.914  447.746  447.746 nbNetFramework.py:119(run)
  9245661   21.271    0.000  314.466    0.000 nbNetFramework.py:139(state_machine)
  6163774   18.426    0.000  172.767    0.000 nbNetFramework.py:192(read2process)
  3081886   17.087    0.000  120.427    0.000 nbNetFramework.py:219(write2read)
  6163774   56.935    0.000  102.944    0.000 nbNetFramework.py:54(read)
  3081888   24.940    0.000   65.176    0.000 nbNetFramework.py:23(setFd)
  3081887   29.895    0.000   51.397    0.000 nbNetFramework.py:170(process)
  9245661   36.182    0.000   36.182    0.000 {method 'poll' of 'select.epoll' objects}
 36982643   35.472    0.000   35.472    0.000 nbNetUtils.py:147(printState)
  6163783   19.757    0.000   31.591    0.000 socket.py:223(meth)
  3081886   14.655    0.000   29.853    0.000 nbNetFramework.py:100(write)
24658882/24658733   21.674    0.000   21.675    0.000 {len}
  6163774   20.780    0.000   20.780    0.000 {method 'recv' of '_socket.socket' objects}
  6163773   16.473    0.000   16.473    0.000 {method 'modify' of 'select.epoll' objects}
  3081886   12.042    0.000   12.042    0.000 {method 'send' of '_socket.socket' objects}
  9245662    8.920    0.000    8.920    0.000 {method 'iterkeys' of 'dict' objects}
  6163816    6.193    0.000    6.193    0.000 {getattr}
  3081888    5.723    0.000    5.723    0.000 nbNetUtils.py:136(__init__)
  6163779    5.640    0.000    5.640    0.000 {method 'fileno' of '_socket.socket' objects}
  3081887    4.770    0.000    4.770    0.000 testQPS.py:22(logic)
        1    0.002    0.002    0.071    0.071 nbNetFramework.py:8(<module>)
        1    0.001    0.001    0.066    0.066 nbNetUtils.py:8(<module>)
        1    0.001    0.001    0.065    0.065 inspect.py:25(<module>)
        1    0.001    0.001    0.056    0.056 tokenize.py:23(<module>)
        6    0.000    0.000    0.055    0.009 re.py:188(compile)
        6    0.000    0.000    0.055    0.009 re.py:226(_compile)
        6    0.000    0.000    0.055    0.009 sre_compile.py:493(compile)
        7    0.000    0.000    0.053    0.008 {map}
        6    0.000    0.000    0.028    0.005 sre_parse.py:677(parse)
     56/6    0.002    0.000    0.028    0.005 sre_parse.py:301(_parse_sub)
    115/6    0.008    0.000    0.028    0.005 sre_parse.py:379(_parse)
        6    0.000    0.000    0.026    0.004 sre_compile.py:478(_code)
    262/6    0.006    0.000    0.022    0.004 sre_compile.py:32(_compile)
      115    0.001    0.000    0.009    0.000 sre_compile.py:178(_compile_charset)
      735    0.002    0.000    0.007    0.000 sre_parse.py:201(get)
        1    0.007    0.007    0.007    0.007 socket.py:45(<module>)
      115    0.004    0.000    0.007    0.000 sre_compile.py:207(_optimize_charset)
      904    0.004    0.000    0.006    0.000 sre_parse.py:182(__next)
        6    0.004    0.001    0.006    0.001 collections.py:288(namedtuple)
     1185    0.004    0.000    0.006    0.000 sre_parse.py:130(__getitem__)
        6    0.000    0.000    0.005    0.001 sre_compile.py:359(_compile_info)
  377/123    0.003    0.000    0.005    0.000 sre_parse.py:140(getwidth)
     3395    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
      718    0.001    0.000    0.003    0.000 sre_parse.py:195(match)
        1    0.002    0.002    0.002    0.002 pdb.py:3(<module>)
      562    0.001    0.000    0.002    0.000 sre_parse.py:126(__len__)
       25    0.002    0.000    0.002    0.000 sre_compile.py:258(_mk_bitmap)
        1    0.001    0.001    0.002    0.002 collections.py:1(<module>)
     1209    0.002    0.000    0.002    0.000 {isinstance}
      310    0.001    0.000    0.001    0.000 sre_parse.py:138(append)
      117    0.001    0.000    0.001    0.000 sre_compile.py:354(_simple)
      609    0.001    0.000    0.001    0.000 {min}
       30    0.000    0.000    0.001    0.000 {all}
        1    0.000    0.000    0.001    0.001 dis.py:1(<module>)
      244    0.001    0.000    0.001    0.000 collections.py:332(<genexpr>)
        1    0.000    0.000    0.001    0.001 opcode.py:5(<module>)
        1    0.000    0.000    0.001    0.001 repr.py:1(<module>)
      262    0.000    0.000    0.000    0.000 sre_parse.py:90(__init__)
       67    0.000    0.000    0.000    0.000 sre_parse.py:257(_escape)
       31    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
      353    0.000    0.000    0.000    0.000 sre_compile.py:24(_identityfunction)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:181(accept2read)
        1    0.000    0.000    0.000    0.000 daemon.py:8(<module>)
        1    0.000    0.000    0.000    0.000 heapq.py:31(<module>)
        1    0.000    0.000    0.000    0.000 bdb.py:1(<module>)
      285    0.000    0.000    0.000    0.000 {ord}
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:148(__init__)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:32(accept)
      157    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       54    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
      214    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
       38    0.000    0.000    0.000    0.000 sre_parse.py:225(_class_escape)
      117    0.000    0.000    0.000    0.000 sre_parse.py:134(__setitem__)
        1    0.000    0.000    0.000    0.000 socket.py:201(accept)
       38    0.000    0.000    0.000    0.000 sre_parse.py:83(closegroup)
      119    0.000    0.000    0.000    0.000 opcode.py:27(def_op)
        1    0.000    0.000    0.000    0.000 socket.py:235(_fileobject)
       38    0.000    0.000    0.000    0.000 sre_parse.py:72(opengroup)
        1    0.000    0.000    0.000    0.000 os.py:35(_get_exports_list)
       30    0.000    0.000    0.000    0.000 collections.py:358(<genexpr>)
       89    0.000    0.000    0.000    0.000 {max}
        2    0.000    0.000    0.000    0.000 socket.py:185(__init__)
       30    0.000    0.000    0.000    0.000 collections.py:356(<genexpr>)
       91    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <string>:1(Attribute)
        2    0.000    0.000    0.000    0.000 {dir}
       19    0.000    0.000    0.000    0.000 tokenize.py:45(group)
       30    0.000    0.000    0.000    0.000 {time.time}
        1    0.000    0.000    0.000    0.000 token.py:1(<module>)
       11    0.000    0.000    0.000    0.000 opcode.py:31(name_op)
        1    0.000    0.000    0.000    0.000 {method 'accept' of '_socket.socket' objects}
        6    0.000    0.000    0.000    0.000 sre_parse.py:178(__init__)
        1    0.000    0.000    0.000    0.000 socket.py:179(_socketobject)
       38    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
        6    0.000    0.000    0.000    0.000 {_sre.compile}
       29    0.000    0.000    0.000    0.000 {setattr}
       12    0.000    0.000    0.000    0.000 sre_compile.py:472(isstring)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:38(decorated)
        1    0.000    0.000    0.000    0.000 pdb.py:59(Pdb)
       30    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
       26    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        6    0.000    0.000    0.000    0.000 opcode.py:35(jrel_op)
        6    0.000    0.000    0.000    0.000 opcode.py:39(jabs_op)
        1    0.000    0.000    0.000    0.000 pprint.py:35(<module>)
       30    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        2    0.000    0.000    0.000    0.000 {method 'register' of 'select.epoll' objects}
        1    0.000    0.000    0.000    0.000 functools.py:17(update_wrapper)
        6    0.000    0.000    0.000    0.000 {repr}
       11    0.000    0.000    0.000    0.000 {range}
       12    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        1    0.000    0.000    0.000    0.000 cmd.py:46(<module>)
       24    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        7    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 collections.py:26(OrderedDict)
        1    0.000    0.000    0.000    0.000 {method 'bind' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 atexit.py:6(<module>)
        1    0.000    0.000    0.000    0.000 {method 'listen' of '_socket.socket' objects}
        6    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 bdb.py:14(Bdb)
        1    0.000    0.000    0.000    0.000 <string>:1(Traceback)
        1    0.000    0.000    0.000    0.000 posixpath.py:68(join)
        2    0.000    0.000    0.000    0.000 tokenize.py:47(maybe)
        1    0.000    0.000    0.000    0.000 <string>:1(ModuleInfo)
        1    0.000    0.000    0.000    0.000 <string>:1(ArgSpec)
        1    0.000    0.000    0.000    0.000 <string>:1(Arguments)
        6    0.000    0.000    0.000    0.000 {sys._getframe}
        6    0.000    0.000    0.000    0.000 sre_parse.py:67(__init__)
        1    0.000    0.000    0.000    0.000 fnmatch.py:11(<module>)
        1    0.000    0.000    0.000    0.000 cmd.py:55(Cmd)
        1    0.000    0.000    0.000    0.000 keyword.py:11(<module>)
        1    0.000    0.000    0.000    0.000 <string>:1(ArgInfo)
        1    0.000    0.000    0.000    0.000 collections.py:390(Counter)
        1    0.000    0.000    0.000    0.000 {method 'setblocking' of '_socket.socket' objects}
        4    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 tokenize.py:46(any)
        1    0.000    0.000    0.000    0.000 pprint.py:84(PrettyPrinter)
        1    0.000    0.000    0.000    0.000 testQPS.py:18(__init__)
        2    0.000    0.000    0.000    0.000 repr.py:10(__init__)
        1    0.000    0.000    0.000    0.000 functools.py:39(wraps)
        1    0.000    0.000    0.000    0.000 {method 'setsockopt' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 repr.py:8(Repr)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:20(nbNetBase)
        1    0.000    0.000    0.000    0.000 nbNetFramework.py:146(nbNet)
        1    0.000    0.000    0.000    0.000 socket.py:167(_closedsocket)
        1    0.000    0.000    0.000    0.000 tokenize.py:179(Untokenizer)
        1    0.000    0.000    0.000    0.000 inspect.py:632(BlockFinder)
        1    0.000    0.000    0.000    0.000 bdb.py:449(Breakpoint)
        1    0.000    0.000    0.000    0.000 daemon.py:15(Daemon)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:37(timeout)
        1    0.000    0.000    0.000    0.000 inspect.py:630(EndOfBlock)
        1    0.000    0.000    0.000    0.000 testQPS.py:15(MyQPSServer)
        1    0.000    0.000    0.000    0.000 bdb.py:614(Tdb)
        1    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.000    0.000 bdb.py:10(BdbQuit)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:33(TimeoutError)
        1    0.000    0.000    0.000    0.000 pdb.py:18(Restart)
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 nbNetUtils.py:134(STATE)
        1    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {globals}
        1    0.000    0.000    0.000    0.000 tokenize.py:146(TokenError)
        1    0.000    0.000    0.000    0.000 tokenize.py:148(StopTokenizing)
        1    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

```
