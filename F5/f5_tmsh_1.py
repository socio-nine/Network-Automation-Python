from netmiko import ConnectHandler
import logging

logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

base = {'device_type': 'f5_tmsh', 
    'username' : 'root',
    'password' : 'eve'}

hosts = ['10.100.116.200', 
        '10.100.116.201']

for i in hosts:
    temp = {}
    temp.update({'ip' : str(i)})
    temp.update(**base)
    net_connect = ConnectHandler(**temp)

    # print(net_connect.send_command('show sys ip-address', read_timeout=30, expect_string=r'Sys::'))
    result=net_connect.send_command('show sys version', read_timeout=30, expect_string=r'Sys::')
    print('============== host: ' + i + ' ===================\n' + result)

    # for n in range(110, 112):
    #     output = net_connect.send_config_set(['vlan ' + str(n), 'name hoge' + str(n)])
    #     print(output)

    # print(net_connect.send_command('copy running-config startup-config'))
