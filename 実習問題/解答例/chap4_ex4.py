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

# キーボードから最低温度を入力
min_temp = float(input('最低温度 = '))
# キーボードから最高温度を入力
max_temp = float(input('最高温度 = '))

try:
    # 繰り返し処理
    while True:
        # 温度を読み取る
        value = adt7410()
        # 読み取った温度が最低温度以上、最高温度以下かどうかを判断
        if value >= min_temp and value <= max_temp:
            # 最低気温以上、最高気温以下なら表示する
            print('温度 = {} 度'.format(value))
        # １秒停止
        sleep(1)

except KeyboardInterrupt: # ［Ctrl］+［C］キーで処理を終える
    pass