import asyncio
import requests
from telegram import Bot
import random

# Acessar a imagem
async def new_image():
    url = "https://epic.gsfc.nasa.gov/api/natural"
    response = requests.get(url)
    num = random.randint(0, 5)
    if response.status_code == 200:
        data = response.json()
        image = (data[num]['image'] + ".png")
        print(image)
    else:
        print("A solicitação falhou, o código status retornado foi:", response.status_code)

    url_image = ("https://epic.gsfc.nasa.gov/epic-archive/png/" + image)

    response_image = requests.get(url_image)

    if response_image.status_code == 200:
        with open(image, "wb") as f:
            f.write(response_image.content)
            print("A imagem foi baixada com sucesso.")
            return image
    else:
        print("A solicitação da imagem falhou, o código status retornado foi:", response_image.status_code)
        return None

# Inicialização do Bot do Telegram
bot = Bot(token='<TOKEN_ID>')
chat_id = '<CHAT_ID>'

async def main():
    image = await new_image()
    if image is not None:
        with open(image, "rb") as f:
            earth = f.read()
            await bot.send_photo(chat_id=chat_id, photo=earth)

asyncio.run(main())
