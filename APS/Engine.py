import face_recognition as fr
from validador import get_user

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
   
        return True, rostos
    
    return False, []

def get_rostos(usuario,senha):
   
    rostos_conhecidos = []
    nomes_dos_rostos = []
    nome_user = get_user(usuario,senha,"Nome")
    arquivo = "img\{}.jpg".format(nome_user)
    print(arquivo)

    jubileia = reconhece_face(arquivo)
    if(jubileia[0]):
   
        rostos_conhecidos.append(jubileia[1][0])
        nomes_dos_rostos.append(nome_user)

        #Teago = reconhece_face("./img/Teago.jpg")
    #if(Teago[0]):
        #rostos_conhecidos.append(Teago[1][0])
        #nomes_dos_rostos.append("Teago")
    print(rostos_conhecidos, nomes_dos_rostos)
    return rostos_conhecidos, nomes_dos_rostos