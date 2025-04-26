# Image Encryption Tool

This is a simple desktop application for image encryption and decryption using XOR operations combined with RGB channel shuffling, built with Python and Tkinter.
Developed for SkillCraft Technology - Task 02.

📋 Task Description
Develop a simple image encryption tool using pixel manipulation.Support operations like:
  Swapping pixel values
  Applying a basic mathematical operation to each pixel

This project uses:
XOR operation with a user-defined key
Swapping of RGB channels for encryption

🛠️ Features
🖼️ Load any JPG, PNG, BMP image
🔐 Encrypt the image using a key (integer)
🔓 Decrypt the encrypted image using the same key
💾 Save the encrypted and decrypted images automatically
🎨 GUI built with Tkinter for easy usage

🧰 Technologies Used
Python 3.x
Pillow (PIL) - for image processing
Tkinter - for the GUI

📦 Setup Instructions
Clone the repository
git clone https://github.com/sdave1226/Image-Encryption-Tool-Pixel-Manipulation
cd Image-Encryption

Install dependencies
pip install pillow

Run the application
python image_encrpytion_decryption.py

🖥️ Application Preview
Select an image
Enter a numeric key
Click Encrypt & Save to encrypt
Click Decrypt & Save to decrypt
Encrypted/Decrypted images are automatically saved in the project directory.

📂 Folder Structure
Image-Encryption/
│
├── task-02.py           # Main application script
├── README.md             # Project Documentation
├── sample_images/        # (Optional) Sample input images
└── outputs/              # (Optional) Encrypted/Decrypted images

⚙️ How Encryption Works
Each pixel's R, G, B values are XOR-ed with the entered key
RGB channels are shuffled after XOR operation
This makes the image appear distorted and unreadable without the correct key

🚀 Future Enhancements
Add drag-and-drop image support
Support batch image encryption
Enhance encryption using more complex pixel transformations
Add password-based key generation

✨ Developed By
SkillCraft Task Submission
Shreeya Dave

