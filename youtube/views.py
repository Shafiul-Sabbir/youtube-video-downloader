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
        # download_folder = 'C:\\Downloads\\'
        # Modify the download_folder to the default downloads directory
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

        
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

# from django.shortcuts import render, redirect
# from pytube import YouTube
# import tempfile
# import os

# # Create your views here.

# def youtube(request):
#     if request.method == "POST":
#         link = request.POST.get('link')
        
#         if not link:
#             return render(request, 'youtube/youtube.html', {'error': 'Please provide a valid YouTube link'})

#         try:
#             video = YouTube(link)
#             stream = video.streams.get_lowest_resolution()
#         except Exception as e:
#             return render(request, 'youtube/youtube.html', {'error': f'Error processing YouTube video: {str(e)}'})

#         # Use a temporary directory for file downloads
#         with tempfile.TemporaryDirectory() as temp_dir:
#             try:
#                 # Downloads video to the temporary directory
#                 stream.download(temp_dir)
                
#                 # Specify the relative path where you want to save the file in your static directory
#                 relative_path = f'videos/{video.title}.mp4'
                
#                 # Assuming your static directory is configured correctly in settings.py
#                 file_path = os.path.join('static', relative_path)
                
#                 # Move the downloaded file to the static directory
#                 os.rename(os.path.join(temp_dir, f'{video.title}.mp4'), file_path)
                
#                 return render(request, 'youtube/successful.html', {'file_path': file_path})
#             except Exception as e:
#                 return render(request, 'youtube/youtube.html', {'error': f'Error saving the video: {str(e)}'})

#     return render(request, 'youtube/youtube.html')

# def successful_page(request):
#     return render(request, 'youtube/successful.html')
