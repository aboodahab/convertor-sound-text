import argparse
import whisper

from pathlib import Path
from gtts import gTTS


def readUserInputs():
    parser = argparse.ArgumentParser(description="hi")
    subparsers = parser.add_subparsers(dest="operation", required=True)
    soundParser = subparsers.add_parser("souToText")
    soundParser.add_argument("filepath", type=str, help="filepath of the file")

    textParser = subparsers.add_parser("textToSou")
    textParser.add_argument("filepath", help="the filepath of the file")
    textParser.add_argument("language", type=str, help="the text langauge ")
    textParser.add_argument(
        "text", nargs="+", help="the text to become a sound")

    args = parser.parse_args()

    return args


def checkFilepath(filepath):
    filepath2 = Path(filepath)
    if filepath2.exists():
        print("from Audio to Text")
        convertAudioToText(filepath)
        return
    print("we coudn't find this filepath!".capitalize())


def convertAudioToText(filepath):
    model = whisper.load_model("tiny")
    result = model.transcribe(filepath)
    print(result["text"])


def doesFileExist(filepath):
    file = Path(f"{filepath}.mp3")
    print(file, filepath)
    if file.exists():
        return True
    return False


def convertTextToAudio(text, langauge, filepath):

    if doesFileExist(filepath) == True:
        print("sorry that file exists",)
        return

    tts = gTTS(text, lang=langauge)
    tts.save(f"{filepath}.mp3")
    print("MP3 file created successfully!")


def codeHandler(operation):
    if operation == "souToText":
        checkFilepath(readUserInputs().filepath)
        return
    convertTextToAudio(" ".join(readUserInputs().text),
                       readUserInputs().language, readUserInputs().filepath)


codeHandler(readUserInputs().operation)
