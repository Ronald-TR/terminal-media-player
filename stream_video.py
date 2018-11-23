from pafy import pafy
from PIL import Image, ImageFilter
from pygame import mixer
from time import sleep
import cv2
import os
import asciigen
import subprocess
import _thread

def convert_mp4_to_wav(filename):
    arr_filename = [aux for aux in filename.split('.')[:-1]]
    wav_filename = ''.join(arr_filename) + '.wav'
    os.system(f'ffmpeg -i \'{filename}\' -ab 160k -ac 2 -ar 44100 -vn \'{wav_filename}\'')
    return wav_filename

def play_sound(soundname):
    mixer.init()
    sound = mixer.Sound(soundname)
    sound.play()

def download_from_youtube(url):
    '''
        Baixa o video do youtube e retorna o nome do arquivo (filename)
    '''
    vPafy = pafy.new(url)
    play = vPafy.getbest()
    play.download(play.filename)
    return play.filename


def play_on_terminal(url):
    cap = cv2.VideoCapture()
    cap.open(url)
    while (cap.isOpened):
        ret,frame = cap.read()
    
        if ret:
            binimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            r, aux = cv2.threshold(binimg, 127, 255, cv2.THRESH_OTSU)
            img = Image.fromarray(frame)
            asciiart = asciigen.from_image(img, width=250)
            os.system('clear')
            print(asciiart)
            sleep(0.003)
        else:
            break    

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import argparse
    youtube_help = '''
    'Declara o link (se URL) como um video do youtube\n
    Por politicas de privacidade do google, o video será baixado por completo antes de ser executado\n'
    '''
    file_help = '''
        Define o caminho, como path/para/arquivo\n
    '''
    parser = argparse.ArgumentParser(description='Assista videos no terminal!!')
    parser.add_argument('url', help='Caminho para o video, pode ser um diretório ou uma URL')
    parser.add_argument('--youtube', '-y', nargs='?', type=bool, default=False, help=youtube_help)
    parser.add_argument('--file', '-f', nargs='?', type=bool, default=False, help=file_help)
    args = parser.parse_args()
    if args.youtube == False and args.file == False:
        play_on_terminal(args.url)
    elif (args.file == False) and (args.youtube == None):
        filename = download_from_youtube(args.url)
        wav_filename = convert_mp4_to_wav(filename)
        sleep(1)
        play_sound(wav_filename)
        play_on_terminal(filename)
    else:
        wav_filename = convert_mp4_to_wav(args.url)
        play_sound(wav_filename)
        sleep(0.8)
        play_on_terminal(args.url)
