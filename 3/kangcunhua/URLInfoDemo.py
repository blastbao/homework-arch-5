#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 10:54:24
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import urllib
import urllib2

url = 'https://github.com'
req = urllib2.Request(url)
response = urllib2.urlopen(req)

print response.info()
print response.info.__class__

# output: 51reboot.com
# Date: Sun, 25 Oct 2015 03:03:02 GMT
# Server: Apache/2.4.2 (Unix) OpenSSL/1.0.1e-fips PHP/5.3.13
# Last-Modified: Fri, 09 Oct 2015 09:33:30 GMT
# ETag: "2f05-521a8ac2a17e9"
# Accept-Ranges: bytes
# Content-Length: 12037
# Vary: Accept-Encoding
# Connection: close
# Content-Type: text/html


# <type 'instancemethod'>
# [Finished in 1.6s]


# output: github.com
# Server: GitHub.com
# Date: Sun, 25 Oct 2015 02:57:32 GMT
# Content-Type: text/html; charset=utf-8
# Transfer-Encoding: chunked
# Connection: close
# Status: 200 OK
# Content-Security-Policy: default-src *; script-src assets-cdn.github.com; object-src assets-cdn.github.com; style-src 'self' 'unsafe-inline' 'unsafe-eval' assets-cdn.github.com; img-src 'self' data: assets-cdn.github.com identicons.github.com www.google-analytics.com checkout.paypal.com collector.githubapp.com *.githubusercontent.com *.gravatar.com *.wp.com; media-src 'none'; frame-src 'self' render.githubusercontent.com gist.github.com www.youtube.com player.vimeo.com checkout.paypal.com; font-src assets-cdn.github.com; connect-src 'self' live.github.com wss://live.github.com uploads.github.com status.github.com api.github.com www.google-analytics.com api.braintreegateway.com client-analytics.braintreegateway.com github-cloud.s3.amazonaws.com; base-uri 'self'; form-action 'self' github.com gist.github.com
# Public-Key-Pins: max-age=300; pin-sha256="WoiWRyIOVNa9ihaBciRSC7XHjliYS9VwUGOIud4PB18="; pin-sha256="JbQbUG5JMJUoI6brnx0x3vZF6jilxsapbXGVfjhN8Fg="; includeSubDomains
# Cache-Control: no-cache
# Vary: X-PJAX
# X-UA-Compatible: IE=Edge,chrome=1
# Set-Cookie: logged_in=no; domain=.github.com; path=/; expires=Thu, 25 Oct 2035 02:57:32 -0000; secure; HttpOnly
# Set-Cookie: _gh_sess=eyJzZXNzaW9uX2lkIjoiMmZiMWE4YzA4YTUzMGRjM2NkZjNiOGEyYWZlMTdiOTEiLCJfY3NyZl90b2tlbiI6IkxkTWhWVVlRemhxVHBab0twN0plQVdJVnkxa0JHVElXVm9WQk5iVis0d3c9In0%3D--769b2a2b11762180d18c382b142a95a3e6d9205d; path=/; secure; HttpOnly
# X-Request-Id: c21d5744be55b04cd2e7df00c7cff7e7
# X-Runtime: 0.008363
# Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
# X-Content-Type-Options: nosniff
# X-XSS-Protection: 1; mode=block
# X-Frame-Options: deny
# Vary: Accept-Encoding
# X-Served-By: a22dbcbd09a98eacdd14ac7804a635dd
# X-GitHub-Request-Id: 01CA41A9:094E:1B93633:562C451C

# <type 'instancemethod'>
# [Finished in 2.7s]
