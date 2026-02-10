# check_apps_no_setup.py
from personal_portfolio import settings

labels = {}
for app in settings.INSTALLED_APPS:
    # نام اپ یا مسیر کامل اپ
    label = app.split('.')[-1]  # آخرین بخش مسیر رو می‌گیریم
    if label in labels:
        print(f"⚠️ Duplicate label found: '{label}'")
        print(f" - {labels[label]}")  # مسیر اپ اول
        print(f" - {app}")           # مسیر اپ دوم
    else:
        labels[label] = app

print("✅ Check finished.")
