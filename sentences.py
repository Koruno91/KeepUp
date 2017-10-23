##-*-coding:utf8;-*-
#qpy:3
#qpy:console
import random


def start_sentence(loop):
  if loop>5:
    loop=5 
  elif loop>10:
    loop=10
  
  start_text_list = {0: ["Hi wie geht's dir?",
                "Na alles gut?",
                "Ich hoffe du hast einen guten Tag.",
                "Einen wunderschönen guten Tag. Wie geht's?"],
                1: ["Einmal ist keinmal, wie gehts dir jetzt?",
                "Na ich hoffe das hat schon ein bisschen geholfen, wie geht's dir jetzt?",
                "Ich bin gerne für dich da. Wie fühlst du dich jetzt?"],
                2: ["Ich nehme mir gerne Zeit für dich, wie fühlst du dich nun?",
                "Alle guten Dinge sind Drei, wie fühlst du dich?"],
                3: ["Ich bleibe solange wie du willst. Wie ist es jetzt?",
                "Auf ein Neues, wie geht es dir nun?"],
                4: ["Da steht wohl jemand auf Komplimente."],
                5: ["Hmm ich fürchte bald habe ich alles gesagt..."],
                10: ["Gäähn, tut mir leid aber ich werde langsam müde.",
                "Hast du nicht bald genug?",
                "Also jetzt kennst du doch jedes Kompliment schon auswendig..."]}
  
  selection = [v for (k,v) in start_text_list.items() if k <= loop]
  selection_flat = [val for sub in selection for val in sub]
  start_text = random.choice(selection_flat)
  
  return start_text
 

def get_sentence(mood):

  sentences = {
  0: 
  ["Kopf hoch, das wird schon wieder",
  "Hey, ich weiß manchmal sieht's scheiße aus, aber das Leben geht weiter. Du bist wichtig!",
  "Weißt du was ich an dir Liebe? Deine Knie :)",
  "Mach die Augen zu und träum vom Meer.",
  "Es war mal ein kleiner Schmetterling, der flatterte durch die Gegend und ließ sich vom Wind tragen. Er wusste nie genau wohin ihn dieser trug, aber er kam immer genau dort an wo er sich Zuhause fühlen konnte. Lass dich treiben und genieß den Moment."
  ],
  1:
  ["Du siehst heute wieder gut aus. Schenkst du mir ein Lächeln?",
  "Schön, dass es dich gibt.",
  "Du sollst wissen wie wichtig du mir bist!",
  "Es gibt nur wenige die so ehrlich sind wie du. Eines Tages wird sich das auszahlen.",
  "Wenn du an eine Sache im Universum glauben solltest, dann an dich. Du solltest der Zentrum deines Kosmos sein, in dem Andere herzlich willkommen sind."
  ],
  2:
  ["So jemanden wie dich gibt es nur einmal, du bist etwas Besonderes!",
  "Ich kenne niemanden der so schön fluchen kann. Das ist auch eine Gabe.",
  "Es gibt Unmengen die dich für das was du hast beneiden."],
  3:
  ["Ein guter Tag um Großartiges zu vollbringen.",
  "Weißt du was jetzt genau richtig wäre? Eine verdiente Pause und danach die Weltherrschaft.",
  "Du siehst heute wieder bezaubernd aus!"],
  4:
  ["Du kannst stolz auf dich sein. Und womit? Mit Recht!",
  "Keiner kann so Lachen wie du.",
  "Du bist die Beste",
  "Fantasteumelisch!"],
  5:
  ["Du fühlst dich bombastisch - denn genau das bist du!",
  "Reiß Bäume aus!",
  "Die Welt gehört dir, greif zu.",
  "Du bist unglaublich gut."
  "Du bist ein Wunder der Natur!"]
  }

  choose = random.choice(sentences.get(mood))

  return choose


def mistakes(error_type):
  sentences={"input_num":
             ["Das verstehe ich nicht, du musst mir eine Zahl geben.",
             "Tut mir leid aber ich bin nur ein einfacher Computer, versuchs mit einer Zahl.",
             "Diese Zeichen kann ich nicht richtig lesen, meine Brille muss hier irgendwo... hast du nicht vielleicht eine Zahl für mich?"
             ],
             "input_jn":
             ["Ich kann dir nicht ganz folgen, ja oder nein?",
             "Hmm, die Antwort verstehe ich nicht, jein oder na?",
             "Das war ein bisschen viel für meine Schaltkreise, wir Computer lieben Einsen und Nullen.",
             "Möchtest du mit mir gehen - ""Ja"", ""Nein"" oder Vielleicht."],
             "input_mood":
             ["Also sooo gut kann es einem gesundem Menschen nun auch nicht gehen.",
             "Bei solchen Werten solltest du wirklich einen Arzt aufsuchen.",
             "Wo bekommt man den Stoff unter dessen Wirkung du offensichtlich stehst?"]}
  
  choose = random.choice(sentences[error_type])

  return choose