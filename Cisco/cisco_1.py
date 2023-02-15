from netmiko import ConnectHandler

base = {'device_type': 'cisco_ios', }




# iosv_l2_1 = {
#     'ip': '10.10.20.177'
#     }

# iosv_l2_2 = {
#     'ip': '10.10.20.178',
#     }

# iosv = [iosv_l2_1, iosv_l2_2]



iosv1 = []

credentials = open("credentials.txt", "r")
print(credentials.read())

# for i in range(177,179):
#     temp = {}
#     temp.update({'ip' : '10.10.20.' + str(i)})
#     temp.update(**base)
#     temp.update(**credentials)
#     # net_connect = ConnectHandler(**temp)
    
#     print(temp)
#     for n in range(110, 112):
#         # output = net_connect.send_config_set(['vlan ' + str(n), 'name hoge' + str(n)])
#         # print(output)

#     # print(net_connect.send_command('copy running-config startup-config'))
