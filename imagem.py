from PIL import Image

# Carrega as imagens
imagem1 = Image.open("gengar.jpg")
imagem2 = Image.open("lucario.jpg")

largura, altura = imagem1.size
print(f"Largura: {largura}\nAltura: {altura}")

imagem1.show()

# Convertendo imagem1 para escala de cinza (exemplo)
cor_imagem1 = imagem1.convert('L')
cor_imagem1.show()

def merge(im1, im2):
    w = im1.size[0] + im2.size[0]  # Corrigido: size[0] ao invés de size([1])
    h = max(im1.size[1], im2.size[1])
    new_im = Image.new("RGBA", (w, h))
    new_im.paste(im1, (0, 0))
    new_im.paste(im2, (im1.size[0], 0))
    return new_im

# Mesclando imagem1 e imagem2
new_img = merge(imagem1, imagem2)
new_img.show()
