import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. PERSIAPAN DATA
# ==========================================
file_path = 'Data Tugas Tuton STDA4101-2025.2 (1).xlsx - 2024.2.csv'

print("Sedang membaca data...")

try:
    # Membaca hanya 4 kolom utama: Y, AGE, LDL, HDL
    # Kolom biasanya ada di indeks 0, 1, 2, 3
    df = pd.read_csv(file_path, usecols=[0, 1, 2, 3])
    df.columns = ['Y', 'AGE', 'LDL', 'HDL']  # Pastikan nama kolom seragam
except Exception as e:
    print(f"Error membaca file: {e}")
    # Opsi cadangan jika format error, coba baca semua
    df = pd.read_csv(file_path)
    df = df.iloc[:, :4] # Ambil 4 kolom pertama
    df.columns = ['Y', 'AGE', 'LDL', 'HDL']

# Bersihkan data: ubah ke angka (numeric) dan buang baris kosong (NaN)
cols = ['Y', 'AGE', 'LDL', 'HDL']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df_clean = df.dropna()
print(f"Data siap! Jumlah sampel bersih: {len(df_clean)} baris.")

# ==========================================
# 2. VISUALISASI DATA (SCATTER PLOT)
# ==========================================
print("\nMembuat Grafik Scatter Plot...")
plt.figure(figsize=(18, 5))

# Plot 1: AGE vs Y
plt.subplot(1, 3, 1)
sns.scatterplot(x=df_clean['AGE'], y=df_clean['Y'], color='blue', alpha=0.6)
plt.title('Hubungan Usia (AGE) vs Penyakit (Y)')
plt.xlabel('Usia (Tahun)')
plt.ylabel('Tingkat Keparahan Penyakit (Y)')
plt.grid(True, linestyle='--', alpha=0.5)

# Plot 2: LDL vs Y
plt.subplot(1, 3, 2)
sns.scatterplot(x=df_clean['LDL'], y=df_clean['Y'], color='red', alpha=0.6)
plt.title('Hubungan LDL vs Penyakit (Y)')
plt.xlabel('LDL (Low-Density Lipoprotein)')
plt.ylabel('Y')
plt.grid(True, linestyle='--', alpha=0.5)

# Plot 3: HDL vs Y
plt.subplot(1, 3, 3)
sns.scatterplot(x=df_clean['HDL'], y=df_clean['Y'], color='green', alpha=0.6)
plt.title('Hubungan HDL vs Penyakit (Y)')
plt.xlabel('HDL (High-Density Lipoprotein)')
plt.ylabel('Y')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
# Simpan gambar biar bisa ditaruh di laporan Word
plt.savefig('scatter_plots_tugas3.png') 
plt.show()
print("Grafik berhasil disimpan sebagai 'scatter_plots_tugas3.png'")

# ==========================================
# 3. PEMODELAN REGRESI LINEAR BERGANDA
# ==========================================
print("\n=== HASIL ANALISIS REGRESI (OLS) ===")

# Tentukan Variabel Independen (X) dan Dependen (y)
X = df_clean[['AGE', 'LDL', 'HDL']]
y = df_clean['Y']

# Wajib tambahkan konstanta (Intercept) untuk Statsmodels
X = sm.add_constant(X)

# Fit Model
model = sm.OLS(y, X).fit()

# Tampilkan Hasil Lengkap
print(model.summary())

# ==========================================
# 4. MEMBUAT RUMUS PERSAMAAN OTOMATIS
# ==========================================
params = model.params
rumus = f"Y = {params['const']:.2f} "

for col in ['AGE', 'LDL', 'HDL']:
    coef = params[col]
    tanda = "+" if coef >= 0 else "-"
    rumus += f"{tanda} {abs(coef):.2f}({col}) "

print("\n" + "="*40)
print("KESIMPULAN PERSAMAAN REGRESI:")
print(rumus)
print("="*40)
