# -*- coding: utf-8 -*-
"""
Akciger-Odakli ViT — yayin duzeyinde yontem sekilleri.

Tasarim kisitlari (dergi sekli):
  * Cift kolon genisligi 180 mm  ->  viewBox genisligi 900 birim (1 birim = 0,2 mm)
  * Metin: 14 birim = 7,9 pt ; 12 birim = 6,8 pt ; 11 birim = 6,2 pt  (>= 6 pt kurali)
  * Tek yazi tipi ailesi (Helvetica / Arial), golge ve gradyan yok
  * Gri tonlamada ayrisma: dolgu tonu + kesik/duz cerceve, yalnizca renk degil
  * Semalar sematik anatomik cizimlerle desteklenir

Cikti:
  1) sekil_*.svg            tek basina, acik tema, satir-ici nitelik  (Word / LaTeX)
  2) akis_diyagramlari.html template.html icine gomulu, tema-duyarli surum

Kullanim:  python make_figures.py
"""

import os
import io
import math

HERE = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Palet — yalnizca tek basina SVG ciktisinda kullanilir (baski icin ayarli).
# --------------------------------------------------------------------------
P = {
    "ink": "#1B2327", "ink2": "#5A686F",
    "node_fill": "#FFFFFF", "node_line": "#7C888E",
    "panel": "#F4F6F7", "panel_line": "#D8DFE1",
    "acc": "#17616B", "acc_fill": "#DDEBED", "acc_ink": "#0E4952",
    "alt": "#96421F", "alt_fill": "#F4E5DC", "alt_ink": "#7A3418",
    "tissue": "#CBD2D5", "lung": "#EDF3F4", "line_soft": "#A9B4B8",
    "edge": "#6E7A80",
}
FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"

# Tipografi olcegi (birim = 0,2 mm)
TS = {"panel": 15, "band": 12, "title": 13.5, "detail": 11.5, "edge": 11, "cap": 11.5}


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def scale_path(d, s, dx, dy):
    """Mutlak komutlu (M/L/C/Q/Z) yol verisini olcekleyip otelemek icin."""
    out, isx = [], True
    for t in d.replace(",", " ").split():
        if t.isalpha():
            out.append(t)
            isx = True
        else:
            v = float(t) * s + (dx if isx else dy)
            out.append("%.2f" % v)
            isx = not isx
    return " ".join(out)


# --------------------------------------------------------------------------
# Sematik gogus radyografisi — 100 x 130 birimlik yerel uzayda tanimli
# --------------------------------------------------------------------------
BODY = ("M 20 4 C 11 10 6 34 6 62 C 6 92 12 118 20 126 L 80 126 "
        "C 88 118 94 92 94 62 C 94 34 89 10 80 4 Z")
LUNG_R = ("M 41 20 C 28 22 18 42 17 66 C 16 86 21 104 28 109 "
          "C 37 113 46 106 46 92 L 46 24 C 46 21 44 20 41 20 Z")
LUNG_L = ("M 59 20 C 72 22 82 42 83 66 C 84 86 79 104 72 109 "
          "C 63 113 54 106 54 92 L 54 24 C 54 21 56 20 59 20 Z")
MEDIAST = "M 44 20 L 56 20 L 56 106 L 44 106 Z"
HEART = "M 54 58 C 67 60 73 78 70 92 C 67 102 59 106 54 105 Z"
CLAV_R = "M 15 27 Q 31 18 45 25"
CLAV_L = "M 85 27 Q 69 18 55 25"
RIBS = ["M 18 34 Q 32 41 45 38", "M 17 50 Q 31 58 45 55",
        "M 18 66 Q 32 75 45 72", "M 20 82 Q 33 91 45 88",
        "M 82 34 Q 68 41 55 38", "M 83 50 Q 69 58 55 55",
        "M 82 66 Q 68 75 55 72", "M 80 82 Q 67 91 55 88"]

GW, GH = 100.0, 130.0          # yerel tuval
LUNG_CX, LUNG_CY = 50.0, 66.0  # akciger kutlesinin merkezi (RoI yakinlastirmasi icin)


class Canvas:
    """SVG parcalarini toplar. mode: 'html' (CSS sinifli) | 'inline' (nitelikli)."""

    def __init__(self, fid, w, h, mode):
        self.fid, self.w, self.h, self.mode = fid, w, h, mode
        self.o = io.StringIO()
        self.defs_extra = io.StringIO()
        self._clip = 0

    # ---- stil cozumleyiciler ---------------------------------------------
    def _sty(self, css, **attrs):
        if self.mode == "html":
            return 'class="%s"' % css
        return " ".join('%s="%s"' % (k.replace("_", "-"), v) for k, v in attrs.items())

    def _shape(self, kind):
        m = {
            "n":  ("n",  dict(fill=P["node_fill"], stroke=P["node_line"], stroke_width=1.1)),
            "a":  ("n-a", dict(fill=P["acc_fill"], stroke=P["acc"], stroke_width=1.6)),
            "b":  ("n-b", dict(fill=P["alt_fill"], stroke=P["alt"], stroke_width=1.3,
                               stroke_dasharray="5 3")),
            "p":  ("n-p", dict(fill=P["panel"], stroke=P["panel_line"], stroke_width=1.0)),
        }[kind]
        return self._sty(m[0], **m[1])

    def _text(self, role, anchor="middle"):
        css = {"panel": "tp", "band": "tb", "title": "tt", "detail": "td",
               "edge": "te", "cap": "tc", "key": "tk", "val": "tv"}[role]
        size = {"panel": TS["panel"], "band": TS["band"], "title": TS["title"],
                "detail": TS["detail"], "edge": TS["edge"], "cap": TS["cap"],
                "key": TS["detail"], "val": TS["detail"]}[role]
        weight = "700" if role == "panel" else ("600" if role in ("title", "band") else "400")
        col = {"panel": P["ink"], "band": P["ink2"], "title": P["ink"],
               "detail": P["ink2"], "edge": P["ink2"], "cap": P["ink2"],
               "key": P["ink2"], "val": P["ink"]}[role]
        extra = {}
        if role == "band":
            extra["letter_spacing"] = 0.9
        if role == "val":
            extra["font_variant_numeric"] = "tabular-nums"
        a = self._sty(css, font_family=FONT, font_size=size, font_weight=weight,
                      fill=col, **extra)
        return a + ' text-anchor="%s"' % anchor

    def _stroke(self, kind, dashed=False):
        css = {"e": "e", "a": "e e-a", "b": "e e-b", "g": "gl", "go": "go",
               "gk": "gk", "ax": "ax", "ref": "ref", "pl": "pl"}[kind]
        d = {
            "e":   dict(fill="none", stroke=P["edge"], stroke_width=1.3),
            "a":   dict(fill="none", stroke=P["acc"], stroke_width=1.6),
            "b":   dict(fill="none", stroke=P["alt"], stroke_width=1.4),
            "g":   dict(fill="none", stroke=P["line_soft"], stroke_width=0.8),
            "go":  dict(fill="none", stroke=P["ink2"], stroke_width=1.0),
            "gk":  dict(fill="none", stroke=P["acc"], stroke_width=1.6),
            "ax":  dict(fill="none", stroke=P["ink2"], stroke_width=0.9),
            "ref": dict(fill="none", stroke=P["line_soft"], stroke_width=0.8,
                        stroke_dasharray="3 2"),
            "pl":  dict(fill="none", stroke=P["acc"], stroke_width=1.4),
        }[kind]
        if dashed:
            d = dict(d); d["stroke_dasharray"] = "5 3"
            css += " dsh"
        return self._sty(css, **d)

    def _mk(self, kind):
        return "mk%s%s" % (kind, self.fid)

    # ---- temel ciziciler --------------------------------------------------
    def defs(self):
        w = self.o.write
        w("<defs>")
        for k in ("e", "a", "b"):
            fill = (self._sty({"e": "mk", "a": "mk mk-a", "b": "mk mk-b"}[k],
                              fill={"e": P["edge"], "a": P["acc"], "b": P["alt"]}[k]))
            w('<marker id="%s" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" '
              'markerHeight="6.5" orient="auto-start-reverse">'
              '<path d="M 0 1 L 9 5 L 0 9 z" %s /></marker>' % (self._mk(k), fill))
        w("</defs>")

    def panel_label(self, x, y, letter, text):
        self.o.write('<text x="%s" y="%s" %s>%s</text>'
                     % (x, y, self._text("panel", "start"), esc(letter)))
        self.o.write('<text x="%s" y="%s" %s>%s</text>'
                     % (x + 32, y, self._text("band", "start"), esc(text)))

    def node(self, x, y, w, h, title, subs=(), kind="n", rx=2.5):
        subs = list(subs)
        self.o.write('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" %s />'
                     % (x, y, w, h, rx, self._shape(kind)))
        cx = x + w / 2.0
        block = 15 + 13.5 * len(subs)
        base = y + (h - block) / 2.0 + 11.5
        self.o.write('<text x="%s" y="%.1f" %s>%s</text>'
                     % (cx, base, self._text("title"), esc(title)))
        for i, s in enumerate(subs):
            self.o.write('<text x="%s" y="%.1f" %s>%s</text>'
                         % (cx, base + 15.5 + 13.5 * i, self._text("detail"), esc(s)))

    def band(self, x, y, w, h, text):
        self.o.write('<rect x="%s" y="%s" width="%s" height="%s" rx="2" %s />'
                     % (x, y, w, h, self._shape("p")))
        self.o.write('<text x="%s" y="%.1f" %s>%s</text>'
                     % (x + w / 2.0, y + h / 2.0 + 4, self._text("band"), esc(text)))

    def diamond(self, cx, cy, hw, hh, title, sub=None):
        pts = "%s,%s %s,%s %s,%s %s,%s" % (cx, cy - hh, cx + hw, cy, cx, cy + hh, cx - hw, cy)
        self.o.write('<polygon points="%s" %s />' % (pts, self._shape("n")))
        self.o.write('<text x="%s" y="%s" %s>%s</text>'
                     % (cx, cy + (-2 if sub else 4), self._text("title"), esc(title)))
        if sub:
            self.o.write('<text x="%s" y="%s" %s>%s</text>'
                         % (cx, cy + 12, self._text("detail"), esc(sub)))

    def edge(self, pts, arrow=True, kind="e", dashed=False, label=None, sub=None,
             lx=None, ly=None, anchor="middle"):
        d = "M %s %s " % pts[0] + " ".join("L %s %s" % p for p in pts[1:])
        mk = ' marker-end="url(#%s)"' % self._mk(kind) if arrow else ""
        self.o.write('<path d="%s" %s%s />' % (d, self._stroke(kind, dashed), mk))
        if label:
            self.o.write('<text x="%s" y="%s" %s>%s</text>'
                         % (lx, ly, self._text("edge", anchor), esc(label)))
        if sub:
            self.o.write('<text x="%s" y="%s" %s>%s</text>'
                         % (lx, ly + 13, self._text("edge", anchor), esc(sub)))

    def caption(self, cx, y, text):
        self.o.write('<text x="%s" y="%s" %s>%s</text>'
                     % (cx, y, self._text("cap"), esc(text)))

    def kv(self, x, w, y, key, val):
        self.o.write('<text x="%s" y="%s" %s>%s</text>'
                     % (x, y, self._text("key", "start"), esc(key)))
        self.o.write('<text x="%s" y="%s" %s>%s</text>'
                     % (x + w, y, self._text("val", "end"), esc(val)))

    # ---- sematik gogus radyografisi ---------------------------------------
    def cxr(self, cx, top, h, mode):
        """mode: 'plain' | 'contour' | 'masked' | 'roi'"""
        s = h / GH
        w = GW * s
        x = cx - w / 2.0
        o = self.o
        soft = self._sty("gs", fill=P["tissue"], stroke="none")
        lungf = self._sty("gf", fill=P["node_fill"], stroke="none")
        keepf = self._sty("gkf", fill=P["acc_fill"], stroke="none")
        frame = self._sty("gfr", fill="none", stroke=P["line_soft"], stroke_width=1.0)

        def pth(d, sty, s_=None, dx=None, dy=None):
            o.write('<path d="%s" %s />'
                    % (scale_path(d, s_ if s_ is not None else s,
                                  dx if dx is not None else x,
                                  dy if dy is not None else top), sty))

        cid = "cl%s_%s" % (self.fid, self._clip)
        self._clip += 1

        if mode in ("plain", "contour"):
            pth(BODY, self._sty("gb", fill=P["panel"], stroke=P["ink2"], stroke_width=1.0))
            pth(LUNG_R, lungf); pth(LUNG_L, lungf)
            pth(MEDIAST, soft); pth(HEART, soft)
            o.write('<clipPath id="%s">' % cid)
            pth(LUNG_R, ""); pth(LUNG_L, "")
            o.write("</clipPath>")
            o.write('<g clip-path="url(#%s)">' % cid)
            for r in RIBS:
                pth(r, self._stroke("g"))
            o.write("</g>")
            pth(CLAV_R, self._stroke("g")); pth(CLAV_L, self._stroke("g"))
            lung_style = self._stroke("gk", dashed=True) if mode == "contour" else self._stroke("go")
            pth(LUNG_R, lung_style); pth(LUNG_L, lung_style)
        else:
            zoom = 1.34 if mode == "roi" else 1.0
            s2 = s * zoom
            dx = cx - LUNG_CX * s2
            dy = top + h / 2.0 - LUNG_CY * s2
            o.write('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" %s />'
                    % (x, top, w, h, soft))
            o.write('<clipPath id="%s">' % cid)
            o.write('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" />' % (x, top, w, h))
            o.write("</clipPath>")
            o.write('<g clip-path="url(#%s)">' % cid)
            pth(LUNG_R, keepf, s2, dx, dy); pth(LUNG_L, keepf, s2, dx, dy)
            cid2 = "cl%s_%s" % (self.fid, self._clip); self._clip += 1
            o.write('<clipPath id="%s">' % cid2)
            pth(LUNG_R, "", s2, dx, dy); pth(LUNG_L, "", s2, dx, dy)
            o.write("</clipPath>")
            o.write('<g clip-path="url(#%s)">' % cid2)
            for r in RIBS:
                pth(r, self._stroke("g"), s2, dx, dy)
            o.write("</g>")
            pth(LUNG_R, self._stroke("gk"), s2, dx, dy)
            pth(LUNG_L, self._stroke("gk"), s2, dx, dy)
            o.write("</g>")
        o.write('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" %s />'
                % (x, top, w, h, frame))
        return x, w

    # ---- dikkat isi haritasi (akciger konturu bindirmeli) -----------------
    def heat(self, cx, top, h, kind, nc=8, nr=10):
        s = h / GH
        w = GW * s
        x = cx - w / 2.0
        cw, ch = w / nc, h / nr
        for r in range(nr):
            for cc in range(nc):
                u, v = (cc + .5) / nc, (r + .5) / nr
                if kind == "central":
                    val = math.exp(-((u - .5) ** 2) / (2 * .055 ** 2)) * (.30 + .95 * max(0., v - .22))
                else:
                    g = max(math.exp(-((u - .28) ** 2) / (2 * .10 ** 2)),
                            math.exp(-((u - .72) ** 2) / (2 * .10 ** 2)))
                    val = g * math.exp(-((v - .40) ** 2) / (2 * .24 ** 2)) * 1.05
                val = max(0.0, min(1.0, val))
                self.o.write('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" %s '
                             'fill-opacity="%.3f" />'
                             % (x + cc * cw, top + r * ch, cw + .3, ch + .3,
                                self._sty("hc", fill=P["acc"], stroke="none"),
                                round(0.06 + 0.86 * val, 3)))
        # Akciger konturu: acik hale + koyu kesikli cizgi -> her iki zeminde okunur
        for d in (LUNG_R, LUNG_L):
            sp = scale_path(d, s, x, top)
            self.o.write('<path d="%s" %s />'
                         % (sp, self._sty("hh", fill="none", stroke="#FFFFFF",
                                          stroke_width=2.8)))
            self.o.write('<path d="%s" %s />'
                         % (sp, self._sty("hl", fill="none", stroke=P["ink"],
                                          stroke_width=1.0, stroke_dasharray="4 2.5")))
        self.o.write('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" %s />'
                     % (x, top, w, h, self._sty("gfr", fill="none",
                                                stroke=P["line_soft"], stroke_width=1.0)))
        return x, w

    # ---- ViT yardimcilari -------------------------------------------------
    def patchgrid(self, x, y, size, n=7):
        c = size / float(n)
        self.o.write('<rect x="%s" y="%s" width="%s" height="%s" %s />'
                     % (x, y, size, size, self._sty("gpg", fill=P["panel"],
                                                    stroke=P["ink2"], stroke_width=1.0)))
        for i in range(1, n):
            self.o.write('<path d="M %.1f %s L %.1f %s" %s />'
                         % (x + i * c, y, x + i * c, y + size, self._stroke("g")))
            self.o.write('<path d="M %s %.1f L %s %.1f" %s />'
                         % (x, y + i * c, x + size, y + i * c, self._stroke("g")))

    def encoder(self, x, y, w, nb=12, ntr=2, bh=7, gap=2.0):
        """Kodlayici yigini; ust ntr blok ince ayarli olarak vurgulanir."""
        for i in range(nb):
            yy = y + i * (bh + gap)
            kind = "a" if i < ntr else "n"
            self.o.write('<rect x="%s" y="%.1f" width="%s" height="%s" rx="1.5" %s />'
                         % (x, yy, w, bh, self._shape(kind)))
        return y + nb * (bh + gap) - gap

    def relplot(self, x, y, size, pts):
        """Kucuk guvenilirlik egrisi (gercek olculen degerler)."""
        self.o.write('<rect x="%s" y="%s" width="%s" height="%s" %s />'
                     % (x, y, size, size, self._sty("gpl", fill=P["node_fill"],
                                                    stroke=P["ink2"], stroke_width=0.9)))
        self.o.write('<path d="M %s %s L %s %s" %s />'
                     % (x, y + size, x + size, y, self._stroke("ref")))
        d = " ".join(("M" if i == 0 else "L") + " %.1f %.1f"
                     % (x + p[0] * size, y + size - p[1] * size) for i, p in enumerate(pts))
        self.o.write('<path d="%s" %s />' % (d, self._stroke("pl")))

    # ---- sarmalayici ------------------------------------------------------
    def render(self, aria):
        body = self.o.getvalue()
        if self.mode == "html":
            return ('<svg class="dg" viewBox="0 0 %s %s" role="img" aria-label="%s" '
                    'xmlns="http://www.w3.org/2000/svg">%s</svg>'
                    % (self.w, self.h, esc(aria), body))
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" '
                'viewBox="0 0 %s %s" role="img"><title>%s</title>'
                '<rect width="%s" height="%s" fill="#FFFFFF"/>%s</svg>'
                % (self.w, self.h, self.w, self.h, esc(aria), self.w, self.h, body))


# ==========================================================================
# SEKIL 1 — Onerilen cerceve (genel bakis)
# ==========================================================================
def fig1(mode):
    c = Canvas(1, 900, 492, mode)
    c.defs()

    # --- (a) On-isleme -----------------------------------------------------
    c.panel_label(20, 26, "(a)", "ÖN-İŞLEME HATTI")
    xs = [80, 320, 560, 800]
    for i, (cx, m) in enumerate(zip(xs, ["plain", "contour", "masked", "roi"])):
        c.cxr(cx, 40, 122, m)
    caps = ["Girdi radyografı", "Akciğer maskesi", "Maskelenmiş görüntü", "İlgi alanı kırpımı"]
    for cx, t in zip(xs, caps):
        c.caption(cx, 180, t)
    ops = [("Anatomik segmentasyon", "ianpan U-Net · CheXmask"),
           ("Maskeleme ve dolgu", "kalp ve mediasten silinir"),
           ("İlgi alanı kırpma", "%5 pay · kare · 224²")]
    for i in range(3):
        x0, x1 = xs[i] + 51, xs[i + 1] - 51
        c.edge([(x0, 101), (x1, 101)], kind="a",
               label=ops[i][0], sub=ops[i][1], lx=(x0 + x1) / 2.0, ly=76)

    # --- (b) Siniflandirici ------------------------------------------------
    c.panel_label(20, 218, "(b)", "AKCİĞER-ODAKLI VISION TRANSFORMER")
    c.cxr(60, 240, 84, "roi")
    c.patchgrid(134, 244, 76, 7)
    c.caption(172, 336, "14 × 14 = 196 yama")
    bot = c.encoder(266, 229, 120, nb=12, ntr=2)
    c.node(440, 261, 110, 42, "MLP başlık", ["2 sınıf"])
    c.node(606, 261, 174, 42, "P(pnömoni)", ["softmax"], kind="a")
    c.edge([(96, 282), (130, 282)], kind="a")
    c.edge([(214, 282), (262, 282)], kind="a")
    c.edge([(390, 282), (436, 282)], kind="a", label="CLS", lx=413, ly=274)
    c.edge([(554, 282), (602, 282)], kind="a")
    c.o.write('<text x="394" y="238" %s>%s</text>'
              % (c._text("cap", "start"), esc("ViT-B/16 kodlayıcı")))
    ly = bot + 17
    c.o.write('<rect x="266" y="%s" width="11" height="8" rx="1" %s />' % (ly - 7, c._shape("a")))
    c.o.write('<text x="283" y="%s" %s>%s</text>' % (ly, c._text("cap", "start"), esc("ince ayar")))
    c.o.write('<rect x="352" y="%s" width="11" height="8" rx="1" %s />' % (ly - 7, c._shape("n")))
    c.o.write('<text x="369" y="%s" %s>%s</text>' % (ly, c._text("cap", "start"), esc("dondurulmuş")))
    c.o.write('<text x="470" y="%s" %s>%s</text>'
              % (ly, c._text("cap", "start"),
                 esc("eğitilebilir 14,18 M / 85,80 M  (%16,5)")))

    # --- (c) Degerlendirme -------------------------------------------------
    c.panel_label(20, 382, "(c)", "DEĞERLENDİRME PROTOKOLÜ")
    c.node(20, 398, 270, 68, "İç doğrulama",
           ["n = 864 · dengeli", "AUC 0,998 · F1 0,978"])
    c.node(315, 398, 270, 68, "Dış doğrulama",
           ["RSNA  n = 800 · AUC 0,930", "NIH    n = 800 · AUC 0,702"], kind="a")
    c.node(610, 398, 270, 68, "Eşik yeniden kalibrasyonu",
           ["ECE 0,191 → 0,015", "Özgüllük 0,645 → 0,820"])
    c.edge([(290, 432), (313, 432)])
    c.edge([(585, 432), (608, 432)])

    return c.render("Onerilen akciger-odakli Vision Transformer cercevesi: "
                    "on-isleme hatti, siniflandirici ve degerlendirme protokolu.")


# ==========================================================================
# SEKIL 2 — Maskeleme ve ilgi alani cikarim algoritmasi
# ==========================================================================
def fig2(mode):
    c = Canvas(2, 900, 552, mode)
    c.defs()
    X, W, CX = 110, 360, 290

    c.node(X, 30, W, 54, "1 · Görüntü yükleme",
           ["PNG / JPG / DICOM (MONOCHROME1 ters çevrilir)",
            "kısa kenar > 512 px ise oranı koruyarak ölçekle"])
    c.node(X, 102, W, 54, "2 · Anatomik segmentasyon",
           ["ianpan U-Net → argmax → M = {sınıf 1, sınıf 2}",
            "sınıf 3 (kalp ve mediasten) dışlanır"])
    c.diamond(CX, 200, 100, 32, "Maske boş mu?", "toplam(M) < 1")
    c.node(X, 250, W, 54, "3 · Tolerans katmanı",
           ["dilatasyon: elips, r = 0,025 × kısa kenar",
            "kenar yumuşatma: Gauss 9 × 9 → soft ∈ [0, 1]"])
    c.node(X, 322, W, 54, "4 · Kompozit",
           ["I′ = I · soft + dolgu · (1 − soft)",
            "dolgu = veri kümesi ortalama grisi (122)"])
    c.node(X, 394, W, 54, "5 · İlgi alanı",
           ["sınır kutusu + %5 pay → kareye tamamla",
            "görüntü sınırına sığdır"])
    c.node(X, 466, W, 54, "6 · Ölçekleme ve normalizasyon",
           ["224 × 224 (INTER_AREA) → ViT-B/16 girdisi"], kind="a")

    c.edge([(CX, 84), (CX, 102)])
    c.edge([(CX, 156), (CX, 168)])
    c.edge([(CX, 232), (CX, 250)], label="hayır", lx=CX + 12, ly=245, anchor="start")
    c.edge([(CX, 304), (CX, 322)])
    c.edge([(CX, 376), (CX, 394)])
    c.edge([(CX, 448), (CX, 466)], kind="a")

    c.node(520, 173, 190, 54, "Geri çekilme",
           ["224'e ölçekle, used = False", "koşum: 0 / 10.128 görüntü"], kind="b")
    c.edge([(390, 200), (518, 200)], kind="b", label="evet", lx=454, ly=193)
    c.edge([(615, 227), (615, 247), (500, 247), (500, 493), (472, 493)], kind="b")

    # Parametre kutusu
    c.o.write('<rect x="560" y="254" width="320" height="228" rx="2.5" %s />' % c._shape("p"))
    c.o.write('<text x="578" y="278" %s>%s</text>'
              % (c._text("title", "start"), esc("Ön-işleme parametreleri")))
    c.o.write('<path d="M 578 288 L 862 288" %s />' % c._stroke("g"))
    rows = [("Kısa kenar üst sınırı", "512 px"),
            ("Maske genişletme", "0,025 × kısa kenar"),
            ("Kenar yumuşatma (Gauss)", "9 × 9"),
            ("Akciğer dışı dolgu", "122 (ort. gri)"),
            ("İlgi alanı güvenlik payı", "0,05 × kısa kenar"),
            ("Çıktı çözünürlüğü", "224 × 224 × 3"),
            ("Normalizasyon", "0,4769 / 0,2414"),
            ("Geri çekilme oranı", "0 / 10.128")]
    for i, (k, v) in enumerate(rows):
        c.kv(578, 284, 310 + i * 21, k, v)

    return c.render("Akciger-odakli maskeleme ve ilgi alani cikarim algoritmasinin "
                    "adimlari, geri cekilme dali ve on-isleme parametreleri.")


# ==========================================================================
# SEKIL 3 — Veri bolumleme ve egitim protokolu
# ==========================================================================
def fig3(mode):
    c = Canvas(3, 900, 424, mode)
    c.defs()

    # --- (a) Veri bolumleme ------------------------------------------------
    c.panel_label(20, 26, "(a)", "VERİ BÖLÜMLEME VE SIZINTI DENETİMİ")
    c.node(20, 74, 158, 62, "Veri kümesi", ["8.528 görüntü", "NORMAL / PNEUMONIA"])
    c.node(238, 44, 172, 56, "Eğitim seti", ["6.800  (3.400 / 3.400)"])
    c.node(238, 112, 172, 56, "Doğrulama + test havuzu", ["1.730  (865 / 865)"])
    c.node(470, 112, 172, 56, "Sızıntı denetimi", ["dosya imzası eşleşmesi", "çakışma: 0"])
    c.node(702, 78, 178, 44, "Doğrulama", ["864  (432 / 432)"])
    c.node(702, 134, 178, 44, "Test", ["864  (432 / 432)"])
    c.edge([(178, 105), (208, 105)], arrow=False)
    c.edge([(208, 105), (208, 72), (236, 72)])
    c.edge([(208, 105), (208, 140), (236, 140)])
    c.edge([(410, 140), (468, 140)])
    c.edge([(642, 140), (672, 140)], arrow=False)
    c.edge([(672, 140), (672, 100), (700, 100)], label="dengeli bölme", lx=655, ly=62)
    c.edge([(672, 140), (672, 156), (700, 156)])

    # --- (b) Egitim protokolu ---------------------------------------------
    c.panel_label(20, 224, "(b)", "EĞİTİM VE MODEL SEÇİMİ")
    c.node(20, 288, 122, 48, "Veri artırma", ["yalnızca eğitim"])
    bot = c.encoder(192, 259, 90, nb=12, ntr=2)
    c.node(332, 288, 118, 48, "MLP başlık", ["2 sınıf"])
    c.node(500, 288, 150, 48, "Çapraz entropi", ["ceza terimi yok"])
    c.node(700, 272, 180, 80, "Model seçimi",
           ["AdamW 1e-4 · wd 1e-2", "cosine → 1e-6 · 15 epoch",
            "en iyi Val F1 = 0,9803"], kind="a")
    c.edge([(142, 312), (190, 312)])
    c.edge([(282, 312), (330, 312)])
    c.edge([(450, 312), (498, 312)])
    c.edge([(650, 312), (698, 312)])
    c.edge([(790, 352), (790, 390), (237, 390), (237, bot + 4)], kind="a", dashed=True,
           label="geri yayılım — yalnızca ince ayarlı katmanlar", lx=520, ly=404)
    c.caption(237, 252, "ViT-B/16")
    c.o.write('<rect x="470" y="233" width="11" height="8" rx="1" %s />' % c._shape("a"))
    c.o.write('<text x="487" y="240" %s>%s</text>'
              % (c._text("cap", "start"), esc("ince ayar: son 2 blok + LN + başlık")))
    c.o.write('<rect x="716" y="233" width="11" height="8" rx="1" %s />' % c._shape("n"))
    c.o.write('<text x="733" y="240" %s>%s</text>'
              % (c._text("cap", "start"), esc("dondurulmuş: 10 blok")))

    return c.render("Veri bolumleme, sizinti denetimi ve ViT-B/16 ince ayar protokolu; "
                    "yalnizca son iki kodlayici blogu, katman normalizasyonu ve "
                    "siniflandirma basligi guncellenir.")


# ==========================================================================
# SEKIL 4 — Dis dogrulama ve esik yeniden kalibrasyonu
# ==========================================================================
def fig4(mode):
    c = Canvas(4, 900, 512, mode)
    c.defs()

    c.node(310, 20, 280, 52, "Eğitilmiş kontrol noktası",
           ["ağırlıklar + ön-işleme parametreleri (CONFIG)"], kind="a")
    c.node(310, 96, 280, 44, "Ön-işleme hattı birebir yeniden kurulur")
    c.edge([(450, 72), (450, 96)], kind="a")
    c.edge([(450, 140), (450, 156)], arrow=False)
    c.edge([(450, 156), (210, 156), (210, 172)])
    c.edge([(450, 156), (690, 156), (690, 172)])

    c.node(40, 172, 340, 72, "RSNA Pneumonia Detection Challenge",
           ["DICOM · radyolog gözden geçirmeli ikili etiket",
            "Lung Opacity = +   ·   Normal = −",
            "belirsiz sınıf dışlanır"])
    c.node(520, 172, 340, 72, "NIH ChestX-ray14",
           ["PNG · rapor-NLP etiketi (≈ %90 doğruluk)",
            "Pneumonia = +   ·   No Finding = −",
            "diğer bulgular dışlanır"])
    c.node(40, 268, 340, 60, "Dengeli örneklem ve çıkarım",
           ["400 + 400 = 800 görüntü · geri çekilme %0,0",
            "AUC 0,930 · Duyarlılık 0,965 · Özgüllük 0,640"], kind="a")
    c.node(520, 268, 340, 60, "Dengeli örneklem ve çıkarım",
           ["400 + 400 = 800 görüntü · geri çekilme %0,0",
            "AUC 0,702 · Duyarlılık 0,850 · Özgüllük 0,432"])
    c.edge([(210, 244), (210, 268)])
    c.edge([(690, 244), (690, 268)])

    c.edge([(210, 328), (210, 348), (450, 348)], arrow=False)
    c.edge([(690, 328), (690, 348), (450, 348)], arrow=False)
    c.edge([(450, 348), (450, 366)])
    c.band(40, 366, 820, 26,
           "%50 KALİBRASYON YARISINDA ÖĞREN  ·  %50 GÖRÜLMEMİŞ YARIDA RAPORLA")
    c.edge([(450, 392), (450, 408)], arrow=False)
    for tx in (170, 450, 730):
        c.edge([(450, 408), (tx, 408), (tx, 422)] if tx != 450 else [(450, 408), (450, 422)])

    rel = {
        "raw": [(0.02, .04), (.15, .50), (.25, 0), (.45, 0), (.62, 0), (.88, 0), (.97, .75)],
        "platt": [(.05, .05), (.15, 0), (.30, 0), (.45, 0), (.60, .33), (.73, .74)],
        "iso": [(.05, .05), (.18, .29), (.39, 1.0), (.42, .60), (.55, .61),
                (.66, 1.0), (.79, .75), (.97, .91)],
    }
    boxes = [(40, "Ham (eşik 0,50)", "raw", ["Özgüllük 0,645", "ECE 0,191"], "n"),
             (320, "Platt (lojistik)", "platt", ["Özgüllük 0,660", "ECE 0,015"], "n"),
             (600, "Isotonic", "iso", ["Özgüllük 0,820", "ECE 0,047"], "a")]
    for x, title, key, vals, kind in boxes:
        c.o.write('<rect x="%s" y="422" width="260" height="70" rx="2.5" %s />'
                  % (x, c._shape(kind)))
        c.relplot(x + 12, 432, 50, rel[key])
        c.o.write('<text x="%s" y="446" %s>%s</text>'
                  % (x + 74, c._text("title", "start"), esc(title)))
        for i, v in enumerate(vals):
            c.o.write('<text x="%s" y="%s" %s>%s</text>'
                      % (x + 74, 463 + i * 14, c._text("detail", "start"), esc(v)))
    c.caption(450, 506, "RSNA · görülmemiş test yarısı · kesikli çizgi = ideal kalibrasyon")

    return c.render("Dis dogrulama tasarimi ve esik yeniden kalibrasyonu; kucuk "
                    "grafikler RSNA guvenilirlik egrilerini gosterir.")


# ==========================================================================
# SEKIL 5 — Attention Rollout ve akciger-odak orani
# ==========================================================================
def fig5(mode):
    c = Canvas(5, 900, 364, mode)
    c.defs()

    c.panel_label(20, 26, "(a)", "DİKKAT AKIŞININ BÜTÜNLEŞTİRİLMESİ")
    c.node(20, 54, 148, 56, "İleri geçiş", ["12 katman", "A(l) : 12 × 197 × 197"])
    c.node(212, 54, 190, 56, "Kafa ortalaması", ["Ã(l) = ort_h A_h(l)"])
    c.node(446, 54, 200, 56, "Artık + satır normalizasyonu",
           ["Â(l) = D⁻¹ (Ã(l) + I)"])
    c.node(690, 54, 190, 56, "Katman çarpımı", ["R = Â(L) ⋯ Â(1)"], kind="a")
    c.edge([(168, 82), (210, 82)])
    c.edge([(402, 82), (444, 82)])
    c.edge([(646, 82), (688, 82)])
    c.caption(785, 128, "R[0, 1:] → 14 × 14 → 224²  =  S(u)")

    c.panel_label(20, 170, "(b)", "AKCİĞER-ODAK ORANI (LFR)")
    c.heat(90, 200, 118, "lungfield")
    c.caption(90, 336, "S(u) : dikkat haritası")
    c.cxr(230, 200, 118, "masked")
    c.caption(230, 336, "L(u) : akciğer maskesi")
    c.node(330, 216, 250, 86, "Akciğer-odak oranı",
           ["Ω = { u : S(u) > 0,20 }",
            "LFR = Σ_Ω S(u)·L(u)  /  Σ_Ω S(u)"])
    c.edge([(90, 198), (90, 188), (305, 188), (305, 259), (328, 259)])
    c.edge([(277, 259), (328, 259)])
    c.edge([(580, 259), (618, 259)], kind="a")

    # Sonuc: V1 / V2 odak orani karsilastirmasi
    c.o.write('<rect x="620" y="216" width="260" height="86" rx="2.5" %s />' % c._shape("a"))
    c.o.write('<text x="636" y="238" %s>%s</text>'
              % (c._text("title", "start"), esc("Ölçülen odak oranı")))
    for lbl, val, y in (("V1", 0.159, 266), ("V2", 0.903, 290)):
        c.o.write('<text x="654" y="%s" %s>%s</text>'
                  % (y + 4, c._text("detail", "end"), esc(lbl)))
        c.o.write('<rect x="660" y="%s" width="%.1f" height="12" rx="1" %s />'
                  % (y - 6, 150 * val, c._sty("bar", fill=P["acc"], stroke="none")))
        c.o.write('<text x="%.1f" y="%s" %s>%s</text>'
                  % (666 + 150 * val, y + 4, c._text("val", "start"),
                     esc(("%.3f" % val).replace(".", ","))))

    return c.render("Attention Rollout hesabi ve akciger-odak oraninin (LFR) "
                    "dikkat haritasi ile akciger maskesinden turetilmesi.")


# ==========================================================================
# SEKIL 6 — Taban cizgi (yumusak ceza) ile onerilen yontemin karsilastirmasi
# ==========================================================================
def fig6(mode):
    c = Canvas(6, 900, 452, mode)
    c.defs()

    c.o.write('<rect x="14" y="34" width="872" height="176" rx="3" %s />' % c._shape("p"))
    c.o.write('<rect x="14" y="248" width="872" height="176" rx="3" %s />' % c._shape("p"))

    c.panel_label(20, 26, "(a)", "TABAN ÇİZGİ — YUMUŞAK RRR CEZASI (V1)")
    c.cxr(110, 50, 142, "plain")
    c.caption(110, 202, "Girdi: tüm toraks")
    c.node(200, 96, 230, 50, "Kısıt: kayıp terimi",
           ["L = L_CE + 5,0 · L_anat"], kind="b")
    c.heat(520, 55, 132, "central")
    c.caption(520, 202, "Dikkat: omurga / mediasten ekseni")
    c.node(608, 92, 272, 58, "Denetim sonucu",
           ["ceza 3,60 → 3×10⁻⁴  (1 epoch)", "LFR = 0,159 ± 0,125"], kind="b")
    c.edge([(165, 121), (198, 121)], kind="b")
    c.edge([(430, 121), (466, 121)], kind="b")
    c.edge([(574, 121), (606, 121)], kind="b")

    c.panel_label(20, 240, "(b)", "ÖNERİLEN — GİRDİ DÜZEYİNDE MASKELEME (V2)")
    c.cxr(110, 264, 142, "masked")
    c.caption(110, 416, "Girdi: yalnızca akciğer parankimi")
    c.node(200, 310, 230, 50, "Kısıt: girdinin yapısı",
           ["L = L_CE  (ceza terimi yok)"], kind="a")
    c.heat(520, 269, 132, "lungfield")
    c.caption(520, 416, "Dikkat: görünür akciğer dokusu")
    c.node(608, 306, 272, 58, "Denetim sonucu",
           ["LFR = 0,903 ± 0,088", "RSNA dış doğrulama AUC 0,930"], kind="a")
    c.edge([(165, 335), (198, 335)], kind="a")
    c.edge([(430, 335), (466, 335)], kind="a")
    c.edge([(574, 335), (606, 335)], kind="a")

    c.edge([(846, 212), (846, 246)], kind="e", dashed=True,
           label="kısıt kayıp teriminden girdiye taşınır", lx=836, ly=234, anchor="end")

    return c.render("Yumusak RRR cezasi ile girdi duzeyinde maskelemenin "
                    "karsilastirmasi: iki kol arasindaki tek yapisal fark "
                    "siniflandiriciya ulasan bilgidir.")


# ==========================================================================
FIGS = [
    ("sekil_01_onerilen_cerceve", fig1),
    ("sekil_02_maskeleme_algoritmasi", fig2),
    ("sekil_03_veri_ve_egitim", fig3),
    ("sekil_04_dis_dogrulama", fig4),
    ("sekil_05_rollout_lfr", fig5),
    ("sekil_06_karsilastirma", fig6),
]


def main():
    for name, fn in FIGS:
        with open(os.path.join(HERE, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(fn("inline"))
        print("yazildi:", name + ".svg")

    tpl = os.path.join(HERE, "template.html")
    if os.path.exists(tpl):
        html = open(tpl, encoding="utf-8").read()
        for i, (_, fn) in enumerate(FIGS, start=1):
            html = html.replace("<!--FIG%d-->" % i, fn("html"))
        with open(os.path.join(HERE, "akis_diyagramlari.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("yazildi: akis_diyagramlari.html")


if __name__ == "__main__":
    main()
