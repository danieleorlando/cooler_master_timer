from ctypes import cdll
import time, math

lib = cdll.LoadLibrary(".\\SDKDLL.dll")

DEV_MKeys_S = 1
ROW = 1

input_time = int(input("Input: "))

def secs_on_keys(i):
    times = math.ceil(float(i) / 10)
    count = float(i) % 10

    if (count==0):
        count=10

    for _ in range(0,int(times)):
        for n in range(1,int(count+1)):
            lib.SetLedColor(ROW, n, 255, 255, 255, DEV_MKeys_S)
    
def finish():    
    blink(0.3, 5)

def blink(delay, times):
    for _ in range(times):
        lib.SetFullLedColor(0, 0, 0, DEV_MKeys_S)
        time.sleep(delay)
        lib.SetFullLedColor(255, 255, 255, DEV_MKeys_S)                
        time.sleep(delay)

if (lib.IsDevicePlug(DEV_MKeys_S)):
    lib.SetControlDevice(DEV_MKeys_S)
    if (lib.EnableLedControl(1, DEV_MKeys_S)):
        while input_time > 0:            
            secs_on_keys(input_time)
            time.sleep(1)
            input_time -= 1
            lib.SetFullLedColor(0, 0, 0, DEV_MKeys_S)
        time.sleep(1)
        finish()
        lib.EnableLedControl(0, DEV_MKeys_S)