# Importando bibliotecas
import cv2 as cv

# Selecionando imagens
img1 = cv.imread("caminho_para_imagem")
img2 = cv.imread("caminho_para_imagem")

# Verifica se as imagens foram lidas corretamente
if img1 is None or img2 is None:
    print("Erro ao carregar imagens.")
    exit()

# Verifica se as imagens têm as mesmas dimensões
if img1.shape[:2] != img2.shape[:2]:
    print("As imagens têm dimensões diferentes.")
    exit()
 
# Juntando as duas imagens lado a lado
final_image = cv.hconcat((img1, img2))
 
# Exibindo a imagem no colab
cv.imshow("Imagens Concatenadas", final_image)
cv.waitKey(0)
cv.destroyAllWindows()

# Verificando o tipo de dados da matriz da imagem
print('Dtype da imagem1 é {} e o Dtype da imagem2 é {}'
     .format(img1.dtype,img2.dtype))
# Verificando a altura da imagem
print('A altura da imagem1 é {} e a altura da imagem2 é {}'
     .format(img1.shape[0],img2.shape[0]))
# Verificando a largura da imagem
print('A largura da imagem1 é {} e a largura da imagem2 é {}'
     .format(img1.shape[1],img2.shape[1]))
# Verificando o número de canais da imagem
print('O número de canais da imagem1 é {} e o número de canais da imagem2 é {}'
     .format(img1.shape[2],img2.shape[2]))
b1, g1, r1 = cv.split(img1)
b2, g2, r2 = cv.split(img2)
# Verificando a cor b da imagem
print('Elementos diferente de zero na imagem1 é de {} e na imagem2 é de {}'
     .format(cv.countNonZero(b1),cv.countNonZero(b2)))
# Verificando a cor g da imagem
print('Elementos diferente de zero na imagem1 é de {} e na imagem2 é de {}'
     .format(cv.countNonZero(g1),cv.countNonZero(g2)))
# Verificando a cor r da imagem
print('Elementos diferente de zero na imagem1 é de {} e na imagem2 é de {}'
     .format(cv.countNonZero(r1),cv.countNonZero(r2)))

def image_difference(image_1, image_2):
    # Salva o shape das imagens
    img1_shape = image_1.shape[:2]
    img2_shape = image_2.shape[:2]
    
    # TESTE 1: Compara a estrutura das imagens
    if img1_shape == img2_shape:
        print("O tamanho das imagens são os mesmos")
        # Extrai a diferença de cor entre duas imagens
        difference = cv.subtract(image_1, image_2)
        # Separa as três cores da imagem
        b, g, r = cv.split(difference)
        # TESTE 2: Compara as cores das imagens
        if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
            print("As cores das imagens são iguais")
        else:
            print('As cores das imagens são diferentes')
    else:
        print("As imagens têm tamanhos diferentes")
        
    # Exibe a diferença entre as imagens
    cv.imshow("Diferença entre as imagens", difference)
    cv.waitKey(0)
    cv.destroyAllWindows()

image_difference(img1, img2)
