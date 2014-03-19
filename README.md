# nLight Reverse Engineering

###UDP Server

Do `python listen.py <UDP port num>` to listen for UDP packets on a given port. `2254` seems to be the default for SensorView

### Dumps

The `dumps` folder contains raw packet sequences:

* `occupied-10-thru-50.pcapng`: unoccupied set to 10%, occupied set incrementally 10%, 20%, ... 50%
* `unoccupied-10-thru-50.pcapng`: occupied set to 10%, unoccupied set incrementally 10%, 20%, ... 50%
* `setup-sequence-192.168.1.6-to-192.168.1.4.pcapng`: series of packets observed while commissioning the nLight SensorView software

### Other files

`process.txt` contains my best guess for the order of packets sent during an acutation command

`status.txt`: more thoughts on the process:

`packetcomaprison.txt`: contains sequences of packets side by side for comparison

`setup_sequence.txt`: contains order of packets sent during setup sequence


