from netmiko.ssh_dispatcher import ConnectHandler
import getpass

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.135',
    'username': 'admin',
    'password': '',
    'port': 22
}

password = getpass.getpass()

device['password'] = password

conn = ConnectHandler(**device)

config = ['do sh ip int brief', 'do sh clock']

sender = conn.send_config_set(config)

print(sender)

