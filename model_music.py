
import requests
artist = input("Enter artist name:") # allow user to input the artist they want

url = "https://youtube-music1.p.rapidapi.com/v2/search"

querystring = {"query":artist}

headers = {
	    "X-RapidAPI-Key": "4a1e45ca8dmshcde31ef8a5baed3p1a2a7ejsn9952d2cf96bd", # use personal key
	    "X-RapidAPI-Host": "youtube-music1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text) # print all data that is in API


import json # using .json to reorganize raw data

    # define variables and assign a value
string_val = response.text
dict_val = json.loads(string_val)
album_list = [] # create a new list to start from scratch
songlist = dict_val["result"]["songs"] # dictionary values from API dictionary

def music_function(): # define whole function
    print("Artist's Albums:")
    for song in songlist:
        if song["album"]["name"] not in album_list: 
            album_list.append(song["album"]["name"]) # if the songs album is not in the album list then the .append code will add


    for albumname in album_list: # all albums in new album list is printed one by one
        print(albumname)
    album = input("Enter album name:") # let user choose an album

    found = False # by default nothing is found
    for song in songlist:
        if song["album"]["name"] == album: # if machine is able to find song name in dictionary then song names will be printed
            print("Song's in " + album)
            print(song["name"])
            found = True # variable is now set as true

    if found == False: 
        print("Information not found") # if correct info not added then output will tell user

music_function() # call the function that was defined before