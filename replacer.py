import os

# Replacement map: "old" : "new"
replacements = {
    "niyati": "niyati",
    "Niyati": "Niyati",
    "NIYATI": "NIYATI",
    "Niyati_music_bot": "Niyati_music_bot",
    "INNOCENT_FUCKER": "INNOCENT_FUCKER",
    "7168729089": "7168729089",
    "KomalMusicUpdate": "KomalMusicUpdate",
    "Komal_Music_Support": "Komal_Music_Support"
}

# 1. Replace file/folder names
for root, dirs, files in os.walk(".", topdown=False):
    for name in files + dirs:
        new_name = name
        for old, new in replacements.items():
            if old in new_name:
                new_name = new_name.replace(old, new)
        if new_name != name:
            old_path = os.path.join(root, name)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

# 2. Replace content inside all files (excluding binary and .git)
for root, _, files in os.walk("."):
    if ".git" in root:
        continue
    for file in files:
        try:
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            original = content
            for old, new in replacements.items():
                content = content.replace(old, new)
            if content != original:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
        except Exception:
            pass  # skip binary or unreadable files
