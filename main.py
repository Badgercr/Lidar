# -*- coding: utf-8 -*
import serial

ser = serial.Serial("/dev/ttyAMA0", 115200) # Opening serial port. Make sure this is UART port and configure PI setting accordingly
#To further understand how code works and why it does check TFmini Lidar manual that can be found online
def getTFminiData():
    while True:
        count = ser.in_waiting #counts the bits available for every transmitting signal the Lidar sends.
        if count > 8:
            recv = ser.read(9) #Every trasmission consist of 9 bytes
            ser.reset_input_buffer() # resets bits for next transmit signal
            if recv[0] == 'Y' and recv[1] == 'Y': # 0x59 is 'Y'  0th and 1st byte is the frame header and shoes sucesfull transmit in the value of 0x59
                low = int(recv[2].encode('hex'), 16) # 2nd byte in the transmit signal is the low distance value
                high = int(recv[3].encode('hex'), 16) # 3rd byte in the transmit signal is the high distance value
                distance = low + high * 256 # add low and high distance value and convert back to base 10 form
                print(distance)

if __name__ == '__main__': #sets source files
    try:
        if ser.is_open == False: # check if port is open
            ser.open()
        getTFminiData() #read data
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()

