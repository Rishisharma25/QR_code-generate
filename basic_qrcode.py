import qrcode as qr
img = qr.make("https://sih-mind-care-platform.vercel.app/login")
img.save("sih_midcare_prodect_qrcode.png")