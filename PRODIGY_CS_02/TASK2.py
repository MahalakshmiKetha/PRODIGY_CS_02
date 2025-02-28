from PIL import Image
import numpy as np


def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)

    encrypted_pixels = pixels ^ key
    encrypted_img = Image.fromarray(encrypted_pixels)
    return encrypted_img


def decrypt_image(encrypted_image, key):
    encrypted_pixels = np.array(encrypted_image)

    decrypted_pixels = encrypted_pixels ^ key
    decrypted_img = Image.fromarray(decrypted_pixels)
    return decrypted_img


def main():
    print("Image Encryption/Decryption Tool")

    action = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()
    key = int(input("Enter an integer key for encryption/decryption: "))

    if action == 'e':
        image_path = input("Enter the path to the image you want to encrypt: ")
        encrypted_image = encrypt_image(image_path, key)
        encrypted_image.show()
        encrypted_image.save("encrypted_image.png")
        print("Image encrypted successfully and saved as 'encrypted_image.png'.")

    elif action == 'd':
        encrypted_image_path = input("Enter the path to the encrypted image: ")
        encrypted_image = Image.open(encrypted_image_path)
        decrypted_image = decrypt_image(encrypted_image, key)
        decrypted_image.show()
        decrypted_image.save("sample.jpg")
        print("Image decrypted successfully and saved as 'decrypted_image.png'.")

    else:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")


if __name__ == "__main__":
    main()
