# -*- coding: utf-8 -*-
"""
Yazar fotograflarini IEEE biyografi olcusune hazirlar.

IEEE-TJ sablonu, "Final printed size": yazar fotograflari tam olarak
1.00 inc genisliginde ve 1.25 inc yuksekliginde basilir (oran 0.80), ve
"Resolution": yazar fotograflari en az 300 dpi olmalidir.

Kaynak goruntuler figures/source/ altinda tutulur; bu betik onlari bas-omuz
cercevesine kirpar ve figures/ altina gonderime hazir olarak yazar.
Bilerek upscale yapilmaz: piksel eklemek gercek cozunurluk uretmez, yalnizca
dosyayi sartlari saglıyormus gibi gosterir.
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "figures", "source")
OUT = os.path.join(HERE, "figures")

RATIO = 1.00 / 1.25          # 0.80  genislik / yukseklik
MIN_DPI = 300

# (kaynak, cikti, yuz merkezi x orani, ustten kirpma orani, alt sinir orani)
# alt sinir None ise goruntunun alt kenarina kadar kirpilir.
JOBS = [
    ("karaduman_original.jpg", "photo_karaduman.jpg", 0.470, 0.12, None),
    ("karateke_original.jpg",  "photo_karateke.jpg",  0.360, 0.10, 0.76),
]


def crop_portrait(im, cx_frac, top_frac, bot_frac=None):
    """Bas-omuz cercevesini 0.80 oranina kirpar, olceklendirme yapmaz."""
    W, H = im.size
    top = int(H * top_frac)
    bot = H if bot_frac is None else int(H * bot_frac)
    h = bot - top
    w = int(round(h * RATIO))
    if w > W:                             # genislik yetmiyorsa yukseklikten kis
        w = W
        h = int(round(w / RATIO))
        top = min(top, H - h)
    cx = int(W * cx_frac)
    left = max(0, min(cx - w // 2, W - w))
    return im.crop((left, top, left + w, top + h))


def main():
    print("IEEE yazar fotograflari (hedef 1.00 x 1.25 inc, min %d dpi):" % MIN_DPI)
    warn = []
    for src, dst, cx, top, bot in JOBS:
        im = Image.open(os.path.join(SRC, src)).convert("RGB")
        out = crop_portrait(im, cx, top, bot)
        out.save(os.path.join(OUT, dst), "JPEG", quality=95, dpi=(300, 300))

        dpi_w, dpi_h = out.size[0] / 1.00, out.size[1] / 1.25
        ok = min(dpi_w, dpi_h) >= MIN_DPI
        print("  %-22s %4dx%-4d  basim %.0f dpi  %s"
              % (dst, out.size[0], out.size[1], min(dpi_w, dpi_h),
                 "OK" if ok else "DUSUK -- daha yuksek cozunurluklu kaynak gerekli"))
        if not ok:
            warn.append((dst, min(dpi_w, dpi_h)))

    if warn:
        print("\nUYARI: asagidaki fotograflar IEEE'nin 300 dpi alt sinirinin altinda.")
        for d, dpi in warn:
            need = int(round(MIN_DPI * 1.25))
            print("  %s: %.0f dpi. En az %dx%d piksellik bir kaynak gerekir."
                  % (d, dpi, MIN_DPI, need))


if __name__ == "__main__":
    main()
