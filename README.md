# Spotipy
Python executable application that allows the user play, pause and skip song on spotify, utilizing spotify api

# Imports installation
To use you need to install
pip install spotipy
pip install PyQt6
pip install requests
pip install dotenv

#Setup and Environmental variables 
Make an .env file where you will have two variables 'CLIENT_ID' and 'CLIENT_SECRET', you can get these values from your spotify app https://developer.spotify.com/dashboard
You also have to make sure that you have a redirect uri set up in the spotify app settings, I used 'http://localhost:8888/callback' but you can change the port and '/callback' to something else, just make sure it matches the redirect uri set in the code.

#run
python main.py
