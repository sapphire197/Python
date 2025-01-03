# Import libraries
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import base64

# Function to encrypt credentials into a QR code
def generate_qr_code(username, password, filename='qr_code.png'):
    # Encode credentials using base64
    credentials = f'{username}:{password}'
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    # Generate QR code with error correction
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(encoded_credentials)
    qr.make(fit=True)

    # Create and save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

# Function to scan and decode the QR code
def scan_qr_code(qr_image_path):
    img = Image.open(qr_image_path)
    decoded_data = decode(img)

    # Check if data is decoded successfully
    if decoded_data:
        # Decode base64 content from the QR code
        qr_content = decoded_data[0].data.decode()
        decoded_credentials = base64.b64decode(qr_content).decode()

        # Extract and print username and password
        username, password = decoded_credentials.split(':')
        print(f"Decoded Credentials - Username: {username}, Password: {password}")
        return username, password
    else:
        print("QR Code could not be read or does not contain valid data.")
        return None, None

# Sample interactive system
def qr_code_auth_system():
    print("\nQR Code Authentication System\n")
    while True:
        print("1. Generate QR Code")
        print("2. Scan QR Code")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            filename = input("Enter filename for the QR code (default 'qr_code.png'): ") or 'qr_code.png'
            generate_qr_code(username, password, filename)
        elif choice == '2':
            qr_image_path = input("Enter the path of the QR code image: ")
            scan_qr_code(qr_image_path)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    qr_code_auth_system()
