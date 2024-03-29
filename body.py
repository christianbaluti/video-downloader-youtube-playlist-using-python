def download_videos(playlist_url, download_path, quality='highest'):
    playlist = Playlist(playlist_url)
    print(f"Downloading {len(playlist)} videos from the playlist...")

    for video in tqdm(playlist.videos, desc="Downloading"):
        stream = video.streams.get_highest_resolution() if quality == 'highest' else video.streams.filter(res=quality).first()
        if stream:
            stream.download(download_path)
            print(f"Downloaded: {video.title}")
        else:
            print(f"No suitable stream found for {video.title}")