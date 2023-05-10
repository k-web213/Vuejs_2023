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
    # 温度を保存するリストの初期化
    value = []
    # インデックス番号の初期化
    index_num = 0
    # 繰り返し処理
    while True:
        # 温度を読み取りリストの末尾に追加
        value.append(adt7410())
        # 温度読み取り初回かどうか
        if index_num == 0:
          # 初回なら温度を表示
          print(value[index_num])
        # １回前測定した温度と同じか否かを判断
        elif value[index_num - 1] != value[index_num]:
          # 違った温度なら表示
          print(value[index_num])
        # １秒停止
        sleep(1)
        # インデックス番号をインクリメント
        index_num += 1

except KeyboardInterrupt: # ［Ctrl］+［C］キーで処理を終える
    pass