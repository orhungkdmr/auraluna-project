#!/usr/bin/env bash
# build.sh

set -o errexit

# 1. Kütüphaneleri kur
pip install -r requirements.txt

# ============================================
# === YENİ HATA AYIKLAMA KODU ===
# ============================================
echo "--- HATA AYIKLAMA: Dosyalar listeleniyor ---"
echo "Ana dizin içeriği:"
ls -lA
echo "---"
echo "Static klasörü içeriği (static/):"
ls -lA static/
echo "---"
echo "CSS klasörü içeriği (static/css/):"
ls -lA static/css/
echo "--- HATA AYIKLAMA BİTTİ ---"
# ============================================

# 2. Statik dosyaları topla (Whitenoise için)
python manage.py collectstatic --no-input

# 3. Veritabanı migrasyonlarını uygula
python manage.py migrate