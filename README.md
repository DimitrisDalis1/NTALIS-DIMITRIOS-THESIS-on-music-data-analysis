#Exelixi mousikis
# important #

Haven't tried it, but I think you can just run the TTS-Lasso_Regression to test the program.
I have not uploaded the program that creates custom song names.
By using audio_analysis.py you convert our mp3 songs into features which are later stored into our CSV
Since the mp3s are not uploaded (at this branch at least) you cannot use audio_analyis.py but it is essentially our "Converter to usefull stuff" programm

Things that I have done

(DAPCA-audio_analysis.py)DAPCA which gives us some important features while also comparing different PCAs
(get_wanted_artists)Creates a csv with only the two artists we want to choose from
(MDS-audio_analysis.ipynb)Uses MDS with different distances
(pyAudioAnalysisFeaturesExtraction)Needs a lot of tweaking and WAV files. Prolly the next step to this project
(testing_pyAudioAnalysis.py)Same as the above
(TSNE-audio_analysis.ipynb)Another way of testing my data
(TTS-CNN.ipynb)A small-dummy CNN WIP
(TTS-Lasso_Regression.py)Used for predicting songs but the UI is not convenient (needs fixing)
(TTS-RandomForestClassifier)Haven't studied it yet
(TTS-RandomForestNestedCrossValidation)Same as the previous one
(create_false_songs.py)Used for creating dummy songs by tweaking what I thought as the most crucial features

About the csvs
(exctracted_data.csv)Output of get_wanted_artists.py
(false_data_songs.csv)Output of create_false_songs.py
(resultsWithALotOfFeatures.csv)Has about 100 diff songs
