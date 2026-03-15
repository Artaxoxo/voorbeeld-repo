from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'S1',
    'password': 'cisco',
    'secret': 'class',
    'port': 5,
}
# Connect via SSH
ssh = ConnectHandler(**cisco_router)

# Switch to enable mode:
ssh.enable()

# Exit enable mode:
ssh.exit_enable_mode()