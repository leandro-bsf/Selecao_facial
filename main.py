import os
from PIL import Image, ImageEnhance, ImageOps

def aplicar_ajustes(img):
    # Simular Ajuste de Temperatura: Aquecer ajustando RGB
    def adjust_temperature(img, value):
        r, g, b = img.split()
        r = r.point(lambda i: i + value)
        b = b.point(lambda i: i - value)
        return Image.merge('RGB', (r, g, b))

    # Ajustar temperatura (simplificado para +14)
    img = adjust_temperature(img, 11)

    # Ajustar saturação (Color Vibrancy +14)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.05)  # Incrementa a saturação próxima de +14

    # Ajustar brilho (aproximação para exposição +0.20)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.5)  # Incrementa a exposição/luminosidade

    return img

def editar_imagens(diretorio_entrada, diretorio_saida):
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    for arquivo_nome in os.listdir(diretorio_entrada):
        caminho_arquivo = os.path.join(diretorio_entrada, arquivo_nome)
        
        if os.path.isfile(caminho_arquivo) and caminho_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            with Image.open(caminho_arquivo) as img:
                # Aplicar os ajustes simulados
                img_final = aplicar_ajustes(img)
                
                # Converter para RGB se a imagem estiver em RGBA
                if img_final.mode == 'RGBA':
                    img_final = img_final.convert('RGB')
                
                # Salvar a imagem processada
                caminho_saida = os.path.join(diretorio_saida, arquivo_nome)
                img_final.save(caminho_saida)
                print(f'Imagem {arquivo_nome} foi processada e salva em {caminho_saida}')
                print(f'Imagem {arquivo_nome} foi processada e salva em {caminho_saida}')


# Defina os diretórios de entrada e saída
diretorio_entrada = 'fotos_sem_edicao'
diretorio_saida = 'foto_editadas'

# Chame a função para editar as imagens
editar_imagens(diretorio_entrada, diretorio_saida)