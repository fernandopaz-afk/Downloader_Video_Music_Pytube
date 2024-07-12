from pytube.cli import on_progress
from pytube import YouTube

# Replace with your video URL
url = input("Ingrese el video a descargar por favor: ")
yt = YouTube(url,on_progress_callback=on_progress)

# Get all available streams
streams = yt.streams.filter(file_extension='mp4')
# Extract unique resolutions and their corresponding streams
resolutions_with_streams = [(stream.resolution, stream.filesize, stream) for stream in streams if stream.resolution]
# Remove duplicates and sort by resolution
unique_resolutions_with_filesizes_and_streams = list(set(resolutions_with_streams))
unique_resolutions_with_filesizes_and_streams.sort(key=lambda x: int(x[0][:-1]))

# Display resolutions with file sizes
print("\n")
print("-----------------------------")
print("Nombre del video: ", yt.title)
print("---Available resolutions and file sizes: ---")
for index, (resolution, filesize, stream) in enumerate(unique_resolutions_with_filesizes_and_streams, start=1):
    print(f"{index}. {resolution}: {filesize / (1024 * 1024):.2f} MB")

# Allow user to select a resolution
selected_index = int(input("\nSeleccione el número de la resolución que desea descargar: ")) - 1
# Get the selected resolution and file size
selected_resolution, selected_filesize, selected_stream = unique_resolutions_with_filesizes_and_streams[selected_index]
# Display selected resolution and file size
print(f"\nHa seleccionado la resolución {selected_resolution} con un tamaño de archivo de {selected_filesize / (1024 * 1024):.2f} MB.")

selected_stream.download()