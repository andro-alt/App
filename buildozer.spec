[app]

# ====== BASIC APP CONFIGURATION ======
title = Camera Streamer
package.name = camerastreamer
package.domain = com.yourdomain
version = 1.0.0
source.dir = .

# ====== APPLICATION REQUIREMENTS ======
requirements = 
    python3==3.11.2,
    kivy==2.2.1,
    opencv-python-headless==4.8.0,
    numpy==1.24.4,
    pyjnius==1.5.0,
    android,
    openssl,
    requests

# ====== ANDROID SPECIFIC CONFIGURATION ======
android.permissions = 
    INTERNET,
    CAMERA,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE,
    ACCESS_NETWORK_STATE,
    WAKE_LOCK,
    FOREGROUND_SERVICE

android.features = 
    camera,
    android.hardware.camera,
    android.hardware.camera.any

android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.archs = arm64-v8a, armeabi-v7a

# ====== OPENCV CONFIGURATION ======
android.add_libs_armeabi_v7a = libopencv_java4.so
android.add_libs_arm64_v8a = libopencv_java4.so

# ====== BUILD OPTIONS ======
orientation = portrait
fullscreen = 0
log_level = 2
android.allow_backup = False
android.accept_sdk_license = True

# ====== GRADLE CONFIGURATION ======
android.gradle_dependencies = 
    implementation 'androidx.core:core-ktx:1.12.0'
    implementation 'androidx.appcompat:appcompat:1.6.1'

# ====== P4A CONFIGURATION ======
p4a.branch = master
p4a.commit = 2023.10.06

# ====== ADVANCED OPTIONS ======
# Uncomment if using background services
# android.meta_data = 
#     android.app.background_running=true

# For Android 12+ splash screens
# android.manifest_placeholders = 
#     splashScreenTheme=@style/Theme.SplashScreen
