# Set this path to any directory like to your todo list.(~/my_doc/to_do_list.md)
# This will not be git.
DIARY_DIR = "./diary.md"

# Set your target H1 Sections
TARGET_HASH = [
    "To Do",
    "Done",
]

# Saving Name
FILENAME_PATH = "./diary/%Y_%m/%Y_%m_%d.md"

# Bundling (This stocks the dairy data)
ALLOW_BUNDLING = True
BUNDLE_FILE_NAME_PATH = "./diary/%Y_%m/README.md"

# Bundle Head
BUNDLE_TARGET_TITLE = "###"
# Extracts only H1 parts when bundling
BUNDLE_TARGET_HASH = ["Done"]
# Bundle Regex {"original":"new form"}
BUNDLE_REGEX_DICT = {
    "#{1,3} (.*)":"**\\1**",
}

# If you want to avoid saving in local repository, you can delete it
DELETE_AFTER_COMMIT = True

