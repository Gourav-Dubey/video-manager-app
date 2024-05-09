import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            test= json.load(file)
            return test
    except FileNotFoundError:
        return[]
    
def help_to_save_date(videos):
    with open('youtube.txt','w') as file:
        json.dump( videos,file)    
      
def list_all_videos(videos):
    if not videos:
        print("No videos available.")
    else:
        print("\n")
        print("*"*50 )
        for index,video  in enumerate(videos,start=1):
          print(f"{index}. Name: {video['name']}, Time: {video['time']}")
        print("\n")
        print("*"*50 )  


def add_a_youtube_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({"name":name,"time":time})
    help_to_save_date(videos)
    

def update_a_youtube_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update"))
    if 1<= index<=len(videos):
        name=input("enter the new video name: ")
        time=input("enter the new video time: ")
        videos[index-1]={'name':name,'time':time}
        help_to_save_date(videos)
    else:
        print("invalid index selected")

def delete_a_video(videos):
    list_all_videos(videos)
    index=int(input("enter the video number to be deleted: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        help_to_save_date(videos)
    else:
        print("invalid  video index selected")    

def exit_the_app(videos):
    help_to_save_date(videos)
    print("Exiting the application.")

def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all Videos")
        print("2. Add a youtube Video")
        print("3. update a youtube video")
        print("4. delete a video")
        print("5. exit the app")
        choice=input("Enter your choice: ")
        # print(videos)
        match choice:
            case'1':
                list_all_videos(videos)
            case'2':
                add_a_youtube_video(videos)
            case'3':
                update_a_youtube_video(videos)
            case'4':
                delete_a_video(videos)
            case'5':
                break
            case _:
                print("invalid number")

if __name__=="__main__":
    main()                

