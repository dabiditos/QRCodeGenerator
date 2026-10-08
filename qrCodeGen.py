# qrCodeGen.py
# made by: @dabiditos
# https://realpython.com/python-generate-qr-code/
import segno

link = input("Enter the link: ")
name = input("Enter the name for the QR code: ")

dark = input("Enter the color for the dark areas (Example: #000000 (black)): ")
light = input("Enter the color for the light areas (Example: #FFFFFF (white)): ")

try:
    qrcode =segno.make_qr(link)
    qrcode.save(f"{name}.png", scale=10, dark=dark, light=light, border=1)
    print(f"QR code generated and saved as '{name}.png'.")
except Exception as e:
    print(f"An error occurred: {e}")

input("Press Enter to exit...")