import socket
import threading

class PhysicalLayer:
    # Event to signal when the server is ready
    server_ready = threading.Event()

    def __init__(self, port=12345):
        self.port = port
        self.received_data = None
        # Event to signal when data has been received
        self.data_received = threading.Event()
        # Start the server thread immediately.
        threading.Thread(target=self._start_server, daemon=True).start()

    def _start_server(self):
        """Starts the server, signals readiness, and waits to receive data."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', self.port))
            s.listen(1)
            # Signal that the server is now listening.
            PhysicalLayer.server_ready.set()
            print(f"[Physical Layer] Listening on port {self.port}...")
            conn, _ = s.accept()
            with conn:
                binary_data = conn.recv(1024).decode()
                # Convert the binary data back to text.
                text_data = ''.join(chr(int(binary_data[i:i+8], 2))
                                    for i in range(0, len(binary_data), 8))
                
                print(f"[Physical Layer] Received: {text_data}")
                
                self.received_data = text_data
                self.data_received.set()

    def send(self, data):
        """Waits for the server to be ready, converts data to binary, and sends it."""
        # Wait until the server thread is ready.
        PhysicalLayer.server_ready.wait()
        # Convert the data to binary bits.
        binary_data = ''.join(format(ord(c), '08b') for c in data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', self.port))
            s.sendall(binary_data.encode())

    def receive(self):
        """Waits until data is received, then returns it."""
        self.data_received.wait()
        return self.received_data