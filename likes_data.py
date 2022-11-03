likes_data = {
    "ts_likes":0,
    "fearless_likes":0
}

def getData():
    return likes_data

def getLikes(song):
    return likes_data[song]

def incrementLikes(song):
    likes_data[song]+=1
    return likes_data[song]

