import numpy as np
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_path = '_static/playback-thumbnail.png'
import librosa
# We'll need IPython.display's Audio widget
from IPython.display import Audio
# We'll also use `mir_eval` to synthesize a signal for us
#import mir_eval.sonify
import os
import re
import random


pattern2 = re.compile(r'skordalos|psarantonis')
mp3list = []
fileList = os.listdir("./")
for f in fileList:
    if f.endswith(".mp3") and pattern2.match(f):
        mp3list.append(f)

  
allnotes={}
alldurations={}
for audio_file in mp3list:
    # Loading the audio file 
    y, sr = librosa.load(audio_file)
    # Extracting the chroma features and onsets
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    chroma = librosa.feature.chroma_stft(y=y_harmonic, sr=sr)
    onset_frames = librosa.onset.onset_detect(y=y_harmonic, sr=sr)
    first = True
    notes = []
    mypitch=[]
    mydurations=[]
    for onset in onset_frames:
        chroma_at_onset = chroma[:, onset]
        note_pitch = chroma_at_onset.argmax()
        # For all other notes
        if not first:
            note_duration = librosa.frames_to_time(onset, sr=sr)
            notes.append((note_pitch,onset, note_duration - prev_note_duration))
            prev_note_duration = note_duration
            # For the first note
        else:
            prev_note_duration = librosa.frames_to_time(onset, sr=sr)
            first = False
    print("Note pitch \t Onset frame \t Note duration")
    for entry in notes:
        print(entry[0],'\t\t',entry[1],'\t\t',entry[2])
        mypitch.append(entry[0])
        mydurations.append(entry[2])
    allnotes[audio_file] = mypitch
    alldurations[audio_file] = mydurations
    len(notes)

notes[0]

[len(i) for i in allnotes.values()]
allnotes['psarantonis1.mp3'][:20]

for i in allnotes.keys():
    print(f">{i}")
    for j in range(len(allnotes[i])):
        print(chr(allnotes[i][j]+65), end="")
    print()
'''
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
# sphinx_gallery_thumbnail_path = '_static/playback-thumbnail.png'
import librosa
# We'll need IPython.display's Audio widget
from IPython.display import Audio
# We'll also use `mir_eval` to synthesize a signal for us
import mir_eval.sonify


allnotes={}
alldurations={}
nres = 1000
resolution = 24
for audio_file in mp3list:
    # Loading the audio file 
    y, sr = librosa.load(audio_file)
    # Extracting the chroma features and onsets
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    ##   totalDuration = librosa.get_duration(y=y, sr=sr)
    ##  totalDuration
    ##  len(y_harmonic)
    ##  step = len(y_harmonic)//nres - 1
    ##  j = step
    ##    while j < len(y_harmonic):

    chroma = librosa.feature.chroma_stft(y=y_harmonic, sr=sr, n_fft=2048, hop_length=256, win_length=2048, n_chroma=24)
    onset_frames = librosa.onset.onset_detect(y=y_harmonic, sr=sr)
    first = True
    notes = []
    mypitch=[]
    mydurations=[]
    #    chroma.shape
    #    len(onset_frames)
    for onset in range(chroma.shape[1]): #onset_frames:
        chroma_at_onset = chroma[:, onset]
        note_pitch = chroma_at_onset.argmax()
        # For all other notes
        if not first:
            note_duration = librosa.frames_to_time(onset, sr=sr)
            notes.append((note_pitch,onset, note_duration - prev_note_duration))
            prev_note_duration = note_duration
            # For the first note
        else:
            prev_note_duration = librosa.frames_to_time(onset, sr=sr)
            first = False
    print("Note pitch \t Onset frame \t Note duration")
    for entry in notes:
        print(entry[0],'\t\t',entry[1],'\t\t',entry[2])
        mypitch.append(entry[0])
        mydurations.append(entry[2])
    allnotes[audio_file] = mypitch
    alldurations[audio_file] = mydurations
    len(notes)

notes[0]

[len(i) for i in allnotes.values()]
allnotes['psarantonis1.mp3'][:20]

countNotesDif=[]
countNotesDifFrequencies=[]
corfactor = 65 + resolution
with open("songs.fa", "w") as outf:
    for i in allnotes.keys():
        cur_note = ""
        prev_note = chr(allnotes[i][0]+65)
        outf.write(f">{i}\n")
        jj = 0
        for j in range(1,len(allnotes[i])):
            dif = allnotes[i][j] - allnotes[i][j-1] + corfactor
            cur_note = chr(allnotes[i][j]+65)
            if prev_note != cur_note:
                countNotesDif.append(dif)
                if dif == 89:
                    print([prev_note, cur_note, dif])
                #print(chr(allnotes[i][j]+65), end="")
                outf.write(f"{chr(dif)}")
            prev_note = cur_note
            jj+=1
        outf.write("\n")

mycntdifs = Counter(countNotesDif)


nrandomsongs = 200
randomlength=2000
with open("randomDifsongs.fa", "w") as outf:
    for i in range(nrandomsongs):
        outf.write(f">random{i}\n")
        seq = random.choices([chr(k) for k in mycntdifs.keys()], weights=list(mycntdifs.values()), k=randomlength)
        outf.write(''.join(seq))
        outf.write("\n")
'''