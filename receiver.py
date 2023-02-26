from microbit import*
import radio
import music
radio.config(group=23)
radio.on()
sirena = 1
while True:
    message = radio.receive()
    if message == "dreapta":
        pin0.write_analog(1023 * 1 / 20)
    elif message == "stanga":
        pin8.write_analog(1023 * 1 / 6)
    elif message == "stop":
        pin0.write_analog(1023 * 1.5 / 20)
        pin8.write_analog(1023 * 1.5 / 20)
    elif message == "cutie":
        pin0.write_analog(1023 * 1 /6)
        pin8.write_analog(1023 * 1 / 20)
