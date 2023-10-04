import time
from itertools impor chain

import numpy as np
import vlc

class Phrase:

    def __init__(self, phrase, description=""):
        self.phrase = phrase
        self.description = description
        self.files = self.get_phrase_files()

    def get_phrase_files(self):
        pass

    def __repr__(self):
        pass

    def __sort__(self):
        pass

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
            phrases.append(['g3', 'b3', 'd4'])
            descrip.append("This phrase forms a G major triad ascending.")
            phrases.append(['d4', 'b3', 'g3'])
            descrip.append("This phrase is the descending version of the above.")
            phrases.append(['a3', 'g3', 'b3', 'a3'])
            descrip.append("A short, neighbor-tone phrase centered around the note A.")
            phrases.append(['d4', 'e4', 'd4', 'b3'])
            descrip.append("A brief turn around the note D.")
            phrases.append(['e4', 'd4', 'b3', 'g3'])
            descrip.append("A stepwise descending phrase.")
            phrases.append(['g3', 'a3', 'b3', 'd4'])
            descrip.append("Ascending through the first four scale degrees of G major.")
            phrases.append(['c4', 'b3', 'a3', 'g3'])
            descrip.append("A stepwise descending phrase from the fourth scale degree.")
            phrases.append(['b3', 'd4', 'g4', 'b4'])
            descrip.append("This one has a wider range but still emphasizes the key of G major with a strong emphasis on the tonic and dominant.")
            phrases.append(['e4', 'fsharp4', 'g4', 'e4'])
            descrip.append("A short phrase emphasizing the leading tone resolving to the tonic.")
            phrases.append(['d4', 'c4', 'b3', 'd4', 'g3'])
            descrip.append("A longer phrase that emphasizes scale degrees in G major.")
            if self.tuning == 'GDAE':
                phrases.append(['g3', 'a3', 'b3', 'd4'])
                descrip.append("A basic stepwise ascending phrase.")
                phrases.append(['d4', 'e4', 'fsharp4', 'g4', 'a4'])
                descrip.append("Ascending through the scale.")
                phrases.append(['g4', 'b4', 'a4', 'g4'])
                descrip.append("A short phrase emphasizing the octave leap.")
                phrases.append(['e4', 'd4', 'b3', 'g3'])
                descrip.append("A descending phrase ending on the tonic.")
                phrases.append(['a4', 'b4', 'g5'])
                descrip.append("Highlighting the upper range with a leap from the dominant.")
                phrases.append(['g5', 'e5', 'd5', 'b4'])
                descrip.append("Descending from the high tonic.")
                phrases.append(['c5', 'b4', 'a4', 'g4'])
                descrip.append("Stepwise descent from the fourth scale degree in the higher octave.")
                phrases.append(['fsharp4', 'g4', 'a4', 'b4', 'c5', 'd5', 'e5', 'fsharp5', 'g5'])
                descrip.append("Ascending through the scale, reaching the high tonic.")
                phrases.append(['b4', 'd5', 'g5', 'a5', 'b5'])
                descrip.append("Emphasizing the upper range with larger leaps.")
                phrases.append(['b5', 'a5', 'g5', 'e5', 'd5'])
                descrip.append("A descending phrase starting from the high dominant.")

        if self.tuning in ('GDAE', 'AEAE') and self.key=='A' and self.scale.lower()=='major':
            phrases.append(['a3', 'b3', 'csharp4', 'e4'])
            descrip.append("A basic stepwise ascending phrase.")
            phrases.append(['e4', 'fsharp4', 'gsharp4', 'a4', 'b4'])
            descrip.append("Ascending through the middle of the scale.")
            phrases.append(['a4', 'b4', 'a4', 'fsharp4'])
            descrip.append("A neighbor-tone phrase centered around the tonic.")
            phrases.append(['e4', 'd4', 'csharp4', 'b3'])
            descrip.append("A descending phrase moving stepwise.")
            phrases.append(['b4', 'csharp5', 'e5', 'a5'])
            descrip.append("Emphasizing a leap to the higher tonic.")
            phrases.append(['a5', 'fsharp5', 'e5', 'csharp5'])
            descrip.append("Descending from the high tonic.")
            phrases.append(['d5', 'csharp5', 'b4', 'a4'])
            descrip.append("A stepwise descent in the upper range.")
            phrases.append(['fsharp4', 'gsharp4', 'a4', 'b4', 'csharp5', 'd5', 'e5', 'fsharp5', 'gsharp5', 'a5'])
            descrip.append("An ascending scalar run reaching the high tonic.")
            phrases.append(['b4', 'e5', 'a5', 'b5'])
            descrip.append("Highlighting the upper range with large leaps.")
            phrases.append(['b5', 'a5', 'gsharp5', 'e5', 'd5'])
            descrip.append("A descending phrase starting from the high dominant.")
            phrases.append(['a3', 'csharp4', 'e4', 'a4'])
            descrip.append("Emphasizing the tonic and the major third.")
            phrases.append(['a4', 'csharp5', 'b4', 'a4', 'gsharp4'])
            descrip.append("A short, turn-like phrase around the tonic.")
            phrases.append(['d4', 'fsharp4', 'a4', 'b4'])
            descrip.append("A stepwise ascending phrase emphasizing the dominant.")
            phrases.append(['b4', 'a4', 'gsharp4', 'fsharp4', 'e4'])
            descrip.append("Descending stepwise through the scale.")
            phrases.append(['fsharp4', 'a4', 'csharp5', 'e5'])
            descrip.append("Ascending skipwise, emphasizing the A major triad.")
            phrases.append(['gsharp4', 'a4', 'b4', 'csharp5', 'b4', 'a4'])
            descrip.append("A phrase emphasizing the leading tone and its resolution.")
            phrases.append(['e5', 'd5', 'csharp5', 'b4', 'a4'])
            descrip.append("A descending phrase in the upper range.")
            phrases.append(['a4', 'gsharp4', 'fsharp4', 'e4', 'fsharp4', 'gsharp4'])
            descrip.append("A wave-like phrase moving around the dominant.")
            phrases.append(['csharp5', 'b4', 'a4', 'fsharp4', 'e4', 'd4', 'csharp4'])
            descrip.append("A longer descending phrase through the scale.")
            phrases.append(['a5', 'e5', 'csharp5', 'b4', 'a4', 'fsharp4'])
            descrip.append("A descending phrase starting from the high tonic and emphasizing the A major triad.")

        if self.tuning in ('GDAE', 'AEAE', 'ADAE') and self.key=='A' and self.scale.lower()=='mixolydian':
            phrases.append(['a3', 'b3', 'csharp4', 'e4', 'g4'])
            descrip.append("Ascending phrase emphasizing the flattened seventh.")
            phrases.append(['g4', 'a4', 'b4', 'csharp5', 'g4'])
            descrip.append("A phrase highlighting the Mixolydian character with the G natural.")
            phrases.append(['e4', 'd4', 'csharp4', 'b3', 'a3'])
            descrip.append("Descending stepwise phrase.")
            phrases.append(['a4', 'g4', 'fsharp4', 'e4'])
            descrip.append("A descending phrase emphasizing the Mixolydian's flattened seventh.")
            phrases.append(['fsharp4', 'a4', 'g4', 'e4'])
            descrip.append("A phrase using the dominant and the flattened seventh.")
            phrases.append(['b4', 'a4', 'g4', 'fsharp4', 'e4', 'd4'])
            descrip.append("A descending phrase through the Mixolydian mode.")
            phrases.append(['csharp5', 'b4', 'a4', 'g4', 'fsharp4'])
            descrip.append("Descending from the third, emphasizing the Mixolydian character.")
            phrases.append(['a4', 'b4', 'csharp5', 'g4'])
            descrip.append("Emphasizing the leap from the third to the flattened seventh.")
            phrases.append(['fsharp4', 'g4', 'a4', 'b4', 'csharp5', 'd5', 'e5', 'fsharp5', 'g5', 'a5'])
            descrip.append("An ascending scalar run through the A Mixolydian mode.")
            phrases.append(['g5', 'fsharp5', 'e5', 'd5', 'csharp5', 'b4'])
            descrip.append("A descending phrase from the flattened seventh in the upper range.")
            phrases.append(['a3', 'csharp4', 'd4', 'e4', 'g4'])
            descrip.append("Ascending stepwise phrase with the flattened seventh.")
            phrases.append(['b4', 'g4', 'a4', 'csharp5'])
            descrip.append("Emphasizing the tonic and flattened seventh.")
            phrases.append(['e4', 'fsharp4', 'g4', 'a4'])
            descrip.append("Ascending through the middle of the scale.")
            phrases.append(['g4', 'a4', 'g4', 'e4', 'd4'])
            descrip.append("A phrase moving around the flattened seventh.")
            phrases.append(['d4', 'e4', 'fsharp4', 'g4', 'a4'])
            descrip.append("A stepwise ascending phrase emphasizing the Mixolydian character.")
            phrases.append(['csharp5', 'd5', 'b4', 'a4', 'g4'])
            descrip.append("Descending with emphasis on the flattened seventh.")
            phrases.append(['b4', 'csharp5', 'd5', 'e5', 'g5'])
            descrip.append("Ascending with the flat seventh on the top.")
            phrases.append(['a5', 'g5', 'fsharp5', 'e5'])
            descrip.append("Descending from the high tonic.")
            phrases.append(['d5', 'e5', 'g5', 'fsharp5', 'd5'])
            descrip.append("A phrase emphasizing the dominant and flattened seventh.")
            phrases.append(['a4', 'b4', 'csharp5', 'd5', 'g5', 'a5'])
            descrip.append("A scalar phrase emphasizing the tonic and flattened seventh in the higher octave.")

        if self.tuning in ('GDAE', 'AEAE', 'ADAE') and self.key=='A' and self.scale.lower()=='dorian':
            phrases.append(['a3', 'b3', 'c4', 'd4', 'fsharp4'])
            descrip.append("Ascending stepwise phrase with the natural sixth.")
            phrases.append(['e4', 'fsharp4', 'g4', 'a4'])
            descrip.append("Ascending through the higher part of the scale.")
            phrases.append(['g4', 'fsharp4', 'e4', 'd4', 'c4'])
            descrip.append("Descending phrase emphasizing the natural sixth.")
            phrases.append(['d4', 'c4', 'b3', 'a3'])
            descrip.append("A descending phrase from the fourth degree.")
            phrases.append(['fsharp4', 'a4', 'g4', 'e4'])
            descrip.append("Emphasizing the natural sixth with a leap to the tonic.")
            phrases.append(['a4', 'b4', 'c5', 'd5', 'fsharp5'])
            descrip.append("Ascending scalar phrase to the natural sixth in the upper range.")
            phrases.append(['g4', 'a4', 'g4', 'e4'])
            descrip.append("A short phrase revolving around the tonic and dominant.")
            phrases.append(['d5', 'e5', 'fsharp5', 'g5'])
            descrip.append("Ascending through the middle of the scale in the upper range.")
            phrases.append(['c5', 'd5', 'e5', 'fsharp5', 'g5', 'a5'])
            descrip.append("A scalar ascent to the high tonic.")
            phrases.append(['b4', 'c5', 'd5', 'fsharp5', 'e5', 'd5'])
            descrip.append("A phrase emphasizing the natural sixth and its surrounding tones.")
            phrases.append(['a3', 'c4', 'e4', 'fsharp4'])
            descrip.append("A leap-based phrase emphasizing the tonic and the natural sixth.")
            phrases.append(['b4', 'a4', 'g4', 'fsharp4', 'e4'])
            descrip.append("A descending stepwise phrase from the second scale degree.")
            phrases.append(['d4', 'e4', 'g4', 'a4'])
            descrip.append("Ascending through the scale with a skip from E to G.")
            phrases.append(['fsharp4', 'g4', 'fsharp4', 'e4', 'd4'])
            descrip.append("A phrase oscillating around the natural sixth.")
            phrases.append(['a4', 'g4', 'e4', 'fsharp4', 'd4'])
            descrip.append("Zigzagging through key tones of the A Dorian mode.")
            phrases.append(['c5', 'b4', 'a4', 'g4'])
            descrip.append("A descending phrase emphasizing the minor third.")
            phrases.append(['e5', 'd5', 'c5', 'b4'])
            descrip.append("A stepwise descent in the upper range.")
            phrases.append(['g4', 'fsharp4', 'e4', 'd4', 'c4', 'b3'])
            descrip.append("Descending scalar run emphasizing the Dorian character.")
            phrases.append(['a4', 'b4', 'c5', 'e5', 'fsharp5', 'a5'])
            descrip.append("An ascending phrase reaching the high tonic.")
            phrases.append(['b5', 'a5', 'g5', 'fsharp5', 'e5', 'd5'])
            descrip.append("Descending from the high second scale degree, moving stepwise.")

        if self.tuning in ('GDAE', 'ADAE') and self.key=='D' and self.scale.lower()=='major':
            phrases.append(['a3', 'b3', 'csharp4', 'd4'])
            descrip.append("Ascending stepwise from the fifth scale degree to the tonic.")
            phrases.append(['d4', 'e4', 'fsharp4', 'a4'])
            descrip.append("Ascending through the scale emphasizing the tonic to dominant jump.")
            phrases.append(['g4', 'fsharp4', 'e4', 'd4'])
            descrip.append("A descending stepwise phrase from the fourth scale degree.")
            phrases.append(['b4', 'a4', 'g4', 'fsharp4', 'e4'])
            descrip.append("Descending phrase emphasizing the dominant to the second scale degree.")
            phrases.append(['csharp5', 'd5', 'e5', 'fsharp5'])
            descrip.append("Ascending through the middle of the scale in the upper range.")
            phrases.append(['fsharp4', 'a4', 'b4', 'csharp5', 'd5'])
            descrip.append("A scalar ascent from the third scale degree to the tonic.")
            phrases.append(['e4', 'fsharp4', 'g4', 'a4', 'b4'])
            descrip.append("A stepwise ascending phrase emphasizing the second half of the D major scale.")
            phrases.append(['a4', 'b4', 'csharp5', 'd5', 'e5', 'fsharp5'])
            descrip.append("Ascending scalar run from the dominant to the high third scale degree.")
            phrases.append(['g5', 'fsharp5', 'e5', 'd5', 'csharp5', 'b4'])
            descrip.append("Descending through the upper range of the scale.")
            phrases.append(['b4', 'd5', 'fsharp5', 'a5', 'b5'])
            descrip.append("Emphasizing larger leaps from the dominant to the high dominant.")
            phrases.append(['d4', 'csharp4', 'b3', 'a3'])
            descrip.append("A descending stepwise phrase starting from the tonic.")
            phrases.append(['a4', 'b4', 'csharp5', 'd5', 'e5'])
            descrip.append("A stepwise ascending phrase from the dominant to the second scale degree in the upper range.")
            phrases.append(['fsharp4', 'g4', 'a4', 'fsharp4', 'e4'])
            descrip.append("A phrase moving around the third scale degree.")
            phrases.append(['b4', 'csharp5', 'b4', 'a4', 'g4'])
            descrip.append("A neighbor-tone phrase centered around the dominant.")
            phrases.append(['d5', 'e5', 'fsharp5', 'a5'])
            descrip.append("Ascending through the scale emphasizing the tonic to dominant leap in the upper range.")
            phrases.append(['a4', 'csharp5', 'b4', 'g4'])
            descrip.append("Zigzagging through key tones of the D major scale.")
            phrases.append(['g4', 'a4', 'b4', 'csharp5', 'd5', 'csharp5', 'b4'])
            descrip.append("A scalar ascent followed by a descent, emphasizing the tonic.")
            phrases.append(['e4', 'g4', 'fsharp4', 'd4'])
            descrip.append("Emphasizing the leaps around the third scale degree.")
            phrases.append(['csharp5', 'd5', 'fsharp5', 'e5', 'd5'])
            descrip.append("A phrase highlighting the tonic and third in the upper range.")
            phrases.append(['b5', 'a5', 'g5', 'fsharp5', 'e5', 'd5'])
            descrip.append("Descending from the high dominant, moving stepwise.")
