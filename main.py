from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from android.permissions import request_permissions, Permission
import socket
import cv2
import time
import struct
import numpy as np

class CameraSenderApp(App):
    def build(self):
        # Request Android permissions
        request_permissions([Permission.CAMERA, Permission.INTERNET])
        
        self.layout = BoxLayout(orientation='vertical')
        
        # Camera preview
        self.image = Image()
        self.layout.add_widget(self.image)
        
        # Status label
        self.status = Label(text="Waiting for server connection...", size_hint=(1, 0.1))
        self.layout.add_widget(self.status)
        
        # Server settings
        self.server_ip = '147.185.221.20'  # CHANGE TO YOUR SERVER IP
        self.server_port = 26712
        self.sock = None
        self.capture = None
        self.connected = False
        
        # Start connection attempts
        Clock.schedule_interval(self.try_connect, 5)  # Try every 5 seconds
        Clock.schedule_interval(self.capture_and_send, 30)  # Send every 30 seconds
        
        return self.layout
    
    def try_connect(self, dt):
        if not self.connected:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.server_ip, self.server_port))
                self.capture = cv2.VideoCapture(0)  # 0=back camera, 1=front
                self.connected = True
                self.status.text = f"Connected to {self.server_ip}:{self.server_port}"
            except Exception as e:
                self.status.text = f"Connection failed: {str(e)}"
                self.connected = False
    
    def capture_and_send(self, dt):
        if not self.connected:
            return
            
        try:
            # Capture frame
            ret, frame = self.capture.read()
            if ret:
                # Update preview
                buf = cv2.flip(frame, 0).tobytes()
                texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
                texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                self.image.texture = texture
                
                # Compress image
                _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
                data = np.array(buffer).tobytes()
                
                # Send image
                self.sock.sendall(struct.pack(">L", len(data)) + data)
                self.status.text = f"Photo sent at {time.strftime('%H:%M:%S')}"
                
        except Exception as e:
            self.status.text = f"Error: {str(e)}"
            self.connected = False
            self.sock.close()

if __name__ == '__main__':
    CameraSenderApp().run()
