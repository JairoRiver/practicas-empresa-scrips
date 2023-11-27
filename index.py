from pydub import AudioSegment
import os

def split_audio(input_file, output_folder, segment_length_ms=60000):
    audio = AudioSegment.from_mp3(input_file)
    audio_name = input_file.split("/")[2].split(".")[0]

    output_path = os.path.join(output_folder, audio_name)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    total_length = len(audio)
    start = 0
    segment_number = 1

    while start < total_length:
        end = start + segment_length_ms
        if end > total_length:
            end = total_length

        segment = audio[start:end]
        output_file = os.path.join(output_folder, audio_name,f"{audio_name}_{segment_number}.wav")
        segment.export(output_file, format="wav")

        start += segment_length_ms
        segment_number += 1

if __name__ == "__main__":
    input_file = "Id_3845085/original/Id_3845085.mp3"  # Reemplaza con el nombre de tu archivo MP3
    output_folder = "Id_3845085/split"

    split_audio(input_file, output_folder)
