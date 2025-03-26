[app]

# Basic App Info
title = Camera Streamer
package.name = camerastreamer
package.domain = com.yourdomain
version = 1.0.0

# Files and Sources
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Requirements
requirements = 
    python3,
    kivy==2.2.1,
    opencv-python-headless,
    numpy,
    pyjnius,
    android,
    openssl

# Android Permissions
android.permissions = 
    INTERNET,
    CAMERA,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE,
    ACCESS_NETWORK_STATE,
    WAKE_LOCK

# Hardware Features
android.features = 
    camera,
    android.hardware.camera,
    android.hardware.camera.any

# Build Configuration
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.archs = arm64-v8a, armeabi-v7a

# OpenCV Configuration
android.add_libs_armeabi_v7a = libopencv_java4.so
android.add_libs_arm64_v8a = libopencv_java4.so

# App Behavior
orientation = portrait
fullscreen = 0
android.allow_backup = False
android.accept_sdk_license = True

# Modern Android Support
android.gradle_dependencies = 
    implementation 'androidx.core:core-ktx:1.12.0'
    implementation 'androidx.appcompat:appcompat:1.6.1'
