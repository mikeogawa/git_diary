# Git Diary
This repository helps keep track of what you've done so far and so forth.

This is mainly intended to keep track of the accomplishment I've acheived during work etc.

# Installing

1. First Fork this repository and clone

2. Setup git configuration
```
git config --local user.name <USERNAME>
git config --local user.email <EMAIL>
git config --local user.password <PASSWORD>
```

3. Add a shortcut (zshrc)
```
echo "alias push_diary=python $(pwd|cat)/command.py" >> "~/.zshrc"
# or echo "alias push_diary=python $(pwd|cat)/command.py" >> "~/.bashrc"
```

4. Remove Current Diary 
```
rm -r diary/
rm diary.md
git commit -m "own commit"
``` 
This is for sample purpose thus this is unrequired

5. modify `config.py`

6. Push: `git push -u origin master`

# How to Use
1. Modify your target markdown file
2. on terminal: `push_diary`

# License 
MIT