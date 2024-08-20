from time import sleep

from vosk_tts import Model, Synth
import recognizer as rec
import voice as v

from characterai import aiocai
import asyncio

from vosk import SetLogLevel

SetLogLevel(-1)

char = "" # Character ID: ex. "https://character.ai/chat/<THIS PART>"
client = aiocai.Client("") # Your C.AI token (getter is in development)

model = Model(model_name="vosk-model-tts-ru-0.7-multi")
synth = Synth(model)


async def main():
    me = await client.get_me()

    async with await client.connect() as chat:
        chatv2 = await client.get_chat(char)

        while True:
            v.listen()
            text = rec.recognize()

            message = await chat.send_message(
                char, chatv2.chat_id, text
            )

            print(f'{message.name}: {message.text}')

            synth.synth(message.text, "output.wav", speaker_id=4)
            v.speak()

            sleep(2)


asyncio.run(main())
