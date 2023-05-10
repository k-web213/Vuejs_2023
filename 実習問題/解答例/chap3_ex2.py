#　1.ライブラリをインポート
import RPi.GPIO as GPIO
from time import sleep

#　2.初期化
GPIO.setmode(GPIO.BCM) # ピン番号ではなくGPIOの番号で指定
GPIO.setup(21, GPIO.OUT) # GPIO 21を出力として指定

#　５回繰り返し処理
for i in range(5):
  GPIO.output(21, GPIO.HIGH) # GPIO 21を HIGHに変更
  sleep(2) # 2秒停止
  GPIO.output(21, GPIO.LOW) # GPIO 21をLOWに変更
  sleep(2) # 2秒停止

#　5.GPIOをリセット
GPIO.cleanup()