import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

img_path = None
img_display = None
canvas_image_id = None

# Core: XOR + RGB swap for encryption and decryption
def process_image(img_path, key, mode="encrypt"):
    img = Image.open(img_path).convert("RGB")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            if mode == "encrypt":
                r_new = (g ^ key) % 256
                g_new = (b ^ key) % 256
                b_new = (r ^ key) % 256
            else:  # decrypt
                b_new = (g ^ key) % 256
                r_new = (b ^ key) % 256
                g_new = (r ^ key) % 256
            pixels[i, j] = (r_new, g_new, b_new)

    return img

def save_image(img, suffix="_encrypted"):
    base, ext = os.path.splitext(os.path.basename(img_path))
    new_path = f"{base}{suffix}{ext}"
    counter = 1
    while os.path.exists(new_path):
        new_path = f"{base}{suffix}_{counter}{ext}"
        counter += 1
    img.save(new_path)
    messagebox.showinfo("Saved", f"Image saved as {new_path}")

def update_canvas(img):
    global img_display, canvas_image_id
    img = img.resize((200, 200))
    img_display = ImageTk.PhotoImage(img)
    canvas.itemconfig(canvas_image_id, image=img_display)

# GUI actions
def select_image():
    global img_path, canvas_image_id
    img_path_local = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if img_path_local:
        img = Image.open(img_path_local).convert("RGB").resize((200, 200))
        img_display_local = ImageTk.PhotoImage(img)
        if canvas_image_id:
            canvas.itemconfig(canvas_image_id, image=img_display_local)
        else:
            canvas_image_id = canvas.create_image(100, 100, image=img_display_local)
        globals()["img_path"] = img_path_local
        globals()["img_display"] = img_display_local
        status_label.config(text="Image loaded successfully")

def encrypt_image():
    try:
        key = int(key_entry.get())
        encrypted_img = process_image(img_path, key, mode="encrypt")
        update_canvas(encrypted_img)
        save_image(encrypted_img, "_encrypted")
        status_label.config(text="Encryption complete")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_image():
    try:
        key = int(key_entry.get())
        decrypted_img = process_image(img_path, key, mode="decrypt")
        update_canvas(decrypted_img)
        save_image(decrypted_img, "_decrypted")
        status_label.config(text="Decryption complete")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Image Encryption Tool")
root.geometry("350x450")
root.resizable(False, False)

tk.Label(root, text="Image Encryption using XOR + RGB Shuffle", font=("Arial", 11, "bold"), wraplength=320).pack(pady=10)

canvas = tk.Canvas(root, width=200, height=200, bg='lightgray')
canvas.pack()
canvas_image_id = canvas.create_image(100, 100)

tk.Button(root, text="Select Image", command=select_image).pack(pady=10)

tk.Label(root, text="Enter Key (Number):").pack()
key_entry = tk.Entry(root)
key_entry.pack()

tk.Button(root, text="Encrypt & Save", command=encrypt_image, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Decrypt & Save", command=decrypt_image, bg="orange", fg="white").pack(pady=5)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=10)

root.mainloop()