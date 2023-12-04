from datetime import datetime
from utilities.transmitter_signals import send_signal

def handle_open_gate():
    send_signal('OPEN')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'🔔 {current_time}: Opening the gate')

def handle_close_gate():
    send_signal('CLOSE')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'🔔 {current_time}: Closing the gate')