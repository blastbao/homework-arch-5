#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 10:08:53
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import urllib
import urllib2


url = 'http://jd.com'
user_agent = 'Mozilla/8.0 (compatible;MSIE 5.5;Windows NT)'
values = {
    'name': 'PC',
    'location': '51reboot',
    'language': 'Python'
}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()

# 调试输出
# 因为JD是gbk编码，输出老是报错： 'ascii' codec can't encode characters
# 加上以下三行代码即可搞定

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
print the_page.decode("gbk")


# output：
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="gbk" />
# <title>京东(JD.COM)-综合网购首选-正品低价、品质保障、配送及时、轻松购物！</title>
# <link rel="dns-prefetch" href="//misc.360buyimg.com" />
# <link rel="dns-prefetch" href="//img10.360buyimg.com" />
# <link rel="dns-prefetch" href="//img11.360buyimg.com" />
# <link rel="dns-prefetch" href="//img12.360buyimg.com" />
# <link rel="dns-prefetch" href="//img13.360buyimg.com" />
# <link rel="dns-prefetch" href="//img14.360buyimg.com" />
# <link rel="dns-prefetch" href="//img30.360buyimg.com" />
# <link rel="dns-prefetch" href="//d.3.cn" />
# <link rel="dns-prefetch" href="//d.jd.com" />
# <link rel="icon" href="http://www.jd.com/favicon.ico" mce_href="http://www.jd.com/favicon.ico" type="image/x-icon">
# <meta name="description" content="京东JD.COM-专业的综合网上购物商城,销售家电、数码通讯、电脑、家居百货、服装服饰、母婴、图书、食品等数万个品牌优质商品.便捷、诚信的服务，为您提供愉悦的网上购物体验!">
# <meta name="Keywords" content="网上购物,网上商城,手机,笔记本,电脑,MP3,CD,VCD,DV,相机,数码,配件,手表,存储卡,京东">

# <script type="text/javascript">window.pageConfig = { compatible: true , navId:"jdhome2015" , preload: false , timestamp:1445942532000, surveyLink : 'http://surveys.jd.com/index.php?r=survey/index/sid/889711/newtest/Y/lang/zh-Hans', surveyTitle : '调查问卷'};
# </script>
# <script type="text/javascript">
# (function(w) {
#     var pcm = readCookie('pcm');
#     //var ua  = w.navigator.userAgent;
#     var ua  = w.navigator.userAgent.toLocaleLowerCase();
#     var url = 'http://union.m.jd.com/click/go.action?to=http%3A%2F%2Fm.jd.com%2F&type=1&unionId=pcmtiaozhuan&subunionId=pcmtiaozhuan&keyword=';
#     var matchedRE = /iphone|android|symbianos|windows\sphone/g;
#     function readCookie(name) {
#         var nameEQ = name + "=";
#         var ca = document.cookie.split(';');
#         for (var i = 0; i < ca.length; i++) {
#             var c = ca[i];
#             while (c.charAt(0) == ' ') {
#                 c = c.substring(1, c.length)
#             }
#             if (c.indexOf(nameEQ) == 0) {
#                 return c.substring(nameEQ.length, c.length)
#             }
#         }
#         return null
#     }
#     if ( matchedRE.test(ua) && pcm != '1' ) {
#         w.location.href = url;
#     }
# })(window);
# </script>


#     <style type="text/css" rel="stylesheet">/* jdf-1.0.0/ ui-base.css Date:2015-09-25 09:37:09 */
# a,address,b,big,blockquote,body,center,cite,code,dd,del,div,dl,dt,em,fieldset,font,form,h1,h2,h3,h4,h5,h6,html,i,iframe,img,ins,label,legend,li,ol,p,pre,small,span,strong,u,ul,var{margin:0;padding:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,nav,section,summary{display:block}hr{-moz-box-sizing:content-box;box-sizing:content-box;height:0}button,html input[type=button],input[type=submit]{-webkit-apperance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}ol,ul{list-style:none}img{border:0;vertical-align:middle}em,i,u{font-style:normal}.fl{float:left}.fr{float:right}.al{text-align:left}.ac{text-align:center}.ar{text-align:right}.hide{display:none}.clear,.clr{display:block;overflow:hidden;clear:both;height:0;line-height:0;font-size:0}.clearfix:after{content:".";display:block;height:0;clear:both;visibility:hidden}.clearfix{*zoom:1}.dorpdown{position:relative}.dorpdown-layer{display:none;position:absolute}.dorpdown:hover .dorpdown-layer,.hover .dorpdown-layer{display:block}.cw-icon{position:relative;cursor:default;zoom:1}.cw-icon .i,.cw-icon i{display:block;position:absolute;overflow:hidden}.w{width:990px;margin:0 auto}.root61 .w{width:1210px}body{font:12px/150% Arial,Verdana,"\5b8b\4f53";color:#666;background:#fff}a{color:#666;text-decoration:none}a:hover{color:#C81623}.m,.mb,.mc,.mt,.p-detail,.p-img,.p-market,.p-name,.p-price,.sm,.smb,.smc,.smt{overflow:hidden}.img-error{background:url(//misc.360buyimg.com/lib/skin/e/i/error-jd.gif) no-repeat 50% 50%}
# /* jdf-1.0.0/ shortcut.css Date:2015-09-15 18:39:09 */
# @charset "UTF-8";#shortcut-2014{width:100%;height:30px;line-height:30px;background:#F1F1F1}#shortcut-2014 .w{background:#F1F1F1}#shortcut-2014 li{float:left;height:30px;padding:0 2px}#shortcut-2014 li#ttbar-navs{padding:0 1px 0 2px}#shortcut-2014 li#ttbar-navs.hover,#shortcut-2014 li#ttbar-navs:hover{padding:0 0 0 1px}#shortcut-2014 li.dorpdown{z-index:13}#shortcut-2014 li.dorpdown:hover{padding:0 1px}#shortcut-2014 li.dorpdown:hover .dt{background:#fff;border:solid #ddd;border-width:0 1px}#shortcut-2014 li.hover{padding:0 1px}#shortcut-2014 li.hover .dt{background:#fff;border:solid #ddd;border-width:0 1px}#shortcut-2014 li.spacer{width:1px;height:12px;margin-top:9px;padding:0;background:#ddd;overflow:hidden}#shortcut-2014 .dt{float:left;padding:0 8px}#shortcut-2014 .dd{line-height:24px}#shortcut-2014 .loading{display:block;height:50px;background:url(//misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/loading.gif) no-repeat center center}#shortcut-2014 .dorpdown-layer{top:30px;background:#fff;border:1px solid #ddd;*left:1px}#shortcut-2014 .ci-right{top:12px;right:8px;height:7px;overflow:hidden;font:400 15px/15px consolas;color:#6A6A6A;transition:transform .1s ease-in 0s;-webkit-transition:-webkit-transform .1s ease-in 0s}#shortcut-2014 .ci-right s{position:relative;top:-7px;text-decoration:none}#shortcut-2014 li:hover .ci-right{transform:rotate(180deg);-webkit-transform:rotate(180deg)}#shortcut-2014 .dd-spacer{position:absolute;top:-7px;height:10px;background:#fff;overflow:hidden}#shortcut-2014 .style-red{color:#C81623}#shortcut-2014 #ttbar-home{padding-left:20px;background:url(//misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/jd2015img.png) no-repeat 0 -136px}#shortcut-2014 #ttbar-mycity{padding-left:0}#shortcut-2014 #ttbar-mycity .dt{padding:0 25px 0 10px}#shortcut-2014 #ttbar-mycity:hover .dt{padding:0 24px 0 9px}#shortcut-2014 #ttbar-mycity .dd{width:301px;padding:10px 0 10px 10px}#shortcut-2014 #ttbar-mycity .dorpdown-layer{*left:0}#shortcut-2014 #ttbar-mycity .item{float:left;width:60px;padding:2px 0}#shortcut-2014 #ttbar-mycity .item a{float:left;padding:0 8px}#shortcut-2014 #ttbar-mycity .item a:hover{background:#F4F4F4}#shortcut-2014 #ttbar-mycity .item a.selected{background:#C81623;color:#fff}#shortcut-2014 #ttbar-mycity .dd-spacer{left:0;width:93px;_width:95px}#shortcut-2014 #ttbar-mycity .dd-spacer-extend{width:105px;_width:107px}#shortcut-2014 #ttbar-login{margin-right:10px}#shortcut-2014 #ttbar-login .link-login{font-family:"verdana,瀹嬩綋"}#shortcut-2014 #ttbar-apps .dt{padding-left:25px;padding-right:25px}#shortcut-2014 #ttbar-apps .dt .ci-left{top:5px;left:7px;width:15px;height:20px;background:url(//misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/jd2015img.png) 0 0 no-repeat}#shortcut-2014 #ttbar-apps .dd{width:250px}#shortcut-2014 #ttbar-apps .dd a{display:block;position:absolute;width:56px;height:44px;overflow:hidden;text-indent:-500px}#shortcut-2014 #ttbar-apps .dd .link{width:100px;height:20px;overflow:hidden}#shortcut-2014 #ttbar-apps .dd .link1,#shortcut-2014 #ttbar-apps .dd .link2,#shortcut-2014 #ttbar-apps .dd .link3{left:92px;top:6px;background-position:0 -44px}#shortcut-2014 #ttbar-apps .dd .link2{top:26px}#shortcut-2014 #ttbar-apps .dd .link3{top:104px;background-position:-1px -66px}#shortcut-2014 #ttbar-apps .dd .jdapp-ipad,#shortcut-2014 #ttbar-apps .dd .wyapp-ipad{width:45px}#shortcut-2014 #ttbar-apps .dd-inner{position:relative;width:250px;height:195px;overflow:hidden}#shortcut-2014 #ttbar-apps .jdapp-ios,#shortcut-2014 #ttbar-apps .wyapp-ios{top:46px;left:92px}#shortcut-2014 #ttbar-apps .jdapp-ios:hover,#shortcut-2014 #ttbar-apps .wyapp-ios:hover{background-position:3px -1px}#shortcut-2014 #ttbar-apps .jdapp-android,#shortcut-2014 #ttbar-apps .wyapp-android{top:46px;left:147px}#shortcut-2014 #ttbar-apps .jdapp-android:hover,#shortcut-2014 #ttbar-apps .wyapp-android:hover{background-position:-52px -1px}#shortcut-2014 #ttbar-apps .jdapp-ipad,#shortcut-2014 #ttbar-apps .wyapp-ipad{width:45px;top:46px;left:202px}#shortcut-2014 #ttbar-apps .jdapp-ipad:hover,#shortcut-2014 #ttbar-apps .wyapp-ipad:hover{background-position:-107px -1px}#shortcut-2014 #ttbar-apps .wyapp-android,#shortcut-2014 #ttbar-apps .wyapp-ios,#shortcut-2014 #ttbar-apps .wyapp-ipad{top:143px}#shortcut-2014 #ttbar-apps .dd-spacer{left:0;width:98px}#shortcut-2014 #ttbar-apps.hover .dt .ci-left{background:url(//misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/jd2015img.png) 0 -25px no-repeat}#shortcut-2014 #ttbar-atte .dt,#shortcut-2014 #ttbar-serv .dt{width:49px;padding-right:25px}#shortcut-2014 #ttbar-atte .dd,#shortcut-2014 #ttbar-serv .dd{width:82px;padding-bottom:8px}#shortcut-2014 #ttbar-atte .item,#shortcut-2014 #ttbar-serv .item{padding-left:15px}#shortcut-2014 #ttbar-atte .dd-spacer,#shortcut-2014 #ttbar-serv .dd-spacer{left:0;width:82px}#shortcut-2014 #ttbar-navs .dt{width:49px;padding-right:25px}#shortcut-2014 #ttbar-navs .dd{right:0;width:988px;padding:20px 0 16px;*left:auto;_right:-1px}#shortcut-2014 #ttbar-navs dl{float:left;width:201px;padding-left:20px;border-left:1px solid #ddd}#shortcut-2014 #ttbar-navs dl.fore1{border-left:none;width:301px}#shortcut-2014 #ttbar-navs dt{font-size:14px;font-weight:700;margin-bottom:6px}#shortcut-2014 #ttbar-navs .item{float:left;width:100px}#shortcut-2014 #ttbar-navs .dd-spacer{right:0;width:82px}#shortcut-2014 .hover .dorpdown-layer{-webkit-transition:all 600ms cubic-bezier(0.23,1,.32,1)}.root61 #shortcut-2014 #ttbar-navs .dd{width:1210px}.root61 #shortcut-2014 #ttbar-navs .fore2{display:block}.root61 #shortcut-2014 #ttbar-navs dl{width:259px}.root61 #shortcut-2014 #ttbar-navs dl.fore1{width:347px}.root61 #shortcut-2014 #ttbar-navs .item{width:86px}
# /* jdf-1.0.0/ global-header.css Date:2015-09-15 18:39:12 */
# @charset "UTF-8";#logo-2014{position:relative;z-index:12;float:left;width:362px;height:60px;padding:20px 0}#logo-2014 .logo{display:block;width:270px;height:60px;background:url(//misc.360buyimg.com/lib/img/e/logo-201305.png) no-repeat 0 0;text-indent:-20000px}#logo-2014 .extra{position:absolute;top:15px;left:168px;width:180px;height:70px;padding-left:10px;background:#fff}#channel{float:left;margin-right:10px;cursor:default;font:400 20px/70px "microsoft yahei";color:#333}#categorys-mini-main{display:none;border:1px solid #ccc;position:absolute;width:152px;padding:13px;margin-top:-1px;background:#fff;overflow:hidden}#categorys-mini-main h3{font-family:"Microsoft YaHei";color:#666;line-height:24px;font-size:14px;font-weight:400}#categorys-mini-main a{color:#666;padding:0;font-size:12px}#categorys-mini{float:left;color:#666;font-size:12px;font-weight:400;position:relative;padding-top:22px;height:27px;font-family:simsun}#categorys-mini .cw-icon{color:#ccc;position:relative;width:63px;height:25px;border:1px solid #ccc;line-height:25px;z-index:1;background:#fff;padding:0 5px}#categorys-mini .cw-icon h2{font-family:"Microsoft YaHei";color:#666;font-size:12px;font-weight:400}#categorys-mini .cw-icon i{top:9px;right:5px;height:7px;font:400 15px/15px consolas}#categorys-mini .cw-icon s{position:relative;top:-7px;text-decoration:none}#categorys-mini .loading{display:block;height:50px;background:url(//misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/loading.gif) no-repeat center center}#categorys-mini .dorpdown-layer{width:150px;border:1px solid #ccc;padding:10px;background:#fff}#categorys-mini .ci-right{top:8px;right:7px;height:7px;overflow:hidden;font:400 15px/15px consolas;color:#6A6A6A;transition:transform .1s ease-in 0s;-webkit-transition:-webkit-transform .1s ease-in 0s;display:block;position:absolute}#categorys-mini.hover .cw-icon{border-bottom:0}#categorys-mini.hover .ci-right{transform:rotate(180deg);-webkit-transform:rotate(180deg)}#search-2014{position:relative;z-index:11;float:left;width:462px;margin-top:25px}#search-2014 .form{width:462px;height:36px}#search-2014 .text{float:left;width:370px;height:24px;line-height:24px;color:#666;padding:4px;margin-bottom:4px;border-width:2px 0 2px 2px;border-color:#B61D1D;border-style:solid;outline:0;font-size:14px;font-family:"microsoft yahei"}#search-2014 .button{float:left;width:82px;height:36px;background:#B61D1D;border:none;line-height:1;color:#fff;font-family:"Microsoft YaHei";font-size:16px;cursor:pointer}#search-2014 .cw-icon i{top:0;left:0;width:82px;height:36px}#hotwords-2014{float:left;width:462px;height:20px;line-height:20px;overflow:hidden}#hotwords-2014 a{float:left;white-space:nowrap;margin-right:10px}#shelper{overflow:hidden;position:absolute;top:36px;left:0;width:379px;border:1px solid #CCC;background:#fff}#shelper li{overflow:hidden;padding:1px 6px;line-height:22px;cursor:pointer}#shelper .search-item{float:left;width:190px;white-space:nowrap;text-overflow:ellipsis;overflow:hidden}#shelper li.fore1 .search-item{width:170px}#shelper .search-count{overflow:hidden;color:#aaa;text-align:right;*zoom:1}#shelper .close{border-top:1px solid #efefef;text-align:right}#shelper .item3{cursor:default}#shelper .item3 a{float:left;margin-right:10px;white-space:nowrap}#shelper li.fore1{width:100%;padding:0;border-bottom:1px solid #ddd}#shelper li.fore1 .item1{height:22px;overflow:hidden;zoom:1}#shelper li.fore1 div.fore1{padding:0 6px}#shelper li.fore1 strong{color:#C00}#shelper li.fore1 .fore1 strong{color:#333}#shelper li.fore1 .item1,#shelper li.fore1 .item2{float:none;width:auto;padding:1px 6px 1px 20px}#shelper li.fore1 .item3{float:none;width:auto;color:#9C9A9C}#shelper li.fore1 span{float:left}#shelper li:hover{background:#f5f5f5!important}#shelper li.close:hover,#shelper li.fore1:hover{background:0 0}#shelper li.fore1 div:hover{background:#f5f5f5!important}.root61 #search-2014,.root61 #search-2014 .form{width:auto;_width:538px}.root61 #search-2014 .text{width:446px}.root61 #hotwords-2014{width:518px}.root61 #shelper{width:455px}#appdownloadTop{display:none}
# /* jdf-1.0.0/ myjd.css Date:2015-09-15 18:39:11 */
# @charset "UTF-8";#ttbar-myjd .dt{width:49px;padding-right:25px}#ttbar-myjd .dorpdown-layer{width:270px}#ttbar-myjd .userinfo{padding:10px 15px;overflow:hidden}#ttbar-myjd .u-pic{float:left;margin-right:10px}#ttbar-myjd .u-pic img{border-radius:50%;-moz-border-radius:50%;-webkit-border-radius:50%}#ttbar-myjd .u-name{padding:6px 0 0;font-weight:700}#ttbar-myjd .orderlist{display:none;background:#000}#ttbar-myjd .otherlist{width:255px;padding:0 0 0 15px;margin:5px 0;overflow:hidden;margin-bottom:10px}#ttbar-myjd .otherlist .fore1,#ttbar-myjd .otherlist .fore2{float:left;width:126px}#ttbar-myjd .viewlist{width:240px;padding:0 15px 10px;border-top:1px dotted #ccc;padding-top:10px}#ttbar-myjd .viewlist .smt{zoom:1}#ttbar-myjd .viewlist .smt h4{float:left}#ttbar-myjd .viewlist .smt .extra{float:right}#ttbar-myjd .viewlist .item{float:left;padding:4px;line-height:0;font-size:0}#ttbar-myjd .dd-spacer{left:0;width:82px}#ttbar-myjd .user-level1,#ttbar-myjd .user-level2,#ttbar-myjd .user-level3,#ttbar-myjd .user-level4,#ttbar-myjd .user-level5,#ttbar-myjd .user-level6{display:inline-block;width:17px;height:17px;line-height:17px;vertical-align:middle;margin-left:5px;background:url(//misc.360buyimg.com/jdf/1.0.0/unit/myjd/2.0.0/i/rank2014.gif)}#ttbar-myjd .user-level2{background-position:0 -17px}#ttbar-myjd .user-level3{background-position:0 -34px}#ttbar-myjd .user-level4{background-position:0 -51px}#ttbar-myjd .user-level5{background-position:0 -68px}#ttbar-myjd .user-level6{background-position:0 -85px}
# /* jdf-1.0.0/ nav.css Date:2015-09-15 18:39:10 */
# @charset "UTF-8";#nav-2014{height:44px;border-bottom:2px solid #B1191A;_overflow:hidden}#nav-2014 .w{position:relative;z-index:9;height:44px}#nav-2014 .w .w-spacer{display:none}#nav-2014 .w-spacer{position:absolute;top:-1px;z-index:1;width:100%;height:44px;border-top:1px solid #DDD;border-bottom:2px solid #B1191A}#categorys-2014{float:left;position:relative;z-index:10;width:210px;height:44px;overflow:visible;background:#B1191A}#categorys-2014 .dt a{display:block;width:190px;height:44px;padding:0 10px;background:#B1191A;font:400 15px/44px "microsoft yahei";color:#fff;text-decoration:none}#categorys-2014 .dt s{position:relative;top:-9px;text-decoration:none}#categorys-2014 .dt .ci-right{top:20px;right:7px;height:7px;overflow:hidden;font:700 20px/16px simsun;color:#fff;transition:transform .1s ease-in 0s;-webkit-transition:-webkit-transform .1s ease-in 0s;display:block;position:absolute}#categorys-2014 .dd{height:466px;background:#c81623;margin-top:2px}#categorys-2014 .dd-inner .item{border-left:1px solid #b61d1d;position:relative;z-index:1;height:31px;color:#fff}#categorys-2014 .dd-inner .item a{color:#fff}#categorys-2014 .dd-inner h3{position:absolute;z-index:2;height:31px;padding:0 10px;line-height:31px;font-family:"microsoft yahei";font-size:14px;font-weight:400}#categorys-2014 .dd-inner i{position:absolute;z-index:1;top:9px;right:14px;width:4px;height:14px;font:400 9px/14px consolas}#categorys-2014 .dd-inner .hover{background:#f7f7f7;color:#B61D1D}#categorys-2014 .dd-inner .hover a{color:#B61D1D}#categorys-2014 .dd-inner .hover i{top:0;left:205px;width:14px;height:31px;background:#f7f7f7;overflow:hidden;line-height:200px}#categorys-2014 .dorpdown-layer{display:none;position:absolute;left:209px;top:45px;width:779px;background:#f7f7f7;border:1px solid #b61d1d;overflow:hidden}#categorys-2014 .dorpdown-layer .hover{display:block}#categorys-2014 .item-sub{display:none;zoom:1;overflow:hidden}#categorys-2014 .item-sub:after{content:".";display:block;height:0;clear:both}#categorys-2014 .item-channels{float:left;display:inline;width:570px;height:24px;padding:20px 0 0 20px;background:#f7f7f7;overflow:hidden}#categorys-2014 .item-channels a{float:left;display:inline;display:inline-block;*display:inline;*zoom:1;padding:0 0 0 8px;margin-right:10px;line-height:24px;background:#7C7171;color:#fff;white-space:nowrap}#categorys-2014 .item-channels a:hover{background:#C81623}#categorys-2014 .item-channels a:hover i{background:#B1191A}#categorys-2014 .item-channels i{display:inline-block;*zoom:1;_display:inline;margin-left:8px;width:23px;height:24px;font:400 9px/24px consolas;background:#5c5251;text-align:center;cursor:pointer}#categorys-2014 .item-channels .line{border-left:1px solid #dbdbdb;display:inline;float:left;height:24px;margin-right:7px;width:1px;overflow:hidden}#categorys-2014 .item-channels .img-link{background:0 0;line-height:normal;padding:0}#categorys-2014 .item-channels .img-link:hover{background:0 0}#categorys-2014 .item-channels .style-red{background:#c81623}#categorys-2014 .item-channels .style-red i{background:#b1191a}#categorys-2014 .item-channels .style-red:hover{background:#961019}#categorys-2014 .item-channels .style-red:hover i{background:#851313}#categorys-2014 .subitems{float:left;width:570px;padding:6px 0 1006px 20px;margin-bottom:-1000px;background:#f7f7f7;min-height:409px;_height:409px;_overflow:visible}#categorys-2014 .subitems dl{width:100%;overflow:hidden;line-height:2em}#categorys-2014 .subitems dl.fore1 dd{border-top:none}#categorys-2014 .subitems dt{position:relative;float:left;width:54px;padding:8px 30px 0 0;text-align:right;font-weight:700}#categorys-2014 .subitems dt i{position:absolute;top:13px;right:18px;width:4px;height:14px;font:400 9px/14px consolas}#categorys-2014 .subitems dd{float:left;width:480px;padding:6px 0;border-top:1px solid #eee}#categorys-2014 .subitems dd a{float:left;padding:0 8px;margin:4px 0;line-height:16px;height:16px;border-left:1px solid #e0e0e0;white-space:nowrap}#categorys-2014 .subitems .style-red{color:#c81623}#categorys-2014 .item-brands{float:right;display:inline;width:168px;overflow:hidden;margin:19px 20px 10px 0}#categorys-2014 .item-brands a{float:left;display:inline;margin:1px 0 0 1px}#categorys-2014 .item-promotions{float:right;display:inline;width:168px;margin-right:20px}#categorys-2014 .item-promotions a{display:block;margin-bottom:1px}#nav-2014 .hover .dt .ci-right{transform:rotate(180deg);-webkit-transform:rotate(180deg);_top:17px}#navitems-2014{float:left;position:relative;z-index:2}#navitems-2014 .spacer,#navitems-2014 a,#navitems-2014 li,#navitems-2014 ul{float:left}#navitems-2014 .spacer{display:none}#navitems-2014 a{height:44px;padding:0 20px;text-align:center;text-decoration:none;font:400 15px/44px "microsoft yahei";color:#333}#navitems-2014 a:hover{color:#C81623}#navitems-2014 .spacer{width:1px;height:24px;margin:10px 0 0;background:#DDD;overflow:hidden}#treasure{float:right}.root61 #categorys-2014 .item-channels{width:790px}.root61 #categorys-2014 .dorpdown-layer{width:999px}.root61 #categorys-2014 .subitems{width:790px}.root61 #categorys-2014 .subitems dd{width:620px}.root61 #categorys-2014 .subitems-main1,.root61 #categorys-2014 .subitems-main2{float:left;width:365px;padding-right:10px;margin-right:10px;border-right:1px solid #eee;margin-top:8px}.root61 #categorys-2014 .subitems-main1 dd,.root61 #categorys-2014 .subitems-main2 dd{width:275px}.root61 #categorys-2014 .subitems-main1 .fore1,.root61 #categorys-2014 .subitems-main1 .fore8,.root61 #categorys-2014 .subitems-main2 .fore1,.root61 #categorys-2014 .subitems-main2 .fore8{margin-top:-5px}.root61 #categorys-2014 .subitems-main1 .fore1 dd,.root61 #categorys-2014 .subitems-main1 .fore8 dd,.root61 #categorys-2014 .subitems-main2 .fore1 dd,.root61 #categorys-2014 .subitems-main2 .fore8 dd{border-top:0}.root61 #categorys-2014 .subitems-main2{border-right:0}
# /* jdf-1.0.0/ shoppingcart.css Date:2015-09-15 18:39:10 */
# #settleup-2014{float:right;z-index:11;height:36px;margin-top:25px}#settleup-2014 .cw-icon{width:75px;height:34px;border:1px solid #DFDFDF;padding:0 28px 0 36px;background:#F9F9F9;text-align:center;line-height:34px}#settleup-2014 .ci-left{top:9px;left:18px;width:18px;height:16px;background:url(//misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/jd2015img.png) 0 -58px no-repeat;_background:url(//misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/jd2015img.png) 0 -91px no-repeat}#settleup-2014 .ci-right{top:11px;right:10px;width:7px;height:13px;overflow:hidden;font:400 13px/13px simsun;color:#999}#settleup-2014 .ci-count{position:absolute;top:-4px;left:104px;display:inline-block;*zoom:1;*display:inline;padding:1px 2px;font-size:12px;line-height:12px;color:#fff;background-color:#c81623;border-radius:7px 7px 7px 0;min-width:12px;text-align:center}#settleup-2014.hover .cw-icon,#settleup-2014.hover .dorpdown-layer,#settleup-2014:hover .cw-icon,#settleup-2014:hover .dorpdown-layer{background:#fff;border:1px solid #ddd;box-shadow:0 0 5px rgba(0,0,0,.2)}#settleup-2014.hover .dorpdown-layer,#settleup-2014:hover .dorpdown-layer{display:block;right:0;_right:-1px;width:308px}#settleup-2014.hover .spacer,#settleup-2014:hover .spacer{position:absolute;right:0;top:-7px;width:139px;height:12px;background:#fff}#settleup-2014 .prompt{padding:10px 15px}#settleup-2014 .nogoods{padding-left:30px;height:49px;line-height:49px;overflow:hidden;color:#999}#settleup-2014 .nogoods b{float:left;width:56px;height:49px;background-image:url(//misc.360buyimg.com/jdf/1.0.0/unit/shoppingcart/2.0.0/i/settleup-nogoods.png)}#settleup-content{position:relative;z-index:2;width:100%;background:#fff}#settleup-content .loading{display:block;height:50px;background:url(//misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/loading.gif) no-repeat center center}#settleup-content .smt{height:25px;padding:6px 8px;line-height:25px}#settleup-content .smc{background:#fff;height:auto!important;height:344px;max-height:344px;overflow-y:auto}#settleup-content .smb{padding:8px;background:#F5F5F5;_height:45px;_padding-top:15px;_padding-bottom:0}#settleup-content .smb .p-total{float:left;line-height:29px}#settleup-content .smb span{color:#c81623}#settleup-content .smb a{float:right;height:29px;padding:0 10px;background:#E4393C;color:#fff;text-align:center;font-weight:700;line-height:29px;border-radius:3px;-moz-border-radius:3px;-webkit-border-radius:3px}#settleup-content ul{margin-top:-1px}#settleup-content li{padding:8px 10px;border-top:1px dotted #ccc;overflow:hidden;line-height:17px;vertical-align:bottom;*zoom:1}#settleup-content li.hover,#settleup-content li:hover{background:#F5F5F5}#settleup-content li .gift{height:17px;width:282px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}#settleup-content li .gift a{color:#999}#settleup-content li .gift-jq{color:#999;clear:both}#settleup-content .p-img{float:left;width:50px;height:50px;border:1px solid #ddd;padding:0;margin-right:10px;font-size:0}#settleup-content .p-name{float:left;width:120px;height:52px}#settleup-content .p-detail{float:right;text-align:right}#settleup-content .p-price{font-weight:700}#settleup-iframe{position:absolute;left:0;top:0;z-index:1;width:100%;background:#fff}#settleup-2014 .dt-mz{color:#999;width:310px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}#settleup-2014 .dt-mz a{color:#999}#settleup-2014 .dt-mz:hover{background:#fff}#mcart-suit .dt,#mcart-suit .dt:hover{background:#d3ebff}#mcart-mj .dt,#mcart-mj .dt:hover,#mcart-mz .dt,#mcart-mz .dt:hover{background:#bffab1}#settleup-content .fr .hl-green,#settleup-content .fr .hl-orange{margin-right:0}#settleup-content .hl-green,#settleup-content .hl-orange{margin-right:5px;color:#fff;display:inline-block;*zoom:1;padding:0 2px;font:12px/16px simsun}#settleup-content .hl-green{background:#3b0}#settleup-content .hl-orange{background:#f60}.root61 #settleup-2014{margin-right:65px}#settleup-2014.hover .ci-left{_background:url(//misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/jd2015img.png) 0 -116px no-repeat}
# /* jdf-1.0.0/ global-footer.css Date:2015-09-15 18:39:12 */
# #footer-2014{border-top:1px solid #E5E5E5;padding:20px 0 30px;text-align:center}#footer-2014 .links a{margin:0 10px}#footer-2014 .copyright{margin:10px 0}#footer-2014 .authentication a{margin:0 5px;text-decoration:none}
# /* jdf-1.0.0/ service.css Date:2015-09-25 09:37:10 */
# #service-2014{margin-bottom:20px}#service-2014 dl{float:left;width:222px}#service-2014 dl.fore5{width:100px}#service-2014 dt{padding:6px 0;font:400 16px/24px "microsoft yahei"}#service-2014 dd{line-height:20px}#service-2014 .slogen{position:relative;height:54px;padding:20px 0;margin-bottom:14px;background:#F5F5F5;text-align:center}#service-2014 .slogen .item{display:inline-block;position:absolute;left:50%;top:20px;width:245px;height:54px;text-align:left;vertical-align:middle;font:400 18px/50px "microsoft yahei"}#service-2014 .slogen .item i{display:block;position:absolute;top:0;left:10px;width:220px;height:54px;background-repeat:no-repeat;background-position:0 0}#service-2014 .slogen .item b{padding:0 10px;font-size:24px;color:#C81623}#service-2014 .slogen .fore1{margin-left:-490px}#service-2014 .slogen .fore1 i{background-image:url(//misc.360buyimg.com/jdf/1.0.0/unit/service/1.0.0/i/service_items_1.png)}#service-2014 .slogen .fore2{margin-left:-245px}#service-2014 .slogen .fore2 i{background-image:url(//misc.360buyimg.com/jdf/1.0.0/unit/service/1.0.0/i/service_items_2.png)}#service-2014 .slogen .fore3{margin-left:0}#service-2014 .slogen .fore3 i{background-image:url(//misc.360buyimg.com/jdf/1.0.0/unit/service/1.0.0/i/service_items_3.png)}#service-2014 .slogen .fore4{margin-left:245px}#service-2014 .slogen .fore4 i{background-image:url(//misc.360buyimg.com/jdf/1.0.0/unit/service/1.0.0/i/service_items_4.png)}#coverage{float:right;width:310px;height:168px;background:url(//misc.360buyimg.com/product/skin/2013/i/20130330B_1.png) no-repeat 60px -131px}#coverage .dt{padding:6px 40px 15px 80px;font:400 16px/24px "microsoft yahei"}#coverage .dd{padding:0 40px 15px 80px}.root61 #service-2014 dl{width:275px}.root61 #service-2014 dl.fore5{width:100px}.root61 #service-2014 .slogen .item{width:302px}.root61 #service-2014 .slogen .fore1{margin-left:-604px}.root61 #service-2014 .slogen .fore2{margin-left:-304px}.root61 #service-2014 .slogen .fore3{margin-left:0}.root61 #service-2014 .slogen .fore4{margin-left:304px}
# /* product-home/1.0.0 home.css Date:2015-09-10 17:53:30 */
# @charset "UTF-8";h2,h3{font-family:"microsoft yahei";font-weight:400}#guessyou .mt,#share .mt,#special .mt,#special-buy .mt,.floor .mt{height:36px}#guessyou .mt .extra,#guessyou .mt .tab,#share .mt .extra,#share .mt .tab,#special .mt .extra,#special .mt .tab,#special-buy .mt .extra,#special-buy .mt .tab,.floor .mt .extra,.floor .mt .tab{float:right;display:inline}#guessyou h2,#share h2,#special h2,#special-buy h2,.floor h2{float:left;display:inline;line-height:30px;font-size:20px}.floor .mt .tab{margin-top:1px}.style-red{color:#C81623}.slider-page a{position:absolute;top:50%;margin-top:-31px;z-index:1;display:block;width:28px;height:62px;line-height:62px;background:gray;background:rgba(0,0,0,.2);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#32000000, endColorstr=#32000000);color:#fff;text-align:center;font-size:22px;font-weight:400;font-family:simsun}.slider-page a:hover{text-decoration:none;color:#fff}.slider-prev{left:0}.slider-next{right:0}.slider-nav{position:absolute;height:9px;bottom:10px}.slider-nav ul{line-height:1}.slider-nav li{display:inline-block;*display:inline;*zoom:1;width:9px;height:9px;margin:0 2px;background:#3e3e3e;border-radius:50%;text-align:center;color:#fff;overflow:hidden;cursor:pointer}.slider-nav .slider-selected{background:#b61b1f;color:#fff}.research .icon-dog,.research .research-text{background:url(http://img30.360buyimg.com/da/jfs/t1048/86/726378277/69532/4fe320ba/553f7750Na2b4a167.png);_background:url(http://img12.360buyimg.com/da/jfs/t1072/210/721102876/30886/fd11c510/553f777eNbf9980a4.png)}.research{cursor:pointer;width:31px;height:90px;overflow:hidden;position:fixed;right:0;bottom:200px}.research a{display:block;width:100%;height:90px;overflow:hidden}.research .icon-dog{float:right;display:inline;display:block;width:31px;height:90px;-webkit-transition:width .4s;-moz-transition:width .4s;transition:width .4s}.research .research-text{background-position:-70px 0;position:absolute;left:0;top:0;display:block;*display:none;width:70px;height:70px;filter:alpha(opacity=0);-moz-opacity:0;opacity:0;overflow:hidden;-webkit-transition:opacity .4s;-moz-transition:opacity .4s;transition:opacity .4s}.research .research-text span{color:#fff;position:absolute;left:7px;top:7px;display:none}.researchhover{width:91px}.researchhover .icon-dog{width:46px}.researchhover .research-text{display:block;filter:alpha(opacity=100);-moz-opacity:1;opacity:1}.researchhover .research-text span{display:block}#guide-enter{width:25px;margin-left:15px}#guide-enter a{display:block;width:25px;height:19px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/drag.jpg) center bottom no-repeat;-webkit-transition:all .4s ease-in-out;-moz-transition:all .4s ease-in-out;transition:all .4s ease-in-out}#guide-enter a:hover{height:27px}.guide-floor{position:relative;width:100%;min-width:1210px;height:500px;overflow:hidden}.guide-floor .slider-body{width:100%;min-width:1210px}.guide-floor .slider-body li{width:1210px}.guide-floor .slider-body a{outline:0}.guide-floor .slider-body .slider-inner{position:relative}.guide-floor .slider-body .fore1{width:100%;min-width:1210px;height:500px;background:#d3261f url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/12.jpg) 0 0 repeat-x}.guide-floor .slider-body .fore1 .slider-inner{min-width:1210px;height:400px;background:url(http://img10.360buyimg.com/da/jfs/t520/54/1445679370/146081/4fa1fa2f/54db6fb4Nd56ba02e.jpg) center 0 no-repeat;margin:0 auto;padding-top:100px}.guide-floor .slider-body .fore1 .text{position:relative;width:734px;height:262px;background:url(http://img11.360buyimg.com/da/jfs/t658/258/1413644303/70089/cc06b160/54db6dd6N7629d3df.png) 0 0 no-repeat;margin:0 auto;opacity:0;top:-350px;-webkit-transition:all 1.2s ease-out,opacity 1.5s;-moz-transition:all 1.2s ease-out,opacity 1.5s;transition:all 1.2s ease-out,opacity 1.5s}.guide-floor .slider-body .fore1 .dog1{position:absolute;display:block;width:57px;height:54px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/guideimg.png) 0 -100px no-repeat;left:25px;top:65px}.guide-floor .slider-body .fore1 .dog2{position:absolute;display:block;width:57px;height:67px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/guideimg.png) 0 -170px no-repeat;left:519px;top:48px}.guide-floor .slider-body .fore1 .dog3{position:absolute;display:block;width:41px;height:34px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/guideimg.png) 0 -240px no-repeat;left:301px;top:186px}.guide-floor .slider-body .fore1 .btn-go{width:110px;height:49px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/guideimg.png) 0 0 no-repeat;margin:0 auto;margin-top:20px;-webkit-animation:heartbeat 1.83s ease-in-out infinite;-moz-animation:heartbeat 1.83s ease-in-out infinite;animation:heartbeat 1.83s ease-in-out infinite}.guide-floor .slider-body .fore1 .btn-go a{display:block;width:100%;height:100%;overflow:hidden;text-indent:-9999px}.guide-floor .slider-body .fore1.slider-panel-selected .text{opacity:1;top:0;-webkit-animation:bounce 1.6s ease-out .8s 1;-moz-animation:bounce 1.6s ease-out .8s 1;animation:bounce 1.6s ease-out .8s 1}.guide-floor .slider-body .fore2{width:100%;min-width:1210px;height:500px;background:#f45f4e}.guide-floor .slider-body .fore2 .slider-inner{width:1210px;height:500px;margin:0 auto;overflow:hidden}.guide-floor .slider-body .fore2 .pic{float:left;display:inline;margin:25px 0 0 110px;width:476px;height:426px;opacity:0;left:-350px}.guide-floor .slider-body .fore2 .dogsay{position:absolute;display:block;width:108px;height:94px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/guideimg.png) 0 -290px no-repeat;left:900px;top:337px}.guide-floor .slider-body .select2 .slider-inner{background:url(http://img11.360buyimg.com/da/jfs/t526/156/1134985507/56753/ee2c8306/54db7109Nf44e387a.jpg) center 0 no-repeat}.guide-floor .slider-body .select2 .pic{opacity:1;left:0;background:url(http://img10.360buyimg.com/da/jfs/t667/213/1387474019/70847/ede40e03/54db6db8Nc1f8564b.jpg) 0 0 no-repeat}.guide-floor .slider-body .fore3{width:100%;min-width:1210px;height:500px;background:#f7a043}.guide-floor .slider-body .fore3 .slider-inner{width:1210px;height:500px;margin:0 auto;overflow:hidden}.guide-floor .slider-body .fore3 .pic{float:left;display:inline;margin:120px 0 0 500px;width:662px;height:310px;opacity:0;left:350px}.guide-floor .slider-body .fore3 .dogsay{position:absolute;display:block;width:75px;height:75px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/guideimg.png) 0 -390px no-repeat;left:289px;top:341px}.guide-floor .slider-body .select3 .slider-inner{background:url(http://img12.360buyimg.com/da/jfs/t490/354/1419347762/49242/750f34aa/54db6e29N1b1968ee.jpg) center 0 no-repeat}.guide-floor .slider-body .select3 .pic{opacity:1;left:0;background:url(http://img13.360buyimg.com/da/jfs/t1144/290/6612869/43336/367a509b/54db6e4cNbb3ef5b9.jpg) 0 0 no-repeat}.guide-floor .slider-body .fore4{width:100%;min-width:1210px;height:500px;background:#975bbd}.guide-floor .slider-body .fore4 .slider-inner{width:1210px;height:500px;margin:0 auto;overflow:hidden}.guide-floor .slider-body .fore4 .pic{float:left;display:inline;margin:30px 0 0 120px;width:476px;height:426px;opacity:0;left:-350px}.guide-floor .slider-body .fore4 .dogsay{position:absolute;display:block;width:94px;height:72px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/guideimg.png) 0 -470px no-repeat;left:726px;top:335px}.guide-floor .slider-body .select4 .slider-inner{background:url(http://img14.360buyimg.com/da/jfs/t841/4/8813868/42790/79bd6a61/54db6e67N6d4b301a.jpg) center 0 no-repeat}.guide-floor .slider-body .select4 .pic{opacity:1;left:0;background:url(http://img20.360buyimg.com/da/jfs/t1267/324/8050548/67591/2b891cf/54db6df4N2d9f9e9e.jpg) 0 0 no-repeat}.guide-floor .slider-body .fore5{width:100%;min-width:1210px;height:500px;background:#f45f4e}.guide-floor .slider-body .fore5 .slider-inner{width:1210px;height:500px;margin:0 auto;overflow:hidden}.guide-floor .slider-body .fore5 .pic{float:left;display:inline;margin:70px 0 0 525px;width:600px;height:264px;opacity:0;left:350px}.guide-floor .slider-body .fore5 .btn-go{width:346px;height:108px;margin:0 auto;margin-top:330px;position:relative;left:-50px}.guide-floor .slider-body .fore5 .btn-go a{display:block;width:100%;height:100%;overflow:hidden;text-indent:-9999px}.guide-floor .slider-body .select5 .slider-inner{background:url(http://img30.360buyimg.com/da/jfs/t1144/299/9212180/32061/b0af2cc1/54db6ea3N9be2bf57.jpg) center 0 no-repeat}.guide-floor .slider-body .select5 .pic{opacity:1;left:0;background:url(http://img10.360buyimg.com/da/jfs/t523/85/1425316096/41138/93f35d38/54db6e88N8ee38d15.jpg) 0 0 no-repeat}.guide-floor .slider-body .select5 .btn-go{background:url(http://img12.360buyimg.com/da/jfs/t478/50/1150926890/19141/79ab73f0/54db6ecfNd4772284.jpg) 0 0 no-repeat}.guide-floor .slider-body .pic{position:relative;-webkit-transition:all 1.2s ease-in-out,opacity 1.5s;-moz-transition:all 1.2s ease-in-out,opacity 1.5s;transition:all 1.2s ease-in-out,opacity 1.5s}.guide-floor .slider-body .slider-panel-selected .dogsay{-webkit-animation:tada .8s ease-in-out 1.2s 1;-moz-animation:tada .8s ease-in-out 1.2s 1;animation:tada .8s ease-in-out 1.2s 1}.guide-floor .slider-nav{display:none;width:1210px;height:0;text-align:center;bottom:40px;left:50%;margin-left:-605px;z-index:5;_bottom:30px}.guide-floor .slider-nav ul{height:0}.guide-floor .slider-nav li{background:#666/9;*background:#666/9}.guide-floor .slider-nav .slider-selected{background:#fff}.guide-floor .slider-page{display:none}.guide-floor .slider-page a{left:50%;width:30px;height:30px;line-height:30px;border-radius:50%;font-size:18px;top:auto;bottom:20px;background:0 0;outline:0}.guide-floor .slider-page a:hover{background:rgba(0,0,0,.2)}.guide-floor .slider-page .slider-prev{margin-left:-80px}.guide-floor .slider-page .slider-next{margin-left:50px}.guide-floor .closebtn{position:absolute;left:50%;top:0;margin-left:563px;width:42px;height:39px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/guideimg.png) 0 -60px no-repeat;z-index:6;text-indent:-9999px;overflow:hidden;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/closeguide.png) 0 0 no-repeat}.guide-floor .closebtn:hover{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/home/i/guideimg.png) -50px -60px no-repeat}.guide-floor .slider-body .slider-mainIe .fore1{background:#d3261f url(http://img11.360buyimg.com/da/jfs/t523/89/1476232634/19443/5a618301/54db6ebcNbad3e3af.jpg) 0 0 repeat-x}.guide-floor .slider-body .slider-mainIe .fore1 .slider-inner{background:url(http://img10.360buyimg.com/da/jfs/t484/236/1422063386/150571/5674c286/54db6d23N077d3fd4.jpg) center 0 no-repeat}.guide-floor .slider-body .slider-mainIe .fore1 .btn-go{position:absolute;background:0 0;margin-top:0;top:382px;left:50%;margin-left:-55px}.guide-floor .slider-body .slider-mainIe .select2 .slider-inner{background:url(http://img12.360buyimg.com/da/jfs/t1246/157/6664715/124463/ab4099ca/54db6d6bN740f3651.jpg) center 0 no-repeat}.guide-floor .slider-body .slider-mainIe .select3 .slider-inner{background:url(http://img13.360buyimg.com/da/jfs/t1048/316/8419231/90953/c243ee0/54db6d80N017d824b.jpg) center 0 no-repeat;overflow:hidden}.guide-floor .slider-body .slider-mainIe .select4 .slider-inner{background:url(http://img11.360buyimg.com/da/jfs/t850/93/7201664/60806/a8f08a14/54db6e16Nc2db5cec.jpg) center 0 no-repeat;overflow:hidden}.guide-floor .slider-body .slider-mainIe .select5 .slider-inner{background:url(http://img14.360buyimg.com/da/jfs/t742/36/754396682/88224/2cfcdcbe/54db6da0Nf66aa3e6.jpg) center 0 no-repeat}.guide-floor .slider-body .slider-mainIe .fore5 .btn-go{background:0 0}@-webkit-keyframes heartbeat{from{opacity:.7}50%{opacity:1}to{opacity:.7}}@-moz-keyframes heartbeat{from{opacity:.7}50%{opacity:1}to{opacity:.7}}@keyframes heartbeat{from{opacity:.7}50%{opacity:1}to{opacity:.7}}@-webkit-keyframes tada{0%{-webkit-transform:scale(1);-moz-transform:scale(1);transform:scale(1)}10%,20%{-webkit-transform:scale(0.9) rotate(-3deg);-moz-transform:scale(0.9) rotate(-3deg);transform:scale(0.9) rotate(-3deg)}30%,50%,70%,90%{-webkit-transform:scale(1.2) rotate(3deg);-moz-transform:scale(1.2) rotate(3deg);transform:scale(1.2) rotate(3deg)}40%,60%,80%{-webkit-transform:scale(1.2) rotate(-3deg);-moz-transform:scale(1.2) rotate(-3deg);transform:scale(1.2) rotate(-3deg)}100%{-webkit-transform:scale(1) rotate(0);-moz-transform:scale(1) rotate(0);transform:scale(1) rotate(0)}}@-moz-keyframes tada{0%{-webkit-transform:scale(1);-moz-transform:scale(1);transform:scale(1)}10%,20%{-webkit-transform:scale(0.9) rotate(-3deg);-moz-transform:scale(0.9) rotate(-3deg);transform:scale(0.9) rotate(-3deg)}30%,50%,70%,90%{-webkit-transform:scale(1.2) rotate(3deg);-moz-transform:scale(1.2) rotate(3deg);transform:scale(1.2) rotate(3deg)}40%,60%,80%{-webkit-transform:scale(1.2) rotate(-3deg);-moz-transform:scale(1.2) rotate(-3deg);transform:scale(1.2) rotate(-3deg)}100%{-webkit-transform:scale(1) rotate(0);-moz-transform:scale(1) rotate(0);transform:scale(1) rotate(0)}}@keyframes tada{0%{-webkit-transform:scale(1);-moz-transform:scale(1);transform:scale(1)}10%,20%{-webkit-transform:scale(0.9) rotate(-3deg);-moz-transform:scale(0.9) rotate(-3deg);transform:scale(0.9) rotate(-3deg)}30%,50%,70%,90%{-webkit-transform:scale(1.2) rotate(3deg);-moz-transform:scale(1.2) rotate(3deg);transform:scale(1.2) rotate(3deg)}40%,60%,80%{-webkit-transform:scale(1.2) rotate(-3deg);-moz-transform:scale(1.2) rotate(-3deg);transform:scale(1.2) rotate(-3deg)}100%{-webkit-transform:scale(1) rotate(0);-moz-transform:scale(1) rotate(0);transform:scale(1) rotate(0)}}@-webkit-keyframes bounce{0%,100%,20%,50%,80%{-webkit-transform:translateY(0);-moz-transform:translateY(0);transform:translateY(0)}40%{-webkit-transform:translateY(-30px);-moz-transform:translateY(-30px);transform:translateY(-30px)}60%{-webkit-transform:translateY(-15px);-moz-transform:translateY(-15px);transform:translateY(-15px)}}@-moz-keyframes bounce{0%,100%,20%,50%,80%{-webkit-transform:translateY(0);-moz-transform:translateY(0);transform:translateY(0)}40%{-webkit-transform:translateY(-30px);-moz-transform:translateY(-30px);transform:translateY(-30px)}60%{-webkit-transform:translateY(-15px);-moz-transform:translateY(-15px);transform:translateY(-15px)}}@keyframes bounce{0%,100%,20%,50%,80%{-webkit-transform:translateY(0);-moz-transform:translateY(0);transform:translateY(0)}40%{-webkit-transform:translateY(-30px);-moz-transform:translateY(-30px);transform:translateY(-30px)}60%{-webkit-transform:translateY(-15px);-moz-transform:translateY(-15px);transform:translateY(-15px)}}#service-2014 dl{width:144px}.root61 #service-2014 dl{width:199px}.navitems-on{position:relative;background:url(http://img20.360buyimg.com/da/jfs/t1312/142/343086215/1737/de4ffd0f/55682432N00b40271.jpg) no-repeat right 1px}
# /* product-home/1.0.0 floor.css Date:2015-03-19 19:37:12 */
# .floor{margin-bottom:30px}.floor .mt{*width:990px;*position:relative;border-bottom:1px solid #c81623;overflow:visible;_zoom:1;position:relative}.floor img{vertical-align:top}.floor h2{position:relative;padding-left:40px;color:#333}.floor h2 i{position:absolute;top:2px;left:0;width:21px;height:25px;padding-right:10px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/floor/i/floor1new.png) no-repeat 0 0;font-size:13px;color:#fff;text-align:center;overflow:hidden}.floor .tab{border:solid 1px #ededed;border-bottom:0 none;height:34px;line-height:34px;z-index:1}.floor .tab-item{float:left;display:inline;height:34px;position:relative;z-index:2}.floor .tab-item a{float:left;height:34px;padding:0 16px;text-decoration:none;line-height:34px;overflow:hidden;background:#fff;border-left:solid 1px #fff;border-right:solid 1px #fff;white-space:nowrap}.floor .tab-item span{position:absolute;width:1px;background:#ccc;overflow:hidden;height:14px;top:10px;right:0}.floor .tab-selected a{position:absolute;white-space:nowrap;border-left:solid 1px #c81623;border-right:solid 1px #c81623;border-top:solid 3px #c81623;top:-1px;left:-1px;height:33px;line-height:30px;color:#c81623;text-indent:1px}.floor .tab-selected span{display:none}.floor .m{_width:990px}.floor .mc{_width:1000px}.floor .side{float:left;width:330px;overflow:hidden;font-family:"microsoft yahei"}.floor .side-inner{position:relative;width:330px;background:#e5ebeb;overflow:hidden}.floor .banner{position:relative;height:474px}.floor .banner a{display:block;height:475px}.floor .themes{position:relative;padding-left:10px;height:92px;margin-top:-237px;overflow:hidden;background:rgba(255,255,255,.5);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#88FFFFFF, endColorstr=#88FFFFFF)}.floor .assists{position:relative;height:48px;padding:21px 0 0;font-size:14px;line-height:24px;overflow:hidden;background:rgba(255,255,255,.7);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#BBFFFFFF, endColorstr=#BBFFFFFF)}.floor .assists li{float:left;width:180px;height:24px;padding-left:25px;overflow:hidden}.floor .assists li a{white-space:nowrap}.floor .words{position:relative;height:76px;background:rgba(255,255,255,.7);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#BBFFFFFF, endColorstr=#BBFFFFFF);font-family:\5b8b\4f53}.floor .words li{float:left;width:135px;height:48px;padding:7px 0 0 25px;overflow:hidden}.floor .words a{float:left;margin-right:10px;line-height:24px;white-space:nowrap}.floor .words a:link,.floor .words a:visited{color:#999}.floor .words a:hover{color:#C81623}.floor .themes li{float:left;width:98px;height:26px;padding:10px 0}.floor .themes a{float:left}.floor .themes a:hover .icon{-webkit-animation:flip .2s ease;-moz-animation:flip .2s ease}.floor .themes i,.floor .themes span{float:left;height:26px;overflow:hidden;line-height:26px}.floor .themes span{font-size:14px;margin-right:5px}.floor .themes .icon{width:26px;margin-right:5px}.floor .themes .arrow{font-family:simsun}.floor .main{position:relative;float:left;width:660px;height:474px;overflow:hidden}.floor .main-inner li{width:220px;overflow:hidden;font-size:0}.floor .main-inner a{display:block;border-right:1px solid #EDEDED;border-bottom:1px solid #EDEDED;overflow:hidden}.floor .main-body{float:left;width:660px}.floor .main-extra{display:none;float:left;width:220px}.floor .slider{position:absolute;top:0;left:0;width:439px;height:236px;overflow:hidden;border-right:1px solid #EDEDED;border-bottom:1px solid #EDEDED}.floor .slider .slider-item{border:none}.floor .slider .slider-nav{width:100%;height:0;line-height:0;text-align:center;bottom:19px;cursor:default}.floor .slider .slider-nav ul{height:0;line-height:0}.floor .slider .slider-nav li{display:inline-block;*display:inline;*zoom:1}.floor .slider .slider-page{display:none}.floor .slider .slider-page a{border:none}.floor .p-list{width:670px;height:474px;overflow:hidden}.floor .p-list li{float:left;width:160px;height:230px;padding:6px 17px 0;border-bottom:1px solid #ededed;border-right:1px solid #ededed;overflow:hidden}.floor .p-list .p-img{height:140px;margin-bottom:4px;text-align:center;padding-top:15px}.floor .p-list .p-name{height:3em;margin-bottom:3px}.floor .p-list .p-price{font-size:15px;font-family:Verdana;color:#E4393C}.floor .img-list{width:670px;height:159px;overflow:hidden}.floor .img-list li{float:left;width:219px;height:158px;border-bottom:1px solid #ededed;border-right:1px solid #ededed}.floor-current h2 i{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/floor/i/sprite_floor.png?__sprite) no-repeat 0 0;background-position:0 0}.floor-current h2:before{content:"";position:absolute;top:2px;left:0;width:31px;height:25px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/floor/i/sprite_floor.png?__sprite) no-repeat 0 0;background-position:0 -35px}.floor-current h2 i{-webkit-animation-name:scaleDisc;-moz-animation-name:scaleDisc;animation-name:scaleDisc;-webkit-animation-duration:1s;-moz-animation-duration:1s;animation-duration:1s}@-webkit-keyframes scaleDisc{0%{opacity:0;height:0}100%{opacity:1;height:25px}}@-moz-keyframes scaleDisc{0%{opacity:0;height:0}100%{opacity:1;height:25px}}@keyframes scaleDisc{0%{opacity:0;height:0}100%{opacity:1;height:25px}}#babys .side,#babys .side-inner,#books .side,#books .side-inner,#cosmetics .side,#cosmetics .side-inner,#foods .side,#foods .side-inner,#life .side,#life .side-inner,#livings .side,#livings .side-inner,#sports .side,#sports .side-inner{width:210px}#babys .main,#books .main,#cosmetics .main,#foods .main,#livings .main,#sports .main{width:780px}#babys .p-list,#books .p-list,#cosmetics .p-list,#foods .p-list,#livings .p-list,#sports .p-list{width:790px}#digitals .assists li,#electronics .assists li,#mobiles .assists li{width:135px}.floor #babys .words li,.floor #books .words li,.floor #cosmetics .words li,.floor #foods .words li,.floor #life .words li,.floor #livings .words li,.floor #sports .words li{width:165px}.root61 .floor .m{_width:1210px}.root61 .floor .mt{*width:1210px}.root61 .floor .mc{_width:1220px}.root61 .floor .main{width:880px}.root61 .floor .p-list{width:890px}.root61 .floor .p-list li{width:165px}.root61 .floor .img-list{width:890px}.root61 .floor .main-extra{display:block}.root61 #babys .main,.root61 #books .main,.root61 #cosmetics .main,.root61 #foods .main,.root61 #livings .main,.root61 #sports .main{width:1000px}.root61 #babys .p-list,.root61 #books .p-list,.root61 #cosmetics .p-list,.root61 #foods .p-list,.root61 #livings .p-list,.root61 #sports .p-list{width:1010px}.root61 #books .slider{left:220px}.lazy-fn{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/floor/i/loading.gif) no-repeat center center}.lazy-fn-done{background:0 0}.floor-banner-body{height:140px;margin:0 auto;width:990px}.root61 .floor-banner-body{width:1210px}#lazy-todays{height:184px}#lazy-guess-like{height:289px}#lazy-features-purchase{height:390px}#lazy-clothes{height:737px}#lazy-cosmetics,#lazy-digitals,#lazy-electronics,#lazy-mobiles{height:578px}#lazy-life,#lazy-livings,#lazy-sports{height:577px}#lazy-babys,#lazy-foods{height:578px}#lazy-books{height:577px}#lazy-special{height:339px}#lazy-footer{height:457px}
# /* product-home/1.0.0 animation-index.css Date:2015-03-13 14:34:22 */
# @-webkit-keyframes rotate{0%{-webkit-transform:rotate(0deg)}100%,25%,50%,75%{-webkit-transform:rotate(360deg)}}@-moz-keyframes rotate{0%{-moz-transform:rotate(0deg)}100%,25%,50%,75%{-moz-transform:rotate(360deg)}}@keyframes rotate{0%{transform:rotate(0deg)}100%,25%,50%,75%{transform:rotate(360deg)}}@-webkit-keyframes rotate-all{0%{-webkit-transform:rotate(0deg)}100%{-webkit-transform:rotate(360deg)}}@-moz-keyframes rotate-all{0%{-moz-transform:rotate(0deg)}100%{-moz-transform:rotate(360deg)}}@keyframes rotate-all{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}@-webkit-keyframes nav-slide{0%{-webkit-transform:translateX(-11px)}100%,50%,70%{-webkit-transform:translateX(0px)}}@-moz-keyframes nav-slide{0%{-moz-transform:translateX(-11px)}100%,50%,70%{-moz-transform:translateX(0px)}}@keyframes nav-slide{0%{transform:translateX(-11px)}100%,50%,70%{transform:translateX(0px)}}.floor .banner a:before{content:"";position:absolute;width:80px;height:350px;top:0;left:-150px;overflow:hidden;background:-moz-linear-gradient(left,rgba(255,255,255,0)0,rgba(255,255,255,.2)50%,rgba(255,255,255,0)100%);background:-webkit-gradient(linear,left top,right top,color-stop(0%,rgba(255,255,255,0)),color-stop(50%,rgba(255,255,255,.2)),color-stop(100%,rgba(255,255,255,0)));background:-webkit-linear-gradient(left,rgba(255,255,255,0)0,rgba(255,255,255,.2)50%,rgba(255,255,255,0)100%);background:-o-linear-gradient(left,rgba(255,255,255,0)0,rgba(255,255,255,.2)50%,rgba(255,255,255,0)100%);-webkit-transform:skewX(-25deg);-moz-transform:skewX(-25deg)}.floor .banner a:hover::before{-webkit-transition:left 1s;-moz-transition:left 1s;transition:left 1s;left:260px}#clothes .banner a:hover::before,#digitals .banner a:hover::before,#electronics .banner a:hover::before,#mobiles .banner a:hover::before{-webkit-transition:left 1s;-moz-transition:left 1s;transition:left 1s;left:460px}@-webkit-keyframes tick-tock{to{-webkit-transform:rotate(360deg) translate3d(0,0,0)}}.jd-clock-wrap{position:relative;width:210px;height:151px;background:url(http://misc.360buyimg.com/product/home/1.0.0/css/i/homebg.png) 0 -136px no-repeat}.jd-clock{position:absolute;left:72px;top:31px;width:43px;height:43px;border-radius:50%;border:7px solid #fff}.jd-clock::before{content:"";position:absolute;left:18px;top:18px;width:7px;height:7px;border-radius:50%;background:#fff}.jd-clock .jd-clock-h{position:absolute;top:5px;left:19px;height:19px;width:5px;background-color:#fff;border-radius:2px;transform:rotate(10deg);-webkit-transform-origin:2.5px 16.5px;-moz-transform-origin:2.5px 16.5px;transform-origin:2.5px 16.5px}.jd-clock .jd-clock-m{position:absolute;left:5px;top:19px;width:19px;height:5px;background:0 0;border-radius:2px}.jd-clock .jd-clock-m::after{content:"";position:absolute;left:14px;top:-17px;width:5px;height:21px;background-color:#fff;border-radius:2px;-webkit-transform-origin:2.5px 19.5px;-webkit-animation:tick-tock 20s steps(60,end) infinite;-moz-transform-origin:2.5px 19.5px;-moz-animation:tick-tock 20s steps(60,end) infinite;transform-origin:2.5px 19.5px;animation:tick-tock 20s steps(60,end) infinite}.jd-clock .jd-clock-s{position:absolute;left:19px;top:-6px;width:5px;height:28px;-webkit-transform-origin:bottom;-webkit-animation:tick-tock 10s linear infinite;-moz-transform-origin:bottom;-moz-animation:tick-tock 10s linear infinite;transform-origin:bottom;animation:tick-tock 10s linear infinite}.jd-clock .jd-clock-s::after{content:"";position:absolute;left:0;top:0;width:5px;height:5px;background-color:#5e5252;border-radius:50%}@-moz-keyframes tick-tock{to{-moz-transform:rotate(360deg) translate3d(0,0,0)}}
# /* product-home/1.0.0 elevator.css Date:2015-02-06 18:02:42 */
# .elevator{width:30px;overflow:hidden;display:none}.elevator ul{overflow:hidden;background-color:rgba(255,255,255,.8);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#ccffffff, endColorstr=#ccffffff)}.elevator li{width:30px;height:30px;line-height:30px;text-align:center;overflow:hidden;margin-top:-1px;cursor:pointer}.elevator li a{display:block;width:30px;height:30px;margin:0 auto;color:#625351;font-size:14px;font-family:Arial;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAMAAAAM7l6QAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA2xpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpFNDg5NURBNDY3MjA2ODExODIyQUVDNTgwRDU1MkZBQiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo1N0M3MTMzQTlBRTQxMUU0OEY2QkNDMkMzNDJCRDdGNiIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo1N0M3MTMzOTlBRTQxMUU0OEY2QkNDMkMzNDJCRDdGNiIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M2IChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6ODBkOTE3NzktZTE1Yi0yNTRkLTljYzMtOGVjNmE4ZTAyMjRjIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjIxNzkxODUyODJEQjExRTQ4RkM0REQwQTBFRkQyNTY2Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+3tRxHgAAAAlQTFRFwsLCycnJ////r0pOrgAAAAN0Uk5T//8A18oNQQAAAB5JREFUeNpiYIIABhTIyAQXxgtGpUelR6VpKw0QYACUOgb65Nz92gAAAABJRU5ErkJggg==) 0 0 no-repeat;*background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/elevator/i/dot.png) 0 0 no-repeat}.elevator li a:hover{color:#fff;text-decoration:none;background:#c81623}.elevator li .etitle{display:none;width:30px;height:30px;color:#fff;font-size:12px}.elevator li.current a{display:none}.elevator li.current .etitle{display:block;color:#c81623}.elevator li.current .etitle:hover{color:#fff}.elevator li.hover a,.elevator li:hover a{display:none}.elevator li.hover .etitle,.elevator li:hover .etitle{display:block;color:#fff}
# /* product-home/1.0.0 go-top.css Date:2015-02-06 18:02:42 */
# .go-top{width:42px;overflow:hidden}.go-top li{float:left;display:inline;width:42px;line-height:33px;cursor:pointer}.go-top li .link-survey{border-top:1px dotted #fff;cursor:pointer;background:#ccc}.go-top li .link-survey:hover{background:#c81623;cursor:pointer}.go-top li .icon-survey{display:block;width:42px;height:33px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAhCAMAAACY2smqAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA21pVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDphYmZiZTQyYi00ZmZmLWI0NGQtOTg2Mi1iNTAwZjQ5OWEwYTkiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MERGRTYwNDQ4NTk1MTFFNDg4QzNCM0UyMTFBQUQzMjIiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MERGRTYwNDM4NTk1MTFFNDg4QzNCM0UyMTFBQUQzMjIiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjliZTU4MWQyLWUyZmQtMTY0OS05ZDQ1LWE1ZWQ2MzNkZTYwNSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo0OTQ2REVGRTg1OTIxMUU0OTJEOUY1RjRBRDY2RTU5MSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PtQqlGgAAAAGUExURfn5+f///ykOvA0AAAACdFJOU/8A5bcwSgAAAERJREFUeNrs0zsKACAMBNHx/pe2FkfYVCokZXhFvow4aPoqJaZASE06VanUpZYPYacnWRjKlidfAdy9AZboh/mXTgEGAKgXBUYYHMVSAAAAAElFTkSuQmCC) 0 0 no-repeat;*background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/go-top/i/icon-survey.png) 0 0 no-repeat}.go-top li .icon-survey-text{display:none}.go-top li a{display:block;overflow:hidden;text-align:center;color:#fff}.go-top li a:hover{background:#c81623;text-decoration:none}.go-top li a:hover .icon-survey{display:none}.go-top li a:hover .icon-survey-text{display:block;color:#fff;cursor:pointer}.go-top li.item{width:42px;line-height:42px}.go-top li.item .icon-top{display:block;width:42px;height:5px;line-height:12px;overflow:hidden;padding-top:18px;font-family:"\5b8b\4f53"}.go-top li.item .text-top{display:none}.go-top li.item a{background:#999;display:block;width:42px;height:42px;overflow:hidden;text-align:center;color:#fff}.go-top li.item a:hover{background:#c81623;text-decoration:none}.go-top li.item a:hover .icon-top{display:none}.go-top li.item a:hover .text-top{display:block;color:#fff;cursor:pointer}
# /* product-home/1.0.0 focus.css Date:2015-04-07 15:15:43 */
# #lifeserv,#news{position:absolute;right:0;padding:0;background:rgba(255,255,255,.85);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#BBFFFFFF, endColorstr=#BBFFFFFF)}#lifeserv .mt,#news .mt{padding:0 15px;border-bottom:1px dotted #E8E8E7;height:43px;line-height:43px}#lifeserv h2,#news h2{font-size:16px}#focus{position:relative}#focus .slider{height:466px}#focus .slider-panel{width:100%;height:466px}#focus .slider-panel .inner{width:990px;margin:0 auto;height:466px;overflow:hidden}#focus .slider-panel a{display:block;overflow:hidden;zoom:1;width:510px;margin:12px 250px 0 220px;height:454px}#focus .slider-extra{position:relative;width:990px;height:466px;margin:0 auto}#focus .slider-page-main{position:absolute;z-index:3;left:210px;width:530px;height:466px}#focus .slider-nav,#focus .slider-next,#focus .slider-prev{position:absolute;z-index:4}#focus .slider-nav{top:440px;width:530px;height:0;line-height:0;left:210px;text-align:center}#focus .slider-nav li{width:18px;height:18px;line-height:18px;display:inline-block;*display:inline;*zoom:1}#focus .slider-prev{left:220px}#focus .slider-next{right:260px}.root61 #focus .slider-nav{width:750px}#focus-extra{position:relative;z-index:8;top:-466px}#focus-extra h2{float:left}#focus-extra .mt .extra{float:right;font-family:consolas}.root61 #focus .slider-panel a{width:730px}.root61 #focus .slider-extra,.root61 #focus .slider-panel .inner{width:1210px}.root61 #focus .slider-page-main{width:750px}
# /* product-home/1.0.0 news.css Date:2015-03-19 19:37:12 */
# #news{height:200px;width:248px;overflow:hidden;top:12px;border:solid 1px #e4e4e4;border-bottom:0}#news .mc{height:140px;padding:8px 0 0 15px}#news li{width:210px;height:27px;line-height:27px;overflow:hidden}#news li span{font-weight:700;margin-right:5px}
# /* product-home/1.0.0 lifeserv.css Date:2015-03-19 19:37:12 */
# @-webkit-keyframes toRightFromLeft{50%{opacity:0;-webkit-transform:translate(-50%)}51%{opacity:1}}@-moz-keyframes toRightFromLeft{50%{opacity:0;-moz-transform:translate(-50%)}51%{opacity:1}}#lifeserv{top:213px;border:solid 1px #e4e4e4;border-top:dashed 1px #e4e4e4;overflow:hidden;width:248px}#lifeserv .mc{height:208px;position:relative}#lifeserv ul{position:relative;width:260px;height:209px;overflow:hidden}#lifeserv .lifeserv-current li{height:27px;border-bottom:1px solid #E8E8E7}#lifeserv li{_position:relative;float:left;display:inline;width:62px;height:70px;border-right:1px solid #E8E8E7;border-bottom:1px solid #E8E8E7;overflow:hidden;cursor:pointer}#lifeserv li.simple a{padding-top:0;height:69px}#lifeserv li.simple i{height:0;line-height:0}#lifeserv li.current{border-top:2px solid #c81623;border-bottom:none;background:#fff}#lifeserv li.current a{line-height:25px}#lifeserv li a{display:block;width:62px;height:28px;padding-top:41px;line-height:28px;text-align:center;text-decoration:none;cursor:pointer}#lifeserv li a:hover span{color:#C81623}#lifeserv .ci-left{top:13px;left:18px;width:25px;height:25px}#lifeserv .fore1 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 0}#lifeserv .fore1 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px 0}#lifeserv .fore2 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -25px}#lifeserv .fore2 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -25px}#lifeserv .fore3 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -50px}#lifeserv .fore3 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -50px}#lifeserv .fore4 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -75px}#lifeserv .fore4 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -75px}#lifeserv .fore5 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -100px}#lifeserv .fore5 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -100px}#lifeserv .fore6 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -125px}#lifeserv .fore6 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -125px}#lifeserv .fore7 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -150px}#lifeserv .fore7 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -150px}#lifeserv .fore8 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -175px}#lifeserv .fore8 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -175px}#lifeserv .fore9 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -200px}#lifeserv .fore9 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -200px}#lifeserv .fore10 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -225px}#lifeserv .fore10 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -225px}#lifeserv .fore11 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -250px}#lifeserv .fore11 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -250px}#lifeserv .fore12 .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat 0 -275px}#lifeserv .fore12 .cw-icon:hover .ci-left{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/lifeserv/i/icon_lifeserv.png) no-repeat -25px -275px}#lifeserv .mc-inner{position:absolute;top:28px;left:0;width:250px;height:180px;background:#fff}#lifeserv .mc-inner .close{display:block;position:absolute;right:0;top:0;width:20px;height:20px;line-height:20px;text-align:center;cursor:pointer}#lifeserv .mc-inner .close:hover{background:#ccc;color:#fff;text-decoration:none}#lifeserv .hide iframe{display:none}
# /* product-home/1.0.0 floor-banner.css Date:2015-02-05 20:14:58 */
# .floor-banner{height:110px;margin-bottom:30px;overflow:visible;_overflow:hidden}.floor-banner .floor-banner-main{_position:relative;overflow:hidden;margin:0 auto;width:960px}.floor-banner .floor-banner-full{width:100%}.root61 .floor-banner .floor-banner-main{width:1200px}.root61 .floor-banner .floor-banner-full{width:100%}
# /* product-home/1.0.0 brands.css Date:2015-02-05 20:14:58 */
# .brands{background:#f7f7f7;padding:13px 0 13px 11px;margin-top:10px}.brands ul{height:40px;overflow:hidden}.brands li{float:left;width:120px;height:40px;border-left:1px dotted #ccc;text-align:center}.brands li.fore1{border-left:none}.root61 .brands{padding-left:0}
# /* product-home/1.0.0 todays.css Date:2015-04-08 09:43:23 */
# #todays{height:164px;margin:10px 0 20px}#todays .mt{display:none;float:left;width:210px;height:151px;background:url(http://misc.360buyimg.com/product/home/1.0.0/css/i/homebg.png) no-repeat -213px -136px;text-indent:-10000px}#todays .slider{float:left;position:relative;width:990px;height:164px;overflow:hidden}#todays .slider li{width:990px;height:164px}#todays .slider li div{float:left;overflow:hidden}#todays .slider li div.fore1,#todays .slider li div.fore2,#todays .slider li div.fore3{width:246px;margin-right:1px}#todays .slider li div.fore4{width:249px}.root61 #todays .mt{display:block}.root61 #todays .slider{width:1000px}.root61 #todays .slider li{width:1000px}.root61 #todays .slider li div.fore1,.root61 #todays .slider li div.fore2,.root61 #todays .slider li div.fore3{width:249px}.root61 #todays .slider li div.fore4{width:250px}
# /* product-home/1.0.0 guess-like.css Date:2015-03-13 11:36:13 */
# #guessyou{height:269px;margin-bottom:20px;overflow:hidden}#guessyou .mt h2{padding-right:228px;background:url(http://misc.360buyimg.com/product/home/1.0.0/css/i/homebg.png) 85px -91px}#guessyou .mt .extra{height:18px;padding-right:25px;margin-top:8px;background:url(http://misc.360buyimg.com/product/home/1.0.0/css/i/homebg.png) -310px -5px no-repeat}#guessyou .mt .extra:hover{background-position:-310px -29px}#guessyou:hover .spacer i{-webkit-animation:guess-slide 1s .5s;-moz-animation:guess-slide 1s .5s;animation:guess-slide 1s .5s}#guessyou .mc{height:232px;border:1px solid #ededed;border-top:0;overflow:visible}#guessyou ul{height:210px;padding-top:20px;overflow:hidden}#guessyou li{float:left;width:197px;overflow:hidden;padding-bottom:15px}#guessyou li.fore1 .p-info{border-left:none}#guessyou .p-img{text-align:center;margin-bottom:10px}#guessyou .p-info{padding:0 36px;border-left:1px solid #e6e6e6}#guessyou .p-name{height:36px;margin-bottom:6px}#guessyou .p-price{color:#b51d1a;font-size:18px}#guessyou .p-price i{font-size:14px}#guessyou .spacer{position:relative;height:1px;line-height:0;font-size:0;background-color:#d1d1d1}#guessyou .spacer i{width:365px;height:5px;overflow:hidden;position:absolute;right:-1px;top:-2px;background:#b72323 url(http://misc.360buyimg.com/product/home/1.0.0/css/i/homebg.png) no-repeat 0 -124px}@-webkit-keyframes guess-slide{0%{right:100%;opacity:.3}100%{right:0;opacity:1}}@-moz-keyframes guess-slide{0%{right:100%;opacity:.3}100%{right:0;opacity:1}}@keyframes guess-slide{0%{right:100%;opacity:.3}100%{right:0;opacity:1}}.root61 #guessyou li{width:201px}
# /* product-home/1.0.0 special-buy-v2.css Date:2015-09-10 18:51:07 */
# @charset "UTF-8";#lazy-special-buy-v2{margin-bottom:20px;height:439px}.home-special-buy-v2 h2{line-height:36px;font-size:20px}.home-special-buy-v2 .hs-content{border-left:solid 1px #ededed;border-top:solid 1px #ededed;height:402px;width:990px;overflow:hidden;*zoom:1;position:relative}.home-special-buy-v2 .hs-item{border-bottom:solid 1px #ededed;border-right:solid 1px #ededed;color:#666;height:200px;width:163px;text-align:center;position:relative;float:left;display:inline;overflow:hidden;font-family:"microsoft yahei"}.home-special-buy-v2 .hs-item img{margin-left:-18px}.home-special-buy-v2 .hs-item .tit{text-align:center;font-size:16px;line-height:18px;font-weight:700;position:absolute;top:20px;width:100%;height:20px;overflow:hidden}.home-special-buy-v2 .hs-item .tit span{display:inline-block;line-height:18px;vertical-align:middle;*vertical-align:baseline;*display:inline;*zoom:1}.home-special-buy-v2 .hs-item .tit .tit-l{color:#fff;font-size:12px;line-height:16px;vertical-align:middle;height:16px;width:30px;overflow:hidden;font-weight:400}.home-special-buy-v2 .hs-item .sub-tit{position:absolute;top:47px;height:18px;overflow:hidden;width:100%}.home-special-buy-v2 .hs-item2{border-bottom:solid 1px #ededed;border-right:solid 1px #ededed;color:#666;height:200px;width:163px;text-align:center;position:relative;float:left;display:inline;overflow:hidden;font-family:"microsoft yahei"}.home-special-buy-v2 .hs-item2 img{margin-left:-18px}.home-special-buy-v2 .hs-item2 .tit{text-align:center;font-size:16px;line-height:18px;font-weight:700;position:absolute;left:0;top:20px;width:100%;height:20px;overflow:hidden}.home-special-buy-v2 .hs-item2 .tit span{display:inline-block;line-height:18px;vertical-align:middle;*vertical-align:baseline;*display:inline;*zoom:1}.home-special-buy-v2 .hs-item2 .tit .tit-l{color:#fff;font-size:12px;line-height:16px;vertical-align:middle;height:16px;width:30px;overflow:hidden;font-weight:400}.home-special-buy-v2 .hs-item2 .sub-tit{position:absolute;left:0;top:47px;height:18px;overflow:hidden;width:100%;color:#dd4957}.home-special-buy-v2 .hs-item-2row{width:331px;position:relative}.home-special-buy-v2 .hs-item-more-m{width:160px;height:111px;margin-top:77px;border:none;border-left:1px dashed #e0e0e0}.home-special-buy-v2 .hs-item-more-m .static-item-more ul{margin-left:15px}.home-special-buy-v2 .hs-item-more-m .static-item-more li{width:135px;height:30px;line-height:30px;border-bottom:0;text-align:left;overflow:hidden;word-wrap:break-word;white-space:normal;word-break:break-all}.home-special-buy-v2 .hs-item-more-m .static-item-more li .tkw{color:#c81623;display:inline}.home-special-buy-v2 .item-more{margin:0 auto;width:126px}.home-special-buy-v2 .item-more h3{border-bottom:dashed 1px #e3e3e3;font-size:16px;height:50px;line-height:50px}.home-special-buy-v2 .item-more ul{overflow:hidden;*zoom:1;margin-top:14px}.home-special-buy-v2 .item-more ul li{float:left;display:inline;margin:6px 0 6px 3px;white-space:nowrap;width:60px;text-align:left}.home-special-buy-v2 .hs-content-left{float:left;display:inline;width:164px;overflow:hidden}.home-special-buy-v2 .hs-content-center{float:left;display:inline;width:328px;overflow:hidden}.home-special-buy-v2 .hs-content-right{float:left;display:inline;overflow:hidden;width:498px}.home-special-buy-v2 .hs-content-right .hs-item{width:165px}.home-special-buy-v2 .hs-item-red .tit{color:#666}.home-special-buy-v2 .hs-item-red .tit-l{background:#dd4957}.home-special-buy-v2 .hs-item-green .tit{color:#8fa952}.home-special-buy-v2 .hs-item-green .tit-l{background:#8fa952}.home-special-buy-v2 .hs-item-main{postion:relative;width:327px}.home-special-buy-v2 .hs-item-main div{position:absolute;cursor:pointer;text-align:center;left:20px;top:60px;width:160px}.home-special-buy-v2 .hs-item-main .hs-m-tit{font-size:18px;line-height:18px;font-weight:600;color:#333;padding-bottom:10px;overflow:hidden;height:20px;*line-height:1.5}.home-special-buy-v2 .hs-item-main .hs-m-subtit{font-size:16px;line-height:16px;color:#333;padding-bottom:10px;height:16px;overflow:hidden}.home-special-buy-v2 .hs-item-main .hs-m-button{display:inline-block;background:#e7004d;color:#fff;width:137px;height:24px;line-height:24px;overflow:hidden;font-size:16px}.home-special-buy-v2 .hs-item-main img{margin-left:0}.home-special-buy-v2 .hs-brands{float:left;width:163px;overflow:hidden;margin-bottom:-1px;height:200px;border-bottom:solid 1px #ededed;border-right:solid 1px #ededed;background:#f7f7f7}.home-special-buy-v2 .hs-brands .hs-brands-con{overflow:hidden;height:199px;margin-bottom:-1px;margin-right:-1px}.home-special-buy-v2 .hs-brands .hs-brands-con .item{display:block;width:163px;height:39px;border-bottom:dashed 1px #e0e0e0;text-align:center;*zoom:1}.home-special-buy-v2 .hs-brands .hs-brands-con .even{display:none}.root61 .home-special-buy-v2 .hs-content{width:1210px}.root61 .home-special-buy-v2 .hs-content-left{width:202px}.root61 .home-special-buy-v2 .hs-content-center{width:404px}.root61 .home-special-buy-v2 .hs-item{width:201px}.root61 .home-special-buy-v2 .hs-item img{margin-left:0}.root61 .home-special-buy-v2 .hs-item2{width:201px}.root61 .home-special-buy-v2 .hs-item2 img{margin-left:0}.root61 .home-special-buy-v2 .hs-item-2row{width:400px}.root61 .home-special-buy-v2 .hs-item-more-m{width:195px}.root61 .home-special-buy-v2 .hs-item-more-m .static-item-more ul{margin-left:15px}.root61 .home-special-buy-v2 .hs-item-more-m .static-item-more li{width:180px}.root61 .home-special-buy-v2 .hs-item-main{width:403px}.root61 .home-special-buy-v2 .hs-content-right{width:604px}.root61 .home-special-buy-v2 .hs-content-right .hs-item{width:200px}.root61 .home-special-buy-v2 .hs-brands{width:201px}.root61 .home-special-buy-v2 .hs-brands .hs-brands-con .item{float:left;display:inline;width:100px;border-right:dashed 1px #e0e0e0}.root61 .home-special-buy-v2 .hs-brands .hs-brands-con .even{border-right:none}.root61 .home-special-buy-v2 .hs-tit-i{width:28px;height:16px;background:url(//misc.360buyimg.com/product/home/1.0.0/widget/special-buy-v2/i/bg.png) no-repeat;_background:url(//misc.360buyimg.com/product/home/1.0.0/widget/special-buy-v2/i/bg8.png) no-repeat}.root61 .home-special-buy-v2 .hs-tit-i-l{background-position:0 center}.root61 .home-special-buy-v2 .hs-tit-i-r{background-position:-30px center}.root61 .home-special-buy-v2 .hs-item-red .hs-tit-i-l{background-position:0 center}.root61 .home-special-buy-v2 .hs-item-red .hs-tit-i-r{background-position:-30px center}.root61 .home-special-buy-v2 .hs-item-green .hs-tit-i-l{background-position:-58px center}.root61 .home-special-buy-v2 .hs-item-green .hs-tit-i-r{background-position:-87px center}.root61 .home-special-buy-v2 .item-more{width:160px}.root61 .home-special-buy-v2 .item-more ul li{margin-left:15px;margin-right:5px}.home-special-buy-v2 .hs-item .sub-tit{color:#c81623}.static-item-more li{position:relative;float:left;width:82px;height:49px;border-bottom:1px solid #efefef}.static-item-more .fore1,.static-item-more .fore3,.static-item-more .fore5,.static-item-more .fore7{border-right:1px solid #efefef}.static-item-more .fore1,.static-item-more .fore4,.static-item-more .fore5,.static-item-more .fore8{background:#f5f5f5}.static-item-more .fore7,.static-item-more .fore8{height:50px}.static-item-more a,.static-item-more span{display:block}.static-item-more b{display:block;width:20px;height:20px;margin:5px auto 2px;background:url(//misc.360buyimg.com/product/home/1.0.0/widget/special-buy-v2/i/bgforspecialbuy.png) no-repeat}.static-item-more .fore1 b{background-position:0 0}.static-item-more .fore2 b{background-position:0 -20px}.static-item-more .fore3 b{background-position:0 -40px}.static-item-more .fore4 b{background-position:0 -60px}.static-item-more .fore5 b{background-position:0 -80px}.static-item-more .fore6 b{background-position:0 -100px}.static-item-more .fore7 b{background-position:0 -120px}.static-item-more .fore8 b{background-position:0 -140px}.root61 .static-item-more li{width:100px}.root61 .static-item-more .fore1,.root61 .static-item-more .fore3,.root61 .static-item-more .fore5,.root61 .static-item-more .fore7{width:99px}
# /* product-home/1.0.0 clothes.css Date:2015-02-05 20:14:58 */
# #clothes .themes{padding-left:25px;margin-top:-221px}#clothes .themes li{width:100px}#clothes .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon8.png) 0 0 no-repeat}#clothes .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon8.png) 0 -26px no-repeat}#clothes .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon8.png) 0 -52px no-repeat}#clothes .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon8.png) 0 -78px no-repeat}#clothes .themes .fore5 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon.png) 0 -104px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon8.png) 0 -104px no-repeat}#clothes .themes .fore6 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon.png) 0 -130px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/clothes/i/clothesicon8.png) 0 -130px no-repeat}#clothes .words{height:128px;border-bottom:1px solid #ededed}#clothes .words li{height:96px;padding-top:16px}#clothes .side-extra{width:328px;height:158px;border:1px solid #ededed;border-left:1px solid #f7f5ee;border-top:0;overflow:hidden}#clothes .main{height:633px}#clothes .main-body li{float:left;height:158px}#clothes .main-body li.fore1{width:440px}#clothes .main-body li.fore2{width:440px;height:159px;padding-top:316px}#clothes .main-body li.fore2 a{height:158px}#clothes .main-body li.fore3{margin-top:-158px}#clothes .main-body li.fore6{height:159px}#clothes .main-body li.fore6 a{height:158px}#clothes .main-body li.fore3,#clothes .main-body li.fore4,#clothes .main-body li.fore5,#clothes .main-body li.fore6{float:right}#clothes .main-extra li{height:158px}#clothes .main-extra li.fore3{height:317px}#clothes .slider{top:158px;height:315px}#clothes .p-list li{width:185px}
# /* product-home/1.0.0 cosmetics.css Date:2015-02-05 20:14:58 */
# #cosmetics .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/cosmetics/i/cosmeticsicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/cosmetics/i/cosmeticsicon8.png) 0 0 no-repeat}#cosmetics .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/cosmetics/i/cosmeticsicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/cosmetics/i/cosmeticsicon8.png) 0 -26px no-repeat}#cosmetics .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/cosmetics/i/cosmeticsicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/cosmetics/i/cosmeticsicon8.png) 0 -52px no-repeat}#cosmetics .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/cosmetics/i/cosmeticsicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/cosmetics/i/cosmeticsicon8.png) 0 -78px no-repeat}#cosmetics .main-inner{padding-left:340px}#cosmetics .main-body{width:440px}#cosmetics .main-body li{float:left;width:220px;height:177px}#cosmetics .main-body li.fore1,#cosmetics .main-body li.fore2{height:297px}#cosmetics .main-extra li{width:220px;height:177px}#cosmetics .main-extra li.fore1{height:297px}#cosmetics .slider{width:339px;height:473px}#cosmetics .slider-panel a{display:block}#cosmetics .slider-panel a.fore1{border-bottom:1px dotted #ccc}
# /* product-home/1.0.0 electronics.css Date:2015-02-05 20:14:58 */
# #electronics .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/electronics/i/electronicsicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/electronics/i/electronicsicon8.png) 0 0 no-repeat}#electronics .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/electronics/i/electronicsicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/electronics/i/electronicsicon8.png) 0 -26px no-repeat}#electronics .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/electronics/i/electronicsicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/electronics/i/electronicsicon8.png) 0 -52px no-repeat}#electronics .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/electronics/i/electronicsicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/electronics/i/electronicsicon8.png) 0 -78px no-repeat}#electronics .themes{height:46px}#electronics .themes li{width:145px;padding:10px 0 10px 15px}#electronics .words{height:122px}#electronics .words li{height:96px}#electronics .main-body li{float:left;height:237px}#electronics .main-body li.fore1{height:118px}#electronics .main-body li.fore2{height:119px}#electronics .main-body li.fore1,#electronics .main-body li.fore2{padding-left:440px}#electronics .main-extra li.fore1{height:118px}#electronics .main-extra li.fore2{height:119px}#electronics .main-extra li.fore3{height:237px}#electronics .p-list li{width:185px}
# /* product-home/1.0.0 mobiles.css Date:2015-03-17 15:29:22 */
# #mobiles .themes .fore1 .icon,.floorStyleA .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/mobiles/i/mobilesicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/mobiles/i/mobilesicon8.png) 0 0 no-repeat}#mobiles .themes .fore2 .icon,.floorStyleA .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/mobiles/i/mobilesicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/mobiles/i/mobilesicon8.png) 0 -26px no-repeat}#mobiles .themes .fore3 .icon,.floorStyleA .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/mobiles/i/mobilesicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/mobiles/i/mobilesicon8.png) 0 -52px no-repeat}#mobiles .themes .fore4 .icon,.floorStyleA .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/mobiles/i/mobilesicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/mobiles/i/mobilesicon8.png) 0 -78px no-repeat}#mobiles .themes,.floorStyleA .themes{height:46px;padding-left:25px}#mobiles .words,.floorStyleA .words{height:122px}#mobiles .words li,.floorStyleA .words li{height:96px}#mobiles .main-body li,.floorStyleA .main-body li{float:left;height:237px}#mobiles .main-body li.fore1,.floorStyleA .main-body li.fore1{height:118px}#mobiles .main-body li.fore2,.floorStyleA .main-body li.fore2{height:119px}#mobiles .main-body li.fore1,#mobiles .main-body li.fore2,.floorStyleA .main-body li.fore1,.floorStyleA .main-body li.fore2{padding-left:440px}#mobiles .main-extra li.fore1,.floorStyleA .main-extra li.fore1{height:118px}#mobiles .main-extra li.fore2,.floorStyleA .main-extra li.fore2{height:119px}#mobiles .main-extra li.fore3,.floorStyleA .main-extra li.fore3{height:237px}#mobiles .p-list li,.floorStyleA .p-list li{width:185px}
# /* product-home/1.0.0 digitals.css Date:2015-03-24 18:04:13 */
# #digitals .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon8.png) 0 0 no-repeat}#digitals .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon8.png) 0 -26px no-repeat}#digitals .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon8.png) 0 -52px no-repeat}#digitals .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon8.png) 0 -78px no-repeat}#digitals .themes{height:46px}#digitals .themes li{width:145px;padding:10px 0 10px 15px}#digitals .words{height:122px}#digitals .words li{height:96px}#digitals .main-body li{float:left;height:237px}#digitals .main-body li.fore1{padding-left:440px}#digitals .main-extra li{height:237px}#digitals .p-list li{width:185px}#digitalsfloorStyleA .assists li{width:135px}#digitalsfloorStyleA .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon8.png) 0 0 no-repeat}#digitalsfloorStyleA .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon8.png) 0 -26px no-repeat}#digitalsfloorStyleA .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon8.png) 0 -52px no-repeat}#digitalsfloorStyleA .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/digitals/i/digitalsicon8.png) 0 -78px no-repeat}#digitalsfloorStyleA .themes li{width:140px;padding:10px 0}#digitalsfloorStyleA .themes .fore1{margin-right:20px}#digitalsfloorStyleA .p-list li{width:185px}
# /* product-home/1.0.0 sports.css Date:2015-02-05 20:14:58 */
# #sports .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/sports/i/sportsicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/sports/i/sportsicon8.png) 0 0 no-repeat}#sports .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/sports/i/sportsicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/sports/i/sportsicon8.png) 0 -26px no-repeat}#sports .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/sports/i/sportsicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/sports/i/sportsicon8.png) 0 -52px no-repeat}#sports .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/sports/i/sportsicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/sports/i/sportsicon8.png) 0 -78px no-repeat}#sports .main-body{width:780px}#sports .main-body li{float:left;height:237px}#sports .main-body li.fore2,#sports .main-body li.fore4{padding-left:340px}#sports .main-extra li{height:237px}#sports .slider{left:220px;width:339px;height:473px}#sports .slider-panel a{display:block}#sports .slider-panel a.fore1{border-bottom:1px dotted #ccc}
# /* product-home/1.0.0 livings.css Date:2015-02-05 20:14:58 */
# #livings .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/livings/i/livingsicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/livings/i/livingsicon8.png) 0 0 no-repeat}#livings .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/livings/i/livingsicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/livings/i/livingsicon8.png) 0 -26px no-repeat}#livings .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/livings/i/livingsicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/livings/i/livingsicon8.png) 0 -52px no-repeat}#livings .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/livings/i/livingsicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/livings/i/livingsicon8.png) 0 -78px no-repeat}#livings .main-body{width:780px}#livings .main-body li{float:left;height:237px}#livings .main-body li.fore2,#livings .main-body li.fore4{padding-left:340px}#livings .main-extra li{height:237px}#livings .slider{left:220px;width:339px;height:473px}#livings .slider-panel a{display:block}#livings .slider-panel a.fore1{border-bottom:1px dotted #ccc}
# /* product-home/1.0.0 babys.css Date:2015-02-05 20:14:58 */
# #babys .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/babys/i/babysicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/babys/i/babysicon8.png) 0 0 no-repeat}#babys .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/babys/i/babysicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/babys/i/babysicon8.png) 0 -26px no-repeat}#babys .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/babys/i/babysicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/babys/i/babysicon8.png) 0 -52px no-repeat}#babys .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/babys/i/babysicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/babys/i/babysicon8.png) 0 -78px no-repeat}#babys .main-body{width:780px}#babys .main-body li{float:left;height:237px}#babys .main-body li.fore2,#babys .main-body li.fore4{padding-left:340px}#babys .main-extra li{height:237px}#babys .slider{left:220px;width:339px;height:473px}#babys .slider-panel a{display:block}#babys .slider-panel a.fore1{border-bottom:1px dotted #ccc}
# /* product-home/1.0.0 foods.css Date:2015-02-05 20:14:58 */
# #foods .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/foods/i/foodsicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/foods/i/foodsicon8.png) 0 0 no-repeat}#foods .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/foods/i/foodsicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/foods/i/foodsicon8.png) 0 -26px no-repeat}#foods .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/foods/i/foodsicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/foods/i/foodsicon8.png) 0 -52px no-repeat}#foods .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/foods/i/foodsicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/foods/i/foodsicon8.png) 0 -78px no-repeat}#foods .main-body{width:780px}#foods .main-body li{float:left;height:237px}#foods .main-body li.fore2,#foods .main-body li.fore4{padding-left:340px}#foods .main-extra li{height:237px}#foods .slider{left:220px;width:339px;height:473px}#foods .slider-panel a{display:block}#foods .slider-panel a.fore1{border-bottom:1px dotted #ccc}
# /* product-home/1.0.0 books.css Date:2015-02-12 20:20:33 */
# #books .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/books/i/booksicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/books/i/booksicon8.png) 0 0 no-repeat}#books .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/books/i/booksicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/books/i/booksicon8.png) 0 -26px no-repeat}#books .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/books/i/booksicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/books/i/booksicon8.png) 0 -52px no-repeat}#books .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/books/i/booksicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/books/i/booksicon8.png) 0 -78px no-repeat}#books .main-body{width:440px;padding-top:237px}#books .main-body li{float:left;height:237px}#books .main-extra li{height:237px}#books .main-inner{position:absolute;left:0;top:0}#books .slider-body{width:439px;height:236px;overflow:hidden}#books .main{position:relative}#author{position:absolute;left:440px;top:0;width:340px;height:473px}#author h3{margin:0 15px 0 10px;padding-left:5px;padding-bottom:10px;font-size:20px;line-height:23px;border-bottom:1px solid #e4e4e4}#author .smt{height:34px;padding-top:13px;border-right:1px solid #EDEDED}#author .smc{height:426px;padding-left:15px;border-right:1px solid #EDEDED;border-bottom:1px solid #EDEDED}#author .smc li{height:80px;margin-top:20px;overflow:hidden}#author .author-info{float:left;width:48px;padding:2px 15px 0 4px;text-align:center}#author .author-info img{vertical-align:top;width:48px;height:48px;border-radius:50%;margin-bottom:6px}#author .author-info span{display:block;height:18px;overflow:hidden}#author .p-img{float:left;padding-left:8px;width:80px;height:80px;border-left:1px dotted #dbdbdb}#author .p-info{float:left;padding-left:10px}#author .p-name{width:150px;height:18px;margin-bottom:5px;font-size:14px;font-family:"microsoft yahei"}#author .p-detail{position:relative;width:115px;height:34px;padding:10px 15px 10px 20px;background:#f8f8f8;color:#999;overflow:visible}#author .p-detail p{height:38px;overflow:hidden;word-break:break-all}#author .detail-arrow{position:absolute;left:-9px;top:19px;color:#f8f8f8;font-size:20px}#author .icon-l{position:absolute;left:4px;top:7px;font-size:38px;line-height:38px;color:#aaa;font-family:Arial;*font-size:20px;*line-height:28px;*text-indent:-.5em}#author .icon-r{font-size:38px;line-height:38px;color:#aaa;vertical-align:-24px;font-family:Arial;*font-size:20px;*line-height:20px;*text-indent:-.5em;*vertical-align:-14px}.root61 #author{left:660px}
# /* product-home/1.0.0 life.css Date:2015-03-17 15:58:23 */
# #life .themes .fore1 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/life/i/lifeicon.png) 0 0 no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/life/i/lifeicon8.png) 0 0 no-repeat}#life .themes .fore2 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/life/i/lifeicon.png) 0 -26px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/life/i/lifeicon8.png) 0 -26px no-repeat}#life .themes .fore3 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/life/i/lifeicon.png) 0 -52px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/life/i/lifeicon8.png) 0 -52px no-repeat}#life .themes .fore4 .icon{background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/life/i/lifeicon.png) 0 -78px no-repeat;_background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/life/i/lifeicon8.png) 0 -78px no-repeat}#life .themes li{width:170px;padding:10px 0 10px 15px}#life .side{*position:relative;height:237px;overflow:hidden}#life .themes{margin-top:-329px}#life .main{width:780px;height:237px;border-top:none}#life .main-body{width:395px;padding-left:395px;padding-top:0}#life .main-body li{float:left;width:192px;height:118px}#life .main-body li.fore1,#life .main-body li.fore2{border-top:1px solid #f5f5f5}#life .main-body li.fore2,#life .main-body li.fore4{width:193px}#life .slider{width:395px;height:237px;border-right:0;border-bottom:0}.root61 #life .side{height:475px}.root61 #life .themes{margin-top:-237px}.root61 #life .main{width:395px;height:475px}.root61 #life .main-body{padding-left:0;padding-top:236px}.root61 #life .main-body li{float:left;width:197px;height:119px}.root61 #life .main-body li.fore1,.root61 #life .main-body li.fore2{border-top:0}.root61 #life .main-body li.fore2,.root61 #life .main-body li.fore4{width:198px}.root61 #life .slider{border-bottom:1px solid #f5f5f5}
# /* product-home/1.0.0 special.css Date:2015-02-05 22:46:19 */
# #special{float:left;width:680px;margin-bottom:20px}#special .mt h2{padding-right:232px;background:url(http://misc.360buyimg.com/product/home/1.0.0/widget/special/i/title.png) no-repeat right 10px}#special .mc{width:679px;height:281px;border:solid #E5E5E5;border-width:1px 0 1px 1px}#special .mc ul{width:690px;overflow:hidden}#special .mc li{float:left;width:199px;height:104px;padding:18px 10px;border-right:1px solid #EDEDED;border-bottom:1px solid #EDEDED;overflow:hidden}#special .mc li:hover .p-img img{margin-left:-10px}#special .mc li.fore1{width:219px;height:245px}#special .mc li.fore1:hover .p-img img{margin-left:-20px}#special .mc li.fore1 .p-img{width:219px;height:180px;margin-bottom:10px;text-align:center}#special .mc li.fore1 .p-info{width:200px}#special .mc li.fore1 .p-name{height:18px}#special .mc li.fore1 .p-price{float:left}#special .mc li.fore1 .p-discount{float:right}#special .mc li .p-img{float:left;width:100px;height:100px}#special .mc li .p-img img{-webkit-transition:all .4s ease-out;-moz-transition:all .4s ease-out;-ms-transition:all .4s ease-out;-o-transition:all .4s ease-out;transition:all .4s ease-out}#special .mc li .p-info{float:right;width:94px}#special .mc li .p-name{height:36px;margin-bottom:6px;color:#666;word-break:break-all}#special .mc li .p-price{margin-bottom:5px}#special .mc li .p-price span{display:block;color:#e12228;font-size:16px;font-weight:700}#special .mc li .p-price del{display:block;color:#c2c2c2}#special .mc li .p-discount{display:inline-block;*display:inline;*zoom:1;height:16px;line-height:16px;background-color:#e12228;padding:0 2px;color:#fff}.root61 #special{width:900px}.root61 #special .mc{width:899px}.root61 #special .mc ul{width:910px}
# /* product-home/1.0.0 share.css Date:2015-02-05 20:14:58 */
# #share{float:left;width:310px}#share .mc{width:268px;height:226px;padding:35px 20px 20px;border:1px solid #EDEDED}#share .mc li{height:100px;margin-bottom:20px;overflow:hidden}#share .sw{width:268px}#share .p-img{float:left;display:inline;padding:10px 0;width:80px;height:80px}#share .p-info{float:left;display:inline;width:166px;padding-left:20px;margin-top:3px}#share .p-info .p-name{height:expression(this.height>54?54:true);max-height:54px;overflow:hidden}#share .author-info{height:28px;margin-bottom:5px;overflow:hidden}#share .author-info img{width:28px;height:28px;margin-right:5px;border-radius:50%;vertical-align:middle}#share .author-info span{line-height:28px}#share .p-detail{position:relative;width:130px;height:34px;padding:10px 15px 10px 20px;background:#f8f8f8;color:#999;overflow:visible}#share .p-detail a,#share .p-detail p{display:block;height:38px;overflow:hidden;word-break:break-all}#share .detail-arrow{position:absolute;left:-9px;top:19px;color:#f8f8f8;font-size:20px}#share .icon-l{position:absolute;left:4px;top:7px;font-size:38px;line-height:38px;color:#aaa;font-family:Arial;*font-size:20px;*line-height:28px;*text-indent:-.5em}#share .icon-r{font-size:38px;line-height:38px;color:#aaa;vertical-align:-24px;font-family:Arial;*font-size:20px;*line-height:20px;*text-indent:-.5em;*vertical-align:-14px}#share .sw{position:relative;overflow:hidden;height:240px}
# </style><script type="text/javascript">/* jdf-1.0.0/ base.js Date:2015-09-15 18:39:13 */
# if(!function(a,b){function c(a){return function(b){return{}.toString.call(b)=="[object "+a+"]"}}function d(){return A++}function e(a){return a.match(D)[0]}function f(a){for(a=a.replace(E,"/");a.match(F);)a=a.replace(F,"/");return a=a.replace(G,"$1/")}function g(a){var b=a.length-1,c=a.charAt(b);return"#"===c?a.substring(0,b):".js"===a.substring(b-2)||a.indexOf("?")>0||".css"===a.substring(b-3)||"/"===c?a:a+".js"}function h(a){var b=v.alias;return b&&x(b[a])?b[a]:a}function i(a){var c,b=v.paths;return b&&(c=a.match(H))&&x(b[c[1]])&&(a=b[c[1]]+c[2]),a}function j(a){var b=v.vars;return b&&a.indexOf("{")>-1&&(a=a.replace(I,function(a,c){return x(b[c])?b[c]:a})),a}function k(a){var b=v.map,c=a;if(b)for(var d=0,e=b.length;e>d;d++){var f=b[d];if(c=z(f)?f(a)||a:a.replace(f[0],f[1]),c!==a)break}return c}function l(a,b){var c,d=a.charAt(0);if(J.test(a))c=a;else if("."===d)c=f((b?e(b):v.cwd)+a);else if("/"===d){var g=v.cwd.match(K);c=g?g[0]+a.substring(1):a}else c=v.base+a;return 0===c.indexOf("//")&&(c=location.protocol+c),c}function m(a,b){if(!a)return"";a=h(a),a=i(a),a=j(a),a=g(a);var c=l(a,b);return c=k(c)}function n(a){return a.hasAttribute?a.src:a.getAttribute("src",4)}function o(a,b,c){var d=S.test(a),e=L.createElement(d?"link":"script");if(c){var f=z(c)?c(a):c;f&&(e.charset=f)}p(e,b,d,a),d?(e.rel="stylesheet",e.href=a):(e.async=!0,e.src=a),T=e,R?Q.insertBefore(e,R):Q.appendChild(e),T=null}function p(a,c,d,e){function f(){a.onload=a.onerror=a.onreadystatechange=null,d||v.debug||Q.removeChild(a),a=null,c()}var g="onload"in a;return!d||!V&&g?(g?(a.onload=f,a.onerror=function(){C("error",{uri:e,node:a}),f()}):a.onreadystatechange=function(){/loaded|complete/.test(a.readyState)&&f()},b):(setTimeout(function(){q(a,c)},1),b)}function q(a,b){var d,c=a.sheet;if(V)c&&(d=!0);else if(c)try{c.cssRules&&(d=!0)}catch(e){"NS_ERROR_DOM_SECURITY_ERR"===e.name&&(d=!0)}setTimeout(function(){d?b():q(a,b)},20)}function r(){if(T)return T;if(U&&"interactive"===U.readyState)return U;for(var a=Q.getElementsByTagName("script"),b=a.length-1;b>=0;b--){var c=a[b];if("interactive"===c.readyState)return U=c}}function s(a){var b=[];return a.replace(X,"").replace(W,function(a,c,d){d&&b.push(d)}),b}function t(a,b){this.uri=a,this.dependencies=b||[],this.exports=null,this.status=0,this._waitings={},this._remain=0}if(!a.seajs){var u=a.seajs={version:"2.2.0"},v=u.data={},w=c("Object"),x=c("String"),y=Array.isArray||c("Array"),z=c("Function"),A=0,B=v.events={};u.on=function(a,b){var c=B[a]||(B[a]=[]);return c.push(b),u},u.off=function(a,b){if(!a&&!b)return B=v.events={},u;var c=B[a];if(c)if(b)for(var d=c.length-1;d>=0;d--)c[d]===b&&c.splice(d,1);else delete B[a];return u};var C=u.emit=function(a,b){var d,c=B[a];if(c)for(c=c.slice();d=c.shift();)d(b);return u},D=/[^?#]*\//,E=/\/\.\//g,F=/\/[^/]+\/\.\.\//,G=/([^:/])\/\//g,H=/^([^/:]+)(\/.+)$/,I=/{([^{]+)}/g,J=/^\/\/.|:\//,K=/^.*?\/\/.*?\//,L=document,M=e(L.URL),N=L.scripts,O=L.getElementById("seajsnode")||N[N.length-1],P=e(n(O)||M);u.resolve=m;var T,U,Q=L.getElementsByTagName("head")[0]||L.documentElement,R=Q.getElementsByTagName("base")[0],S=/\.css(?:\?|$)/i,V=+navigator.userAgent.replace(/.*AppleWebKit\/(\d+)\..*/,"$1")<536;u.request=o;var Z,W=/"(?:\\"|[^"])*"|'(?:\\'|[^'])*'|\/\*[\S\s]*?\*\/|\/(?:\\\/|[^\/\r\n])+\/(?=[^\/])|\/\/.*|\.\s*require|(?:^|[^$])\brequire\s*\(\s*(["'])(.+?)\1\s*\)/g,X=/\\\\/g,Y=u.cache={},$={},_={},ab={},bb=t.STATUS={FETCHING:1,SAVED:2,LOADING:3,LOADED:4,EXECUTING:5,EXECUTED:6};t.prototype.resolve=function(){for(var a=this,b=a.dependencies,c=[],d=0,e=b.length;e>d;d++)c[d]=t.resolve(b[d],a.uri);return c},t.prototype.load=function(){var a=this;if(!(a.status>=bb.LOADING)){a.status=bb.LOADING;var c=a.resolve();C("load",c);for(var e,d=a._remain=c.length,f=0;d>f;f++)e=t.get(c[f]),e.status<bb.LOADED?e._waitings[a.uri]=(e._waitings[a.uri]||0)+1:a._remain--;if(0===a._remain)return a.onload(),b;var g={};for(f=0;d>f;f++)e=Y[c[f]],e.status<bb.FETCHING?e.fetch(g):e.status===bb.SAVED&&e.load();for(var h in g)g.hasOwnProperty(h)&&g[h]()}},t.prototype.onload=function(){var a=this;a.status=bb.LOADED,a.callback&&a.callback();var c,d,b=a._waitings;for(c in b)b.hasOwnProperty(c)&&(d=Y[c],d._remain-=b[c],0===d._remain&&d.onload());delete a._waitings,delete a._remain},t.prototype.fetch=function(a){function c(){u.request(g.requestUri,g.onRequest,g.charset)}function d(){delete $[h],_[h]=!0,Z&&(t.save(f,Z),Z=null);var a,b=ab[h];for(delete ab[h];a=b.shift();)a.load()}var e=this,f=e.uri;e.status=bb.FETCHING;var g={uri:f};C("fetch",g);var h=g.requestUri||f;return!h||_[h]?(e.load(),b):$[h]?(ab[h].push(e),b):($[h]=!0,ab[h]=[e],C("request",g={uri:f,requestUri:h,onRequest:d,charset:v.charset}),g.requested||(a?a[g.requestUri]=c:c()),b)},t.prototype.exec=function(){function a(b){return t.get(a.resolve(b)).exec()}var c=this;if(c.status>=bb.EXECUTING)return c.exports;c.status=bb.EXECUTING;var e=c.uri;a.resolve=function(a){return t.resolve(a,e)},a.async=function(b,c){return t.use(b,c,e+"_async_"+d()),a};var f=c.factory,g=z(f)?f(a,c.exports={},c):f;return g===b&&(g=c.exports),delete c.factory,c.exports=g,c.status=bb.EXECUTED,C("exec",c),g},t.resolve=function(a,b){var c={id:a,refUri:b};return C("resolve",c),c.uri||u.resolve(c.id,b)},t.define=function(a,c,d){var e=arguments.length;1===e?(d=a,a=b):2===e&&(d=c,y(a)?(c=a,a=b):c=b),!y(c)&&z(d)&&(c=s(""+d));var f={id:a,uri:t.resolve(a),deps:c,factory:d};if(!f.uri&&L.attachEvent){var g=r();g&&(f.uri=g.src)}C("define",f),f.uri?t.save(f.uri,f):Z=f},t.save=function(a,b){var c=t.get(a);c.status<bb.SAVED&&(c.id=b.id||a,c.dependencies=b.deps||[],c.factory=b.factory,c.status=bb.SAVED)},t.get=function(a,b){return Y[a]||(Y[a]=new t(a,b))},t.use=function(b,c,d){var e=t.get(d,y(b)?b:[b]);e.callback=function(){for(var b=[],d=e.resolve(),f=0,g=d.length;g>f;f++)b[f]=Y[d[f]].exec();c&&c.apply(a,b),delete e.callback},e.load()},t.preload=function(a){var b=v.preload,c=b.length;c?t.use(b,function(){b.splice(0,c),t.preload(a)},v.cwd+"_preload_"+d()):a()},u.use=function(a,b){return t.preload(function(){t.use(a,b,v.cwd+"_use_"+d())}),u},t.define.cmd={},a.define=t.define,u.Module=t,v.fetchedList=_,v.cid=d,u.require=function(a){var b=t.get(t.resolve(a));return b.status<bb.EXECUTING&&b.exec(),b.exports};var cb=/^(.+?\/)(\?\?)?(seajs\/)+/;v.base=(P.match(cb)||["",P])[1],v.dir=P,v.cwd=M,v.charset="utf-8",v.preload=function(){var a=[],b=location.search.replace(/(seajs-\w+)(&|$)/g,"$1=1$2");return b+=" "+L.cookie,b.replace(/(seajs-\w+)=1/g,function(b,c){a.push(c)}),a}(),u.config=function(a){for(var b in a){var c=a[b],d=v[b];if(d&&w(d))for(var e in c)d[e]=c[e];else y(d)?c=d.concat(c):"base"===b&&("/"!==c.slice(-1)&&(c+="/"),c=l(c)),v[b]=c}return C("config",a),u}}}(this),!function(){function a(a){var b=a.length;if(!(2>b)){q.comboSyntax&&(s=q.comboSyntax),q.comboMaxLength&&(t=q.comboMaxLength),n=q.comboExcludes;for(var d=[],e=0;b>e;e++){var f=a[e];if(!r[f]){var h=o.get(f);h.status<p&&!l(f)&&!m(f)&&d.push(f)}}d.length>1&&g(c(d))}}function b(a){a.requestUri=r[a.uri]||a.uri}function c(a){return e(d(a))}function d(a){for(var b={__KEYS:[]},c=0,d=a.length;d>c;c++)for(var e=a[c].replace("://","__").split("/"),f=b,g=0,h=e.length;h>g;g++){var i=e[g];f[i]||(f[i]={__KEYS:[]},f.__KEYS.push(i)),f=f[i]}return b}function e(a){for(var b=[],c=a.__KEYS,d=0,e=c.length;e>d;d++){for(var g=c[d],h=g,i=a[g],j=i.__KEYS;1===j.length;)h+="/"+j[0],i=i[j[0]],j=i.__KEYS;j.length&&b.push([h.replace("__","://"),f(i)])}return b}function f(a){for(var b=[],c=a.__KEYS,d=0,e=c.length;e>d;d++){var g=c[d],h=f(a[g]),i=h.length;if(i)for(var j=0;i>j;j++)b.push(g+"/"+h[j]);else b.push(g)}return b}function g(a){for(var b=0,c=a.length;c>b;b++)for(var d=a[b],e=d[0]+"/",f=j(d[1]),g=0,i=f.length;i>g;g++)h(e,f[g]);return r}function h(a,b){var c=a+s[0]+b.join(s[1]),d=c.length>t;if(b.length>1&&d){var e=i(b,t-(a+s[0]).length);h(a,e[0]),h(a,e[1])}else{if(d)throw new Error("The combo url is too long: "+c);for(var f=0,g=b.length;g>f;f++)r[a+b[f]]=c}}function i(a,b){for(var c=s[1],d=a[0],e=1,f=a.length;f>e;e++)if(d+=c+a[e],d.length>b)return[a.splice(0,e),a]}function j(a){for(var b=[],c={},d=0,e=a.length;e>d;d++){var f=a[d],g=k(f);g&&(c[g]||(c[g]=[])).push(f)}for(var h in c)c.hasOwnProperty(h)&&b.push(c[h]);return b}function k(a){var b=a.lastIndexOf(".");return b>=0?a.substring(b):""}function l(a){return n?n.test?n.test(a):n(a):void 0}function m(a){var b=q.comboSyntax||["??",","],c=b[0],d=b[1];return c&&a.indexOf(c)>0||d&&a.indexOf(d)>0}var n,o=seajs.Module,p=o.STATUS.FETCHING,q=seajs.data,r=q.comboHash={},s=["??",","],t=2e3;if(seajs.on("load",a),seajs.on("fetch",b),q.test){var u=seajs.test||(seajs.test={});u.uris2paths=c,u.paths2hash=g}define("seajs/seajs-combo/1.0.1/seajs-combo",[],{})}(),window.pageConfig=window.pageConfig||{},"undefined"==typeof pageConfig.autoConfig&&(pageConfig.autoConfig=!0),"undefined"==typeof pageConfig.preload&&(pageConfig.preload=!0),pageConfig.jdfVersion||(pageConfig.jdfVersion="1.0.0"),pageConfig.jdfBaseUri||(pageConfig.jdfBaseUri=("https:"==document.location.protocol?"//":"http://")+"misc.360buyimg.com/"),pageConfig.autoConfig){var preloadArray=pageConfig.preload?[pageConfig.jdfBaseUri+"jdf/"+pageConfig.jdfVersion+"/ui/ui/"+pageConfig.jdfVersion+"/ui.js"]:[];var seajsConfig={base:pageConfig.jdfBaseUri,alias:{},map:[],preload:preloadArray,debug:0};("localhost"==location.hostname||/isdebug=(-\d)*-1/.test(location.search)||/isdebug=-31#-1/.test(location.href))&&(seajsConfig.comboExcludes=/.*/),seajs.config(seajsConfig)}if(pageConfig.wideVersion=function(){return/isdebug=(-\d)*-2/.test(location.search)?!1:screen.width>=1210&&pageConfig.compatible}(),pageConfig.wideVersion&&(document.getElementsByTagName("html")[0].className="root61"),pageConfig.FN_getDomain=function(){var a=location.hostname;var b="jd.com";return/jd.com/.test(a)?b="jd.com":/jd360.hk/.test(a)?b="jd360.hk":/jd.hk/.test(a)?b="jd.hk":/360buy.com/.test(a)&&(b="360buy.com"),b},/jd\.com|360buy\.com|jd\.hk|jd360\.hk/.test(location.hostname))try{document.domain=pageConfig.FN_getDomain()}catch(e){}pageConfig.FN_GetImageDomain=function(a){var b,a=String(a);switch(a.match(/(\d)$/)[1]%5){case 0:b=10;break;case 1:b=11;break;case 2:b=12;break;case 3:b=13;break;case 4:b=14;break;default:b=10}return"//img{0}.360buyimg.com/".replace("{0}",b)},pageConfig.FN_ImgError=function(a){var b=a.getElementsByTagName("img");for(var c=0;c<b.length;c++)b[c].onerror=function(){var a="",b=this.getAttribute("data-img");if(b){switch(b){case"1":a="err-product";break;case"2":a="err-poster";break;case"3":a="err-price";break;default:return}this.src="//misc.360buyimg.com/lib/img/e/blank.gif",this.className=a}}},pageConfig.FN_GetRandomData=function(a){var d,b=0,c=0,e=[];for(var f=0;f<a.length;f++)d=a[f].weight?parseInt(a[f].weight):1,e[f]=[],e[f].push(b),b+=d,e[f].push(b);c=Math.ceil(b*Math.random());for(var f=0;f<e.length;f++)if(c>e[f][0]&&c<=e[f][1])return a[f]};var login=function(){return location.href="https://passport.jd.com/new/login.aspx?ReturnUrl="+escape(location.href).replace(/\//g,"%2F"),!1};var regist=function(){return location.href="https://reg.jd.com/reg/person?ReturnUrl="+escape(location.href),!1};var createCookie=function(a,b,c,d){var d=d?d:"/";if(c){var e=new Date;e.setTime(e.getTime()+24*c*60*60*1e3);var f="; expires="+e.toGMTString()}else var f="";document.cookie=a+"="+b+f+"; path="+d};var readCookie=function(a){var b=a+"=";var c=document.cookie.split(";");for(var d=0;d<c.length;d++){var e=c[d];for(;" "==e.charAt(0);)e=e.substring(1,e.length);if(0==e.indexOf(b))return e.substring(b.length,e.length)}return null};var addToFavorite=function(){var a="//www.jd.com/";var b="\u4eac\u4e1cJD.COM-\u7f51\u8d2d\u4e0a\u4eac\u4e1c\uff0c\u7701\u94b1\u53c8\u653e\u5fc3";document.all?window.external.AddFavorite(a,b):window.sidebar&&window.sidebar.addPanel?window.sidebar.addPanel(b,a,""):alert("\u5bf9\u4e0d\u8d77\uff0c\u60a8\u7684\u6d4f\u89c8\u5668\u4e0d\u652f\u6301\u6b64\u64cd\u4f5c!\n\u8bf7\u60a8\u4f7f\u7528\u83dc\u5355\u680f\u6216Ctrl+D\u6536\u85cf\u672c\u7ad9\u3002"),createCookie("_fv","1",30,"/;domain=jd.com")};pageConfig.getHashProbability=function(a,b){var c=function(a){for(var b=0,c=0;c<a.length;c++)b=(b<<5)-b+a.charCodeAt(c),b&=b;return b};return Math.abs(c(a))%b},(/isdebug=(-\d)*-1/.test(location.search)||/isdebug=-31#-1/.test(location.href))&&!function(){function a(){var a=document.getElementsByTagName("link");var b=null,c=null;for(var d=0;d<a.length;d++){var e=a[d];if(e){var f=e.getAttribute("href");if(f){var g=f.indexOf("??");var h=[];var i="";if(-1!=g&&(c=document.createDocumentFragment(),h=f.substring(g+2).split(","),i=f.substring(0,g),h.length)){for(var j=0,k=h.length;k>j;j++)h[j].replace(/ /g)&&(b=document.createElement("link"),b.type="text/css",b.rel="stylesheet",b.href=i+h[j],c.appendChild(b),d++);e.parentNode.insertBefore(c,e),e.parentNode.removeChild(e),d--}}}}}var b=setInterval(function(){document.body&&(clearInterval(b),a())},10)}(),pageConfig.insertStyles=function(a){var b=document,c=b.getElementsByTagName("head"),d=b.createElement("style"),e=b.createElement("link");if(/\.css$/.test(a))e.rel="stylesheet",e.type="text/css",e.href=a,c.length?c[0].appendChild(e):b.documentElement.appendChild(e);else{if(d.setAttribute("type","text/css"),d.styleSheet)d.styleSheet.cssText=a;else{var f=b.createTextNode(a);d.appendChild(f)}c.length&&c[0].appendChild(d)}};
# </script><!--index_ok-->

# <style type="text/css" rel="stylesheet">
# .double11-brands{margin-bottom:40px}.double11-brands .db-left{width:180px;height:220px;overflow:hidden}.double11-brands .db-left a{width:180px;height:220px;display:block;background:url(http://img12.360buyimg.com/da/jfs/t2320/198/558629385/27537/aa79ff11/5618b96cNb6ec4974.jpg)}.double11-brands .brandslist{width:810px;border-top:1px solid #dcdcdc}.double11-brands .brandslist ul li{float:left;display:inline;border-right:1px solid #dcdcdc;border-bottom:1px solid #dcdcdc;width:80px;height:72px}.double11-brands .brandslist ul a{position:absolute;display:block;width:80px;height:72px;background:url(about:blank);z-index:1}.double11-brands .brandslist ul img{width:80px;height:72px}.double11-brands .brandslist ul a:hover{margin:-1px;border:solid 3px #f0394a;width:76px;height:68px}.root61 .double11-brands .db-left{width:210px;height:271px}.root61 .double11-brands .db-left a{width:210px;height:271px;background:url(http://img10.360buyimg.com/da/jfs/t2059/244/563977789/23390/216e4c48/56178cb2N414ab1d7.jpg)}.root61 .double11-brands .brandslist{width:1000px}.root61 .double11-brands .brandslist ul li{width:99px;height:89px}.root61 .double11-brands .brandslist ul a{width:99px;height:89px}.root61 .double11-brands .brandslist ul img{width:99px;height:89px}.root61 .double11-brands .brandslist ul a:hover{width:95px;height:85px}.double11-products{border-top:solid 2px #e12013;margin-bottom:20px}.double11-products .dp-head{height:59px;background:url(http://img12.360buyimg.com/da/jfs/t1810/18/1871283140/33925/133fca34/5618af62Nc4effa93.jpg) no-repeat center center;position:relative}.double11-products .dp-head img{display:none}.double11-products .dp-head a{display:block;height:59px;width:290px;left:0;top:0;position:absolute;background:url(about:blank)}.double11-products .dp-item{display:block;float:left;overflow:hidden;border-right:solid 1px #e5e5e5;border-top:solid 1px #e5e5e5}.double11-products .dp-con{height:342px;border-bottom:solid 1px #e5e5e5}.double11-products .dp-con-left{width:990px}.double11-products .dp-con-center{width:593px}.double11-products .dp-con-right{width:220px}.double11-products .dp-item{float:left;display:inline;position:relative;font-family:'Microsoft YaHei'}.double11-products .dp-item span{position:absolute;left:20px}.double11-products .dp-item .tit{font-size:24px;line-height:24px;color:#c81623;top:30px}.double11-products .dp-item .subtit{font-size:14px;color:#999;top:62px}.double11-products .dp-item1{width:395px;height:341px;border-left:solid 1px #e5e5e5}.double11-products .dp-item2,.double11-products .dp-item3{width:372px;height:170px}.double11-products .dp-item2 .tit,.double11-products .dp-item3 .tit{font-size:18px;top:25px}.double11-products .dp-item2 .subtit,.double11-products .dp-item3 .subtit{top:51px}.double11-products .dp-item4{margin-top:-171px}.double11-products .dp-item4,.double11-products .dp-item5,.double11-products .dp-item6,.double11-products .dp-item7{float:right}.double11-products .dp-item4 .tit,.double11-products .dp-item5 .tit,.double11-products .dp-item6 .tit,.double11-products .dp-item7 .tit{font-size:16px;top:25px}.double11-products .dp-item4 .subtit,.double11-products .dp-item5 .subtit,.double11-products .dp-item6 .subtit,.double11-products .dp-item7 .subtit{top:51px}.double11-products .dp-con-right{display:none}.root61 .double11-products .dp-head{background:0 0}.root61 .double11-products .dp-head img{display:block}.root61 .double11-products .dp-head a{width:330px}.root61 .dp-con-right{display:block}
# </style>
# </head>
# <body>
# <div id="shortcut-2014">
#     <div class="w">
#         <ul class="fl" clstag="h|keycount|2015|01a">
#             <li class="dorpdown" id="ttbar-mycity"></li>
#         </ul>
#         <ul class="fr">
#             <li class="fore1" id="ttbar-login" clstag="h|keycount|2015|01b">
#                 <a target="_blank" href="javascript:login();" class="link-login">你好，请登录</a>&nbsp;&nbsp;<a href="javascript:regist();" class="link-regist style-red">免费注册</a>
#         </li>
#             <li class="spacer"></li>
#         <li class="fore2" clstag="h|keycount|2015|01c">
#                 <div class="dt">
#                     <a target="_blank" href="http://order.jd.com/center/list.action" target="_blank">我的订单</a>
#                 </div>
#             </li>
#             <li class="spacer"></li>
#         <li class="fore3 dorpdown" id="ttbar-myjd" clstag="h|keycount|2015|01d">
#             <div class="dt cw-icon">
#                     <i class="ci-right"><s>◇</s></i>
#                     <a target="_blank" href="http://home.jd.com/">我的京东</a>
#                 </div>
#         <div class="dd dorpdown-layer"></div>
#             </li>
#             <li class="spacer"></li>
#         <li class="fore4" clstag="h|keycount|2015|01e">
#                 <div class="dt">
#                     <a target="_blank" href="http://vip.jd.com/">京东会员</a>
#                 </div>
#             </li>
#             <li class="spacer"></li>
#         <li class="fore5" clstag="h|keycount|2015|01f">
#                 <div class="dt">
#                     <a target="_blank" href="http://b.jd.com/">企业采购</a>
#                 </div>
#             </li>
#             <li class="spacer"></li>
#         <li class="fore6 dorpdown" id="ttbar-apps" clstag="h|keycount|2015|01g">
#                 <div class="dt cw-icon">
#                     <i class="ci-left"></i>
#             <i class="ci-right"><s>◇</s></i>
#                     <a target="_blank" href="http://app.jd.com/">手机京东</a>
#                 </div>
#             </li>
#         <li class="spacer"></li>
#             <li class="fore7 dorpdown" id="ttbar-atte" clstag="h|keycount|2015|01h">
#                 <div class="dt cw-icon">
#                     <i class="ci-right"><s>◇</s></i>关注京东
#                 </div>
#                 <div class="dd dorpdown-layer"></div>
#             </li>
#             <li class="spacer"></li>
#         <li class="fore8 dorpdown" id="ttbar-serv" clstag="h|keycount|2015|01i">
#                 <div class="dt cw-icon">
#                     <i class="ci-right"><s>◇</s></i>客户服务
#                 </div>
#                 <div class="dd dorpdown-layer"></div>
#             </li>
#             <li class="spacer"></li>
#         <li class="fore9 dorpdown" id="ttbar-navs" clstag="h|keycount|2015|01j">
#                 <div class="dt cw-icon">
#                     <i class="ci-right"><s>◇</s></i>网站导航
#                 </div>
#                 <div class="dd dorpdown-layer"></div>
#             </li>
#         </ul>
#         <span class="clr"></span>
#     </div>
# </div>
# <div class="w">
#     <div id="logo-2014" clstag="h|keycount|2015|02a">
#         <a href="http://www.jd.com/" class="logo">京东</a>
#     </div>
#     <div id="search-2014" >
#         <ul id="shelper" class="hide"></ul>
#         <div class="form">
#             <input clstag="h|keycount|2015|03a" type="text" onkeydown="javascript:if(event.keyCode==13) search('key');" autocomplete="off" id="key" accesskey="s" class="text" />
#             <button clstag="h|keycount|2015|03c" onclick="search('key');return false;" class="button cw-icon"><i></i>搜索</button>
#         </div>
#     </div>
#     <div id="settleup-2014" class="dorpdown" clstag="h|keycount|2015|04a">
#     <div class="cw-icon">
#         <i class="ci-left"></i>
#         <i class="ci-right">&gt;</i>
#         <a target="_blank" href="http://cart.jd.com/cart/cart.html">我的购物车</a>
#     </div>
#     <div class="dorpdown-layer">
# <div class="spacer"></div>
# <div id="settleup-content">
#     <span class="loading"></span>
# </div>
#     </div>
# </div>
#     <div id="hotwords-2014"></div>
#     <span class="clr"></span>
# </div>
# <div id="nav-2014">
#     <div class="w">
#         <div class="w-spacer"></div>


#             <div id="categorys-2014" class="dorpdown">
#             <div class="dt" clstag="h|keycount|2015|05a">
#                 <a target="_blank" href="http://www.jd.com/allSort.aspx">全部商品分类</a>
#             </div>
#             <div class="dd">
#                 <div class="dd-inner">

#                     <div class="item fore1" data-index="1" clstag="h|keycount|2015|0501a">
#                         <h3><a target="_blank" href="http://channel.jd.com/electronic.html">家用电器</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore2" data-index="2" clstag="h|keycount|2015|0502a">
#                         <h3><a target="_blank" href="http://shouji.jd.com/">手机</a>、<a target="_blank" href="http://shuma.jd.com/">数码</a>、<a target="_blank" href="http://mobile.jd.com/">京东通信</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore3" data-index="3" clstag="h|keycount|2015|0503a">
#                         <h3><a target="_blank" href="http://diannao.jd.com/">电脑、办公</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore4" data-index="4" clstag="h|keycount|2015|0504a">
#                         <h3><a target="_blank" href="http://channel.jd.com/home.html">家居</a>、<a target="_blank" href="http://channel.jd.com/furniture.html">家具</a>、<a target="_blank" href="http://channel.jd.com/decoration.html">家装</a>、<a target="_blank" href="http://channel.jd.com/kitchenware.html">厨具</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore5" data-index="5" clstag="h|keycount|2015|0505a">
#                         <h3><a target="_blank" href="http://channel.jd.com/1315-1342.html">男装</a>、<a target="_blank" href="http://channel.jd.com/1315-1343.html">女装</a>、<a target="_blank" href="http://channel.jd.com/1315-1345.html">内衣</a>、<a target="_blank" href="http://channel.jd.com/jewellery.html">珠宝</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore6" data-index="6" clstag="h|keycount|2015|0506a">
#                         <h3><a target="_blank" href="http://channel.jd.com/beauty.html">个护化妆</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore7" data-index="7" clstag="h|keycount|2015|0507a">
#                         <h3><a target="_blank" href="http://channel.jd.com/shoes.html">鞋靴</a>、<a target="_blank" href="http://channel.jd.com/bag.html">箱包</a>、<a target="_blank" href="http://channel.jd.com/watch.html">钟表</a>、<a target="_blank" href="http://channel.jd.com/1672-2615.html">奢侈品</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore8" data-index="8" clstag="h|keycount|2015|0508a">
#                         <h3><a target="_blank" href="http://channel.jd.com/sports.html">运动户外</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore9" data-index="9" clstag="h|keycount|2015|0509a">
#                         <h3><a target="_blank" href="http://car.jd.com/">汽车</a>、<a target="_blank" href="http://channel.jd.com/auto.html">汽车用品</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore10" data-index="10" clstag="h|keycount|2015|0510a">
#                         <h3><a target="_blank" href="http://baby.jd.com">母婴</a>、<a target="_blank" href="http://channel.jd.com/toys.html">玩具乐器</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore11" data-index="11" clstag="h|keycount|2015|0511a">
#                         <h3><a target="_blank" href="http://channel.jd.com/food.html">食品</a>、<a target="_blank" href="http://channel.jd.com/wine.html">酒类</a>、<a target="_blank" href="http://channel.jd.com/freshfood.html">生鲜</a>、<a target="_blank" href="http://china.jd.com">特产</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore12" data-index="12" clstag="h|keycount|2015|0512a">
#                         <h3><a target="_blank" href="http://channel.jd.com/health.html">营养保健</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore13" data-index="13" clstag="h|keycount|2015|0513a">
#                         <h3><a target="_blank" href="http://book.jd.com/">图书</a>、<a target="_blank" href="http://mvd.jd.com/">音像</a>、<a target="_blank" href="http://e.jd.com/ebook.html">电子书</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore14" data-index="14" clstag="h|keycount|2015|0514a">
#                         <h3><a target="_blank" href="http://caipiao.jd.com/">彩票</a>、<a target="_blank" href="http://trip.jd.com/">旅行</a>、<a target="_blank" href="http://chongzhi.jd.com/">充值</a>、<a target="_blank" href="http://piao.jd.com/">票务</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                     <div class="item fore15" data-index="15" clstag="h|keycount|2015|0515a">
#                         <h3><a target="_blank" href="http://licai.jd.com/">理财</a>、<a target="_blank" href="http://z.jd.com/">众筹</a>、<a target="_blank" href="http://baitiao.jd.com/activity/third">白条</a>、<a target="_blank" href="http://bao.jd.com/">保险</a></h3>
#                         <i>&gt;</i>
#                     </div>
#                 </div>
#             </div>
#         </div><!--index_ok-->
#         <div id="navitems-2014">

#         <ul id="navitems-group1">
#             <li clstag="h|keycount|2015|06a" id="nav-fashion" class="fore1" >
#                 <a target="_blank" href="http://channel.jd.com/fashion.html">服装城</a>
#             </li>
#             <li clstag="h|keycount|2015|06b" id="nav-beauty" class="fore2" >
#                 <a target="_blank" href="http://channel.jd.com/beautysale.html">美妆馆</a>
#             </li>
#             <li clstag="h|keycount|2015|06c" id="nav-chaoshi" class="fore3" >
#                 <a target="_blank" href="http://channel.jd.com/chaoshi.html">超市</a>
#             </li>
#             <li clstag="h|keycount|2015|06d" id="nav-jdww" class="fore4" >
#                 <a target="_blank" href="http://www.jd.hk/">全球购</a>
#             </li>
#         </ul>
#         <div class="spacer"></div>
#         <ul id="navitems-group2">
#             <li clstag="h|keycount|2015|06e" id="nav-red" class="fore1" >
#                 <a target="_blank" href="http://red.jd.com/">闪购</a>
#             </li>
#             <li clstag="h|keycount|2015|06f" id="nav-tuan" class="fore2" >
#                 <a target="_blank" href="http://tuan.jd.com/">团购</a>
#             </li>
#             <li clstag="h|keycount|2015|06g" id="nav-auction" class="fore3" >
#                 <a target="_blank" href="http://paimai.jd.com/">拍卖</a>
#             </li>
#             <li clstag="h|keycount|2015|06h" id="nav-jr" class="fore4" >
#                 <a target="_blank" href="http://jr.jd.com/">金融</a>
#             </li>
#             <li clstag="h|keycount|2015|06i" id="nav-auction" class="fore5 navitems-on" >
#                 <a target="_blank" href="http://smart.jd.com/">智能</a>
#             </li>
#         </ul>
#     </div><!--index_ok-->

#         <div id="treasure"></div>
#         <span class="clr"></span>
#     </div>
# </div>


# <div id="focus">
#     <div class="slider"></div>
# </div>
# <script type="text/javascript">
#     pageConfig.focusData = [
#         [{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mWlR1HP401IHmvwFQGlQg60DJb9r+zq29UgjWVTaa7YeNB0ffESre4p46kgY508LDs4qpGKj6+FVSHW0qNWenNBHWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakpSlIKu58rshL0NjPJth01z2S7WVJwUVWWlj5uqkFQYTO8kB+sSzSS0dWVpqx287jLMnQRjLX8LeruC5DQu2wwDKXBn/4XyfZBkqZDvr0dRqsYAhmxRmBoISpVNFyZRXL4a+892nOos/0aSRnf6vbMmf9HLeDipRHAKm4vcfN+U1KKFU6qVYkYEbrR18iEkgIA==&cv=2.0&url=http://sale.jd.com/act/M7J62hoy1vugS.html",alt: "",src: "http://img12.360buyimg.com/da/jfs/t2320/241/818048839/98916/c3a1e0e8/562f4313N2d060e78.jpg",ext1: "",index: "0",widthB: 510,heightB: 454,clog: "9959.101580.223338.1.2_955_6217", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img12.360buyimg.com/da/jfs/t2221/229/848550322/99941/c2f19185/562f4316N29bac119.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mWlR1HP401IHmvwFQGlQg60DJb9r+zq29UgjWVTaa7YebcomA5aIQVw9VJs90rsX7yO7ryMq2s5p6rIsOMPOIFNHWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakpSlIKu58rshL0NjPJth01z2S7WVJwUVWWlj5uqkFQYTO8kB+sSzSS0dWVpqx287jLMnQRjLX8LeruC5DQu2wwDKXBn/4XyfZBkqZDvr0dRqsYAhmxRmBoISpVNFyZRXL4a+892nOos/0aSRnf6vbMmf9HLeDipRHAKm4vcfN+U1KKFU6qVYkYEbrR18iEkgIA==&cv=2.0&url=http://sale.jd.com/act/M7J62hoy1vugS.html",alt: "",src: "http://img14.360buyimg.com/da/jfs/t2311/278/846224547/100467/91818546/562f436fN4f99d34c.jpg",ext1: "",index: "1",widthB: 510,heightB: 454,clog: "9959.101581.223341.1.2_955_6217", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img14.360buyimg.com/da/jfs/t2101/303/854659236/99478/96f1d793/562f4372N74184642.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mWlR1HP401IHmvwFQGlQg60DJb9r+zq29UgjWVTaa7YelCB58ipQrKCglbRpvdOyGSD8F1fap+YedgTuim9I9k1HWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakpSlIKu58rshL0NjPJth01z2S7WVJwUVWWlj5uqkFQYTO8kB+sSzSS0dWVpqx287jLMnQRjLX8LeruC5DQu2wwDKXBn/4XyfZBkqZDvr0dRqsYAhmxRmBoISpVNFyZRXL4a+892nOos/0aSRnf6vbMmf9HLeDipRHAKm4vcfN+U1KKFU6qVYkYEbrR18iEkgIA==&cv=2.0&url=http://sale.jd.com/act/M7J62hoy1vugS.html",alt: "",src: "http://img30.360buyimg.com/da/jfs/t2137/300/838732673/95480/b08a3e43/562dca10Ned523e25.jpg",ext1: "",index: "2",widthB: 510,heightB: 454,clog: "9959.101582.222978.1.2_955_6217", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img12.360buyimg.com/da/jfs/t2422/297/818444849/81820/81d50045/562dca12N2cdca20b.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mWlR1HP401IHmvwFQGlQg60DJb9r+zq29UgjWVTaa7YebSgkO5yzAJNW5suhrUK11XlIhwUcaJ1s7PXbooy08upHWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakpSlIKu58rshL0NjPJth01z2S7WVJwUVWWlj5uqkFQYTO8kB+sSzSS0dWVpqx287jLMnQRjLX8LeruC5DQu2wwDKXBn/4XyfZBkqZDvr0dRqsYAhmxRmBoISpVNFyZRXL4a+892nOos/0aSRnf6vbMmf9HLeDipRHAKm4vcfN+U1KKFU6qVYkYEbrR18iEkgIA==&cv=2.0&url=http://sale.jd.com/act/M7J62hoy1vugS.html",alt: "",src: "http://img11.360buyimg.com/da/jfs/t2359/342/858186811/96771/4dbab08a/562f41ccN1bcad0b7.jpg",ext1: "",index: "3",widthB: 510,heightB: 454,clog: "9959.101583.223331.1.2_955_6217", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img10.360buyimg.com/da/jfs/t2272/22/858736295/95965/3f045f49/562f41d0N4ec29fa6.jpg"}],
#         [{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv/3U13fcaD1hCd4kErziTaNd2T5KyN+Ye47W/IaNEKkJWSfDje4RkxhHKcGc6aNkd593+Cz7jXoPxtJSbvfsN2St2zzWxLf+f/hKdgnq53OJNf/M8b7jjE9eIUno/d2y8YWmnMzt/7B3mouxQBXXYkeBvY0tDzeYVvO6GD7pv64H8vAa6QAm01CnX10pC6qyde7NopedPC3du7DL5C86LCm7rgAJfsDkN3cr39q/mKyOw8DnD4R7zcofvTr4ytU1fEqjV5eNKY+ZtEexFIgZ9O50KLb4qjigzwt6HHBU+SMjg==&cv=2.0&url=http://sale.jd.com/mall/LJFvAI8CUK.html",alt: "",src: "http://img11.360buyimg.com/da/jfs/t2440/53/827799979/101572/19b20772/562ed771N767d76ed.jpg",ext1: "",index: "0",widthB: 510,heightB: 454,clog: "11799.101173.223146.1.2_955_6458", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img20.360buyimg.com/da/jfs/t2137/47/844955329/101562/19defef1/562ed775N4b4cb2e9.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv8PUxFqbjLihk8NAMRMKLCR8TeGr5kqOoYctqJQb4rzuz+r9smTgBaRR+ibbVgP3WFvSP7fJcZDDCPh5oUgehjyt2zzWxLf+f/hKdgnq53OJDYqbyB6Ott3khfiqRkvzxFRYPl0xcNo3sQwsoS745Wyqg7lBKMNaPUH7HUwVbi2CBd0Hr7Fi8hVunvZC4tPYiigwBDdtxSPU3z8cp50sfgiF1pAhcXBWv+zgtdSUzgYBEGXVSM3evs0GIN7W0oIHYZuynqN4iTv4/b1f66WBNE0YyuRuUC5Ueuy0w4BtYM9ig==&cv=2.0&url=http://sale.jd.com/act/iklG3xhS1LRcQqNJ.html",alt: "",src: "http://img12.360buyimg.com/da/jfs/t2386/311/838410665/97755/15f1c551/562d87cdNe5e1176e.jpg",ext1: "",index: "1",widthB: 510,heightB: 454,clog: "11801.101174.222839.1.2_955_6458", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img14.360buyimg.com/da/jfs/t2158/312/803978052/99687/c6d8132f/562d87d1Nb21a4561.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv96DriTRU7q2LuYWI1qys1ZBCFxWVMr6YsXeSWcON/pVNAg5J7G82y2H0zJ1hbwa41mjCtZceDU7pD/uVJH+FqXt2zzWxLf+f/hKdgnq53OJDRACxAQ23MhK2Hj+l3MaMz0B4ZidhOkgBl8VaVKD6EePcADfOydEgb3r/t/IOD6jebwKAFQoJNlTkPYqRWHa7QpodVXpEL15gIhF7tS9XGTIH/3PVpFk1yWjCKplUWsYiZkUIzjmhlPlHv4wTLvUHI6PS3e2iAxIftN/cIOoqdkLMz+Zwh2Sv2uEPtOqU+3QA==&cv=2.0&url=http://sale.jd.com/act/ugeGThzBV8P37oW.html",alt: "",src: "http://img20.360buyimg.com/da/jfs/t1867/137/801327818/97799/9c6f1ede/562e00e1N2091a9d8.jpg",ext1: "",index: "2",widthB: 510,heightB: 454,clog: "11808.101175.223111.1.2_955_6458", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img10.360buyimg.com/da/jfs/t2116/144/876544798/101254/b61bca0c/562e00e3Nbd8b7410.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv8wUCeWENbB2Yc9Pp/Ioly1GpviWrFTJraFuQx4PbuWijmvmDBLuPoTRF/ugvBW3xIfGnteWoMlhC3hwOZgMSv3t2zzWxLf+f/hKdgnq53OJH6xIi/yQYpbvTUa64qzipc1v6/58qkR+ZEFEKBHsNw4AkuOIdHLRtkW/q4CIdzM/gKe2acHG0Ajuj9L8JXxidE+hmSpgLz9xmR1xEiObDPEY2cXhMASnNvmSUyLnxgFsxMv49nQdfWafuMVCtVmz8qXOlcppL6VE6XAjxQTKJJ8WOo1bdnPYgppNB+nDWfC8A==&cv=2.0&url=http://sale.jd.com/act/hG3N4B2nt6XUCA.html",alt: "",src: "http://img20.360buyimg.com/da/jfs/t1885/54/856042332/81499/b982b285/562eeabfN10000a8e.jpg",ext1: "",index: "3",widthB: 510,heightB: 454,clog: "11809.101176.223172.1.2_955_6458", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img13.360buyimg.com/da/jfs/t2488/32/851449116/54980/cff814ce/562eeac0Nf9f31156.jpg"}],
#         [{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv/6dnzt4nCpT9s8r6AId29kjtRGAW7oXojMmqAaBJ2kqy1pij19h9TzZJkPlHEqXLxEzEhpsksRzvrhNzN2x68ot2zzWxLf+f/hKdgnq53OJBEKOnKJbhObuU7kQz1NctYGv8yqjRMddTsEj7G9DagWBvY0tDzeYVvO6GD7pv64H8vAa6QAm01CnX10pC6qyde7NopedPC3du7DL5C86LCm7rgAJfsDkN3cr39q/mKyOw8DnD4R7zcofvTr4ytU1fEqjV5eNKY+ZtEexFIgZ9O50KLb4qjigzwt6HHBU+SMjg==&cv=2.0&url=http://sale.jd.com/act/SAUrKO2pLwl.html",alt: "",src: "http://img13.360buyimg.com/da/jfs/t2059/135/829504713/92357/a3c3350a/562de7f2N7ccb72ee.jpg",ext1: "",index: "0",widthB: 510,heightB: 454,clog: "11878.101177.223058.1.2_955_6459", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img20.360buyimg.com/da/jfs/t2227/152/832457268/63852/134e5ad1/562de7f5Nd8ec62aa.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv83kJsyb3t+bswONhJSObKNtqrhQDGUkjj/UG6uAg7+eyNlgCXsELU6rZP7q5v59LYLPzs8KKG2erw9q8YPqgI4t2zzWxLf+f/hKdgnq53OJMNqgUQEo8Oqe6dmMl+DVHAwCbNowFs2lfit8570QMCjqg7lBKMNaPUH7HUwVbi2CBd0Hr7Fi8hVunvZC4tPYiigwBDdtxSPU3z8cp50sfgiF1pAhcXBWv+zgtdSUzgYBEGXVSM3evs0GIN7W0oIHYZuynqN4iTv4/b1f66WBNE0YyuRuUC5Ueuy0w4BtYM9ig==&cv=2.0&url=http://sale.jd.com/act/8moeT1M3DQWcn2SV.html",alt: "",src: "http://img13.360buyimg.com/da/jfs/t2092/78/811164108/89321/aafb300f/562dc514Nd2ae4ce8.jpg",ext1: "",index: "1",widthB: 510,heightB: 454,clog: "11908.101178.222970.1.2_955_6459", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img30.360buyimg.com/da/jfs/t1864/54/854820682/83136/7f62e424/562dc516Ncb325f93.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv84BkE+ToXOUs30Suc8tDGXKawBFQS1g6TbJdNPnIm2lywwwtnBSiXApUMXXyrfX51km3+x2TG8MswgjF5hZkBIt2zzWxLf+f/hKdgnq53OJBFkH3zsvTFY5lg6OUVaJ5K9IlZ7CAXVxE2pSzx8hob7PcADfOydEgb3r/t/IOD6jebwKAFQoJNlTkPYqRWHa7QpodVXpEL15gIhF7tS9XGTIH/3PVpFk1yWjCKplUWsYiZkUIzjmhlPlHv4wTLvUHI6PS3e2iAxIftN/cIOoqdkLMz+Zwh2Sv2uEPtOqU+3QA==&cv=2.0&url=http://sale.jd.com/act/OGUVyXK2aF7clf5.html",alt: "",src: "http://img14.360buyimg.com/da/jfs/t2086/186/817894569/99701/f7096edb/562e2d8bN4b55e1fb.jpg",ext1: "",index: "2",widthB: 510,heightB: 454,clog: "11923.101179.223134.1.2_955_6459", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img12.360buyimg.com/da/jfs/t2323/169/801550236/100693/64d0a8b2/562e2d8fN01a96d91.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv/jCsrENpnSIXNZ7aTQXtN+iclWPR6aLKuTSLxCT1Ro7S1pij19h9TzZJkPlHEqXLxvSP7fJcZDDCPh5oUgehjyt2zzWxLf+f/hKdgnq53OJJOzGbhOY1B/YGFhgbFM2tRrMUJ42TXs+sUtcrdt3MxdAkuOIdHLRtkW/q4CIdzM/gKe2acHG0Ajuj9L8JXxidE+hmSpgLz9xmR1xEiObDPEY2cXhMASnNvmSUyLnxgFsxMv49nQdfWafuMVCtVmz8qXOlcppL6VE6XAjxQTKJJ8WOo1bdnPYgppNB+nDWfC8A==&cv=2.0&url=http://sale.jd.com/act/Zosz3hlpC1rewH.html",alt: "",src: "http://img10.360buyimg.com/da/jfs/t2020/219/814486474/60422/d28c63aa/562de871N554ffc18.jpg",ext1: "",index: "3",widthB: 510,heightB: 454,clog: "11934.101180.223059.1.2_955_6459", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img20.360buyimg.com/da/jfs/t1957/241/844032932/52174/970411a9/562de873N3934183a.jpg"}],
#         [{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv/lOd7wGWRcvkeNppVhkBVZHZumvsYSLg/Ojk7uTJcl8ACN6GC/nuxHZEutsr9Q/vFHWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakh+h07uvQ1LOcoZ9l7LGyoTdw9YA0970NK557EH13T2Wej6oVx0BseliqtSegr3IlbDtf3eVfWb1orhErN4jTcO+rjt+wmNBqathelSaHUsWvi3DP9vR6BVkUfiEtycMxl/Qae9xh2e/T9YWCueIsatyVMmKJ+LujoLlfkmAfmKTYpUboR8ciyR5H4ne31buZoYjevjHNvGqTDM3fonDawQ=&cv=2.0&url=http://sale.jd.com/act/plAbPj2CLtYDVuix.html?from=jdsj_04_101181",alt: "",src: "http://img30.360buyimg.com/da/jfs/t1978/101/885320834/118881/7cede5df/562edd16N482e6b09.jpg",ext1: "",index: "0",widthB: 510,heightB: 454,clog: "9191.101181.223151.1.2_955_6460", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img13.360buyimg.com/da/jfs/t2332/102/845064284/84484/32efb7e6/562edd1cN8e16ef35.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv/lOd7wGWRcvkeNppVhkBVZRn4S7QdXBJfTrEo+AYgVXx86plUeVx9fM/r+SP07zChHWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakkxkD8k+b/ilU+e0PQ/UN956DtfT3WNgHsuECpd+asFMNXgNPwQZThLJq6HGCCbi/TmXJWUMvLQ/EpiX0ZeubNh0TT1ztTpTp6Y0nbIMp97b+iChiFRuX/P9TOzXCKNL3vJQPDO9C6vATK5RFXPG/jY5VwrVScu9+qzU5QxSbo0iGdGx2/l6AdAx+dWHtPeCxXtdFIueQ5q97nFJe3rLrCY=&cv=2.0&url=http://sale.jd.com/act/8Nat4ZXTEeYRgU.html?from=jdsj_04_101182",alt: "",src: "http://img20.360buyimg.com/da/jfs/t2254/25/815992679/102907/bf53e7f0/562ddaa1N076ba9ce.jpg",ext1: "",index: "1",widthB: 510,heightB: 454,clog: "9191.101182.223018.1.2_955_6460", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img10.360buyimg.com/da/jfs/t2488/1/796722302/99059/56919e00/562ddaa3N178f2097.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv+/7laPZOHVqK174EWjdeOPogm18VPgvhP7wjBfdynJHrun2UrDNVvJCc0u/14yqP8WA954k5k+rEGpxP131Cxkt2zzWxLf+f/hKdgnq53OJPNJ+fR7bnC4ajBMc/TaP6qePsXq4BP5EOxiV0F1uEwYBvY0tDzeYVvO6GD7pv64H8vAa6QAm01CnX10pC6qyde7NopedPC3du7DL5C86LCm7rgAJfsDkN3cr39q/mKyOw8DnD4R7zcofvTr4ytU1fEqjV5eNKY+ZtEexFIgZ9O50KLb4qjigzwt6HHBU+SMjg==&cv=2.0&url=http://sale.jd.com/act/3u5UnTCcGE4.html",alt: "",src: "http://img13.360buyimg.com/da/jfs/t2062/323/784223974/99814/bad65de2/5629f811N83bda5a6.jpg",ext1: "",index: "2",widthB: 510,heightB: 454,clog: "11955.101183.222595.1.2_955_6460", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img12.360buyimg.com/da/jfs/t2377/317/827023296/96042/11655c53/5629f816N43111337.jpg"}],
#         [{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv/5jbTyz/vqpYkh4vLn5nXdFj7q2Sw+23uZDp2TIOx2uP7UPzVSMkN8GBFLuR8S4HnW8RAi674cFuEN84YZEeQot2zzWxLf+f/hKdgnq53OJICCIoVcCuY/Y/GTjOKZnBRIASmtDA2BQwf9REPYzOrCPcADfOydEgb3r/t/IOD6jebwKAFQoJNlTkPYqRWHa7QpodVXpEL15gIhF7tS9XGTIH/3PVpFk1yWjCKplUWsYiZkUIzjmhlPlHv4wTLvUHI6PS3e2iAxIftN/cIOoqdkLMz+Zwh2Sv2uEPtOqU+3QA==&cv=2.0&url=http://sale.jd.com/act/Dbtsrjw10WXHm6u.html",alt: "",src: "http://img12.360buyimg.com/da/jfs/t2461/72/808611271/101845/2f5a377e/562d9f21N4b8785e1.jpg",ext1: "",index: "0",widthB: 510,heightB: 454,clog: "12020.101184.222907.1.2_955_6461", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img10.360buyimg.com/da/jfs/t2368/83/835904148/95902/151ee694/562d9f23Nb3d8360e.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv+45mFMFKOY3N5VdY1HT1vpgD41vUIcVZZz7uhHcIuhpow87ndgX3kXja++Xv4WTi5HWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakmfbFVK6fh8G4dr8iaPrTvyvriYLOUx7x1GM0B0P0yVMAkuOIdHLRtkW/q4CIdzM/gKe2acHG0Ajuj9L8JXxidE+hmSpgLz9xmR1xEiObDPEY2cXhMASnNvmSUyLnxgFsxMv49nQdfWafuMVCtVmz8qXOlcppL6VE6XAjxQTKJJ8WOo1bdnPYgppNB+nDWfC8A==&cv=2.0&url=http://sale.jd.com/act/IgFU54dLM0rGxZb.html",alt: "",src: "http://img30.360buyimg.com/da/jfs/t2251/235/843335851/186333/57c7f998/562ecd39Nd59fc4f3.jpg",ext1: "",index: "1",widthB: 510,heightB: 454,clog: "9574.101185.215614.1.2_955_6461", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img11.360buyimg.com/da/jfs/t1885/190/839215826/155157/87d9839b/562ecd3bN92d566a5.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv+KVe7JORae+WMretq2VP5ouIozFOJOVkOS9ecpclg/co7ItiiMT/Agz1hzWKyS02yZI7p/OOlX6LABVlykvJwqJ7lPLEoFZ8/A01jk7X1pIJ7dY8gntHoMNfiDm3s9g8VI/N2VNLEH15IRFzBOMYeUQod+KYxCPcjDhX1RouGJvWWX8sgBMRRsCf+zfYrDghP7Yf0/1mWhQd/EwOPW33yN6Y76pEUjnWhXnKNVdZJvVXCZyfP4uMqYgQ3v+5kk/jcO2L9Q0Zc72tSD7laS1JfwqCGCSkwWB0UZE/clm1+XfA==&cv=2.0&url=http://sale.jd.com/act/fT7G4AmBOvVWEx.html",alt: "",src: "http://img11.360buyimg.com/da/jfs/t1900/95/818619561/119105/b71047a/562f13c0Ncad97452.jpg",ext1: "",index: "2",widthB: 510,heightB: 454,clog: "0.101186.221136.1.2_955_6461", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img11.360buyimg.com/da/jfs/t1966/112/838102702/87921/473da342/562f13c4Na7bbeba2.jpg"}],
#         [{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv8g8nrlUtx8f+sSGQJVVA8H7yEd0PUy3Nz7oyXuw/PTYf7UPzVSMkN8GBFLuR8S4Hl93+Cz7jXoPxtJSbvfsN2St2zzWxLf+f/hKdgnq53OJIj6pVVuPsrkBdQ05IeVFv9t4NJWiZ5ASPdBwX7NrZ2oO8kB+sSzSS0dWVpqx287jLMnQRjLX8LeruC5DQu2wwDKXBn/4XyfZBkqZDvr0dRqsYAhmxRmBoISpVNFyZRXL4a+892nOos/0aSRnf6vbMmf9HLeDipRHAKm4vcfN+U1KKFU6qVYkYEbrR18iEkgIA==&cv=2.0&url=http://sale.jd.com/act/bVrThYuwy4iC.html",alt: "",src: "http://img11.360buyimg.com/da/jfs/t2299/49/831779047/143297/7c1b66fe/562d9ee4Nbd1f24de.jpg",ext1: "",index: "0",widthB: 510,heightB: 454,clog: "11418.101187.222906.1.2_955_6462", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img10.360buyimg.com/da/jfs/t1933/24/793124385/114238/4d7e0f3d/562d9ee9N14c906cd.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv+AVZr8UZW/OAVIanFmf7QGZbNdcBvhxfkWlrcPqXjWAzs6xzleKII3yhXvIe1Vu39vSP7fJcZDDCPh5oUgehjyt2zzWxLf+f/hKdgnq53OJHfAdwHpzTz8eDxfLXQKRrt8qaJD9Ib0HBoWfR3T3kV6PcADfOydEgb3r/t/IOD6jebwKAFQoJNlTkPYqRWHa7QpodVXpEL15gIhF7tS9XGTIH/3PVpFk1yWjCKplUWsYiZkUIzjmhlPlHv4wTLvUHI6PS3e2iAxIftN/cIOoqdkLMz+Zwh2Sv2uEPtOqU+3QA==&cv=2.0&url=http://sale.jd.com/act/KYZbk5Ex6uSBrhL.html",alt: "",src: "http://img12.360buyimg.com/da/jfs/t2071/134/734883842/100380/818a50e/5625f502N1890a75c.jpg",ext1: "",index: "1",widthB: 510,heightB: 454,clog: "12307.101188.221869.1.2_955_6462", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img12.360buyimg.com/da/jfs/t2200/245/749608682/91023/159bd3f8/5625f507Ne0a90bdf.jpg"},{width: 730,height: 454,href: "http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mcSXfzjWtbuODvGjWG1VVv+PsermMNxzeWwF5xxOFl/LvQ7y/4jpE9aYEhr8102XsPPwm9cqOUuiZlYGavFVqkfW8RAi674cFuEN84YZEeQot2zzWxLf+f/hKdgnq53OJIQiArLpHTLwe/u886jFsFqeDwLHsej/1yzAiAyk1QGqZzMI/FNcIyqPvs7l7kzfgqwuiHO85wBSyA1FPeT/jgXBkyxapGKK0bayuRsyF1CjSHY0JSwCJdCXubq2wQCesktkSSOFA1pdGE/Iy7jQSEYQlCt5qtzWUNQR7nMClgnfA8pekfb4uNQnqgcfk9CP5w==&cv=2.0&url=http://sale.jd.com/act/Dd7JcnwfWzTNQ.html",alt: "",src: "http://img10.360buyimg.com/da/jfs/t2098/197/822760080/86876/7f61e55/562dc3c5N6f4f82b7.jpg",ext1: "",index: "2",widthB: 510,heightB: 454,clog: "10978.101189.222967.1.2_955_6462", logDomain: "http://s.nfa.jd.com/bd?info=", logV: "1.0",srcB: "http://img11.360buyimg.com/da/jfs/t2173/148/855316816/100129/bd6103cf/562dc3c7N95079b8f.jpg"}]
#     ];
# </script><!--index_ok-->

# <div class="w" id="focus-extra">

#         <div id="news" class="m">
#         <div class="mt">
#             <h2>京东快报</h2>
#             <div class="extra"><a target="_blank" href="http://www.jd.com/moreSubject.aspx" clstag="h|keycount|2015|09a">更多 &gt;</a></div>
#         </div>
#         <div class="mc">
#         <ul>

#                     <li clstag="h|keycount|2015|09b1"><a target="_blank" href="http://sale.jd.com/act/Myuwq64inZILfg2.html"><span>[特惠]</span>9.9能买到这个？</a></li>
#                     <li clstag="h|keycount|2015|09b2"><a target="_blank" href="http://www.jd.com/news.aspx?id=26354"><span>[公告]</span>京东超市 销售连创新高</a></li>
#                     <li clstag="h|keycount|2015|09b3"><a target="_blank" href="http://sale.jd.com/act/tV2kZLq4YvE3.html"><span>[特惠]</span>抢货秘籍  8亿手机券放送</a></li>
#                     <li clstag="h|keycount|2015|09b4"><a target="_blank" href="http://www.jd.com/news.aspx?id=26343"><span>[公告]</span>大牌盛宴 有品质才能爽购11天</a></li>
#                     <li clstag="h|keycount|2015|09b5"><a target="_blank" href="http://sale.jd.com/act/mlCSv701bGqP.html"><span>[特惠]</span>欧德堡奥妙强强联合超低价</a></li>
#         </ul>
#         </div>
#     </div><!--index_ok-->
#     <div id="lifeserv" class="m">
#     <div class="mt">
#         <h2>生活服务</h2>
#         <div class="extra"></div>
#     </div>
#     <div class="mc">
#         <ul>

#             <li class="fore1" data-iframe="http://chongzhi.jd.com/jd-index-ifame.htm" clstag="h|keycount|2015|10b01">
#                 <a class="cw-icon" target="_blank" href="http://chongzhi.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>话费</span>
#                 </a>
#             </li>
#             <li class="fore2" data-iframe="http://jipiao.jd.com/htm/iframeTrip.html" clstag="h|keycount|2015|10b02">
#                 <a class="cw-icon" target="_blank" href="http://jipiao.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>机票</span>
#                 </a>
#             </li>
#             <li class="fore3" data-iframe="http://movie.jd.com/jdmovie.html" clstag="h|keycount|2015|10b03">
#                 <a class="cw-icon" target="_blank" href="http://movie.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>电影票</span>
#                 </a>
#             </li>
#             <li class="fore4" data-iframe="http://card.jd.com/html/card-jdIndex2015.html" clstag="h|keycount|2015|10b04">
#                 <a class="cw-icon" target="_blank" href="http://game.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>游戏</span>
#                 </a>
#             </li>
#             <li class="fore5" clstag="h|keycount|2015|10b05">
#                 <a class="cw-icon" target="_blank" href="http://caipiao.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>彩票</span>
#                 </a>
#             </li>
#             <li class="fore6" clstag="h|keycount|2015|10b06">
#                 <a class="cw-icon" target="_blank" href="http://tuan.jd.com/homevirtual-beijing.html?cpdad=1DLSUE">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>团购</span>
#                     <i class="ci-tip" style="width:12px;height:15px;top:0px;right:0px;background: url(http://img10.360buyimg.com/da/jfs/t2161/29/277121102/1033/bb98ca5d/55fa836fN29b00ae8.png);_background: url(http://img30.360buyimg.com/da/jfs/t2239/157/257074274/1022/fffbd45c/55fa837fNa1b41ba4.png); no-repeat scroll 0 0"></i>
#                 </a>
#             </li>
#             <li class="fore7" clstag="h|keycount|2015|10b07">
#                 <a class="cw-icon" target="_blank" href="http://hotel.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>酒店</span>
#                 </a>
#             </li>
#             <li class="fore8" clstag="h|keycount|2015|10b08">
#                 <a class="cw-icon" target="_blank" href="http://jiaofei.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>水电煤</span>
#                 </a>
#             </li>
#             <li class="fore11" clstag="h|keycount|2015|10b11">
#                 <a class="cw-icon" target="_blank" href="http://z.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>众筹</span>
#                 </a>
#             </li>
#             <li class="fore9" clstag="h|keycount|2015|10b09">
#                 <a class="cw-icon" target="_blank" href="http://licai.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>理财</span>
#                 </a>
#             </li>
#             <li class="fore12" clstag="h|keycount|2015|10b12">
#                 <a class="cw-icon" target="_blank" href="http://giftcard.jd.com/market/index.action">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>礼品卡</span>
#                 </a>
#             </li>
#             <li class="fore10" clstag="h|keycount|2015|10b10">
#                 <a class="cw-icon" target="_blank" href="http://baitiao.jd.com/">
#                     <i class="ci-left" style="background-image: url(http://img14.360buyimg.com/da/jfs/t1456/28/1208095754/7218/651e2541/55bf27beN7565bc0e.png);_background-image: url(http://img14.360buyimg.com/da/jfs/t1396/62/1212384285/4632/c314ab35/55bf27d6N9a8eae98.png);"></i><span>白条</span>
#                     <i class="ci-tip" style="width:12px;height:15px;top:0px;right:3px;background: url(http://img12.360buyimg.com/da/jfs/t2332/40/253298210/1032/55bc7991/55fa838bNd53c791c.png);_background: url(http://img11.360buyimg.com/da/jfs/t1777/221/1595870691/1018/dfa81ce9/55fa8394N32470916.png); no-repeat scroll 0 0"></i>
#                 </a>
#             </li>
#         </ul>
#         <div class="mc-inner hide">
#             <a class="close">×</a>
#             <div class="hide"></div>
#             <div class="hide"></div>
#             <div class="hide"></div>
#             <div class="hide"></div>
#         </div>
#     </div>
# </div><!--index_ok-->

# </div>


#     <div class="lazy-fn-wrap clearfix" data-space="1">
#     <div class="w lazy-fn" id="lazy-todays" data-path="todayRecommend-todayRecommend.js" data-time="4d9ecf27194596a25da8e1f5d65c1a86" ></div>
#     <div class="w lazy-fn" id="lazy-guess-like" data-path-js="product/home/1.0.0/widget/guess-like/guess-like.js"></div>
#     <div class="w lazy-fn" id="lazy-special-buy-v2" data-path="featuresPurchase-featuresPurchaseV2.js" data-time="df29a9f7f2d79aa72def14520fdcb9f4"></div>
# </div>
# <div class="lazy-fn-wrap clearfix" data-space="2">
#     <div class="floor-banner-body lazy-fn" id="lazy-floor-banner-1"  data-path="floor1-floor_banner.js" data-time="d18850ed426855ee9a3811014021f4c3"></div>
#     <div class="w floor lazy-fn" data-title="服饰" id="lazy-clothes" data-path="floor1-floor_index.js" data-time="b499fc7ac7027fde63dbe7e15bebbc42"></div>
#     <div class="w floor lazy-fn" data-title="美妆" id="lazy-cosmetics" data-path="floor2-floor_index.js" data-time="c87cbd7fb7765f3076a324c2b63cbcf6"></div>
#     <div class="floor-banner-body lazy-fn" id="lazy-floor-banner-2"  data-path="floor3-floor_banner.js" data-time="94b025167762de2afd49d85033cdaf61"></div>
#     <div class="w floor lazy-fn" data-title="手机" id="lazy-mobiles" data-path="floor5-floor_index.js" data-time="efd58a0f8ede5514d5e8a1d71460b24d"></div>
#     <div class="w floor lazy-fn" data-title="家电" id="lazy-electronics" data-path="floor3-floor_index.js" data-time="e446e4526101388eaf7aabde31759638"> </div>
#     <div class="w floor lazy-fn" data-title="数码" id="lazy-digitals" data-path="floor4-floor_index.js" data-time="baa97af471fdd5463553524425aa7ff9"></div>
#     <div class="floor-banner-body lazy-fn" id="lazy-floor-banner-3"  data-path="floor6-floor_banner.js" data-time="cfc1be7f936cda88f195d85cd0cb70a8"> </div>
#     <div class="w floor lazy-fn" data-title="运动" id="lazy-sports" data-path="floor6-floor_index.js" data-time="16218e5b3450e122f69e09066d13caeb"></div>
#     <div class="w floor lazy-fn" data-title="居家" id="lazy-livings" data-path="floor7-floor_index.js" data-time="7d812bff4efae5153675e144ac9968af"></div>
#     <div class="w floor lazy-fn" data-title="母婴" id="lazy-babys" data-path="floor8-floor_index.js" data-time="0ce383cb48e96c48ec3ca984ac3a07f8"></div>
#     <div class="w floor lazy-fn" data-title="食品" id="lazy-foods" data-path="floor9-floor_index.js" data-time="7fdf4386b951bc7514793bbd8d8111a5"></div>
#     <div class="floor-banner-body lazy-fn" id="lazy-floor-banner-4" data-path="floor10-floor_banner.js" data-time="10a7a04d657fb9a8e1d7a4a03fdb87c2" ></div>
#     <div class="w floor lazy-fn" data-title="图书" id="lazy-books" data-path="floor10-floor_index.js" data-time="41ae763572de4a521b8d27350fbd4016"></div>
#     <div class="w floor lazy-fn" data-title="服务" id="lazy-life" data-path="floor11-floor_index.js" data-time="28a3d24fde07f00e3de368e0f51d4c3b"></div>
#     <div class="w clearfix lazy-fn" id="lazy-special" data-path="special-special.js" data-time="17a6abc49239554c5cbc483dae1e42f6"></div>
#     <div class="lazy-fn" id="lazy-footer" data-path-js="product/home/1.0.0/widget/home-footer/home-footer.js"></div>
# </div><!--index_ok-->

# <script type="text/javascript" src="http://misc.360buyimg.com/??jdf/lib/jquery-1.6.4.js,jdf/1.0.0/ui/ui/1.0.0/ui.js"></script>
# <script type="text/javascript" src="http://misc.360buyimg.com/product/home/1.0.0/js/init.js"></script>
# <script type="text/javascript" src="http://wl.jd.com/wl.js"></script>
# <script type="text/javascript">
# !function(a,b){function c(){var a=b("#J-banner-top"),c=b("#J-banner-close"),d=b("#J-openapp"),f='openApp.jdiPad://CPS?params={"category":"jump","des":"Home","SourceType":"PC"}';c[0].addEventListener("click",function(){l.set(p,"false",{expires:3}),a.animate({height:0},"fast")},!1),d[0].addEventListener("click",function(){e(f);try{var a="MPCHomeMain_OpenApp",b=new MPing.inputs.Click(a);b.updateEventSeries();var c=new MPing;c.send(b)}catch(d){}},!1)}function d(){var a='<div id="J-banner-top" class="banner-top">';a+='<a class="link">',a+='   <img src="http://img12.360buyimg.com/da/jfs/t1150/27/693141209/10948/be228f20/553de1fcNc9986b77.png" class="logo" width="50" height="50">',a+='       <span class="top-info">上iPad客户端 首单满79送79元，更有无线专享商品天天秒杀！</span>',a+='       <span id="J-openapp" class="btn">立即打开</span>',a+="    </a>",a+='   <a href="javascript:;" id="J-banner-close" class="close">X</a>',a+="</div>";var c=["*{margin:0;padding:0;}",'.banner-top {position:relative; height: 80px;background-color: #44444E; font-family: "Helvetica Neue", Helvetica, DroidSansFallback, HeiTi SC, Arial, sans-serif; overflow: hidden;width:990px;}',".banner-top .link{display:block; padding-left: 54px;padding-right:64px; overflow: hidden;}",".banner-top .logo{float: left; margin-top: 15px;}",".banner-top .top-info{float: left; margin-top: 28px; padding-left: 20px; color: #FFF; font-size: 16px;}",".banner-top .btn{float: right; padding: 8px 30px; margin-top: 25px; border-radius: 5px; background-color: #FFF; font-size: 14px; color: #333;}",".banner-top .close{position: absolute; right: 10px; top: 10px; width: 20px;height: 20px;border-radius: 10px;background-color: #2E2E35; color: #D5D5D6; line-height: 22px;text-decoration: none !important; text-align: center;font-family: Arial; font-size: 12px;}"].join("");b("<style></style>").html(c).appendTo(b("head")),b("body").prepend(b(a));try{var d="MPCHomeMain_OpenApp_Expo",e=new MPing.inputs.Click(d);e.updateEventSeries();var f=new MPing;f.send(e)}catch(g){}}function e(a){var b,c="https://itunes.apple.com/cn/app/jing-dong-hd/id434374726";o||(o=document.createElement("iframe"),o.style.display="none",o.style.height="0",o.style.width="0",document.body.appendChild(o)),o.src=a,b=setTimeout(function(){location=c},100)}function f(a,b){var c,d,e,f=document.head||document.getElementsByTagName("head")[0]||document.documentElement;"object"==typeof a&&(d=a,a=void 0),e=d||{},a=a||e.url,b=b||e.success,c=document.createElement("script"),c.async=e.async||!1,c.type="text/javascript",e.charset&&(c.charset=e.charset),e.cache===!1&&(a=a+(/\?/.test(a)?"&":"?")+"_="+(new Date).getTime()),c.src=a,f.insertBefore(c,f.firstChild),b&&(document.addEventListener?c.addEventListener("load",b,!1):c.onreadystatechange=function(){/loaded|complete/.test(c.readyState)&&(c.onreadystatechange=null,b())})}function g(a,b){var c={};if(h(a)&&a.length>0)for(var d,e,f,g=b?m:k,i=a.split(/;\s/g),j=0,l=i.length;l>j;j++){if(f=i[j].match(/([^=]+)=/i),f instanceof Array)try{d=m(f[1]),e=g(i[j].substring(f[1].length+1))}catch(n){}else d=m(i[j]),e="";d&&(c[d]=e)}return c}function h(a){return"string"==typeof a}function i(a){return h(a)&&""!==a}function j(a){if(!i(a))throw new TypeError("Cookie name must be a non-empty string")}function k(a){return a}var l={},m=decodeURIComponent,n=encodeURIComponent;l.get=function(a,b){j(a),b="function"==typeof b?{converter:b}:b||{};var c=g(document.cookie,!b.raw);return(b.converter||k)(c[a])},l.set=function(a,b,c){j(a),c=c||{};var d=c.expires,e=c.domain,f=c.path;c.raw||(b=n(String(b)));var g=a+"="+b,h=d;return"number"==typeof h&&(h=new Date,h.setDate(h.getDate()+d)),h instanceof Date&&(g+="; expires="+h.toUTCString()),i(e)&&(g+="; domain="+e),i(f)&&(g+="; path="+f),c.secure&&(g+="; secure"),document.cookie=g,g},l.remove=function(a,b){return b=b||{},b.expires=new Date(0),this.set(a,"",b)};var o,p="showIPadTop",q=navigator.userAgent.toLowerCase(),r=function(){var a=/iPad/i;return a.test(q)}(),s=l.get(p);return r&&"false"!==s?void f({url:"http://h5.m.jd.com/active/track/mping.min.js",async:"async"},function(){d(),c()}):!1}(window,jQuery);
# </script>
# <!--index_ok-->

#     <script type="text/javascript">
#     function dataHandle_6858_6859(config) {

#     // 未设置顶通背景图则直接退出，避免显示异常
#     if (config.bg == undefined) {
#         return;
#     }
#     // 2个顶通背景对刷，随机选择
#     config.bg.sort(function() {
#         return 0.5 - Math.random()
#     });

#     // 广告词打乱顺序
#     config.list.sort(function () {
#         return 0.5 - Math.random();
#     });

#     // 单次展示最多选取20条，避免页面DOM数暴增
#     config.list.splice(20);

#     // 注意事项：
#     // 1. 首页默认的顶通广告位在双十一期间需要暂时下线。
#     // 2. 广告位埋点数据需要业务方更新。
#     // 3. 注意检查走马灯文字是否因为过长被遮盖。
#     // 4. 顶通背景色通过广告位ext1字段设置。

#     // 关闭时间判断，由后台控制
#      var narrowVersion = screen.width < 1210 || /isdebug=(-\d)*-2/.test(location.search);
#     // var currentTime = getCurrentTime();
#     // var showZMD = false;
#     // // 是否显示走马灯
#     // var time_1026_000000 = 1445788800000;
#     // var time_1031_235959 = 1446307199000;


#     // 2015-10-26 00:00:00 => 1433088000000
#     // 2015-10-31 23:59:59 => 1446307199000 顶通跑马灯10月26日~10月31日
#     // 还未到10月26日，或10月31日后完全不显示，包括背景图
#     // if (currentTime < time_1026_000000 || currentTime > time_1031_235959) {
#     //     return;
#     // }

#     // if (config.list && config.list.length > 0) {
#     //     showZMD = true;
#     // }

#     showZMD = true;

#     var html = buildHTML(showZMD);
#     var styleText = "#top-banner-20151111{width:100%;height:80px;margin:0 auto;overflow:hidden}#top-banner-20151111 img{vertical-align:top}#marquee-20151111{overflow:hidden;position:relative;width:180px;height:80px;font-family:'microsoft yahei'}#marquee-20151111 .act1111-list{width:173px;overflow:hidden}#marquee-20151111 .act1111-list li{float:left;width:173px;height:24px;margin-bottom:4px;position:relative;*float:left;overflow:hidden;-webkit-box-shadow:0 2px 2px rgba(0,0,0,.3);-moz-box-shadow:0 2px 2px rgba(0,0,0,.3);box-shadow:0 2px 2px rgba(0,0,0,.3);background:url(http://img10.360buyimg.com/da/jfs/t2497/135/694419556/3569/f1eb2f20/56237614N8a57de6c.png) no-repeat}#marquee-20151111 .act1111-list li .bg{display:none}#marquee-20151111 .act1111-list li a{display:block;width:164px;height:14px;max-height:14px;line-height:14px;padding:4px 0 6px 10px;overflow:hidden}#marquee-20151111 .act1111-list li .tag,#marquee-20151111 .act1111-list li .txt{float:left;color:#fff;height:14px;line-height:14px;cursor:pointer}#marquee-20151111 .act1111-list li .tag{width:30px;margin-right:20px;text-align:center}#marquee-20151111 .act1111-list li .txt{width:108px;overflow:hidden;text-shadow:1px 1px 1px rgba(0,0,0,.3)}#marquee-20151111 .act1111-list li.hover{background:url(http://img12.360buyimg.com/da/jfs/t1930/106/766149248/3030/f2cc4d41/56237586N8ac6049f.png) no-repeat}#marquee-20151111 .act1111-list li.hover .txt{color:#fffa88}";
#     insertStyles(styleText);
#     $('#shortcut-2014').after(html);

#     bindEvent(showZMD);

#     function buildHTML(showZMD) {
#         var marqueeHTML = "";
#         var bg = compatibleSet(config.bg[0]);
#         var bgColor = bg.ext1 ? 'background-color:#' + bg.ext1.replace(/#/g, '') + ';': '';
#         var left = narrowVersion ? '792px': '1012px';
#         var topZMD;

#         var i;

#         if (showZMD) {
# var marquee = ['<div id="marquee-20151111" style="left:' + left +
# ';top:-80px">', '<ul class="act1111-list" >'];

#             for (i = 0; i < config.list.length; i++) {
#                 marquee.push('<li class="act1111-item"><a clstag="h|keycount|2015|00a_' + config.list[i].trackcode + '" href="' + config.list[i].href + '" target="_blank"><span class="tag">' + config.list[i].tag.substr(0, 2) + '</span><em class="txt">' + config.list[i].des + '</em></a></li>');
#             }

#             marquee.push('</ul></div>');

#             marqueeHTML = marquee.join(" ");
#         }

#         var html = ['<div id="top-banner-20151111" style="' + bgColor + '">', '<div class="w" style="position:relative;">', '<a clstag="h|keycount|2015|00a" href="' + bg.href + '" target="_blank">', '<img src="' + bg.src + '" width="' + bg.width + '" height="80">', '</a>', marqueeHTML, '</div>', '</div>'];
#         return html.join(" ");
#     }

#     function bindEvent(showZMD) {
#         if (showZMD) {
#             seajs.use(['jdf/1.0.0/ui/switchable/1.0.0/switchable'],
#             function() {
#                 $('#marquee-20151111').switchable({
#                     type: 'slider',
#                     contentClass: 'act1111-list',
#                     mainClass: 'act1111-item',
#                     direction: 'top',
#                     seamlessLoop: true,
#                     includeMargin: true,
#                     autoPlay: true,
#                     playDirection: 'next',
#                     stayTime: 3000,
#                     step: 1,
#                     visible: 3,
#                     height: 28
#                 });
#             });

#             $("#marquee-20151111").delegate('li', 'mouseenter', function () {
#                 $(this).addClass("hover");
#             });

#             $("#marquee-20151111").delegate('li', 'mouseleave', function () {
#                 $(this).removeClass("hover");
#             });
#         }
#     }

#     function compatibleSet(object) {
#         if (narrowVersion) {
#             object.width = object.widthB ? object.widthB: object.width;
#             object.height = object.heightB ? object.heightB: object.height;
#             object.src = object.srcB ? object.srcB: object.src;
#         }
#         return object;
#     };

#     function insertStyles(cssString) {
#         var doc = document,
#         heads = doc.getElementsByTagName("head"),
#         style = doc.createElement("style"),
#         link = doc.createElement("link");
#         if (/\.css$/.test(cssString)) link.rel = "stylesheet",
#         link.type = "text/css",
#         link.href = cssString,
#         heads.length ? heads[0].appendChild(link) : doc.documentElement.appendChild(link);
#         else {
#             if (style.setAttribute("type", "text/css"), style.styleSheet) style.styleSheet.cssText = cssString;
#             else {
#                 var cssText = doc.createTextNode(cssString);
#                 style.appendChild(cssText)
#             }
#             heads.length && heads[0].appendChild(style)
#         }
#     };

#     function getCurrentTime() {
#         var serverTime, currentTime;
#         var localTime = (new Date()).valueOf();
#         var result;
#         if (window.pageConfig && window.pageConfig.timestamp) {
#             serverTime = window.pageConfig.timestamp;
#         }

#         if (serverTime) {
#             // 如果本地时间比服务器时间快5分钟之内，则使用本地时间(更精确，因为服务器时间有CDN延迟)
#             if ((localTime > serverTime) && (localTime - serverTime) / 1000 < 300) {
#                 currentTime = localTime;
#             } else {
#                 currentTime = serverTime;
#             }
#         } else {
#             currentTime = localTime;
#         }

#         if (result = window.location.search.match(/isdebugServerTime=([\d-]+)/)) {
#             result = result[1].split(/-/);
#             currentTime = (new Date(result[0], result[1] - 1, result[2], result[3], result[4], result[5])).valueOf();
#         }

#         return currentTime;
#     }
# }
#         dataHandle_6858_6859({
#     bg: [

#     {
#         src: 'http://img12.360buyimg.com/da/jfs/t2065/199/859498377/37097/d6b562b5/562e1a96N422f8c34.jpg',
#         srcB: 'http://img10.360buyimg.com/da/jfs/t2023/221/814478979/31305/1624c065/562e1a99N4772734c.jpg',
#         href: 'http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mZIX6PRJqjCheeObEYAlcRIYNQ6+FOBziNxSx73BZ8spFCdKSYYEPOZcVHAoH9Xqzn87g5dn6WryBofegWFXtfVHWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakuaSE9FCbUazZlNpAmySjW+Tl0RnD5lSCmOXQ4AoBzwqO8kB+sSzSS0dWVpqx287jLMnQRjLX8LeruC5DQu2wwDKXBn/4XyfZBkqZDvr0dRqsYAhmxRmBoISpVNFyZRXL4a+892nOos/0aSRnf6vbMmf9HLeDipRHAKm4vcfN+U1KKFU6qVYkYEbrR18iEkgIA==&cv=2.0&url=http://sale.jd.com/act/q4NHmiVZEOt7G.html',
#         width: '1210',
#         widthB: '990',
#         height: '80',
#         ext1: 'ca0022'
#     }
#     ,
#     {
#         src: 'http://img13.360buyimg.com/da/jfs/t1870/348/840649168/37097/d6b562b5/562ed058N284c20e3.jpg',
#         srcB: 'http://img11.360buyimg.com/da/jfs/t1999/361/839793147/31305/1624c065/562ed061N1d72f2cc.jpg',
#         href: 'http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mZIX6PRJqjCheeObEYAlcRIYNQ6+FOBziNxSx73BZ8spUmj0c163e3Y9jlNHwp0k12MMfg2r29fFwZKBI3MK4dlHWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakuaSE9FCbUazZlNpAmySjW+Tl0RnD5lSCmOXQ4AoBzwqO8kB+sSzSS0dWVpqx287jLMnQRjLX8LeruC5DQu2wwDKXBn/4XyfZBkqZDvr0dRqsYAhmxRmBoISpVNFyZRXL4a+892nOos/0aSRnf6vbMmf9HLeDipRHAKm4vcfN+U1KKFU6qVYkYEbrR18iEkgIA==&cv=2.0&url=http://sale.jd.com/act/q4NHmiVZEOt7G.html',
#         width: '1210',
#         widthB: '990',
#         height: '80',
#         ext1: 'ca0022'
#     }
#     ],

#             list: [
#         {
#             tag: '男装',
#             des: '大尺度男装券等你来',
#             href: 'http://sale.jd.com/act/IDdbUafVgXqHRhJy.html',
#             trackcode: 'dzw12'
#         }
#         ,{
#             tag: '运动',
#             des: '运动领券享满减',
#             href: 'http://sale.jd.com/act/Dn3SclLdfAytQEvT.html',
#             trackcode: 'dzw13'
#         }
#         ,{
#             tag: '奢品',
#             des: '满减优惠券放肆抢',
#             href: 'http://sale.jd.com/act/PWVTgjNw6muGJQ.html',
#             trackcode: 'dzw14'
#         }
#         ,{
#             tag: '儿童',
#             des: '宝贝萌品百万优惠券',
#             href: 'http://sale.jd.com/act/QeatAZ2huzo1C.html',
#             trackcode: 'dzw15'
#         }
#         ,{
#             tag: '食品',
#             des: '美食满减疯抢11天',
#             href: 'http://sale.jd.com/act/cXFd0qwpuZ4xosD.html',
#             trackcode: 'dzw16'
#         }
#         ,{
#             tag: '酒饮',
#             des: '300元神券免费领',
#             href: 'http://sale.jd.com/act/X6mOosHRxPBvjV.html',
#             trackcode: 'dzw17'
#         }
#         ,{
#             tag: '美妆',
#             des: '国际大牌抢先看',
#             href: 'http://sale.jd.com/act/ti1vXdINr6.html',
#             trackcode: 'dzw18'
#         }
#         ,{
#             tag: '个护',
#             des: '爆款单品抢先关注',
#             href: 'http://sale.jd.com/act/ilDfk0JzSa.html',
#             trackcode: 'dzw19'
#         }
#         ,{
#             tag: '女装',
#             des: '精品优惠券限量抢',
#             href: 'http://sale.jd.com/act/xtwUGlvqV8kM0B.html',
#             trackcode: 'dzw11'
#         }
#         ,{
#             tag: '汽车',
#             des: '车品嗨爆年度低价',
#             href: 'http://sale.jd.com/act/klVZOFJfGyBM7.html',
#             trackcode: 'dzw10'
#         }
#         ,{
#             tag: '办公',
#             des: '投影神券大放送',
#             href: 'http://sale.jd.com/act/Xit5CNhzKu1om7w.html',
#             trackcode: 'dzw2'
#         }
#         ,{
#             tag: '数码',
#             des: '10亿神券疯狂抢',
#             href: 'http://sale.jd.com/act/Co2sQmHX8Nen.html',
#             trackcode: 'dzw3'
#         }
#         ,{
#             tag: '通信',
#             des: '抢靓号送语音送流量',
#             href: 'http://sale.jd.com/act/4Tfn1K2oGzk.html',
#             trackcode: 'dzw4'
#         }
#         ,{
#             tag: '手机',
#             des: '8亿优惠券大让利',
#             href: 'http://sale.jd.com/act/IbdqXpVU7GRN.html',
#             trackcode: 'dzw5'
#         }
#         ,{
#             tag: '生活',
#             des: '手机流量免费送',
#             href: 'http://sale.jd.com/act/KYZbk5Ex6uSBrhL.html',
#             trackcode: 'dzw6'
#         }
#         ,{
#             tag: '团购',
#             des: '60元NB券抢先领',
#             href: 'http://sale.jd.com/act/U8PYMGrp2QqcOC1.html',
#             trackcode: 'dzw7'
#         }
#         ,{
#             tag: '图书',
#             des: '图书五周年满减在即',
#             href: 'http://sale.jd.com/act/midqPBTzYL.html',
#             trackcode: 'dzw8'
#         }
#         ,{
#             tag: '家居',
#             des: '满减神券免费领',
#             href: 'http://sale.jd.com/act/CfE6xL0Omzel.html',
#             trackcode: 'dzw9'
#         }
#         ,{
#             tag: '母婴',
#             des: '奶粉领券300减30',
#             href: 'http://sale.jd.com/act/krBMbH1j6KRuUE.html',
#             trackcode: 'dzw20'
#         }
#         ,{
#             tag: '全球',
#             des: '全球大牌特卖会',
#             href: 'http://sale.jd.com/act/fQ4uMWwdq5OLKo.html',
#             trackcode: 'dzw21'
#         }
#         ,{
#             tag: '家电',
#             des: '10元买900元券',
#             href: 'http://sale.jd.com/act/Dbtsrjw10WXHm6u.html',
#             trackcode: 'dzw22'
#         }
#         ,{
#             tag: '家电',
#             des: '80元东券仅售10元',
#             href: 'http://sale.jd.com/act/UM5itNRnl2.html',
#             trackcode: 'dzw23'
#         }
#         ,{
#             tag: '钟表',
#             des: '名表领券享满减',
#             href: 'http://sale.jd.com/act/1QrRsueYog3iz.html',
#             trackcode: 'dzw24'
#         }
#         ,{
#             tag: '专享',
#             des: '亿元优惠券等你抢',
#             href: 'http://sale.jd.com/act/lcUPzRiEsjZ.html',
#             trackcode: 'dzw25'
#         }
#         ,{
#             tag: '电脑',
#             des: '笔记本神券抢不停',
#             href: 'http://sale.jd.com/act/L82e6RZDxiEtUPk.html',
#             trackcode: 'dzw1'
#         }
#     ]
# });


#     /* xiaojinku */
# (function(){if(!pageConfig.wideVersion){return;}var html = '';html = '<a style="float:right;width:140px;height:40px;cursor:pointer;display:block;margin-top:2px;position:relative;z-index:2;" href="http://c-nfa.jd.com/adclick?keyStr=z5AXFoIimt1jiDK32+w4mWlR1HP401IHmvwFQGlQg638WCZpcGV2iFV+NNq5Kf3oiD9ytKezVTM1gpWSBrgh9fwBPWh6cx9gX5Fai1JoghNHWmoByPeXmwN+vPPmAue8nPRVaxDTMvb4FGTgPthakjVoyYMgeystLq1UIqijgPGnZ6kYwsY/2FAosiX/1DToQBm0Myq73ZmTaMYtfetTW8ZG+bOJzueASAX30AkC+BJM7KhKAzacsw4AdWt8CpsTWGOQzs6c6SvsrASo0uZP0+sMmgEhkY9EeMVx6X1nDXuTWk+LdBAe6AGHS3ze5vGalrw0VRUczI/aZKUbzeydkA==&cv=2.0&url=http://sale.jd.com/act/w2kQpxmqCS.html" target="_blank" title="" clstag="h|keycount|2015|07a" fclog="9348.100234.223143.1.2_955_6216"><em style="float:left;width:140px;height:40px;background:url(http://img11.360buyimg.com/da/jfs/t2113/316/847124125/15589/eb2b388c/562ed562N1c7848b1.jpg) no-repeat;">&#160;</em></a>';$("#treasure").html(html);})();

# /**toolbar*/
# (function(){
#     pageConfig.toolbar = true;
#     if ( $('#J-global-toolbar').length ) return false;
#     $("body").append('<div id="J-global-toolbar"></div>');
#     var opts = {pType: 'home'};
#     var url = 'product/toolbar/1.0.1/js/main.js';

#     function isDB11(){
#         if ( /test_r_toolbar=1/.test(location.search) ) return true;
#         if ( !window['pageConfig'] || !pageConfig['timestamp'] ) return false;
#         var startTime = 1445788800000;//+new Date('2015/10/26 00:00:00');
#         var endTime = 1447344000000;//+new Date('2015/11/13 00:00:00');
#         var curDate = new Date(pageConfig.timestamp);
#         var curLocalDate = new Date();

#         //校正时间，cdn会有0-5分钟左右缓存时间，所以判断本地时间在这5分钟范围内的话，就用本地时候作为系统时间
#         if ( curLocalDate.getTime() > curDate.getTime() && curLocalDate.getTime() < curDate.getTime() + 300000) {
#             curDate = new Date();
#         }

#         //如果没有系统时间或未在指定的时间内，不执行
#         return !isNaN( curDate ) && curDate >= startTime && curDate < endTime;
#     }

#     if ( isDB11() ) {
#         url = '//static.360buyimg.com/devfe/toolbar/1.0.0/js/main.js';
#         opts.ad = {
#             id: "0_0_7209",
#             startTime: +new Date(2015, 9, 25, 0, 0, 1) / 1000,
#             endTime: +new Date(2015, 10, 13, 0, 0, 0) / 1000
#         };
#     }

#     seajs.use([url], function(toolbar) {
#         var linksConfig = {top:{anchor:"#"}};
#         if(pageConfig.surveyLink) {linksConfig.feedback = { href : pageConfig.surveyLink };}
#         if(pageConfig.awardsLink && pageConfig.awardsTitle ) linksConfig.survey = { href : pageConfig.awardsLink, title:pageConfig.awardsTitle }
#         opts.links = linksConfig;
#         pageConfig.toolbar = new toolbar(opts);
#     });
# })();

# seajs.use('jdf/1.0.0/unit/insertStyles/1.0.0/insertStyles.js',function(insertStyles){insertStyles('.root61
# #focus{margin:0 auto;width:1210px;}#focus{margin:0
# auto;width:990px;}');});

# /* nav icon */
# (function(){
#     if ( !window['pageConfig'] || !pageConfig['timestamp'] ) return false;
#     var timestamp = pageConfig.timestamp;
#     var newicon = '//img14.360buyimg.com/da/jfs/t2035/288/642332786/1170/3ab523bc/561dcb61N07241b06.png';
#     if ( $.browser.isIE6() ) {
#         newicon = '//img13.360buyimg.com/da/jfs/t2221/259/650376358/1120/17900559/561dcb7aNe71c4091.png';
#     }
#     /* 2015/10/15 - 2015/10/21*/
#     if(/isshowtip=1/.test(location.search) || (!isNaN(timestamp) && (timestamp >= 1444838400000 && timestamp <= 1445443200000))){
#         $('#nav-jr').css('position','relative').append('<img src="'+newicon+'" style="position:absolute;right:-17px;top:1px;" >');
#     }
# })();
# </script><!--index_ok-->


# <img src="http://ccc.jd.com/cookie_check" width="1" height="1" />
# </body>
# </html><!--index_ok-->
# [Finished in 22.7s]
