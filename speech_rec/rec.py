import speech_recognition as sr

import click


def speech_to_text(file):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)
    text = r.recognize_google(audio, language='ja-JP')
    return text


@click.command()
@click.option('--file', type=str, default='output.wav')
def main(file):
    text = speech_to_text(file)
    print(text)

if __name__ == '__main__':
    main()
