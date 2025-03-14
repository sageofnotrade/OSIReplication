from OSI_Layers.DataLink import DataLinkLayer

class NetworkLayer:
    def __init__(self, ip_address="192.168.1.1", port=7777): 
        self.ip_address = ip_address
        self.datalink = DataLinkLayer(port=port)

    def send(self, data):
        """Encapsulate data into a network packet and send it."""
        packet = f"[NET]{data}[NET_END]"
        print(f"Network Layer Sending: {packet}")
        self.datalink.send(packet.encode(), mac_address="00:1A:2B:3C:4D:5E")  

    def receive(self):
        """Receive data from the Data Link Layer and extract the packet contents."""
        frame = self.datalink.receive()
        packet_str = frame.decode()
        
        if "[NET]" in packet_str and "[NET_END]" in packet_str:
            data = packet_str.split("[NET]")[1].split("[NET_END]")[0]
            print(f"Network Layer Received: {data}")
            return data.encode()
        else:
            print("[Network Layer] Error: Malformed packet received.")
            return b""
