#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 14:12:53
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

# 抓取豆瓣《请不要害羞》组的帖子照片
# OSChina查的匹配url正则为：  ur'[a-zA-z]+://[^\s]*'
# <td class="title">
#     <a href="http://www.douban.com/group/topic/79221666/" title="【晒黑白调】你瞅啥？" class="">【晒黑白调】你瞅啥？</a>
# </td>
#
# <img src="http://img3.douban.com/view/group_topic/large/public/p35070581.jpg" alt="" class="">
# <img src="http://img3.douban.com/view/group_topic/large/public/p35070591.jpg" alt="" class="">
#
# 如果多页抓取参考http://www.douban.com/group/haixiuzu/discussion?start=0

import re
import urllib2
user_agent = 'Mozilla/8.0 (compatible;MSIE 5.5;Windows NT)'
headers = {'User-Agent': user_agent}

req = urllib2.Request('http://www.douban.com/group/haixiuzu/', '', headers)
response = urllib2.urlopen(req)

html = response.read()
# 需要进行读取
# print html
#
match = re.findall(ur'[a-zA-z]+://[^\s]*/topic/\d{8}', html)

for i in xrange(0, len(match)):
    # print match[i]
    response = urllib2.urlopen(match[i])
    html = response.read()
    matches = re.findall(ur'[a-zA-z]+://[^\s]*/p\d{8}.jpg', html)
    for m in matches:
        with file(m.split("/")[-1], "wb") as f:
            f.write(urllib2.urlopen(m).read())
        # print m


# output：不小心自动补全成了关键字作变量 file-->filter
# Traceback (most recent call last):
# File "D:\PythonHome\Python-arch-5-Lesson\lession03\DoubanCrawler.py", line 40, in <module>
#     with filter(m.split("/")[-1], "w") as f:
# TypeError: 'str' object is not callable
# [Finished in 1.3s with exit code 1]


# output： 被封了
# Traceback (most recent call last):
#   File "D:\PythonHome\Python-arch-5-Lesson\lession03\DoubanCrawler.py", line 16, in <module>
#     'http://www.douban.com/group/haixiuzu/')
#   File "C:\Python27\lib\urllib2.py", line 154, in urlopen
#     return opener.open(url, data, timeout)
#   File "C:\Python27\lib\urllib2.py", line 437, in open
#     response = meth(req, response)
#   File "C:\Python27\lib\urllib2.py", line 550, in http_response
#     'http', request, response, code, msg, hdrs)
#   File "C:\Python27\lib\urllib2.py", line 475, in error
#     return self._call_chain(*args)
#   File "C:\Python27\lib\urllib2.py", line 409, in _call_chain
#     result = func(*args)
#   File "C:\Python27\lib\urllib2.py", line 558, in http_error_default
#     raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
# urllib2.HTTPError: HTTP Error 403: Forbidden
# [Finished in 1.8s with exit code 1]

 # "not fixed E501"
 # 行太长了，超过80字符了
 #
# output：
# http://www.douban.com/group/topic/79785475
# .......
# http://www.douban.com/group/topic/80782574
# http://img3.douban.com/view/group_topic/large/public/p35931675.jpg
# .......
# http://img3.douban.com/view/group_topic/large/public/p37431190.jpg
# [Finished in 94.2s]


# output：居然还有删帖的情况
# http: // www.douban.com/group/topic/79786668
# .......
# http: // www.douban.com/group/topic/80627821
# http: // img3.douban.com/view/group_topic/large/public/p35931675.jpg
# .......
# http: // img4.douban.com/view/group_topic/large/public/p29410208.jpg
# Traceback(most recent call last):
#   File "D:\PythonHome\Python-arch-5-Lesson\lession03\DoubanCrawler.py", line 39, in < module >
#     for i in xrange(0, len(match)):
#   File "C:\Python27\lib\urllib2.py", line 154, in urlopen
#     return opener.open(url, data, timeout)
#   File "C:\Python27\lib\urllib2.py", line 437, in open
#     response = meth(req, response)
#   File "C:\Python27\lib\urllib2.py", line 550, in http_response
#     'http', request, response, code, msg, hdrs)
#   File "C:\Python27\lib\urllib2.py", line 475, in error
#     return self._call_chain(*args)
#   File "C:\Python27\lib\urllib2.py", line 409, in _call_chain
#     result=func(*args)
#   File "C:\Python27\lib\urllib2.py", line 558, in http_error_default
#     raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
# urllib2.HTTPError: HTTP Error 404: Not Found
# [Finished in 244.7s with exit code 1]


# output：终于搞定了彩虹马赛克，感谢 钱禹坤，B4老陶
# http://www.douban.com/group/topic/79785475
# http://www.douban.com/group/topic/80514605
# http://www.douban.com/group/topic/79786668
# http://www.douban.com/group/topic/80591938
# http://www.douban.com/group/topic/80728775
# http://www.douban.com/group/topic/72522805
# http://www.douban.com/group/topic/33751116
# http://www.douban.com/group/topic/77335650
# http://www.douban.com/group/topic/74445636
# http://www.douban.com/group/topic/80810688
# http://www.douban.com/group/topic/80790326
# http://www.douban.com/group/topic/72915314
# http://www.douban.com/group/topic/80813512
# http://www.douban.com/group/topic/80170487
# http://www.douban.com/group/topic/80752756
# http://www.douban.com/group/topic/80813513
# http://www.douban.com/group/topic/71704653
# http://www.douban.com/group/topic/80632939
# http://www.douban.com/group/topic/79978156
# http://www.douban.com/group/topic/80781241
# http://www.douban.com/group/topic/75404590
# http://www.douban.com/group/topic/80812924
# http://www.douban.com/group/topic/80806047
# http://www.douban.com/group/topic/80811992
# http://www.douban.com/group/topic/80640680
# http://www.douban.com/group/topic/80803397
# http://www.douban.com/group/topic/80808902
# http://www.douban.com/group/topic/80698919
# http://www.douban.com/group/topic/73259929
# http://www.douban.com/group/topic/80627821
# http://www.douban.com/group/topic/80812918
# http://www.douban.com/group/topic/80344012
# http://www.douban.com/group/topic/80186611
# http://www.douban.com/group/topic/80701410
# http://www.douban.com/group/topic/80787170
# http://www.douban.com/group/topic/80779816
# http://www.douban.com/group/topic/80809692
# http://www.douban.com/group/topic/80813091
# http://www.douban.com/group/topic/80800880
# http://www.douban.com/group/topic/80789330
# http://www.douban.com/group/topic/80785590
# http://www.douban.com/group/topic/80737824
# http://www.douban.com/group/topic/80812089
# http://www.douban.com/group/topic/79274229
# http://www.douban.com/group/topic/80793781
# http://www.douban.com/group/topic/63602339
# http://www.douban.com/group/topic/80811627
# http://www.douban.com/group/topic/80807759
# http://www.douban.com/group/topic/80812000
# http://www.douban.com/group/topic/80781361
# http://www.douban.com/group/topic/73900259
# http://www.douban.com/group/topic/80729679
# http://www.douban.com/group/topic/74829328
# http://www.douban.com/group/topic/80156419
# http://www.douban.com/group/topic/80782419
# http://www.douban.com/group/topic/80798767
# http://img3.doubanio.com/view/group_topic/large/public/p37049979.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049982.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049984.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049987.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049990.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049993.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049903.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049910.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049913.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049916.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049918.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049920.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049944.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049947.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049951.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049927.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37049929.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049931.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049932.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049933.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049938.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049952.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049955.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049956.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049960.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37049939.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049942.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049962.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049965.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049968.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049973.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049974.jpg
# http://img3.douban.com/view/group_topic/large/public/p37049923.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049926.jpg
# http://img4.douban.com/view/group_topic/large/public/p37049996.jpg
# http://img3.douban.com/view/group_topic/large/public/p35931675.jpg
# http://img4.douban.com/view/group_topic/large/public/p35931798.jpg
# http://img3.douban.com/view/group_topic/large/public/p35931813.jpg
# http://img3.douban.com/view/group_topic/large/public/p35931841.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p35931849.jpg
# http://img3.douban.com/view/group_topic/large/public/p35931891.jpg
# http://img4.douban.com/view/group_topic/large/public/p35931897.jpg
# http://img4.douban.com/view/group_topic/large/public/p37171617.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37171629.jpg
# http://img4.douban.com/view/group_topic/large/public/p37171638.jpg
# http://img4.douban.com/view/group_topic/large/public/p37171658.jpg
# http://img4.douban.com/view/group_topic/large/public/p37171668.jpg
# http://img3.douban.com/view/group_topic/large/public/p37173073.jpg
# http://img3.douban.com/view/group_topic/large/public/p37385111.jpg
# http://img3.douban.com/view/group_topic/large/public/p37385152.jpg
# http://img3.douban.com/view/group_topic/large/public/p37385284.jpg
# http://img4.douban.com/view/group_topic/large/public/p37385326.jpg
# http://img3.douban.com/view/group_topic/large/public/p37385340.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37385369.jpg
# http://img3.douban.com/view/group_topic/large/public/p37385755.jpg
# http://img3.douban.com/view/group_topic/large/public/p27781391.jpg
# http://img3.douban.com/view/group_topic/large/public/p27781441.jpg
# http://img3.douban.com/view/group_topic/large/public/p32393325.jpg
# http://img3.douban.com/view/group_topic/large/public/p32393333.jpg
# http://img3.douban.com/view/group_topic/large/public/p32393351.jpg
# http://img3.douban.com/view/group_topic/large/public/p32393354.jpg
# http://img3.douban.com/view/group_topic/large/public/p32393363.jpg
# http://img3.douban.com/view/group_topic/large/public/p32393371.jpg
# http://img3.douban.com/view/group_topic/large/public/p32393453.jpg
# http://img3.douban.com/view/group_topic/large/public/p37517544.jpg
# http://img4.douban.com/view/group_topic/large/public/p37485916.jpg
# http://img4.douban.com/view/group_topic/large/public/p37518876.jpg
# http://img4.douban.com/view/group_topic/large/public/p37518878.jpg
# http://img3.douban.com/view/group_topic/large/public/p27216962.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p36519279.jpg
# http://img3.douban.com/view/group_topic/large/public/p36519293.jpg
# http://img4.douban.com/view/group_topic/large/public/p36519308.jpg
# http://img3.douban.com/view/group_topic/large/public/p37180580.jpg
# http://img3.douban.com/view/group_topic/large/public/p37424433.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p32989879.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p32989899.jpg
# http://img3.douban.com/view/group_topic/large/public/p32989913.jpg
# http://img4.douban.com/view/group_topic/large/public/p37235207.jpg
# http://img4.douban.com/view/group_topic/large/public/p36197166.jpg
# http://img3.douban.com/view/group_topic/large/public/p37471065.jpg
# http://img3.douban.com/view/group_topic/large/public/p30557094.jpg
# http://img3.douban.com/view/group_topic/large/public/p30722034.jpg
# http://img4.douban.com/view/group_topic/large/public/p30722046.jpg
# http://img4.douban.com/view/group_topic/large/public/p32261148.jpg
# http://img4.douban.com/view/group_topic/large/public/p32401768.jpg
# http://img3.douban.com/view/group_topic/large/public/p32401781.jpg
# http://img3.douban.com/view/group_topic/large/public/p33154253.jpg
# http://img3.douban.com/view/group_topic/large/public/p33927713.jpg
# http://img4.douban.com/view/group_topic/large/public/p34321656.jpg
# http://img4.douban.com/view/group_topic/large/public/p34482486.jpg
# http://img3.douban.com/view/group_topic/large/public/p34682300.jpg
# http://img3.douban.com/view/group_topic/large/public/p34682311.jpg
# http://img3.douban.com/view/group_topic/large/public/p35018971.jpg
# http://img3.douban.com/view/group_topic/large/public/p36039743.jpg
# http://img3.douban.com/view/group_topic/large/public/p36744173.jpg
# http://img4.douban.com/view/group_topic/large/public/p36891448.jpg
# http://img4.douban.com/view/group_topic/large/public/p37147538.jpg
# http://img3.douban.com/view/group_topic/large/public/p37510204.jpg
# http://img3.douban.com/view/group_topic/large/public/p37401430.jpg
# http://img4.douban.com/view/group_topic/large/public/p37401448.jpg
# http://img3.douban.com/view/group_topic/large/public/p37401475.jpg
# http://img3.douban.com/view/group_topic/large/public/p37505972.jpg
# http://img4.douban.com/view/group_topic/large/public/p37505976.jpg
# http://img3.douban.com/view/group_topic/large/public/p37506012.jpg
# http://img3.douban.com/view/group_topic/large/public/p37514995.jpg
# http://img4.douban.com/view/group_topic/large/public/p37514997.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37338899.jpg
# http://img3.douban.com/view/group_topic/large/public/p37338902.jpg
# http://img3.douban.com/view/group_topic/large/public/p37338903.jpg
# http://img3.douban.com/view/group_topic/large/public/p37338905.jpg
# http://img3.douban.com/view/group_topic/large/public/p28012915.jpg
# http://img4.douban.com/view/group_topic/large/public/p28013058.jpg
# http://img3.douban.com/view/group_topic/large/public/p30494242.jpg
# http://img3.douban.com/view/group_topic/large/public/p30494415.jpg
# http://img3.douban.com/view/group_topic/large/public/p30494442.jpg
# http://img3.douban.com/view/group_topic/large/public/p30494471.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p32346729.jpg
# http://img3.douban.com/view/group_topic/large/public/p33887705.jpg
# http://img3.douban.com/view/group_topic/large/public/p34907240.jpg
# http://img3.douban.com/view/group_topic/large/public/p34907263.jpg
# http://img4.douban.com/view/group_topic/large/public/p36781437.jpg
# http://img4.douban.com/view/group_topic/large/public/p36542108.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p36542109.jpg
# http://img3.douban.com/view/group_topic/large/public/p36542110.jpg
# http://img3.douban.com/view/group_topic/large/public/p36542115.jpg
# http://img3.douban.com/view/group_topic/large/public/p36542114.jpg
# http://img3.douban.com/view/group_topic/large/public/p36542113.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p36542119.jpg
# http://img3.douban.com/view/group_topic/large/public/p37342182.jpg
# http://img3.douban.com/view/group_topic/large/public/p37342181.jpg
# http://img3.douban.com/view/group_topic/large/public/p37342183.jpg
# http://img3.douban.com/view/group_topic/large/public/p37342184.jpg
# http://img3.douban.com/view/group_topic/large/public/p37342194.jpg
# http://img3.douban.com/view/group_topic/large/public/p37342185.jpg
# http://img4.douban.com/view/group_topic/large/public/p37342187.jpg
# http://img4.douban.com/view/group_topic/large/public/p37342188.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37342189.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37480699.jpg
# http://img4.douban.com/view/group_topic/large/public/p37469017.jpg
# http://img3.douban.com/view/group_topic/large/public/p37516210.jpg
# http://img3.douban.com/view/group_topic/large/public/p37516215.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37502299.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37506519.jpg
# http://img3.douban.com/view/group_topic/large/public/p37506531.jpg
# http://img3.douban.com/view/group_topic/large/public/p37506540.jpg
# http://img3.douban.com/view/group_topic/large/public/p37478102.jpg
# http://img4.douban.com/view/group_topic/large/public/p37478106.jpg
# http://img4.douban.com/view/group_topic/large/public/p37478107.jpg
# http://img4.douban.com/view/group_topic/large/public/p37478108.jpg
# http://img3.douban.com/view/group_topic/large/public/p37416052.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37416059.jpg
# http://img3.douban.com/view/group_topic/large/public/p37519594.jpg
# http://img3.douban.com/view/group_topic/large/public/p37491014.jpg
# http://img3.douban.com/view/group_topic/large/public/p37491020.jpg
# http://img3.douban.com/view/group_topic/large/public/p29826263.jpg
# http://img4.douban.com/view/group_topic/large/public/p37518477.jpg
# http://img3.douban.com/view/group_topic/large/public/p37518484.jpg
# http://img3.douban.com/view/group_topic/large/public/p37518504.jpg
# http://img3.douban.com/view/group_topic/large/public/p37519402.jpg
# http://img3.douban.com/view/group_topic/large/public/p37471203.jpg
# http://img3.douban.com/view/group_topic/large/public/p37471232.jpg
# http://img3.douban.com/view/group_topic/large/public/p37471233.jpg
# http://img3.douban.com/view/group_topic/large/public/p36843774.jpg
# http://img3.douban.com/view/group_topic/large/public/p36843810.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p36845149.jpg
# http://img4.douban.com/view/group_topic/large/public/p36845166.jpg
# http://img3.douban.com/view/group_topic/large/public/p36845185.jpg
# http://img3.douban.com/view/group_topic/large/public/p36845204.jpg
# http://img3.douban.com/view/group_topic/large/public/p36845592.jpg
# http://img3.douban.com/view/group_topic/large/public/p36845312.jpg
# http://img3.douban.com/view/group_topic/large/public/p36845325.jpg
# http://img4.douban.com/view/group_topic/large/public/p36845366.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p36845379.jpg
# http://img3.douban.com/view/group_topic/large/public/p36956934.jpg
# http://img4.douban.com/view/group_topic/large/public/p36535796.jpg
# http://img4.douban.com/view/group_topic/large/public/p36578316.jpg
# http://img4.douban.com/view/group_topic/large/public/p36578327.jpg
# http://img3.douban.com/view/group_topic/large/public/p36578361.jpg
# http://img3.douban.com/view/group_topic/large/public/p36578371.jpg
# http://img3.douban.com/view/group_topic/large/public/p36578390.jpg
# http://img3.douban.com/view/group_topic/large/public/p36578403.jpg
# http://img4.douban.com/view/group_topic/large/public/p36578427.jpg
# http://img3.douban.com/view/group_topic/large/public/p36578453.jpg
# http://img4.douban.com/view/group_topic/large/public/p36578457.jpg
# http://img3.douban.com/view/group_topic/large/public/p36578482.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p36578489.jpg
# http://img3.douban.com/view/group_topic/large/public/p36578525.jpg
# http://img3.douban.com/view/group_topic/large/public/p36578535.jpg
# http://img4.douban.com/view/group_topic/large/public/p36578548.jpg
# http://img4.douban.com/view/group_topic/large/public/p36578557.jpg
# http://img4.douban.com/view/group_topic/large/public/p36579448.jpg
# http://img3.douban.com/view/group_topic/large/public/p36535440.jpg
# http://img3.douban.com/view/group_topic/large/public/p36535444.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p36535449.jpg
# http://img3.douban.com/view/group_topic/large/public/p36535454.jpg
# http://img3.douban.com/view/group_topic/large/public/p36535462.jpg
# http://img3.douban.com/view/group_topic/large/public/p36535471.jpg
# http://img3.douban.com/view/group_topic/large/public/p36535495.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p36535539.jpg
# http://img3.douban.com/view/group_topic/large/public/p36535545.jpg
# http://img4.douban.com/view/group_topic/large/public/p36535636.jpg
# http://img3.douban.com/view/group_topic/large/public/p36535652.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p36535779.jpg
# http://img3.douban.com/view/group_topic/large/public/p36535784.jpg
# http://img3.douban.com/view/group_topic/large/public/p28285330.jpg
# http://img3.douban.com/view/group_topic/large/public/p28285455.jpg
# http://img3.douban.com/view/group_topic/large/public/p28298103.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p30786309.jpg
# http://img3.douban.com/view/group_topic/large/public/p30786334.jpg
# http://img3.douban.com/view/group_topic/large/public/p30786344.jpg
# http://img3.douban.com/view/group_topic/large/public/p30786364.jpg
# http://img3.douban.com/view/group_topic/large/public/p30786374.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p30786639.jpg
# http://img4.douban.com/view/group_topic/large/public/p30786656.jpg
# http://img3.douban.com/view/group_topic/large/public/p30786675.jpg
# http://img4.douban.com/view/group_topic/large/public/p30786698.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p30786739.jpg
# http://img4.douban.com/view/group_topic/large/public/p30786776.jpg
# http://img3.douban.com/view/group_topic/large/public/p30786802.jpg
# http://img3.douban.com/view/group_topic/large/public/p30786903.jpg
# http://img3.douban.com/view/group_topic/large/public/p30786913.jpg
# http://img4.douban.com/view/group_topic/large/public/p30786928.jpg
# http://img3.douban.com/view/group_topic/large/public/p31277290.jpg
# http://img3.douban.com/view/group_topic/large/public/p37387155.jpg
# http://img3.douban.com/view/group_topic/large/public/p37387162.jpg
# http://img4.douban.com/view/group_topic/large/public/p37387157.jpg
# http://img3.douban.com/view/group_topic/large/public/p37387160.jpg
# http://img4.douban.com/view/group_topic/large/public/p37387156.jpg
# http://img3.douban.com/view/group_topic/large/public/p37387161.jpg
# http://img4.douban.com/view/group_topic/large/public/p37387166.jpg
# http://img3.douban.com/view/group_topic/large/public/p37387165.jpg
# http://img3.douban.com/view/group_topic/large/public/p37387164.jpg
# http://img4.douban.com/view/group_topic/large/public/p37417467.jpg
# http://img3.douban.com/view/group_topic/large/public/p34578353.jpg
# http://img3.douban.com/view/group_topic/large/public/p34578510.jpg
# http://img3.douban.com/view/group_topic/large/public/p34578843.jpg
# http://img3.douban.com/view/group_topic/large/public/p34579005.jpg
# http://img3.douban.com/view/group_topic/large/public/p34579154.jpg
# http://img3.douban.com/view/group_topic/large/public/p34579245.jpg
# http://img3.douban.com/view/group_topic/large/public/p34579431.jpg
# http://img3.douban.com/view/group_topic/large/public/p33283752.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p33284269.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p33284609.jpg
# http://img3.douban.com/view/group_topic/large/public/p33284650.jpg
# http://img3.douban.com/view/group_topic/large/public/p33284822.jpg
# http://img3.douban.com/view/group_topic/large/public/p33285102.jpg
# http://img3.douban.com/view/group_topic/large/public/p33285225.jpg
# http://img4.douban.com/view/group_topic/large/public/p33297436.jpg
# http://img3.douban.com/view/group_topic/large/public/p33098900.jpg
# http://img4.douban.com/view/group_topic/large/public/p33099178.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p33099449.jpg
# http://img3.douban.com/view/group_topic/large/public/p29566881.jpg
# http://img4.douban.com/view/group_topic/large/public/p29567007.jpg
# http://img3.douban.com/view/group_topic/large/public/p29481903.jpg
# http://img3.douban.com/view/group_topic/large/public/p29481942.jpg
# http://img3.douban.com/view/group_topic/large/public/p29389831.jpg
# http://img3.douban.com/view/group_topic/large/public/p29389863.jpg
# http://img4.douban.com/view/group_topic/large/public/p29389868.jpg
# http://img3.douban.com/view/group_topic/large/public/p29389873.jpg
# http://img3.douban.com/view/group_topic/large/public/p29389890.jpg
# http://img3.douban.com/view/group_topic/large/public/p29389905.jpg
# http://img3.douban.com/view/group_topic/large/public/p29389910.jpg
# http://img3.douban.com/view/group_topic/large/public/p29389953.jpg
# http://img4.douban.com/view/group_topic/large/public/p29389956.jpg
# http://img4.douban.com/view/group_topic/large/public/p29389976.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p29389989.jpg
# http://img4.douban.com/view/group_topic/large/public/p29390077.jpg
# http://img4.douban.com/view/group_topic/large/public/p29410058.jpg
# http://img4.douban.com/view/group_topic/large/public/p29410137.jpg
# http://img3.douban.com/view/group_topic/large/public/p29410150.jpg
# http://img4.douban.com/view/group_topic/large/public/p29410208.jpg
# http://img3.douban.com/view/group_topic/large/public/p36498370.jpg
# http://img3.douban.com/view/group_topic/large/public/p37473133.jpg
# http://img4.douban.com/view/group_topic/large/public/p37498858.jpg
# http://img3.douban.com/view/group_topic/large/public/p37498863.jpg
# http://img3.douban.com/view/group_topic/large/public/p37498874.jpg
# http://img3.douban.com/view/group_topic/large/public/p37498881.jpg
# http://img4.douban.com/view/group_topic/large/public/p37498888.jpg
# http://img3.douban.com/view/group_topic/large/public/p37498894.jpg
# http://img3.doubanio.com/view/group_topic/large/public/p37498899.jpg
# http://img3.douban.com/view/group_topic/large/public/p37498905.jpg
# [Finished in 771.1s]
