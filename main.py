import requests
from googletrans import Translator
url = 'https://api.quotable.io/random'
sayari=outhre=""




# import required classes



from flask import Flask, flash, request, redirect, url_for, render_template



app = Flask(__name__)



@app.route('/')
def index():
    global sayari
    global outhre
    r = requests.get(url)
    quote = r.json()
    sayari = quote['content']
    outhre = f"\t-',{quote['author']}"
    return render_template('index.html',sayari=sayari,outhre=outhre)


@app.route('/tra')
def tra():
    translator = Translator()  # initalize the Translator object
    translations = translator.translate(sayari, dest='hi')  # translate two phrases to Hindi
    translations1 = translator.translate(outhre, dest='hi')  # translate two phrases to Hindi
    return render_template('index.html', sayari=translations.text, outhre=translations1.text)


@app.route('/down')
def down():
    global sayari
    global outhre
    from PIL import Image, ImageDraw, ImageFont

    # create Image object with the input image

    image = Image.open('download.png')

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Roboto-Bold.ttf', size=12)

    (x, y) = (9, 9)
    color = 'rgb(0, 0, 0)'  # black color

    # draw the message on the background

    draw.text((x, y), sayari+"\n"+outhre, fill=color, font=font)

    image.save('static/your.png')
    return render_template('signup.html')





if __name__ == '__main__':
    app.run(debug=True)
