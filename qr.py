import qrcode
import qrcode.constants

data = {
    "S": "MOVISTAR_7BB0",
    "T": "WPA2",
    "P": "3NS5tYuBb67BK3LMHKL9",
}
wifi = f"WIFI:S:{data['S']};T:{data['T']};P:{data['P']};;"
qr = qrcode.QRCode(
    version=1,
    error_correction= qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(wifi)
qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color="white")

img.save("CasaWIFI.png")