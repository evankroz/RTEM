import serial
import csv
import time
from datetime import datetime
from time import sleep
from CountdownTester import loading_bar
import glob

#scanning for usb modem ports on laptop'''
#
#
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
SERIAL_PORT = "/dev/cu.usbmodem1301"

BAUD_RATE = 115200  # Make sure this matches your Arduino's baud rate

# CSV file configuration
CSV_FILENAME = f"load_cell_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

grain_dia = "What is the internal grain dia.?"
cont = input("Are you ready to start y/n?")
if cont == "n":
    exit()


def countdown_func():
    seconds = 15
    while seconds > 0:
        sleep(1)
        print(f"Starting data recording in {seconds} seconds")
        seconds -= 1
    print("Data recording has started: ")


def main():
    try:
        # Open serial port
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Connected to {SERIAL_PORT}")

            # Open CSV file
            with open(CSV_FILENAME, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Time (s)', 'Thrust'])  # Write header

                print(f"Saving data to {CSV_FILENAME}")
                print("Press Ctrl+C to stop...")

                ser.write(b"S")
                print("Start signal sent to Arduino")

                start_time = time.time()  # Record the start time

                while True:
                    # Read a line from the serial port
                    line = ser.readline().decode('utf-8').strip()

                    if line:
                        current_time = time.time()
                        elapsed_time = current_time - start_time - 2.242
                        weight = float(line)

                        # Write to CSV
                        csv_writer.writerow([f"{elapsed_time:.3f}", weight])

                        # Print to console
                        print(f"{elapsed_time:.3f}: {weight}")

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("\nData collection stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    countdown_func()
    main()
    print(CSV_FILENAME)
    print("done")
