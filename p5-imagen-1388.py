import cv2
## Ler la imagen con cv2. = computer vision
img = cv2.imread("dragon.jpg")
#} determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles (447, 447, 3)  
print(img.shape)
# mostrando imagen en Ventana barra de titulo dragon 1388
cv2.imshow("Dragon 1388", img)
## tiempo de espera
cv2.waitKey(0)
#destruir todas las vetanas
cv2.destroyAllWindows()