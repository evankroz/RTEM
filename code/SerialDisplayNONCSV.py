import serial
from datetime import datetime
import time
#from CountdownTester import loading_bar
from time import sleep
import glob

report = None
SERIAL_PORT = "/dev/cu.usbmodem1301" #this depends on the usb port your arduino is plugged in.
                                     #check with arduino and close the app afterwards, or else you will get a error
'''
ports = glob.glob("/dev/cu.*")
for port in ports:
    if "/dev/cu.usbmodem" in port:
        SERIAL_PORT = port
        report = True
    else:
        report = False
        print("USB MODEM PORT NOT FOUND")
        quit()
        '''

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
                    elapsed_time = current_time - start_time-2.242 #approximate ping time from arduino, just about 2.2 seconds, not necessary may be removed.
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

