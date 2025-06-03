import sqlite3

# Run this file to start the program
# python3 youtube_manager_db.py

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS youtube_videos (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL
                )
                ''')


def main():
    while (True):
        print('*' * 20)
        print("1. List videos")
        print("2. Add videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        print('*' * 20)

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                list_videos()
            case 2:
                add_videos()
            case 3:
                update_videos()
            case 4:
                delete_videos()
            case 5:
                break
            case _:
                print("Invalid choice")
    conn.close()


def list_videos():
    cursor.execute('SELECT * FROM youtube_videos')
    videos = cursor.fetchall()

    if len(videos) == 0:
        print("No videos found")
    else:
        for video in videos:
            print(video)


def add_videos():
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    cursor.execute('INSERT INTO youtube_videos (name, time) VALUES (?, ?)',
                   (name, time))
    conn.commit()
    print("Video added successfully")


def update_videos():
    id = int(input("Enter video id: "))
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    cursor.execute('SELECT * FROM youtube_videos WHERE id = ?',
                           (id, )).fetchone()
    video = cursor.fetchone()
    if video is None:
        print("Video not found")
        return
    if name.strip() == "":
        name = video[1]
    if time.strip() == "":
        time = video[2]
    cursor.execute('UPDATE youtube_videos SET name = ?, time = ? WHERE id = ?',
                   (name, time, id))
    conn.commit()
    print("Video updated successfully")


def delete_videos():
    id = int(input("Enter video id: "))
    video = cursor.execute('SELECT * FROM youtube_videos WHERE id = ?',
                           (id, )).fetchone()
    if video is None:
        print("Video not found")
        return
    cursor.execute('DELETE FROM youtube_videos WHERE id = ?', (id, ))
    conn.commit()
    print("Video deleted successfully")


if __name__ == "__main__":
    main()
