impor os
from dotenv import load_dotenv
from telegram import update, replykeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler
    MessageHandler
    ContextTypes,
    filters
)

# ─── Load .env ────────────────────────────────────────────────────────────────
load_dotenv()
Token = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TOKEN bot Telegram tidak ditemukan. Pastikan variabel TELEGRAM_BOT_TOKEN ada di. env")

# ─── Daftar menu dan isi respon ───────────────────────────────────────────────
menu_responses={
    "🌐 Web Perpustakaan": (
        "Silahkan kunjungi website resmi Perpustakaan Daerah Kabupaten Pesisir Selatan untuk informasi lebih lanjut; "
        "https://diskerpus.pesisirselatankab.go.id/"
        
    ),
    "⏰ Jam Operasional": (
        "Senin-Jumat         : 08.00 WIB s.d 16.30 WIB\n"
        "Sabtu               : 09.00 WIB s.d 16.30 WIB\n"
        "Minggu & Hari Libur : Tutup"

    ), 
    "🗂️ Layanan Lantai 2 Perpusda Pessel": (
        " "

    ),  
    "🗂️ Layanan Lantai 3 Perpusda Pessel": (
        " "

    ),
    "🔁📚 Alur Peminjaman dan Pengembalian Buku": (
        ""

    ),
    "👥Syarat Pendaftaran Anggota Perpusda Pessel": (
        ""

    ), 
    "Tata Tertib Perpusda Pessel": (
        "Pengguna wajib menjaga ketenangan dan ketertiban di dalam perpustakaan\n"
        "Dilarang makan, minum, atau merokok di area perpustakaan\n"
        "Tas, jaket, dan barang bawaan disimpan di loker yang sudah disediakan\n"
        "Barang berharga menjadi tanggung jawab masing-masing pemustaka"

    ),
    "📆 Info Kegiatan Perpusda Pessel": (
        ""
        "Update kegiatan terbaru bisa kamu temukan di media sosial kami!"

    ),
    "📍☎ Alamat dan Kontak Perpusda Pessel": (
        "📍 Jl. Imam Bonjol – Painan\n"

        "📧 arsippustaka.pessel@gmail.com\n"
        "📞 0756) 21508"
        "📷 https://www.instagram.com/dispusker_pessel/"
        
    )
}

# ─── Siapkan keyboard menu ────────────────────────────────────────────────────
all_menus = ["📽️ Video Profil Perpustakaan"] + list(menu_responses.keys())
menu_keyboard = [[item] for item in all_menus]
reply_markup = replykeyboardMarkup(menu_keyboard, resize_keyboard=True)

# ─── Handler /start ──────────────────────────────────────────────────────────
async def start(update: Update, context; ContextTypes. DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo Dunsanak!👋 Si Sako di sini, siap membantu Dunsanak mencari informasi. Yuk, jelajahi berbagai layanan Perpustakaan Daerah Kabupaten Pesisir Selatan bersama Si Sako!😀 Silakan klik menu di bawah untuk mengakses informasi seputar layanan, program, dan fasilitas yang tersedia di Perpustakaan Daerah Kabupaten Pesisir Selatan."
        reply_markup=reply_markup
    )

# ─── Handler pesan teks ───────────────────────────────────────────────────────
 async def handle_message(update: update, context:contextTypes. DEFAULT_TYPE):
    text = update.message.text

    if text == "📽️ Video Profil Perpustakaan":
        video_path = os.path.join("video", "testing.mp4")
        if os.path.exists(video_path):
            with open(Perpusda_path, "rb") as vid:
                await update.message.reply_video(
                    video=vid,
                    caption="📽️ Berikut video profil Perpustakaan Daerah Kabupaten Pesisir Selatan.",
                    reply_markup=reply_markup
                )
        
        else:
            await update.message.reply_text(
                "⚠️Maaf, Video Belum Tersedia"
                reply_markup=reply_markup
            )
        return

    # Default: respon dari dictionary atau fallback
    response = menu_responses.get(
        text,
        "Maaf, menu tidak dikenali. Silakan pilih salah satu tombol yang tersedia."
    )
    await update.message.reply_text(response, reply_markup=reply_markup)

    # ─── Main ────────────────────────────────────────────────────────────────────
    if _name_ == "_main_":
        app = ApplicationBuilder().token(TOKEN).build()

        app.add_handler(commandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler_message))

        print("Bot berjalan...")
        app.run_polling()