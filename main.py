from network_discovery_sdk import NetworkDiscoverySdk
import time

# Create an instance of NetworkDiscoverySdk
sdk = NetworkDiscoverySdk("edge-ai-service", 8000)

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
