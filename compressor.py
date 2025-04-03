import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def compress_image():
    file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        return

    try:
        quality = int(quality_entry.get())
        if not (1 <= quality <= 100):
            messagebox.showerror("Erro", "A qualidade deve estar entre 1 e 100.")
            return

        output_path = file_path.replace(".", "_compressed.")

        # Abrir e salvar a imagem com compressão
        image = Image.open(file_path)
        image.save(output_path, "JPEG", quality=quality, optimize=True)

        compressed_size = os.path.getsize(output_path) / 1024  # em KB
        messagebox.showinfo("Sucesso", f"Imagem comprimida salva em:\n{output_path}\nTamanho: {compressed_size:.2f} KB")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criar a janela
root = tk.Tk()
root.title("Compressor de Imagens")
root.geometry("400x600")

# Instruções
instruction_label = tk.Label(root, text="Selecione uma imagem para comprimir")
instruction_label.pack(pady=10)

# Campo de qualidade
quality_label = tk.Label(root, text="Qualidade (1-100):")
quality_label.pack()

quality_entry = tk.Entry(root)
quality_entry.insert(0, "40")
quality_entry.pack(pady=5)

# Botão para selecionar imagem
compress_button = tk.Button(root, text="Selecionar Imagem", command=compress_image)
compress_button.pack(pady=20)

# Rodar a interface
tk.mainloop()
