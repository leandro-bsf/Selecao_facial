import os
import shutil
import threading
import numpy as np
from sklearn.cluster import DBSCAN
from deepface import DeepFace
from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, ttk, messagebox


class FaceClusteringApp:
    def __init__(self, master):
        self.master = master
        master.title("Classificador de Rostos")
        master.geometry("650x400")
        master.resizable(False, False)

        # Variáveis
        self.input_folder = StringVar()
        self.output_folder = StringVar()
        self.eps_value = StringVar(value="0.4")  # Valor padrão

        # Labels e Inputs
        Label(master, text="Pasta de Entrada (Fotos):").pack(pady=5)
        Entry(master, textvariable=self.input_folder, width=70).pack()
        Button(master, text="Selecionar Pasta", command=self.selecionar_pasta_entrada).pack(pady=5)

        Label(master, text="Pasta de Saída (Organizadas):").pack(pady=5)
        Entry(master, textvariable=self.output_folder, width=70).pack()
        Button(master, text="Selecionar Pasta", command=self.selecionar_pasta_saida).pack(pady=5)

        Label(master, text="EPS (sensibilidade do agrupamento, padrão 0.4):").pack(pady=5)
        Entry(master, textvariable=self.eps_value, width=10).pack()

        # Botão Executar
        self.btn_executar = Button(master, text="Iniciar Classificação", command=self.iniciar_classificacao)
        self.btn_executar.pack(pady=15)

        # Barra de progresso
        self.progress = ttk.Progressbar(master, orient="horizontal", length=500, mode="determinate")
        self.progress.pack(pady=10)

        # Status
        self.status_label = Label(master, text="")
        self.status_label.pack(pady=5)

        # Modelo que será usado
        self.model_name = "ArcFace"
        self.embedding_size = 512

    def selecionar_pasta_entrada(self):
        pasta = filedialog.askdirectory(title="Selecione a pasta de entrada")
        if pasta:
            self.input_folder.set(pasta)

    def selecionar_pasta_saida(self):
        pasta = filedialog.askdirectory(title="Selecione a pasta de saída")
        if pasta:
            self.output_folder.set(pasta)

    def iniciar_classificacao(self):
        if not self.input_folder.get() or not self.output_folder.get():
            messagebox.showerror("Erro", "Selecione as pastas de entrada e saída.")
            return

        self.btn_executar.config(state="disabled")
        self.status_label.config(text="Processando...")
        self.progress["value"] = 0

        threading.Thread(target=self.executar_classificacao).start()

    def executar_classificacao(self):
        try:
            input_folder = self.input_folder.get()
            output_folder = self.output_folder.get()

            try:
                eps = float(self.eps_value.get())
                if eps <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Erro", "EPS inválido. Informe um número maior que zero (ex.: 0.4)")
                self.status_label.config(text="Erro no EPS.")
                self.btn_executar.config(state="normal")
                return

            img_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder)
                         if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

            if not img_files:
                messagebox.showerror("Erro", "Nenhuma imagem encontrada na pasta.")
                self.status_label.config(text="")
                self.btn_executar.config(state="normal")
                return

            embeddings = []
            self.progress["maximum"] = len(img_files)

            for idx, img_path in enumerate(img_files):
                try:
                    obj = DeepFace.represent(img_path, model_name=self.model_name, enforce_detection=False)
                    embeddings.append(obj[0]["embedding"])
                except Exception as e:
                    print(f"Erro na imagem {img_path}: {e}")
                    embeddings.append(np.zeros(self.embedding_size))
                self.progress["value"] = idx + 1
                self.master.update_idletasks()

            embeddings = np.array(embeddings)

            clustering = DBSCAN(eps=eps, min_samples=1, metric="euclidean").fit(embeddings)

            for cluster_id in set(clustering.labels_):
                cluster_folder = os.path.join(output_folder, f"Pessoa_{cluster_id}")
                os.makedirs(cluster_folder, exist_ok=True)

                for idx, label in enumerate(clustering.labels_):
                    if label == cluster_id:
                        shutil.copy2(img_files[idx], cluster_folder)

            self.status_label.config(text="Processamento concluído com sucesso!")
            messagebox.showinfo("Concluído", "Fotos organizadas com sucesso na pasta de saída!")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
            self.status_label.config(text="Erro no processamento.")
        finally:
            self.btn_executar.config(state="normal")
            self.progress["value"] = 0


if __name__ == "__main__":
    root = Tk()
    app = FaceClusteringApp(root)
    root.mainloop()
