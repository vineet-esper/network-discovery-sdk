from network_discovery_sdk import NetworkDiscoverySdk
import time
import logging

# Create an instance of NetworkDiscoverySdk
sdk = NetworkDiscoverySdk("edge-ai-service", 8000)

try:
    # Register the service
    sdk.register()

    logging.info("Service registered. Press Ctrl+C to stop.")
    
    # Keep the service running
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    logging.info("\nStopping the service...")

finally:
    # Unregister the service
    sdk.unregister()
    logging.info("Service unregistered.")
