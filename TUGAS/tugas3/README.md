# Analisis Regresi Linear - Tugas 3 STDA4101 (Pengantar Sains Data)

Repository ini berisi penyelesaian Tugas 3 untuk mata kuliah **STDA4101 - Pengantar Sains Data** di Universitas Terbuka. Analisis dilakukan menggunakan bahasa pemrograman Python.

## 📋 Deskripsi Tugas
Melakukan analisis statistik deskriptif dan inferensial pada dataset medis (Diabetes) untuk memprediksi perkembangan penyakit ($Y$) berdasarkan variabel kesehatan pasien.

**Lingkup Pengerjaan:**
1. Visualisasi Data (Scatter Plot).
2. Pemodelan Regresi Linear Berganda (OLS).
3. Interpretasi Model Statistik.

## 🛠️ Teknologi yang Digunakan
- **Python 3.x**
- **Pandas** (Pembersihan & Manipulasi Data)
- **Statsmodels** (Analisis Regresi OLS)
- **Seaborn & Matplotlib** (Visualisasi Data)

## 📊 Hasil Analisis Singkat
Berdasarkan model regresi yang dibuat dengan variabel prediktor `AGE`, `LDL`, dan `HDL`:
- **Model Equation:** $Y = 266.63 + 0.60(AGE) - 0.04(LDL) - 2.74(HDL)$
- **R-Squared:** 16.8%
- **Insight:** Variabel **HDL** memiliki pengaruh signifikan negatif terhadap perkembangan penyakit (semakin tinggi HDL, risiko penyakit menurun).

---
*Dibuat oleh: Satria Revaldi NIM : 057282119*
