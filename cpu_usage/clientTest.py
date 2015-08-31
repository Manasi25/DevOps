import time
import paramiko
from multiprocessing import Pool
import datetime

def current_time_stamp():
  '''
    Displays Current Time stamp. Eg: 2013-02-30 22:34:40
  '''
  return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def query_server(server_ip):
  '''
    Method to query the server
    server_ip: server string to connect
  '''
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(server_ip, username = 'ubuntu', key_filename = '''/path_to_my_securitykey.pem''')
  stdin, stdout, stderr = client.exec_command('python /tmp/serverTest.py')
  
  error = stderr.read()

  if len(error) != 0:
    return "Server " + str(server_ip) + " Error: " + str(error.splitlines()[0])
  else:
    return "Server " + str(server_ip) + " CPU Usage: " + str(stdout.read().splitlines()[0])

# Public IPs of the servers
list_of_servers = ['xx.x.xxx.xx', 'xx.x.xxx.xx', 'xx.x.xxx.xx']

# Counting the number of servers
number_of_processes = len(list_of_servers)

# Set the number of processes
p = Pool(number_of_processes)

# Query the servers simultaneously
print "\nRUNNING IN PARALLEL WITH " + str(number_of_processes) + " PROCESSES"
print "-----------------------------"
print current_time_stamp()
print p.map(query_server, list_of_servers)
print current_time_stamp()

# Testing the response time of sequential server request without Pool Class
print "\nRUNNING SEQUENTIALLY"
print "-----------------------------"
print current_time_stamp()
print map(query_server, list_of_servers)
print current_time_stamp()
