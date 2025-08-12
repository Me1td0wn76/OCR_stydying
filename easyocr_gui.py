import tkinter as tk
from tkinter import filedialog, messagebox
import easyocr
from PIL import Image, ImageTk

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        try:
            # Display the selected image
            img = Image.open(file_path)
            img.thumbnail((400, 400))
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img

            # Perform OCR
            reader = easyocr.Reader(["en", "ja"])
            result = reader.readtext(file_path, detail=0)

            # Display OCR result
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "\n".join(result))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("EasyOCR GUI")

# Create and place widgets
frame = tk.Frame(root)
frame.pack(pady=10)

select_button = tk.Button(frame, text="Select Image", command=select_image)
select_button.pack()

image_label = tk.Label(root)
image_label.pack(pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

# Run the application
root.mainloop()
