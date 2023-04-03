import ctypes
from time import sleep
while True:
    for i in range(25):
        if len(str(i)) == 1:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, f"C:/Users/crab_/OneDrive/デスクトップ/result/myBGAnim0{i}.png" , 0)
        else:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, f"C:/Users/crab_/OneDrive/デスクトップ/result/myBGAnim{i}.png" , 0)
        sleep(0.1)