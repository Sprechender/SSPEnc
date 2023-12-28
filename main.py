import os
import argparse
import time
import ffmpeg
import threading

start_time = time.perf_counter()

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="the file to encode")
args = parser.parse_args()
print(args.file)

def ffmpeg_func(file, res):
    output = f'encoded/{args.file}_enc_video_{res}p.mp4'
    cmd = ffmpeg.input(file).filter_('scale', -1, res).output(output)
    cmd.run()
    #cmd.run_async()

def convert_to_mp3(file):
    mp3_output = f'encoded/{args.file}_audio.mp3'
    audio_cmd = ffmpeg.input(file).output(mp3_output)
    audio_cmd.run()

if not os.path.exists(args.file):
    print("File does not exist")
    quit()
else:
    if not os.path.exists("encoded"):
        os.mkdir("encoded")

    video = ffmpeg.probe(args.file)
    height = video['streams'][0]['height']

    resolutions = [1080, 720, 360, 144]

    threads = []
    for res in resolutions:
        if height >= res:
            t = threading.Thread(target=ffmpeg_func, args=(args.file, res))
            t.start()
            threads.append(t)

    mp3_thread = threading.Thread(target=convert_to_mp3, args=(args.file,))
    mp3_thread.start()
    threads.append(mp3_thread)

    for t in threads:
        t.join()

end_time = time.perf_counter()
execution_time = end_time - start_time

print("\n\n\n")
print(f'Execution time in seconds: {execution_time:.2f}')
