# Convert m4a extension files to wav extension files

import os
import argparse

from pydub import AudioSegment

formats_to_convert = ['.m4a']
path = r'E:\BladeData\YunNanDa\\'
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename.endswith(tuple(formats_to_convert)):

            filepath = dirpath + '/' + filename
            (path, file_extension) = os.path.splitext(filepath)
            file_extension_final = file_extension.replace('.', '')
            try:
                track = AudioSegment.from_file(filepath,
                                               file_extension_final)
                wav_filename = filename.replace(file_extension_final, 'wav')
                wav_path = wav_filename
                print('CONVERTING: ' + str(filepath))
                file_handle = track.export(wav_path, format='wav')
                os.remove(filepath)
            except:
                print("ERROR CONVERTING " + str(filepath))

