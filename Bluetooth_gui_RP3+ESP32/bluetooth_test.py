import bluetooth
# bluetooth low energy scan
# from bluetooth.ble import DiscoveryService

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))
print(nearby_devices)
for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))