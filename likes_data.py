likes_data = {
    "Midnights":0,
    "Midnights (3am Edition)":0,
    "reputation":0,
    "This Love (Taylorâ€™s Version)":0,
    "Fearless (Taylor's Version)":0,
    "1989":0,
    "Bad Blood":0,
    "Speak Now":0,
    "Lover":0,
    "Red (Taylor's Version)":0,
    "1989 (Deluxe Edition)":0,
    "Red":0,
    "Today Was A Fairytale":0,
}

def getData():
    return likes_data

def getLikes(song):
    return likes_data[song]

def incrementLikes(song):
    likes_data[song]+=1
    return likes_data[song]

