# NASA Earth Picture Bot 🇺🇸

This bot is designed to send an image of Earth, taken by NASA's EPIC camera, to a Telegram chat. The image is selected at random from a list of the latest images available on the [NASA EPIC API](https://epic.gsfc.nasa.gov/api/natural).

## Requirements

- Python 3.5 or later
- `requests` library
- `telegram` library

## Usage

1. Clone this repository.
~~~
 git clone https://github.com/<username>/nasa-earth-picture-bot.git >
~~~
  
2. Create a Telegram bot using the [BotFather](https://t.me/BotFather) and obtain the API token for your bot.

3. Replace the placeholder `<token>` in `nasa_earth_ picture_bot.py` with the API token for your bot.

4. Replace the placeholder `<chat_id>` in `nasa_earth_ picture_bot.py` with the chat ID of the chat where you want the images to be sent.

5. Install the required libraries by running the following command in the terminal:
~~~
pip install -r requirements.txt>
~~~
6. Run the script `nasa_earth_ picture_bot.py` using the following command:
~~~
python nasa_earth_picture_bot.py
~~~
## Details
The bot should now send a random image of Earth to the specified Telegram chat. The script can be run periodically (e.g. using a cron job) to send updated images.
_______________________________________________________________________________________________________________________________________________________________________


# Bot de Imagens da Terra da NASA 🇧🇷

Este bot foi projetado para enviar uma imagem da Terra, tirada pela câmera EPIC da NASA, para um bate-papo do Telegram. A imagem é selecionada aleatoriamente a partir de uma lista das últimas imagens disponíveis na [API EPIC da NASA](https://epic.gsfc.nasa.gov/api/natural).

## Requisitos

- Python 3.5 ou posterior
- Biblioteca `requests`
- Biblioteca `telegram`

## Uso

1. Clone este repositório.
~~~
 git clone https://github.com/<username>/nasa-earth-picture-bot.git >
~~~
  

2. Crie um bot do Telegram usando o [BotFather](https://t.me/BotFather) e obtenha o token da API para o seu bot.

3. Substitua o placeholder `<token>` em `nasa_earth_ picture_bot.py` pelo token da API para o seu bot.

4. Substitua o placeholder `<chat_id>` em `nasa_earth_picture_bot.py` pelo ID do bate-papo onde você deseja enviar as imagens.

5. Instale as bibliotecas necessárias executando o seguinte comando no terminal:
~~~
pip install -r requirements.txt>
~~~

6. Execute o script `nasa_earth_picture_bot.py` usando o seguinte comando:
~~~
python nasa_earth_picture_bot.py
~~~
## Detalhes

O bot deverá agora enviar uma imagem aleatória da Terra para o bate-papo do Telegram especificado. O script pode ser executado periodicamente (por exemplo, usando um trabalho cron) para enviar imagens atualizadas.
