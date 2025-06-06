import os
from pathlib import Path
from PIL import Image
from realesrgan.archs import RealESRGAN

# 📂 Diretório de entrada com imagens
input_folder = Path("teste")

# 📁 Diretório de saída
output_folder = Path("foto_editadas")
output_folder.mkdir(exist_ok=True)

# 🔥 Inicializa o modelo (CPU ou GPU)
model = RealESRGAN('cpu')  # Use 'cuda' se tiver GPU ou 'cpu' se não tiver
model.load_weights('RealESRGAN_x4.pth')

# 🖼️ Processa todas as imagens do diretório
for img_path in input_folder.glob("*.*"):
    try:
        image = Image.open(img_path).convert("RGB")
        print(f"Processando: {img_path.name}")

        # ✨ Melhora a imagem
        sr_image = model.predict(image)

        # 💾 Salva na pasta de saída
        output_path = output_folder / img_path.name
        sr_image.save(output_path)

        print(f"Salvo em: {output_path}")
    except Exception as e:
        print(f"Erro na imagem {img_path.name}: {e}")

print("✅ Todas as imagens foram processadas!")
