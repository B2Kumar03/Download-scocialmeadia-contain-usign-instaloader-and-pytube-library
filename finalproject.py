import instaloader
import instaloader
from pytube import YouTube
from moviepy.editor import *
from pytube import YouTube
def profilepiloader():
    
    Instadownloader=instaloader.Instaloader()

    acc=input("Enetr InstaId(Eg :- keshav23):")

    Instadownloader.download_profile(acc,profile_pic_only=True)


def videoLoaderYt():
    link=input("Enter Your Url/link :")
    yt=YouTube(link)
    yt.streams.filter(progressive=True,file_etension='mp4').order_by('resulation')[-1].download()



def download_instagram_reels(username, download_path):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username '{username}' does not exist.")
        return

    for post in profile.get_posts():
        if post.typename == 'GraphVideo' and post.is_video:
            try:
                loader.download_post(post, target=download_path)
                print(f"Reel downloaded: {post.url}")
                break
            except Exception as e:
                print(f"Failed to download reel: {post.url}")
                print(f"Error: {e}")
                break
def audioloader():
    youtube_video_url = input("Enter Your Url/link :")

    yt = YouTube(youtube_video_url)
    video_stream = yt.streams.filter(only_audio=True).first()
    video_stream.download(filename='temp_video')


    video_clip = VideoFileClip('temp_video.mp4')
    audio_clip = video_clip.audio
    audio_clip.write_audiofile('extracted_audio.mp3')

    video_clip.close()
    audio_clip.close()
    os.remove('temp_video.mp4')

print('Audio extraction complete.')



while True:
    print("--------------------------------------")
    print('1.Download profilePic from Instagram.')
    print("2.Download Reels Using insta Id.")
    print("3.Download Audio from YouTube.")
    print("4.Download Video From YouTube.")
    print("--------------------------------------")
    #print()
    print("Enter Your choice 1 to 4 :")
    ch=int(input())
    if ch==1:
        profilepiloader()
    elif ch==2:
         if __name__ == "__main__":
            id=input(r"Enter Insta Id :")
            download_instagram_reels(id,r'C:\Users\hello\OneDrive\Desktop\kkkk')
    elif ch==3:
        audioloader()
    elif ch==4:
        videoLoaderyt()
    else:
        print("Invalid Choice")

    print("-----------------------------------------------------------------------")
    print('Do you want run Again click Y/n:')
    print("-----------------------------------------------------------------------")
    y=input()
    if y=='y' or y=='Y':
        continue
    else:
        print("---------Thank You-----------")
        break
        
       


