import spotipy
from spotipy.oauth2 import SpotifyOAuth
from init_selen import *
from time import sleep
import json

google_form = "ADD URL HERE"

def get_playlist(sp):
    playlists = sp.current_user_playlists()
    playlist_id = playlists['items'][2]['id']
    tracks = sp.playlist_items(playlist_id)

    return(tracks)

def submit_tracks(playlist):
    #Start from first song in playlist
    track = 0

    while True:
        #Open google chrome in incognito
        [browser, song_artist, className, submitbutton] = init_form(google_form)
        option = webdriver.ChromeOptions()
        option.add_argument("-incognito")

        #Find answer sections
        className = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionRadioChoice")
        song_artist = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
        submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")

        #click class name
        #0-4
        #Hail ISP is 1 for example

        className["error here, index based on desired className"].click()
        try:
            song_artist[0].send_keys(playlist['items'][track]['track']['name'])
            song_artist[1].send_keys(playlist['items'][track]['track']['album']['artists'][0]['name'])
            sleep(10)
            submitbutton[0].click()
            sleep(5)
            browser.close()
        except IndexError:
            print("Last track sent: {} ".format(track))
            break

        print("Last track sent: {} ".format(track))
        track += 1

    return

def get_keys(file_name):
    with open(file_name) as f:
        keys = f.read()

    keys_json = json.loads(keys)
    return(keys_json)


if __name__ == "__main__":

    if google_form == "ADD URL HERE":
        raise Exception("\n\nYou need to link a google form, check around line 6")
        exit()

    keys = get_keys("keys.txt")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=keys["client_id"],
                                                client_secret=keys["client_secret"],
                                                redirect_uri="https://github.com/",
                                                scope="user-modify-playback-state"))

    playlist = get_playlist(sp)
    #submit_tracks(playlist)
    print("Done or index errored lol")
