
def evaluate_hiring(results):
    waiting = results["Bekleyen Müşteri"]
    utilization = results["Çalışan Kullanım Oranı (%)"]

    if waiting > 10 or utilization > 90:
        return (
            "Yeni çalışan alınması öneriliyor. "
            "Mevcut personel yoğunluğu yüksek."
        )

    elif waiting > 0:
        return (
            "Şu an sistem sınırda çalışıyor. "
            "Yoğun günlerde ek personel düşünülebilir."
        )

    return (
        "Mevcut çalışan sayısı yeterli görünüyor."
    )
