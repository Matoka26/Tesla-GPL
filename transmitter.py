from microbit import*
import radio
import audio
import music
radio.config(group=23)
radio.on()
while True:
    if pin2.is_touched():
        radio.send("sirena")
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send("stanga")
        radio.send("dreapta")
        display.show(Image.ARROW_N)
    elif button_a.is_pressed():
        radio.send("stanga")
        display.show(Image.ARROW_W)
    elif button_b.is_pressed():
        radio.send("dreapta")
        display.show(Image.ARROW_E)

    elif pin_logo.is_touched():
        radio.send("cutie")
        display.show(Image.ARROW_S)
    else:
        radio.send("stop")
        display.show(Image.ANGRY)