# QrcodeGenerator

simple qrcode generator with userfriendly gui.

![Screenshot (231)](https://github.com/Akshil742/QrcodeGenerator/assets/111780794/5f5efa39-4fda-48df-b4f1-686d9559bc39)

# how to use

1. Download the repository.
2. Open the repository folder, click inside of the "path bar", type "cmd" and press enter to open the terminal in your current directory.
3. Enter "pip install -r requirements.txt" to install the needed libraries (qrcode, tkinter, customtkinter and pillow) or install them manually.
   
       pip install -r requirements.txt

5. Enter "python main.py" for run the application.
   
       python main.py


# Functionality

File Extension: Choose between .png, .jpg, and .webp file extensions for your QR-Code.

Error Correction: Changes Error Correction Level. M allows up to 15% of the QR-Code to be unreadable but still work. Q allows for 25% and so on. If you enable the logo, you will be locked to using Q (25%) or H (30%).

Color: Changes the color of the QR-Code itself.

Background Color: Changes the background color. Choosing transparent removes the option to export as .jpg since it doesnt support transparency.

Version: Determines the version of the QR-Code. Higher versions increase the complexity of the QR-Code and allow for more data to be stored in it.

Border Size: Changes distance from the edge of the code to the border of the image. The lowest recommended value is 4.

Size: Changes the "line/block thickness" of the QR-Code. Your image resolution will be <number_of_blocks(determined by version and content) * size> pixels.

Enable Preview: Extends the window to the right and shows a live preview of your QR-Code. Using high versions whith preview enabled may lead to lag.

Enable Logo: Adds a chosen logo to the center of the QR-Code. This option disables .svg export and some other sliders. Saving a QR-Code with a logo, will always be 2000x2000px image.

Logosize: Changes the logosize. Depending on your logo, used Version and Error Correction, values above 5 might make the QR-Code unreadable. Its best to test this beforehand by trying to scan the QR-Code.

Change Logo: Opens up the file explorer to select a logo. Only supports .png, .jpg and .webp files.

Save: Generates and saves the QR-Code.

Open folder: Opens the file explorer in the folder where the QR-Codes are saved.
