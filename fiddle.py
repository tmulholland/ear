import time
import glob
from itertools impor chain

import numpy as np
import vlc

class Phrase:

    def __init__(self, phrase, description=""):
        self.phrase = phrase
        self.description = description
        self.files = self.get_phrase_files()

    def get_phrase_files(self):
        all_files = glob.glob('~/ear/audio/*')
        files = []
        for note in self.phrase:
            for file in all_files:
                if file.endswith(note+'.wav'):
                    files.append(file)
        return files

    def __repr__(self):
        print(self.description)

    def __sort__(self):
        indices = sorted(range(len(self.phrase)), key=lambda x: int(self.phrase[x][-1])*1000 + ord(self.phrase[x][0])%99 + 0.5*('sharp' in self.phrase[x]))
        self.phrase = list(np.array(self.phrase)[indices])
        self.files  = list(np.array(self.files )[indices])

class FiddleScale:

    def __init__(self, tuning='GDAE', key=None, scale='major'):

        self.tuning='GDAE'
        if key is None:
            if tuning in ('GDAE', 'GDGD'):
                self.key='G'
            elif tuning == 'AEAE':
                self.key='A'
            elif tuning == 'ADAE':
                self.key='D'
            else:
                self.key='G'
        else:
            self.key=key

        self.scale=scale

    def play(self, file):
        p = vlc.MediaPlayer(file)
        p.play()
        time.sleep(0.01)
        duration = p.get_length() / 1550
        time.sleep(duration)
        p.stop()

    def play_phrase(self, phrase, include_descriptions=True, time_buffer=0.5):

        start = time.time()
        if include_descriptions:
            print(phrase)
        for file in phrase.files:
            play(file)

        time.sleep(time_buffer)
        return time.time()-start

    def run(self, silent_echo=False, include_descriptions=True, time_buffer=0.5):
        phrases = self.get_phrases()
        self.play_phrase(Phrase(list(chain(*[phrase.phrase for phrase in phrases])), "Notes in scale"), include_descriptions)

        while True:
            phrase = np.random.choice(phrases)
            phrase_length = self.play_phrase(phrase, include_descriptions)
            if silent_echo:
                time.sleep(phrase_length)
            else:
                self.play_phrase(phrase, include_descriptions)

    def get_phrases(self):

        phrases = []
        descrip = []
        if self.tuning in ('GDAE', 'GDGD') and self.key=='G':
            phrases.append(Phrase(['g3', 'b3', 'd4'],
                                  ,"This phrase forms a G major triad ascending."))
            phrases.append(Phrase(['d4', 'b3', 'g3'],
                                  ,"This phrase is the descending version of the above."))
            phrases.append(Phrase(['a3', 'g3', 'b3', 'a3'],
                                  ,"A short, neighbor-tone phrase centered around the note A."))
            phrases.append(Phrase(['d4', 'e4', 'd4', 'b3'],
                                  ,"A brief turn around the note D."))
            phrases.append(Phrase(['e4', 'd4', 'b3', 'g3'],
                                  ,"A stepwise descending phrase."))
            phrases.append(Phrase(['g3', 'a3', 'b3', 'd4'],
                                  ,"Ascending through the first four scale degrees of G major."))
            phrases.append(Phrase(['c4', 'b3', 'a3', 'g3'],
                                  ,"A stepwise descending phrase from the fourth scale degree."))
            phrases.append(Phrase(['b3', 'd4', 'g4', 'b4'],
                                  ,"This one has a wider range but still emphasizes the key of G major"
                                   " with a strong emphasis on the tonic and dominant."))
            phrases.append(Phrase(['e4', 'fsharp4', 'g4', 'e4'],
                                  ,"A short phrase emphasizing the leading tone resolving to the tonic."))
            phrases.append(Phrase(['d4', 'c4', 'b3', 'd4', 'g3'],
                                  ,"A longer phrase that emphasizes scale degrees in G major."))
            if self.tuning == 'GDAE':
                phrases.append(Phrase(['g3', 'a3', 'b3', 'd4'],
                                      ,"A basic stepwise ascending phrase."))
                phrases.append(Phrase(['d4', 'e4', 'fsharp4', 'g4', 'a4'],
                                      ,"Ascending through the scale."))
                phrases.append(Phrase(['g4', 'b4', 'a4', 'g4'],
                                      ,"A short phrase emphasizing the octave leap."))
                phrases.append(Phrase(['e4', 'd4', 'b3', 'g3'],
                                      ,"A descending phrase ending on the tonic."))
                phrases.append(Phrase(['a4', 'b4', 'g5'],
                                      ,"Highlighting the upper range with a leap from the dominant."))
                phrases.append(Phrase(['g5', 'e5', 'd5', 'b4'],
                                      ,"Descending from the high tonic."))
                phrases.append(Phrase(['c5', 'b4', 'a4', 'g4'],
                                      ,"Stepwise descent from the fourth scale degree in the higher octave."))
                phrases.append(Phrase(['fsharp4', 'g4', 'a4', 'b4', 'c5', 'd5', 'e5', 'fsharp5', 'g5'],
                                      ,"Ascending through the scale, reaching the high tonic."))
                phrases.append(Phrase(['b4', 'd5', 'g5', 'a5', 'b5'],
                                      ,"Emphasizing the upper range with larger leaps."))
                phrases.append(Phrase(['b5', 'a5', 'g5', 'e5', 'd5'],
                                      ,"A descending phrase starting from the high dominant."))

        if self.tuning in ('GDAE', 'AEAE') and self.key=='A' and self.scale.lower()=='major':
            phrases.append(Phrase(['a3', 'b3', 'csharp4', 'e4'],
                                  ,"A basic stepwise ascending phrase."))
            phrases.append(Phrase(['e4', 'fsharp4', 'gsharp4', 'a4', 'b4'],
                                  ,"Ascending through the middle of the scale."))
            phrases.append(Phrase(['a4', 'b4', 'a4', 'fsharp4'],
                                  ,"A neighbor-tone phrase centered around the tonic."))
            phrases.append(Phrase(['e4', 'd4', 'csharp4', 'b3'],
                                  ,"A descending phrase moving stepwise."))
            phrases.append(Phrase(['b4', 'csharp5', 'e5', 'a5'],
                                  ,"Emphasizing a leap to the higher tonic."))
            phrases.append(Phrase(['a5', 'fsharp5', 'e5', 'csharp5'],
                                  ,"Descending from the high tonic."))
            phrases.append(Phrase(['d5', 'csharp5', 'b4', 'a4'],
                                  ,"A stepwise descent in the upper range."))
            phrases.append(Phrase(['fsharp4', 'gsharp4', 'a4', 'b4', 'csharp5', 'd5', 'e5', 'fsharp5', 'gsharp5', 'a5'],
                                  ,"An ascending scalar run reaching the high tonic."))
            phrases.append(Phrase(['b4', 'e5', 'a5', 'b5'],
                                  ,"Highlighting the upper range with large leaps."))
            phrases.append(Phrase(['b5', 'a5', 'gsharp5', 'e5', 'd5'],
                                  ,"A descending phrase starting from the high dominant."))
            phrases.append(Phrase(['a3', 'csharp4', 'e4', 'a4'],
                                  ,"Emphasizing the tonic and the major third."))
            phrases.append(Phrase(['a4', 'csharp5', 'b4', 'a4', 'gsharp4'],
                                  ,"A short, turn-like phrase around the tonic."))
            phrases.append(Phrase(['d4', 'fsharp4', 'a4', 'b4'],
                                  ,"A stepwise ascending phrase emphasizing the dominant."))
            phrases.append(Phrase(['b4', 'a4', 'gsharp4', 'fsharp4', 'e4'],
                                  ,"Descending stepwise through the scale."))
            phrases.append(Phrase(['fsharp4', 'a4', 'csharp5', 'e5'],
                                  ,"Ascending skipwise, emphasizing the A major triad."))
            phrases.append(Phrase(['gsharp4', 'a4', 'b4', 'csharp5', 'b4', 'a4'],
                                  ,"A phrase emphasizing the leading tone and its resolution."))
            phrases.append(Phrase(['e5', 'd5', 'csharp5', 'b4', 'a4'],
                                  ,"A descending phrase in the upper range."))
            phrases.append(Phrase(['a4', 'gsharp4', 'fsharp4', 'e4', 'fsharp4', 'gsharp4'],
                                  ,"A wave-like phrase moving around the dominant."))
            phrases.append(Phrase(['csharp5', 'b4', 'a4', 'fsharp4', 'e4', 'd4', 'csharp4'],
                                  ,"A longer descending phrase through the scale."))
            phrases.append(Phrase(['a5', 'e5', 'csharp5', 'b4', 'a4', 'fsharp4'],
                                  ,"A descending phrase starting from the high tonic and emphasizing the A major triad."))

        if self.tuning in ('GDAE', 'AEAE', 'ADAE') and self.key=='A' and self.scale.lower()=='mixolydian':
            phrases.append(Phrase(['a3', 'b3', 'csharp4', 'e4', 'g4'],
                                  ,"Ascending phrase emphasizing the flattened seventh."))
            phrases.append(Phrase(['g4', 'a4', 'b4', 'csharp5', 'g4'],
                                  ,"A phrase highlighting the Mixolydian character with the G natural."))
            phrases.append(Phrase(['e4', 'd4', 'csharp4', 'b3', 'a3'],
                                  ,"Descending stepwise phrase."))
            phrases.append(Phrase(['a4', 'g4', 'fsharp4', 'e4'],
                                  ,"A descending phrase emphasizing the Mixolydian's flattened seventh."))
            phrases.append(Phrase(['fsharp4', 'a4', 'g4', 'e4'],
                                  ,"A phrase using the dominant and the flattened seventh."))
            phrases.append(Phrase(['b4', 'a4', 'g4', 'fsharp4', 'e4', 'd4'],
                                  ,"A descending phrase through the Mixolydian mode."))
            phrases.append(Phrase(['csharp5', 'b4', 'a4', 'g4', 'fsharp4'],
                                  ,"Descending from the third, emphasizing the Mixolydian character."))
            phrases.append(Phrase(['a4', 'b4', 'csharp5', 'g4'],
                                  ,"Emphasizing the leap from the third to the flattened seventh."))
            phrases.append(Phrase(['fsharp4', 'g4', 'a4', 'b4', 'csharp5', 'd5', 'e5', 'fsharp5', 'g5', 'a5'],
                                  ,"An ascending scalar run through the A Mixolydian mode."))
            phrases.append(Phrase(['g5', 'fsharp5', 'e5', 'd5', 'csharp5', 'b4'],
                                  ,"A descending phrase from the flattened seventh in the upper range."))
            phrases.append(Phrase(['a3', 'csharp4', 'd4', 'e4', 'g4'],
                                  ,"Ascending stepwise phrase with the flattened seventh."))
            phrases.append(Phrase(['b4', 'g4', 'a4', 'csharp5'],
                                  ,"Emphasizing the tonic and flattened seventh."))
            phrases.append(Phrase(['e4', 'fsharp4', 'g4', 'a4'],
                                  ,"Ascending through the middle of the scale."))
            phrases.append(Phrase(['g4', 'a4', 'g4', 'e4', 'd4'],
                                  ,"A phrase moving around the flattened seventh."))
            phrases.append(Phrase(['d4', 'e4', 'fsharp4', 'g4', 'a4'],
                                  ,"A stepwise ascending phrase emphasizing the Mixolydian character."))
            phrases.append(Phrase(['csharp5', 'd5', 'b4', 'a4', 'g4'],
                                  ,"Descending with emphasis on the flattened seventh."))
            phrases.append(Phrase(['b4', 'csharp5', 'd5', 'e5', 'g5'],
                                  ,"Ascending with the flat seventh on the top."))
            phrases.append(Phrase(['a5', 'g5', 'fsharp5', 'e5'],
                                  ,"Descending from the high tonic."))
            phrases.append(Phrase(['d5', 'e5', 'g5', 'fsharp5', 'd5'],
                                  ,"A phrase emphasizing the dominant and flattened seventh."))
            phrases.append(Phrase(['a4', 'b4', 'csharp5', 'd5', 'g5', 'a5'],
                                  ,"A scalar phrase emphasizing the tonic and flattened seventh in the higher octave."))

        if self.tuning in ('GDAE', 'AEAE', 'ADAE') and self.key=='A' and self.scale.lower()=='dorian':
            phrases.append(Phrase(['a3', 'b3', 'c4', 'd4', 'fsharp4'],
                                  ,"Ascending stepwise phrase with the natural sixth."))
            phrases.append(Phrase(['e4', 'fsharp4', 'g4', 'a4'],
                                  ,"Ascending through the higher part of the scale."))
            phrases.append(Phrase(['g4', 'fsharp4', 'e4', 'd4', 'c4'],
                                  ,"Descending phrase emphasizing the natural sixth."))
            phrases.append(Phrase(['d4', 'c4', 'b3', 'a3'],
                                  ,"A descending phrase from the fourth degree."))
            phrases.append(Phrase(['fsharp4', 'a4', 'g4', 'e4'],
                                  ,"Emphasizing the natural sixth with a leap to the tonic."))
            phrases.append(Phrase(['a4', 'b4', 'c5', 'd5', 'fsharp5'],
                                  ,"Ascending scalar phrase to the natural sixth in the upper range."))
            phrases.append(Phrase(['g4', 'a4', 'g4', 'e4'],
                                  ,"A short phrase revolving around the tonic and dominant."))
            phrases.append(Phrase(['d5', 'e5', 'fsharp5', 'g5'],
                                  ,"Ascending through the middle of the scale in the upper range."))
            phrases.append(Phrase(['c5', 'd5', 'e5', 'fsharp5', 'g5', 'a5'],
                                  ,"A scalar ascent to the high tonic."))
            phrases.append(Phrase(['b4', 'c5', 'd5', 'fsharp5', 'e5', 'd5'],
                                  ,"A phrase emphasizing the natural sixth and its surrounding tones."))
            phrases.append(Phrase(['a3', 'c4', 'e4', 'fsharp4'],
                                  ,"A leap-based phrase emphasizing the tonic and the natural sixth."))
            phrases.append(Phrase(['b4', 'a4', 'g4', 'fsharp4', 'e4'],
                                  ,"A descending stepwise phrase from the second scale degree."))
            phrases.append(Phrase(['d4', 'e4', 'g4', 'a4'],
                                  ,"Ascending through the scale with a skip from E to G."))
            phrases.append(Phrase(['fsharp4', 'g4', 'fsharp4', 'e4', 'd4'],
                                  ,"A phrase oscillating around the natural sixth."))
            phrases.append(Phrase(['a4', 'g4', 'e4', 'fsharp4', 'd4'],
                                  ,"Zigzagging through key tones of the A Dorian mode."))
            phrases.append(Phrase(['c5', 'b4', 'a4', 'g4'],
                                  ,"A descending phrase emphasizing the minor third."))
            phrases.append(Phrase(['e5', 'd5', 'c5', 'b4'],
                                  ,"A stepwise descent in the upper range."))
            phrases.append(Phrase(['g4', 'fsharp4', 'e4', 'd4', 'c4', 'b3'],
                                  ,"Descending scalar run emphasizing the Dorian character."))
            phrases.append(Phrase(['a4', 'b4', 'c5', 'e5', 'fsharp5', 'a5'],
                                  ,"An ascending phrase reaching the high tonic."))
            phrases.append(Phrase(['b5', 'a5', 'g5', 'fsharp5', 'e5', 'd5'],
                                  ,"Descending from the high second scale degree, moving stepwise."))

        if self.tuning in ('GDAE', 'ADAE') and self.key=='D' and self.scale.lower()=='major':
            phrases.append(Phrase(['a3', 'b3', 'csharp4', 'd4'],
                                  ,"Ascending stepwise from the fifth scale degree to the tonic."))
            phrases.append(Phrase(['d4', 'e4', 'fsharp4', 'a4'],
                                  ,"Ascending through the scale emphasizing the tonic to dominant jump."))
            phrases.append(Phrase(['g4', 'fsharp4', 'e4', 'd4'],
                                  ,"A descending stepwise phrase from the fourth scale degree."))
            phrases.append(Phrase(['b4', 'a4', 'g4', 'fsharp4', 'e4'],
                                  ,"Descending phrase emphasizing the dominant to the second scale degree."))
            phrases.append(Phrase(['csharp5', 'd5', 'e5', 'fsharp5'],
                                  ,"Ascending through the middle of the scale in the upper range."))
            phrases.append(Phrase(['fsharp4', 'a4', 'b4', 'csharp5', 'd5'],
                                  ,"A scalar ascent from the third scale degree to the tonic."))
            phrases.append(Phrase(['e4', 'fsharp4', 'g4', 'a4', 'b4'],
                                  ,"A stepwise ascending phrase emphasizing the second half of the D major scale."))
            phrases.append(Phrase(['a4', 'b4', 'csharp5', 'd5', 'e5', 'fsharp5'],
                                  ,"Ascending scalar run from the dominant to the high third scale degree."))
            phrases.append(Phrase(['g5', 'fsharp5', 'e5', 'd5', 'csharp5', 'b4'],
                                  ,"Descending through the upper range of the scale."))
            phrases.append(Phrase(['b4', 'd5', 'fsharp5', 'a5', 'b5'],
                                  ,"Emphasizing larger leaps from the dominant to the high dominant."))
            phrases.append(Phrase(['d4', 'csharp4', 'b3', 'a3'],
                                  ,"A descending stepwise phrase starting from the tonic."))
            phrases.append(Phrase(['a4', 'b4', 'csharp5', 'd5', 'e5'],
                                  ,"A stepwise ascending phrase from the dominant to the"
                                   " second scale degree in the upper range."))
            phrases.append(Phrase(['fsharp4', 'g4', 'a4', 'fsharp4', 'e4'],
                                  ,"A phrase moving around the third scale degree."))
            phrases.append(Phrase(['b4', 'csharp5', 'b4', 'a4', 'g4'],
                                  ,"A neighbor-tone phrase centered around the dominant."))
            phrases.append(Phrase(['d5', 'e5', 'fsharp5', 'a5'],
                                  ,"Ascending through the scale emphasizing the tonic to dominant leap in the upper range."))
            phrases.append(Phrase(['a4', 'csharp5', 'b4', 'g4'],
                                  ,"Zigzagging through key tones of the D major scale."))
            phrases.append(Phrase(['g4', 'a4', 'b4', 'csharp5', 'd5', 'csharp5', 'b4'],
                                  ,"A scalar ascent followed by a descent, emphasizing the tonic."))
            phrases.append(Phrase(['e4', 'g4', 'fsharp4', 'd4'],
                                  ,"Emphasizing the leaps around the third scale degree."))
            phrases.append(Phrase(['csharp5', 'd5', 'fsharp5', 'e5', 'd5'],
                                  ,"A phrase highlighting the tonic and third in the upper range."))
            phrases.append(Phrase(['b5', 'a5', 'g5', 'fsharp5', 'e5', 'd5'],
                                  ,"Descending from the high dominant, moving stepwise."))
