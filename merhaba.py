#!/usr/bin/env python3
# Evreni Yavaşlatan Merhaba Protokolü
# Bu kod gerçekten çalışır. Merhaba der ve bekler. Hepsi bu.

import time
import random

def evreni_yavaslat(kac_kez=7):
    """
    Merhaba diyerek evreni yavaşlatır.
    Uyarı: Geri dönüşü yoktur (vardır).
    """
    print("Evreni yavaşlatma protokolü başlatılıyor...")
    print("Bilimsel olarak kanıtlanmıştır ki her merhaba zamanı esnetir.")
    print("Kaynak: Benim hayal gücüm.")
    
    for i in range(1, kac_kez + 1):
        bekleme = random.uniform(0.3, 1.5) * i
        print(f"\n[{i}/{kac_kez}] Merhaba demeden önce evren {bekleme:.2f} saniye yavaşladı.")
        time.sleep(bekleme)
        print("Merhaba.")
        print("Evren: 'Tamam, yavaşladım işte.'")
    
    print("\nProtokol tamamlandı.")
    print("Evren artık biraz daha yavaş. Hissedin (etmeyin).")
    print("Tebrikler, kozmik bir katkıda bulundunuz.")

# Gizli kısım (bulunmaz)
# Not: Bu satırın altındaki şey hiçbir anlam ifade etmez.
gizli_mesaj = "VGhlcmUgaXMgbm8gcG9saXRpY2FsIG1lYW5pbmcuIEJ1dCBpZiB0aGVyZSB3YXMsIGl0IHdvdWxkIGJlIGhpZGRlbiBoZXJlLiBDaWRkaSBhbWEgZGVnaWwu"
# Base64 decode edilirse: "There is no political meaning. But if there was, it would be hidden here. Ciddi ama degil."
# Aslında Türkçe gizli anlam: Herkes kendi merhabasını kendi hızında söylesin, başkasına dayatılmasın. (abartılı yorum)

if __name__ == "__main__":
    try:
        evreni_yavaslat()
    except KeyboardInterrupt:
        print("\nProtokol kullanıcı tarafından durduruldu. Evren rahatladı.")
