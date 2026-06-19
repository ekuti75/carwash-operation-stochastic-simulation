
from simulation.engine import run_simulation
from simulation.decision import evaluate_hiring

def main():
    print("=" * 60)
    print("OTO YIKAMA DÜKKANI PERSONEL SİMÜLASYONU")
    print("=" * 60)

    mevcut_personel = int(input("Mevcut çalışan sayısı: "))
    gunluk_musteri = int(input("Günlük ortalama müşteri sayısı: "))
    ortalama_hizmet = int(input("Bir aracın ortalama yıkama süresi (dakika): "))

    sonuc = run_simulation(
        mevcut_personel,
        gunluk_musteri,
        ortalama_hizmet
    )

    karar = evaluate_hiring(sonuc)

    print("\n--- SİMÜLASYON SONUÇLARI ---")
    for k, v in sonuc.items():
        print(f"{k}: {v}")

    print("\n--- KARAR ---")
    print(karar)

if __name__ == "__main__":
    main()
