# ライブラリをインポート
import smbus
from time import sleep

# 初期設定
bus = smbus.SMBus(1)

# 温度を読み込む関数
def adt7410():
    block = bus.read_i2c_block_data(0x48, 0x00, 2)
    data = (block[0] << 8 | block[1]) >> 3
    if (data >= 4096):
        data -= 8192
    temp = data * 0.0625
    return temp

try:
    # 繰り返し処理
    while True:
        # 温度を読み取る
        value = adt7410()
        # 温度を表示する
        print('温度 = {} 度'.format(value))
        # １秒停止
        sleep(1)

except KeyboardInterrupt: # ［Ctrl］+［C］キーで処理を終える
    pass