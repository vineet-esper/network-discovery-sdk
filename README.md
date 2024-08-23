# Network Discovery SDK

Network Discovery SDK is a Python package that simplifies network service discovery and registration using Zeroconf. It allows you to easily register services on a local network and discover services registered by other devices.

## Features

- Simple service registration on local networks
- Automatic IP address detection
- Easy-to-use API for service management

## Installation

You can install the Network Discovery SDK directly from GitHub using pip:

```bash
pip install git+https://github.com/keyur2maru/network-discovery-sdk.git#egg=network_discovery_sdk
```

## Usage

Here's a quick example of how to use the Network Discovery SDK:

```python
from network_discovery_sdk import NetworkDiscoverySdk
import time

# Create an instance of NetworkDiscoverySdk
sdk = NetworkDiscoverySdk("MyService", 8080)

try:
    # Register the service
    sdk.register()

    print("Service registered. Press Ctrl+C to stop.")
    
    # Keep the service running
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping the service...")

finally:
    # Unregister the service
    sdk.unregister()
    print("Service unregistered.")
```

### Registering a Service

To register a service:

1. Create an instance of `NetworkDiscoverySdk` with a service name and port.
2. Call the `register()` method to register the service on the network.

```python
sdk = NetworkDiscoverySdk("MyService", 8080)
sdk.register()
```

### Unregistering a Service

To unregister a service:

1. Call the `unregister()` method on your `NetworkDiscoverySdk` instance.

```python
sdk.unregister()
```

## API Reference

### `NetworkDiscoverySdk(service_name, service_port)`

Creates a new instance of the Network Discovery SDK.

- `service_name` (str): The name of your service.
- `service_port` (int): The port number your service is running on.

### `register()`

Registers the service on the local network.

### `unregister()`

Unregisters the service from the local network.

## Requirements

- Python 3.6+
- zeroconf
