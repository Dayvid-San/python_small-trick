from PIL import Image

imagem = Image.open(r'mia.jpg')

esquerda, cima, direita, baixo = (250,10,500,250)

imagem_cortada = imagem.crop((esquerda, cima, direita, baixo))

imagem_cortada.show()