import sys
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
import requests
from dotenv import load_dotenv, dotenv_values

config = dotenv_values(".env")

# Spotify OAuth setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=config['CLIENT_ID'],
    client_secret=config['CLIENT_SECRET'],
    redirect_uri='http://localhost:8888/callback',
    scope="user-read-currently-playing user-modify-playback-state"
))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Spotify Controller")

        # Create UI elements
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        # Get initial track info
        self.update_ui()

        # Create control buttons
        button1 = QPushButton("Play", self)
        button1.clicked.connect(self.on_button1_clicked)
        layout.addWidget(button1)

        button2 = QPushButton("Pause", self)
        button2.clicked.connect(self.on_button2_clicked)
        layout.addWidget(button2)

        button3 = QPushButton("Next", self)
        button3.clicked.connect(self.on_button3_clicked)
        layout.addWidget(button3)

        # Set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_ui(self):
        results = sp.current_user_playing_track()
        if results:
            track_info = results['item']
            artist_name = track_info['artists'][0]['name']
            song_name = track_info['name']

            # Update window title
            self.setWindowTitle(f"{artist_name} - {song_name}")

            # Update album image
            album_image_url = track_info['album']['images'][0]['url']
            pixmap = self.load_image_from_url(album_image_url)
            if pixmap:
                self.image_label.setPixmap(pixmap)
                self.image_label.setScaledContents(True)

    def load_image_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            return pixmap
        return None

    def on_button1_clicked(self):
        sp.start_playback()
        self.update_ui()

    def on_button2_clicked(self):
        sp.pause_playback()
        self.update_ui()

    def on_button3_clicked(self):
        sp.next_track()
        time.sleep(0.2)
        self.update_ui()

# Create and show the window
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
