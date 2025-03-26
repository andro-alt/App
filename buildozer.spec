[app]

# ===== BASIC APP INFO =====
title = Camera Streamer
package.name = camstream
package.domain = com.yourname
version = 1.0

# ===== REQUIREMENTS =====
requirements = 
    python3,
    kivy==2.1.0,
    opencv-python-headless,
    numpy,
    pyjnius,
    android,
    openssl

# ===== ANDROID PERMISSIONS =====
android.permissions = 
    INTERNET,
    CAMERA,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE,
    WAKE_LOCK

# ===== CAMERA CONFIGURATION =====
android.features = camera
android.add_libs_armeabi_v7a = libopencv_java4.so

# ===== BUILD SETTINGS =====
android.api = 33
android.minapi = 21
android.ndk = 23b
android.arch = armeabi-v7a  # For maximum compatibility
orientation = portrait
fullscreen = 0

# ===== OPTIMIZATIONS =====
# android.allow_backup = False  # Uncomment to disable app backups
# android.arch = arm64-v8a     # Uncomment for newer devices only
