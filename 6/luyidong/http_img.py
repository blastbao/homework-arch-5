from daemon import Daemon
import socket
import Queue
import threading
import time

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection:close\r\nContent-Length:  """
html = 404 = """ """
