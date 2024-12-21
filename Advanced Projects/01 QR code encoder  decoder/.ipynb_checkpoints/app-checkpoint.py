import qrcode

def generate_qr_code(data, filename):
    # Create an instance of QRCode
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(filename)

if __name__ == "__main__":
    data = "https://github.com"
    filename = "github_qr.png"
    generate_qr_code(data, filename)
    print(f"QR Code generated and saved as {filename}")