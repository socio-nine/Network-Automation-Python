from netmiko import ConnectHandler
import logging

logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

base = {'device_type': 'f5_tmsh', 
    'username' : 'root',
    'password' : 'eve'}

# iosv_l2_1 = {
#     'ip': '10.10.20.177'
#     }

# iosv_l2_2 = {
#     'ip': '10.10.20.178',
#     }

# iosv = [iosv_l2_1, iosv_l2_2]

iosv1 = []

for i in ['10.100.115.100']:
    temp = {}
    temp.update({'ip' : str(i)})
    temp.update(**base)
    net_connect = ConnectHandler(**temp)

    print(net_connect.send_command('show sys ip-address', read_timeout=30, expect_string=r'Sys::'))

    # for n in range(110, 112):
    #     output = net_connect.send_config_set(['vlan ' + str(n), 'name hoge' + str(n)])
    #     print(output)

    # print(net_connect.send_command('copy running-config startup-config'))
