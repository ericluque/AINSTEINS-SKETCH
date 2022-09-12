import cv2
import numpy as np

def sketch(image):
    h,w,_ = image.shape
    y = 0
    x = 0
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_inv = 255 - img_gray
    img_blur = cv2.GaussianBlur(img_gray_inv, (21,21), 0, 0)

    # fazemos o blend na imagem utilizando cv2.divide
    img_blend = cv2.divide(img_gray, 255 - img_blur, scale=256)
    imageN = image[y:h, x:int(w/2)]
    imageB = img_blend[y:h, int(w/2):w]
    imageB = np.stack((imageB,)*3, axis=-1)
    imagemfinal = np.hstack([imageN,imageB])

    return imagemfinal

# Inicializando a Webcam com VideoCapture
# O retorno contem  um booleano que diz se capturou ou não a imagem (ret)
# e a imagem da webcam (frame)
cap = cv2.VideoCapture(4)


while True:
    ret, frame = cap.read()
    cv2.imshow('A-HA Style', sketch(frame))
    if cv2.waitKey(1) == 13: #13 é o Enter Key
        break
        
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()  