import datetime
import pyglet
datetime.datetime.now()
print ("Thoi gian bay gio la:",datetime.datetime.now().strftime('%H:%M'))
alarmClock = input("Gio ban muon hen:")
while True:
    currentHour = datetime.datetime.now().strftime("%H:%M")
    
    if currentHour == alarmClock:
        music = pyglet.resource.media('crowd-cheering.mp3')
        music.play()

        pyglet.app.run()
