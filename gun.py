# -*- coding: utf-8 -*
import os
import gevent.monkey
gevent.monkey.patch_all()
import multiprocessing
debug = False
loglevel = 'info'
bind = '0.0.0.0:8000'
# 日志
backlog = 64          #允许挂起的连接数的最大值，官方推荐这个值设在64-2048
timeout = 30             #超时时间，单位秒
worker_class = "gevent"  #工作方式，使用gevent模式，默认的是sync模式（并发只有1个），可选值eventlet、gevent、tornado、gthread、giohttp
worker_connections = 100  #进程链接数，默认值1000，同时链接客户端的阀值，这个设置只对进程工作方式为Eventlet和Gevent的产生影响
pidfile = 'log/gunicorn.pid'
#accesslog = "log/access.log"
errorlog = 'log/error.log'
# 开启后台执行
daemon = True
# 指定每个工作者的线程数
threads = 2
# 并行工作进程数，work数一般是2*cpu+1
workers = 2
x_forwarded_for_header = 'X-FORWARDED-FOR'