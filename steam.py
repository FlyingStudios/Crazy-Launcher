import winreg
from pathlib import Path

def find_steam():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\WOW6432Node\Valve\Steam"
        )

        steam_path, _ = winreg.QueryValueEx(
            key,
            "InstallPath"
        )

        return Path(steam_path)

    except:
        return None


def find_library_folders(steam_path):

    folders = []

    vdf = steam_path / "steamapps" / "libraryfolders.vdf"

    if not vdf.exists():
        return folders

    with open(vdf, "r", encoding="utf-8") as file:
        data = file.read()

    for line in data.splitlines():

        if '"path"' in line:
            path = line.split('"')[3]
            folders.append(Path(path))

    return folders


def find_games(libraries):

    games = []

    for library in libraries:

        steamapps = library / "steamapps"

        for file in steamapps.glob("appmanifest_*.acf"):

            with open(file, "r", encoding="utf-8") as f:
                content = f.read()


            name = None
            appid = None


            for line in content.splitlines():

                line = line.strip()


                if line.startswith('"name"'):
                    name = line.split('"')[3]


                if line.startswith('"appid"'):
                    appid = line.split('"')[3]


            if name and appid:
                games.append({
                    "name": name,
                    "appid": appid
                })


    return games

steam_path = find_steam()
libraries = find_library_folders(steam_path)
games = find_games(libraries)



print("Bibliotheken:")
for lib in libraries:
    print(lib)