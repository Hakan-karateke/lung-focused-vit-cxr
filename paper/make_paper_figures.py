# -*- coding: utf-8 -*-
"""
IEEE JBHI icin yayin kalitesinde grafik figurleri uretir.

Kaydedilmis analiz ciktilarindan (npz/csv) calisir; hicbir modeli yeniden
calistirmaz. Cikti: vektor PDF, IEEE kolon genisliginde, olceklenmeden
yerlestirilmek uzere.

Kullanim:  python paper/make_paper_figures.py
"""
import os, io, json, zipfile
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from sklearn.metrics import roc_curve, auc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "paper", "figures")
os.makedirs(OUT, exist_ok=True)

# ---------------- IEEE geometrisi ve tipografisi ----------------
COL1, COL2 = 3.50, 7.16          # inch
FS_L, FS_T, FS_P = 8, 7, 8.5     # etiket / eksen / panel harfi

plt.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"],
    "font.size": FS_L, "axes.labelsize": FS_L, "axes.titlesize": FS_L,
    "xtick.labelsize": FS_T, "ytick.labelsize": FS_T, "legend.fontsize": FS_T,
    "axes.linewidth": 0.6, "lines.linewidth": 1.0,
    "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "xtick.major.size": 2.4, "ytick.major.size": 2.4,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": "#4a4a4a", "axes.labelcolor": "#111111",
    "text.color": "#111111", "xtick.color": "#333333", "ytick.color": "#333333",
    "grid.color": "#cccccc", "grid.linewidth": 0.5,
    "legend.frameon": False, "legend.handlelength": 1.4, "legend.handletextpad": 0.5,
    "legend.columnspacing": 1.1, "legend.borderaxespad": 0.2,
    "figure.facecolor": "white", "savefig.facecolor": "white",
    "savefig.bbox": "tight", "savefig.pad_inches": 0.01,
    "pdf.fonttype": 42, "ps.fonttype": 42,
})

ARMS = ["raw", "roi", "lung"]
LBL = {"raw": "A: no segmentation", "roi": "B: ROI crop only", "lung": "C: mask + ROI"}
SHORT = {"raw": "A", "roi": "B", "lung": "C"}
CLR = {"raw": "#B04A1E", "roi": "#C2900A", "lung": "#0D8FA2"}
GREY = "#8a8a8a"


def panel(ax, letter, dx=-0.115, dy=1.045):
    ax.text(dx, dy, f"({letter})", transform=ax.transAxes, fontsize=FS_P,
            fontweight="bold", va="top", ha="left")


def npz(path):
    """.npz ya da .zip olarak kaydedilmis dizileri okur."""
    z = zipfile.ZipFile(path)
    return {n[:-4]: np.load(io.BytesIO(z.read(n))) for n in z.namelist() if n.endswith(".npy")}


def first(*cands):
    for c in cands:
        p = os.path.join(ROOT, c)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(cands[0])


def save(fig, name):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=600)
    w, h = fig.get_size_inches()
    print(f"  {name:<28} {w:.2f} x {h:.2f} in")
    plt.close(fig)


# ==========================================================================
# karat3  (belgede Fig. 3) — Ayristirma: kollar ayirt edilemez, tohum gurultusu baskin
# ==========================================================================
def fig_discrimination():
    met = pd.read_csv(first("kaggle/Ablation-Segmentation-V3/output/ablation_metrics.csv"))
    ci = pd.read_csv(first("kaggle/Ablation-Segmentation-V3/output/ablation_auc_ci.csv"))
    seed = pd.read_csv(first("kaggle/MultiSeed-V5/output/seed_auc_by_seed.csv"))

    sets = ["Ic test", "RSNA (yetiskin)", "NIH ChestX-ray14"]
    disp = ["Internal test", "RSNA", "NIH ChestX-ray14"]

    fig, axes = plt.subplots(1, 3, figsize=(COL2, 2.40),
                             gridspec_kw={"width_ratios": [1.65, 0.72, 0.72],
                                          "wspace": 0.42})

    # --- (a) kol x kume AUC, bootstrap GA ---
    ax = axes[0]
    xs = np.arange(len(sets)); w = 0.25
    for k, a in enumerate(ARMS):
        v = np.array([met[(met.kume == s) & (met.kol == a)]["AUC"].iloc[0] for s in sets])
        lo = np.array([ci[(ci.kume == s) & (ci.kol == a)]["AUC_GA_alt"].iloc[0] for s in sets])
        hi = np.array([ci[(ci.kume == s) & (ci.kol == a)]["AUC_GA_ust"].iloc[0] for s in sets])
        p = xs + (k - 1) * w
        ax.bar(p, v, width=w * 0.9, color=CLR[a], edgecolor="white", linewidth=0.6,
               label=LBL[a], zorder=3)
        ax.errorbar(p, v, yerr=[v - lo, hi - v], fmt="none", ecolor="#222222",
                    elinewidth=0.7, capsize=1.8, capthick=0.7, zorder=4)
        for x, val, h in zip(p, v, hi):
            ax.text(x, h + 0.016, f"{val:.3f}", ha="center", va="bottom",
                    fontsize=5.6, rotation=90, zorder=5)
    ax.axhline(0.5, color=GREY, ls=":", lw=0.6, zorder=2)
    ax.set_xticks(xs); ax.set_xticklabels(disp, fontsize=6.4)
    ax.set_ylabel("ROC-AUC"); ax.set_ylim(0.45, 1.16)
    ax.set_yticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.yaxis.grid(True, alpha=0.55); ax.set_axisbelow(True)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.29), ncol=3, fontsize=FS_T)
    panel(ax, "a", dx=-0.12)

    # --- (b,c) tohum dagilimi: her kume kendi olceginde ---
    rng = np.random.default_rng(0)
    for j, (s, sd_, ltr) in enumerate([("RSNA (yetiskin)", "RSNA", "b"),
                                       ("NIH ChestX-ray14", "NIH", "c")]):
        ax = axes[j + 1]
        for k, a in enumerate(ARMS):
            d = seed[(seed.kume == s) & (seed.kol == a)]["AUC"].values
            ax.scatter(k + rng.uniform(-0.10, 0.10, len(d)), d, s=10, color=CLR[a],
                       edgecolor="white", linewidth=0.4, zorder=4)
            m = d.mean()
            ax.plot([k - 0.28, k + 0.28], [m, m], lw=1.5, color=CLR[a], zorder=5)
            if len(d) > 1:
                sdv = d.std(ddof=1)
                ax.plot([k, k], [m - sdv, m + sdv], lw=0.7, color="#222222", zorder=3)
        ax.set_xticks(range(3)); ax.set_xticklabels([SHORT[a] for a in ARMS])
        ax.set_xlim(-0.55, 2.55)
        ax.set_title(sd_, fontsize=FS_T, pad=3)
        ax.yaxis.grid(True, alpha=0.55); ax.set_axisbelow(True)
        ax.ticklabel_format(axis="y", useOffset=False)
        ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4))
        if j == 0:
            ax.set_ylabel("ROC-AUC")
        panel(ax, ltr, dx=-0.34, dy=1.12)

    save(fig, "karat3")            # belgede Fig. 3


# ==========================================================================
# karat4  (belgede Fig. 4) — Dikkat hizalamasi: LFR + toplu dikkat haritalari
# ==========================================================================
def fig_attention():
    per = pd.read_csv(first("kaggle/External-LFR-V6/output/extlfr_per_image.csv"))
    summ = pd.read_csv(first("kaggle/External-LFR-V6/output/extlfr_summary.csv"))
    area = pd.read_csv(first("kaggle/External-LFR-V6/output/extlfr_mask_area.csv"))
    agg = npz(first("kaggle/External-LFR-V6/output/extlfr_aggregate_maps.npz"))
    # Ic test LFR degerleri: ablasyon kosumundan GERCEK diziler (n=120/kol)
    internal = npz(first("kaggle/Ablation-Segmentation-V3/output/ablation_predictions.zip",
                         "kaggle/Ablation-Segmentation-V3/output/ablation_predictions.npz"))
    chance = float(area["ort"].mean())

    fig = plt.figure(figsize=(COL2, 2.05))
    gs = fig.add_gridspec(1, 4, width_ratios=[1.55, 1, 1, 1], wspace=0.10, left=0.06,
                          right=0.995, top=0.86, bottom=0.16)

    # --- (a) LFR dagilimlari ---
    ax = fig.add_subplot(gs[0, 0])
    rng = np.random.default_rng(1)
    pos = 0; ticks, ticklab = [], []
    for s, sd in [("Ic test", "Internal"), ("RSNA", "RSNA"), ("NIH", "NIH")]:
        for a in ARMS:
            if s == "Ic test":
                v = internal[f"lfr__{a}"]          # gercek olculen degerler
            else:
                v = per[per.kume == s][f"lfr_{a}"].dropna().values
            ax.scatter(pos + rng.uniform(-0.10, 0.10, len(v)), v, s=1.4, alpha=0.28,
                       color=CLR[a], edgecolor="none", zorder=3, rasterized=True)
            ax.plot([pos - 0.28, pos + 0.28], [np.median(v)] * 2, lw=1.5,
                    color=CLR[a], zorder=5)
            ticks.append(pos); ticklab.append(SHORT[a]); pos += 1
        pos += 0.6
    ax.axhline(chance, color="#222222", ls="--", lw=0.75, zorder=6)
    ax.text(pos - 0.75, chance + 0.035, "chance", fontsize=5.8, ha="right", color="#222222")
    ax.set_xticks(ticks); ax.set_xticklabels(ticklab)
    ax.set_ylabel("Lung-focus ratio"); ax.set_ylim(-0.04, 1.06)
    ax.yaxis.grid(True, alpha=0.5); ax.set_axisbelow(True)
    for i, sd in enumerate(["Internal", "RSNA", "NIH"]):
        ax.text(i * 3.6 + 1.0, -0.185, sd, transform=ax.get_xaxis_transform(),
                ha="center", va="top", fontsize=FS_T)
    panel(ax, "a", dx=-0.24, dy=1.10)

    # --- (b-d) toplu dikkat haritalari (RSNA) ---
    cm = matplotlib.colors.LinearSegmentedColormap.from_list(
        "att", ["#0b1a33", "#0f4c81", "#2a9d8f", "#e9c46a", "#e76f51"], N=256)
    for i, a in enumerate(ARMS):
        ax = fig.add_subplot(gs[0, i + 1])
        cam = agg[f"RSNA__{a}__cam"]
        cam = (cam - cam.min()) / (cam.max() - cam.min() + 1e-8)
        ax.imshow(cam, cmap=cm, vmin=0, vmax=1, interpolation="bilinear", rasterized=True)
        ax.contour(agg[f"RSNA__{a}__mask"], levels=[0.4], colors="white", linewidths=0.7)
        lfr = summ[(summ.kume == "RSNA") & (summ.kol == a)]["ort"].iloc[0]
        ax.set_title(f"{SHORT[a]}   LFR = {lfr:.3f}", fontsize=FS_T, pad=2.5)
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_linewidth(0.5); sp.set_color("#666666"); sp.set_visible(True)
        if i == 0:
            panel(ax, "b", dx=-0.09, dy=1.20)

    save(fig, "karat4")            # belgede Fig. 4


# ==========================================================================
# karat5  (belgede Fig. 5) — Nedensel okluzyon
# ==========================================================================
def fig_occlusion():
    occ = pd.read_csv(first("kaggle/Occlusion-V9/output/occlusion_results.csv"))
    P = npz(first("kaggle/Occlusion-V9/output/occlusion_predictions.npz"))

    def A(k, a, c):
        y = P[f"{k}__y"]
        fpr, tpr, _ = roc_curve(y, P[f"{k}__{a}__{c}"])
        return auc(fpr, tpr)

    fig, axes = plt.subplots(1, 3, figsize=(COL2, 2.30),
                             gridspec_kw={"width_ratios": [1, 1, 1.22], "wspace": 0.34})

    conds = ["baseline", "rand_lungs", "lungs", "non_lungs"]
    cdisp = ["intact", "random", "lungs", "outside"]

    for ax, kume, disp in zip(axes[:2], ["Ic test", "RSNA"], ["Internal test", "RSNA"]):
        xs = np.arange(len(conds)); w = 0.36
        for k, a in enumerate(["raw", "lung"]):
            v = [A(kume, a, c) for c in conds]
            p = xs + (k - 0.5) * w
            ax.bar(p, v, width=w * 0.9, color=CLR[a], edgecolor="white", linewidth=0.6,
                   label=LBL[a], zorder=3)
            for x, val in zip(p, v):
                ax.text(x, val + 0.012, f"{val:.3f}", ha="center", va="bottom",
                        fontsize=5.6, rotation=90, zorder=5)
        ax.axhline(0.5, color=GREY, ls=":", lw=0.6, zorder=2)
        ax.set_xticks(xs); ax.set_xticklabels(cdisp, fontsize=6.4)
        ax.set_ylim(0.45, 1.16); ax.set_yticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        ax.set_ylabel("ROC-AUC" if disp == "Internal test" else "")
        ax.set_title(disp, fontsize=FS_T, pad=3)
        ax.yaxis.grid(True, alpha=0.55); ax.set_axisbelow(True)
    axes[0].legend(loc="upper center", bbox_to_anchor=(1.12, 1.36), ncol=2, fontsize=FS_T)
    panel(axes[0], "a", dx=-0.24, dy=1.16)
    panel(axes[1], "b", dx=-0.14, dy=1.16)

    # --- (c) net etki: hicbir alt bolge tek basina belirleyici degil ---
    ax = axes[2]
    # "lungs" burada gosterilmez: (a)-(b) panellerinde zaten var ve olcegi
    # ezdigi icin alt bolgelerin okunmasini engelliyor.
    regs = ["corners", "border", "subdiaphragm", "upper", "center"]
    rdisp = ["corners", "border", "subdiaph.", "upper", "centre"]
    ys = np.arange(len(regs)); w = 0.36
    for k, a in enumerate(["raw", "lung"]):
        v = []
        for c in regs:
            r = occ[(occ.kume == "Ic test") & (occ.kol == a) & (occ.kosul == c)]
            x = r["net etki"].iloc[0]
            v.append(float(x) if not pd.isna(x) else float(r["dAUC"].iloc[0]))
        ax.barh(ys + (k - 0.5) * w, v, height=w * 0.9, color=CLR[a],
                edgecolor="white", linewidth=0.6, zorder=3)
    ax.axvline(0, color="#222222", lw=0.7, zorder=4)
    ax.set_yticks(ys); ax.set_yticklabels(rdisp, fontsize=FS_T); ax.invert_yaxis()
    ax.set_xlabel("net effect on ROC-AUC")
    ax.xaxis.grid(True, alpha=0.5); ax.set_axisbelow(True)
    ax.set_title("Sub-regions, internal test", fontsize=FS_T, pad=3)
    ax.set_xlim(-0.028, 0.014)
    panel(ax, "c", dx=-0.30, dy=1.16)

    save(fig, "karat5")            # belgede Fig. 5


# ==========================================================================
# karat2  (belgede Fig. 2) — Veri butunlugu: sizintili ve sizintisiz ic test
# ==========================================================================
def fig_integrity():
    m = pd.read_csv(first("kaggle/Clean-Internal-V8/output/clean_internal_metrics.csv"))
    order = ["Orijinal test (sizintili)", "Kaynak duzeyi temiz", "Hasta duzeyi temiz (birincil)"]
    disp = ["as distributed\n(leaky)", "source-disjoint", "patient-disjoint"]

    SHORTLBL = {"raw": "A: none", "roi": "B: ROI", "lung": "C: mask+ROI"}
    fig, ax = plt.subplots(figsize=(COL1, 2.00))
    xs = np.arange(len(order)); w = 0.25
    for k, a in enumerate(ARMS):
        v, lo, hi = [], [], []
        for s in order:
            r = m[(m["alt kume"] == s) & (m.kol == a)].iloc[0]
            v.append(r["AUC"]); lo.append(r["GA alt"]); hi.append(r["GA ust"])
        v, lo, hi = map(np.array, (v, lo, hi))
        p = xs + (k - 1) * w
        ax.bar(p, v, width=w * 0.9, color=CLR[a], edgecolor="white", linewidth=0.6,
               label=SHORTLBL[a], zorder=3)
        ax.errorbar(p, v, yerr=[v - lo, hi - v], fmt="none", ecolor="#222222",
                    elinewidth=0.7, capsize=1.6, capthick=0.7, zorder=4)
    ax.set_xticks(xs); ax.set_xticklabels(disp, fontsize=6.2, linespacing=1.15)
    ax.set_ylabel("ROC-AUC"); ax.set_ylim(0.95, 1.005)
    ax.yaxis.grid(True, alpha=0.55); ax.set_axisbelow(True)
    # Cubuklar tum ic alani doldurdugundan aciklama eksenin ustune alinir
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.20), ncol=3, fontsize=6.0,
              columnspacing=0.8, handlelength=1.1, handletextpad=0.35)
    save(fig, "karat2")            # belgede Fig. 2


if __name__ == "__main__":
    print("IEEE JBHI figurleri uretiliyor (vektor PDF, kolon genisliginde):")
    fig_integrity()        # karat2
    fig_discrimination()   # karat3
    fig_attention()        # karat4
    fig_occlusion()        # karat5
    print(f"\ncikti dizini: {OUT}")
