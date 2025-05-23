🖼️ Edição Automatizada de Fotos com IA
Este projeto utiliza redes neurais para realizar classificação automática de rostos e aprimoramento de qualidade de imagens. Ele permite identificar diferentes pessoas em um diretório de fotos e organiza as imagens em pastas separadas. Além disso, o projeto conta com um recurso de melhoria da qualidade das imagens utilizando super-resolução com IA.

✅ O projeto foi convertido em um arquivo executável (.exe) para facilitar o uso sem a necessidade de configurar um ambiente Python.

🚀 Funcionalidades
🔍 Reconhecimento facial automático

📂 Classificação de fotos por pessoa (cada pessoa em uma pasta separada)

🏞️ Aprimoramento da qualidade das imagens usando IA (Real-ESRGAN)

🖥️ Interface de linha de comando interativa

📦 Aplicativo compilado em .exe para uso fácil

⚙️ Tecnologias Utilizadas
Python 3.11

DeepFace — Reconhecimento facial

Real-ESRGAN — Super-resolução de imagem

OpenCV — Manipulação de imagens

Pillow — Processamento de imagens

Scikit-learn — Agrupamento e comparação de faces

NumPy — Processamento numérico

tqdm — Barra de progresso para interatividade

📦 Instalação (Modo Desenvolvedor)
1. Clone o projeto
bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
2. Crie o ambiente virtual
bash
Copiar
Editar
python -m venv venv
3. Ative o ambiente
Windows:

bash
Copiar
Editar
venv\Scripts\activate
Linux/Mac:

bash
Copiar
Editar
source venv/bin/activate
4. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
5. Execute o script
bash
Copiar
Editar
python classificao_rosto.py
🛠️ Gerar o Executável (.exe)
Se desejar criar o executável para Windows:

bash
Copiar
Editar
pip install pyinstaller
pyinstaller --onefile classificao_rosto.py
