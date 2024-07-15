## with 
with open('my_path/my_file.txt', 'r') as f:
    file_data=f.read()


with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())