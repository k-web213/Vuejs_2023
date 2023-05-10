#　1.ライブラリをインポート
import RPi.GPIO as GPIO
from time import sleep

#　2.初期化
GPIO.setmode(GPIO.BCM) # ピン番号ではなくGPIOの番号で指定
GPIO.setup(12, GPIO.OUT) # GPIO 12を出力として指定

#　3.繰り返し処理
try:
  while True:
    GPIO.output(12, GPIO.HIGH) # GPIO 12を HIGHに変更
    sleep(1) # １秒停止
    GPIO.output(12, GPIO.LOW) # GPIO 12をLOWに変更
    sleep(1) # １秒停止

#　4.［Ctrl］+［C］キーで繰り返し処理を終了
except KeyboardInterrupt:
  pass

#　5.GPIOをリセット
GPIO.cleanup()