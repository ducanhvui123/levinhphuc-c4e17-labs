from youtube_dl import YoutubeDL
# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=vGDpNEFrBwU'])
# Sample 2: Download mutiple youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=irOXGybIJLI','https://www.youtube.com/watch?v=SA35ldy92s0']) 
# SAmple 3: Download audio
options = {
    # Tell the downloader to download only the best quality of audio
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])
#sample 4
options = {
    # tell downloader to search instead of directly downloading
    'default_search': 'ytsearch',
    # Tell downloader to download only the first entry (video)
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])
# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Nhớ mưa sài gòn lam trường'])
