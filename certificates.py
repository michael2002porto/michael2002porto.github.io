import os
import gdown
import fitz  # Ini adalah PyMuPDF

# --- KONFIGURASI FOLDER ---
PDF_DIR = "assets/pdf/certificates"
IMG_DIR = "assets/img/certificates"

# Buat folder jika belum ada
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

# --- DATA SERTIFIKAT (ID Drive : Nama File) ---
certificates = {
    # Internship
    "14ckQnCwrVStjgXo-vVpBtcYkoSCwhOua": "internship-hnix",
    "1yrx6IJHFsvEWFOZY78LD0pRAlG9w_fc-": "internship-adw",
    
    # Competition
    "1oyh12BV1FrYQtuwRgTCFU3vNPp-F4iz4": "comp-pilmapres",
    "1jEd_zNH-J-jcF5HKANVMN0MUMFoi26XQ": "comp-iisma",
    "1WG8rZKoc4dIMvednETRAdpRB1UT-K5ag": "comp-gemastik-data",
    "1r4jv7yEq27ff9tVDIrxCujYQ365tyxS_": "comp-gemastik-prog",
    "1e8FbkSBQTssNNLYbytxNt-ljfK-ZeypQ": "comp-ara-its",
    "1uzyOrxuN1J_Py_bibo8TD72XrM8P5uwZ": "comp-kreatif-smk",
    "1-9bJBkhuZuy5Z0Oona6VOapPwX7KKYal": "comp-seameo",
    
    # Training
    "1jQwZh2O7NdoMDfb14dsgjAmKfnCCNpXm": "train-azure",
    "1RzDFwXYaBOFegP3TH9K5Bus56ob71M0S": "train-coursera",
    "1gAY9kkmhIX2vvYrLK-w7z_GL0398mHBV": "train-data-journalism",
    "1wlbJtV7AqxwxgA2a2f1k4B7IyYN4fp9r": "train-blockchain",
    "1a0kEle-sW2jRRxdwcMsXiclS1VlNV9v6": "train-junior-web",
    "1ZOwsc-mc2HvvzrfSY1wc8gBrGwM_v7HR": "train-data-science",
    "1IuNs5aV9ICQuwZJCyRKMZvfl9Yg9pk82": "train-cyber-security",
    "1v4IN64wMGImvPjGOEUVf6JBCyobfhg4V": "train-data-scientist",
    "1jeptO_ct87NyExInFVrhFV1aD42CinoI": "train-progate-python",
    
    # Certification
    "1khNW4kuSNlQrRYAXttm0j-Eh2bbdHxtj": "cert-data-scientist",
    "1evpBl_gQ-V9Eu1Uf7T8Vbo_3myh_lVJG": "cert-alibaba-db",
    "1mm6eByX0gD1gkCHzhzgVeBncpem_K85U": "cert-data-engineer",
    "1thTMYFVzlmFlHnCZiBENXlWbdEf56HlR": "cert-mendix",
    "12MAjuAG-xu5PM-cx2O1_XnM6saYVLgPp": "cert-blockchain",
    "1pQhSokuK7joqsWPiL_j2vM-tYZ0ezL6c": "cert-java2",
    "1FDbEtQsfal2JdYPrKXmMNCxoz7YNeJhH": "cert-spring4",
    "1voqWNfzJjqt8UW1dx6iKqiobRfkPYnCn": "cert-junior-web",
}

def download_and_convert():
    print(f"Memulai sinkronisasi {len(certificates)} file...\n")
    
    for file_id, name in certificates.items():
        pdf_path = os.path.join(PDF_DIR, f"{name}.pdf")
        jpg_path = os.path.join(IMG_DIR, f"{name}.jpg")
        
        # 1. DOWNLOAD PDF (Jika belum ada)
        if not os.path.exists(pdf_path):
            print(f"⬇️ Mengunduh PDF: {name}...")
            url = f"https://drive.google.com/uc?id={file_id}"
            try:
                gdown.download(url, pdf_path, quiet=True)
            except Exception as e:
                print(f"❌ Gagal unduh {name}: {e}")
                continue
        
        # 2. KONVERSI PDF KE JPG (Halaman Pertama)
        if os.path.exists(pdf_path) and not os.path.exists(jpg_path):
            print(f"🖼️ Membuat Thumbnail JPG: {name}...")
            try:
                # Buka dokumen PDF
                doc = fitz.open(pdf_path)
                page = doc.load_page(0) # Ambil halaman 1 (index 0)
                
                # Matrix untuk meningkatkan resolusi (2x zoom = 144 DPI)
                # Tanpa matrix, gambar akan terlihat buram/pecah
                zoom = 2 
                mat = fitz.Matrix(zoom, zoom)
                
                pix = page.get_pixmap(matrix=mat)
                pix.save(jpg_path)
                doc.close()
                print(f"✅ Berhasil: {name}.jpg")
            except Exception as e:
                print(f"❌ Gagal konversi {name}: {e}")
        else:
            if os.path.exists(jpg_path):
                print(f"⏭️ {name}.jpg sudah ada, melewati...")

    print("\n✨ Semua proses selesai! Folder assets Anda sudah siap.")

if __name__ == "__main__":
    download_and_convert()