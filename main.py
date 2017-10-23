
#qpy:3
#qpy:console

import sl4a
import random
import sys
import sentences as stc
import json

# TextTone - Displays and Reads Text if Tone On
def texttone(string):
  print(string)
  if tone==1: droid.ttsSpeak(string)

# Startup - Shows Greeting Text
def startup(loop):
  print("\n")
  texttone(stc.start_sentence(loop))

# Get_Mood - Lists Mood Options and gets User Input  
def get_mood():
  mood_rating = {5: "super",
                 4: "sehr gut",
                 3: "gut",
                 2: "okay",
                 1: "geht so",
                 0: "schlecht"}
  for key, val in mood_rating.items():
    print(key, ': ', val)
  #droid.dialogSetItems(json.dumps(mood_rating))
  
  while True:
    try:
      mood = int(input())
    except ValueError:
      texttone(stc.mistakes('input_num'))
      continue
    if mood>5 or mood<0:
      texttone(stc.mistakes('input_mood'))
      continue
    else:
      break
  return mood


# Give_Keepup - Returns Sentence Corresponding to Mood
def give_keepup(mood):
  texttone(stc.get_sentence(mood))
  print("\n")


# Main - Runs Routine until it is stopped
def main():
  loop_num = 0
  while True:
    startup(loop_num)
    mood = get_mood()
    give_keepup(mood)
    
    while True:
      answer = input("Noch einmal? (j/n)")
      if answer not in ['j', 'n']:
        texttone(stc.mistakes('input_jn'))
        continue
      elif answer=='j':
        loop_num += 1
        break
      else:
        raise SystemExit
  
if __name__ == '__main__':
  droid = sl4a.Android()
  tone = 0
  main()