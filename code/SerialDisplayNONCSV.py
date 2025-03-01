import serial
from datetime import datetime
import time
from CountdownTester import loading_bar
from time import sleep
import glob

report = None
#SERIAL_PORT = None

ports = glob.glob("/dev/cu.*")
for port in ports:
    if "/dev/cu.usbmodem" in port:
        res = True
        SERIAL_PORT = port
        print(port.replace("/dev/cu.", ""))
    else:
        res = False

BAUD_RATE = 115200  # Make sure this matches your Arduino's baud rate


def countdown_func():
    seconds = 5
    while seconds > 0:
        sleep(1)
        print(f"Beginning collection in {seconds} seconds, igniting motor in {seconds} seconds, step back")
        seconds -= 1
    print("Data recording has started: ")


def main():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Connected to {SERIAL_PORT}")

            start_time = time.time()  # Record the start time

            while True:
                line = ser.readline().decode('utf-8').strip()

                if line:
                    current_time = time.time()
                    elapsed_time = current_time - start_time-2.242 #approximate ping time from arduino, just really slow for some reason?
                    weight = line

                    # Print to console
                    print(f"{elapsed_time:.3f}: {weight}")

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("\nData collection stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    pre = input("Are you firing a motor, or testing igniters? m/i")
    if pre == "m":
        countdown_func()
        main()
    else:
        main()

