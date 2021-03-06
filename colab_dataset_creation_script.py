# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ljao-SBQ4ejjrVt18R-5j9g88AwRhkPU

# New Section
"""

!sudo apt install imagemagick

!git clone https://github.com/shubham303/IndicSceneTextRender.git

!sudo apt-get install -y libsdl-pango-dev

!sudo apt-get install libcairo2-dev

!sudo apt install font-manager

!sudo mkdir /usr/local/share/fonts/sample

!sudo cp /content/IndicSceneTextRender/Tamil/* /usr/local/share/fonts/sample/

from google.colab import drive
drive.mount('/content/drive')

!python /content/IndicSceneTextRender/render_Indian_language_scenetext.py /content/drive/MyDrive/MTP/dataset/IndicCorpus/wordlists/ta/1/train_words.txt  /content/IndicSceneTextRender/fontlists/tamil_fclistRS.txt  /content/drive/MyDrive/MTP/dataset/synthetic_text/tamil/  Tamil  1  /content/drive/MyDrive/MTP/dataset/plain_background_images/*.jpg

!python /content/IndicSceneTextRender/render_Indian_language_scenetext.py /content/drive/MyDrive/MTP/dataset/IndicCorpus/wordlists/ta/1/val_words.txt  /content/IndicSceneTextRender/fontlists/tamil_fclistRS.txt  /content/drive/MyDrive/MTP/dataset/synthetic_text/tamil/  Tamil  2  /content/drive/MyDrive/MTP/dataset/plain_background_images/*.jpg

!python /content/IndicSceneTextRender/render_Indian_language_scenetext.py /content/drive/MyDrive/MTP/dataset/IndicCorpus/wordlists/ta/1/test_words.txt  /content/IndicSceneTextRender/fontlists/tamil_fclistRS.txt  /content/drive/MyDrive/MTP/dataset/synthetic_text/tamil/  Tamil  3 /content/drive/MyDrive/MTP/dataset/plain_background_images/*.jpg

!python /content/IndicSceneTextRender/render_Indian_language_scenetext.py /content/drive/MyDrive/MTP/dataset/IndicCorpus/wordlists/ta/2/train_words.txt  /content/IndicSceneTextRender/fontlists/tamil_fclistRS.txt  /content/drive/MyDrive/MTP/dataset/synthetic_text/tamil/  Tamil  4  /content/drive/MyDrive/MTP/dataset/plain_background_images/*.jpg

!python /content/IndicSceneTextRender/render_Indian_language_scenetext.py /content/drive/MyDrive/MTP/dataset/IndicCorpus/wordlists/ta/2/val_words.txt  /content/IndicSceneTextRender/fontlists/tamil_fclistRS.txt  /content/drive/MyDrive/MTP/dataset/synthetic_text/tamil/  Tamil  5  /content/drive/MyDrive/MTP/dataset/plain_background_images/*.jpg

!python /content/IndicSceneTextRender/render_Indian_language_scenetext.py /content/drive/MyDrive/MTP/dataset/IndicCorpus/wordlists/ta/2/test_words.txt  /content/IndicSceneTextRender/fontlists/tamil_fclistRS.txt  /content/drive/MyDrive/MTP/dataset/synthetic_text/tamil/  Tamil  6  /content/drive/MyDrive/MTP/dataset/plain_background_images/*.jpg