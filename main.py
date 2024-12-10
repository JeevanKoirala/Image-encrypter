import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import os

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        image_array = np.array(image)
        key_array = np.array([key], dtype=np.uint8)
        encrypted_decrypted_array = np.bitwise_xor(image_array, key_array)
        output_image = Image.fromarray(encrypted_decrypted_array)
        output_image.save(output_path)
        messagebox.showinfo("Success", f"Processed image saved at: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process the image: {e}")

def choose_input_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("All Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.webp"),
            ("PNG Files", "*.png"),
            ("JPEG Files", "*.jpg;*.jpeg"),
            ("Bitmap Files", "*.bmp"),
            ("TIFF Files", "*.tiff"),
            ("WebP Files", "*.webp"),
            ("All Files", "*.*"),
        ]
    )
    if file_path:
        input_path_var.set(file_path)
    else:
        messagebox.showerror("Error", "No file selected or invalid file.")

def choose_output_file():
    file_path = filedialog.asksaveasfilename(
        filetypes=[
            ("PNG Files", "*.png"),
            ("JPEG Files", "*.jpg;*.jpeg"),
            ("Bitmap Files", "*.bmp"),
            ("TIFF Files", "*.tiff"),
            ("WebP Files", "*.webp"),
        ],
        defaultextension=".png",
    )
    if file_path:
        output_path_var.set(file_path)

def process_image():
    input_path = input_path_var.get()
    output_path = output_path_var.get()
    key = key_var.get()
    if not input_path or not os.path.isfile(input_path):
        messagebox.showerror("Error", "Input file not found.")
        return
    if not output_path:
        messagebox.showerror("Error", "Please select an output file path.")
        return
    try:
        key = int(key)
        if 0 <= key <= 255:
            encrypt_decrypt_image(input_path, output_path, key)
        else:
            messagebox.showerror("Error", "Key must be between 0 and 255.")
    except ValueError:
        messagebox.showerror("Error", "Key must be a valid integer.")

root = tk.Tk()
root.title("Image Encrypter and Decrypter")

input_path_var = tk.StringVar()
output_path_var = tk.StringVar()
key_var = tk.StringVar()

tk.Label(root, text="Input Image Path:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=input_path_var, width=40).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=choose_input_file).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Output Image Path:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=output_path_var, width=40).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=choose_output_file).grid(row=1, column=2, padx=10, pady=5)

tk.Label(root, text="Encryption Key (0-255):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=key_var, width=10).grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Button(root, text="Process Image", command=process_image).grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()
