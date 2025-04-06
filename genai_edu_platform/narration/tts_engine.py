import azure.cognitiveservices.speech as speechsdk

def generate_audio(text, filename="output.mp3"):
    speech_config = speechsdk.SpeechConfig(subscription="YourAzureKey", region="YourAzureRegion")
    speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text).get()