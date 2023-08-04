from dotenv import load_dotenv
import os
import azure.cognitiveservices.speech as speech_sdk
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
cog_key = os.getenv('COG_SERVICE_KEY')
cog_region = os.getenv('COG_SERVICE_REGION')

# Initialize the conversation list with the system message
conversation = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Keep your responses short and engaging, and funny as well."
    }
]


def main():
    try:
        global speech_config
        # Instantiate and configure speech service
        speech_config = speech_sdk.SpeechConfig(cog_key, cog_region)
        print('Ready to use speech service in:', speech_config.region)

        while True:

            # Get spoken input prompt
            prompt = recognize_speech()

            # Send prompt to GPT and get the response as text
            response = get_response_from_gpt(prompt)

            # Generate speech from the GPT response
            speak(response)

    except Exception as ex:
        print("An error occurred:", ex)


def recognize_speech():
    prompt = ""

    # Configure speech recognition
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speech_sdk.SpeechRecognizer(
        speech_config, audio_config)
    print('Speak...')

    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        prompt = speech.text
        print(prompt)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    return prompt


def get_response_from_gpt(prompt):
    global conversation

    # Append the new user message to the conversation history
    conversation.append({"role": "user", "content": prompt})

    # Limit the conversation history to the last 4 exchanges
    conversation = conversation[-8:]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        max_tokens=80,
        messages=conversation
    )

    response = completion.choices[0].message.content

    # Append the assistant's reply to the conversation list
    conversation.append({"role": "assistant", "content": response})

    return response


def speak(response):

    print(response)

    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesis failed:", speak.reason)


if __name__ == "__main__":
    main()
