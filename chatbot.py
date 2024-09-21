import random

# Daftar respons chatbot
responses = {
    "halo": ["Hai! Senang bertemu denganmu."],
    "apa kabar": ["Saya baik-baik saja, terima kasih! "],
    "siapa kamu": ["Saya adalah chatbot yang siap membantu kamu.", "Saya chatbot yang bisa ngobrol denganmu.", "Saya asisten virtualmu!"],
    "terima kasih": ["Sama-sama!", "Tidak masalah!", "Senang bisa membantu!"],
    "bye": ["Sampai jumpa!", "Selamat tinggal!", "Semoga harimu menyenangkan!"],
}

# Fungsi untuk mendapatkan respons dari chatbot
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Maaf, saya tidak mengerti. Bisa diulang?"

# Fungsi utama untuk menjalankan chatbot
def chatbot():
    print("Selamat datang di Chatbot! (Ketik 'bye' untuk keluar)")
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == "bye":
            print("Chatbot: Sampai jumpa!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Menjalankan chatbot
if __name__ == "__main__":
    chatbot()
