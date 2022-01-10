import time, os
from pygame import mixer
from pydub import AudioSegment
# original file: "slow.mp3"
# new fast file: "fast.mp3"
# speed: 1.3 (1.0 is actual speed)

def speed_swifter(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate
newSpeed = 1.3
sound = AudioSegment.from_file('squid-game-doll.wav')    
speed_sound = speed_swifter(sound, newSpeed)
speed_sound.export(os.path.join("fast.wav"), format="wav")
mixer.init()
mixer.music.load("fast.wav")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(0.1)