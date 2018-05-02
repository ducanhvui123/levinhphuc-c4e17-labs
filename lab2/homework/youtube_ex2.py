from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Famous', 'Meant to be', 'What ever it takes', 'No tears left to cry', 'THe middle', 'You make it easy', 'Heaven', 'Zombie bad wolves', 'Wait marron5', 'say amen' ])
