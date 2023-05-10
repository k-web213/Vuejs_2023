#　1.ライブラリをインポート
import RPi.GPIO as GPIO
from time import sleep

#　2.初期化
GPIO.setmode(GPIO.BCM) # ピン番号ではなくGPIOの番号で指定
GPIO.setup(21, GPIO.OUT) # GPIO 21を出力として指定

# 繰り返し回数の入力
count = int(input('LED点滅回数 = '))

# 点滅間隔の入力
interval = float(input('点滅間隔（秒）= '))

#　繰り返し処理
for i in range(count):
  GPIO.output(21, GPIO.HIGH) # GPIO 21を HIGHに変更
  sleep(interval) # 停止
  GPIO.output(21, GPIO.LOW) # GPIO 21をLOWに変更
  sleep(interval) # 停止

#　5.GPIOをリセット
GPIO.cleanup()