# from rpi_rf import RFDevice

# Configure GPIO pin
# rfdevice = RFDevice(17)  # GPIO pin 17
# rfdevice.enable_tx()

# Transmitter signals
# TODO: Replace with the real signals
signals = [
    {
        'name': 'OPEN',
        'type': 'PulseLength',
        'pulse_length': 350,
        'code': 12345678,
        'protocol': 1
    },
    {
        'name': 'CLOSE',
        'type': 'PulseLength',
        'pulse_length': 350,
        'code': 87654321,
        'protocol': 1
    }
]

# Function to send the signal to the receiver
def send_signal(command):
    # Get the signal
    signal = next((item for item in signals if item['name'] == command), None)
    # Send the signal
    # rfdevice.tx_code(signal['code'], signal['protocol'], signal['pulse_length'])
    print(f'📡 Sent signal: {signal}')
    # Cleanup
    # rfdevice.cleanup()