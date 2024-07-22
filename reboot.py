import RPi.GPIO as GPIO
import time
import subprocess

global contador
global startTime

contador = startTime = 0

def botoes(canal):

  global contador
  global startTime

  if(GPIO.input(11) == 0 AND GPIO.input(25) == 0:
    contador += 1
    startTime = time.time()



      lcd_string('{:^16}'.format("A FAZER REBOOT"),LCD_LINE_2)
      command = "/usr/bin/sudo /sbin/shutdown -r now"
      process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
      output = process.communicate()[0]
      print output


print "Ctl-C para sair"

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(25, GPIO.FALLING, callback = botoes, bouncetime = 100)
GPIO.add_event_detect(11, GPIO.FALLING, callback = botoes, bouncetime = 100)

if __name__ == '__main__':
    try:
        while 1:
          if startTime - time.time() > 10:
            print "Time Up"
                        contador = 0

          if contador > 100:
            print "contador"
            contador = 0

    except KeyboardInterrupt:
        exit()

