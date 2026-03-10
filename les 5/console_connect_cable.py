from netmiko import ConnectHandler

platform = 'cisco_ios_serial'
port = 'COM3' #afhankelijk van je aparaatbeheer
baudrate= 9600

device_object= ConnectHandler(device_type=platform, serial_settings= {
"port": port,
"baudrate": baudrate})

print(device_object.send_command("show version"))

print(Connection.check_enable_mode())
print("dit is leuk")

print(connection.send_command("show version", use_textfsm = True))

#>output.txt je notities schrijven naar een bestand