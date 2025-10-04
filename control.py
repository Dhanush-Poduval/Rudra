import serial 
import time
import keyboard

ser=serial.Serial
motor1=0
motor2=0

def speed(motor,speed):
    if speed<0:
        speed=256+speed;
    ser.write(bytes([speed]))

try:
    print("Enter w a s d")
    while True:
        l_speed=0
        r_speed=0
        if keyboard.is_pressed('w'):
            l_speed+=50
            r_speed+=50
        if keyboard.is_pressed('a'):
            l_speed-=50
            r_speed-=50
        if keyboard.is_pressed('s'):
            l_speed-=30
            r_speed+=30
        if keyboard.is_pressed('d'):
            l_speed+=30
            r_speed-=30

        l_speed=max(min(l_speed,127),-127)
        r_speed=max(min(r_speed,127),-127)
        speed(motor1,l_speed)
        speed(motor2 , r_speed)

        if keyboard.ispressed('q'):
            break
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

finally:
    speed(motor2, 0)
    speed(motor1, 0)
    ser.close()

