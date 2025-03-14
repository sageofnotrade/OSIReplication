import socket
import threading
import time

class PhysicalLayer:
    server_ready = threading.Event()

    def __init__(self, port=7777): 
        self.port = port
        self.received_data = None
        self.data_received = threading.Event()
        threading.Thread(target=self._start_server, daemon=True).start()

    def _start_server(self):
        """Starts the server and waits for data."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', self.port))
            s.listen(1)
            print(f"[Physical Layer] Server is now listening on port {self.port}!")  
            PhysicalLayer.server_ready.set()

            try:
                print("[Physical Layer] Waiting for a connection...\n")
                conn, addr = s.accept()
                print(f"[Physical Layer] Connection established with {addr}")  

                with conn:
                    binary_data = conn.recv(1024).decode()
                    if not binary_data:
                        print("[Physical Layer] No data received, closing connection.")
                        return

                    text_data = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
                    print(f"[Physical Layer] Received Data: {text_data}")  

                    self.received_data = text_data
                    self.data_received.set()
            except socket.timeout:
                print("[Physical Layer] No connection received, timeout.")

    def send(self, data):
        PhysicalLayer.server_ready.wait()
        time.sleep(1)
        binary_data = ''.join(format(ord(c), '08b') for c in data)

        print(f"[Physical Layer] Attempting to connect to localhost:{self.port}")  

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('localhost', self.port))  
                print("[Physical Layer] Connection successful!")  
                s.sendall(binary_data.encode())
                print("[Physical Layer] Data sent successfully!\n")  
        except ConnectionRefusedError:
            print("[Physical Layer] Connection refused! Is the server running?")

    def receive(self):
        """Wait until data is received, then return it."""
        self.data_received.wait()
        print(f"[Physical Layer] Forwarding Data Up: {self.received_data}") 
        return self.received_data
