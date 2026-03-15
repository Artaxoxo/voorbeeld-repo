from netmiko import ConnectHandler

platform = 'cisco_ios_serial'
port = 'COM5'
baudrate = 9600

device_object = ConnectHandler(
    device_type=platform, 
    serial_settings = {
        "port": port,
        "baudrate": baudrate
    }
)

output = device_object.send_command("show version")

print(output)
with open("uitleg4-output-show-version.txt", "w") as f : 
    f.write(output)
