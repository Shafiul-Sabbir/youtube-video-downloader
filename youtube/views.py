from django.shortcuts import render, redirect
from pytube import *
import os
# Create your views here.

# defining function
def youtube(request):
    # checking wheather youtube request is post or not
    if request.method == "POST":
        # Getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        
        # setting video resolution
        stream = video.streams.get_lowest_resolution()
        
        # specify the path where you I to save the video
        download_folder = 'C:\\Downloads\\'
        
        # create the folder if it doesnt exist
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        
        # downloads Video to the specified folder
        stream.download(download_folder)
        
        # returning html page
        return redirect('successful_page')
    
    return render(request, '../templates/youtube/youtube.html')

def successful_page(request):
    return render(request, '../templates/youtube/successful.html')