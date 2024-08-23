import socket
from zeroconf import ServiceInfo, Zeroconf

service_type = "_http._tcp.local."

class NetworkDiscoverySdk:
    active_connections = []
    def __init__(self, service_name, service_port):
        self.service_name = service_name
        self.service_port = service_port
        self.zeroconf = Zeroconf()

    def register(self):
        self.service_ip = self.__get_ip()
        print(f"Server IP: {self.service_ip}")
        service_info = ServiceInfo(
            service_type,
            f"{self.service_name}.{service_type}",
            addresses=[socket.inet_aton(self.service_ip)],
            port=self.service_port,
            properties={"description": "This is " + self.service_name + " service running on " + self.service_ip + ":" + str(self.service_port)},
            server="local."
        )
        self.zeroconf.register_service(service_info)
        print(f"Service {self.service_name} registered successfully.")

    def unregister(self):
        self.zeroconf.unregister_all_services()
        self.zeroconf.close()
        print(f"Service {self.service_name} unregistered successfully.")

    def __get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
