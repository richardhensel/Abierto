To set up:

1. Edit the file abierto.service. 
    Change the "USER=" to the user of the raspberrypi. 
    Change the "EXECUTE=" to the full path of the run script inside the Abierto/RaspberryPi directory. 

2. Copy the abierto.service file to /etc/systemd/system/

3. Enable the service "sudo systemctl enable abierto.service"

4. Start the service "sudo systemctl start abierto.service"

5. Test "systemctl status abierto.service"
