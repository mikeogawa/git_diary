# Git Diary
This repository helps keep track of what you've done so far and so forth.

This is mainly intended to keep track of the accomplishment I've made during work etc.

You can have a to do list (ex:`diary.md`) and target sections that you want to keep track of.

You will also be able to budle sections of markdowns. 

If you check `diary/`, you'll notice that it only takes part of `diary.md`.
```
# To Do
- [ ] wash the dishes
- [ ] Clean My room
...

# Gone
# # Private Stuff
# - [ ] Watch Starwars 

# Done
- Aboslutely Nothing
```

You can also extract and change markdown text using `config.py` when bundling as shown below:
```
### 2020/...
**Done**
- Aboslutely Nothing
```

# Installing

1. First Fork this repository and clone

2. modify `config.py`

3. Setup git configuration
```
git config --local user.name <USERNAME>
git config --local user.email <EMAIL>
git config --local user.password <PASSWORD>
```

4. Add a terminal shortcut (zshrc)
The following adds shortcut to zshrc.
```
cd git_diary
echo "alias push_diary=\"python $(pwd|cat)/command.py\"" >> ~/.zshrc
source ~/.zshrc
```

5. Remove Current Diary 
```
rm -r diary/
rm diary.md
git commit -m "own commit"
``` 
This is for sample purpose thus this is unrequired

6. Push: `git push -u origin master`

# How to Use
1. Modify your target markdown file
2. on terminal: `push_diary`

# License 
MIT