from OSI_Layers.DataLink import DataLinkLayer

class NetworkLayer:
    def __init__(self, ip_address="192.168.1.1", port=12345):
        self.ip_address = ip_address
        self.datalink = DataLinkLayer(port=port)

    def send(self, data):
        packet = f"[NET]{data}[NET_END]"
        print(f"Network Layer Sending: {packet}")
        return packet.encode()
    
    def receive(self, packet):
        packet_str = packet.decode()
        data = packet_str.split("[NET]")[1].split("[NET_END]")[0]
        print(f"Network Layer Received: {data}")
        return data.encode()
