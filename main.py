from pirc522 import RFID
import signal
import time
import RPi.GPIO as GPIO
import smtplib

ledpin=33

GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()


GPIO.setup(ledpin, GPIO.OUT)
rdr = RFID()
util = rdr.util()
util.debug = True

pir_sensor = 16
piezo = 31
sari_led=37
kirmizi_led=35
GPIO.setup(sari_led, GPIO.OUT)
GPIO.setup(kirmizi_led, GPIO.OUT)
GPIO.setup(pir_sensor, GPIO.IN)
GPIO.setup(piezo, GPIO.OUT)
current_state = 0
devam = True
correct_card_id = [61, 20, 115, 213, 143]

def mail_gonder():
    smtpUser= "example@gmail.com"
    smtpPass="password"

    tarih=time.strftime("%d"+ "."+"%m"+ "."+"%Y")
    saat=time.strftime("%X")
    #print(tarih)
    toAdd="example@gmail.com"
    fromAdd=smtpUser

    subject="!! SECURITY SAFE UYARI !!"
    header="To:"+ toAdd + "\n" + "From:" + fromAdd + "\n" + "Subject:" + subject
    body=f"""{tarih} tarihinde,  {saat} saatinde kasaniza izinsiz giris tespit edilmistir."""

    s=smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(smtpUser,smtpPass)

    s.sendmail(fromAdd,toAdd,header + "\n\n" + body)
    print("Mail Gönderildi...")

    s.quit()



try:
    while devam:
                GPIO.output(kirmizi_led,False)
                GPIO.output(ledpin, False)
                GPIO.output(sari_led,True)
                GPIO.output(piezo,False)

                time.sleep(1)
                GPIO.output(sari_led,False)
                current_state = GPIO.input(pir_sensor)
                if current_state ==1:
                    mail_gonder()
                    print("GPIO pin %s is %s" % (pir_sensor, current_state))
                    GPIO.output(piezo,True)
                    GPIO.output(kirmizi_led,True)
                    time.sleep(5)


                    GPIO.output(piezo,False)
                    GPIO.output(kirmizi_led,False)
                    time.sleep(2)

                (error, data) = rdr.request()
                if not error:
                    print("\nKart Algilandi!")
                    (error, uid) = rdr.anticoll()
                    if not error:

                        card_id= uid
                        if uid == correct_card_id:

                            GPIO.output(ledpin, True)
                            GPIO.output(piezo, True)
                            time.sleep(0.2)
                            GPIO.output(piezo,False)
                            time.sleep(0.01)
                            GPIO.output(piezo, True)
                            time.sleep(0.3)
                            GPIO.output(piezo,False)
                            time.sleep(5)
                            devam = False

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()