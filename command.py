import os
import sys
import re
import config
import datetime
import subprocess as sub
import time

current_dir = os.path.dirname(os.path.abspath(__file__))

class MDReader:
    def __init__(self,file_text, target_hash=config.TARGET_HASH):
        self.target_hash = target_hash
        self.res = []
        line_array = file_text.split("\n")
        self.extract_markdown(line_array)
    
    def extract_markdown(self,line_array):
        self.res = []
        target_header = ""
        for line in line_array:
            if self.has_header(line):
                head = self.extract_header(line)
                if self.is_target_header(head):
                    target_header = line
                else:
                    target_header = ""
            
            if target_header != "":
                self.add_line(line)

    def has_header(self,x):
        return re.match("^#{1}",x) is not None

    def extract_header(self,x):
        return re.sub("^#{1}","",x).strip()

    def is_target_header(self,x):
        return x in self.target_hash

    def add_line(self,line):
        self.res.append(line)
    
    def get_text(self):
        return "\n".join(self.res)

def get_md_text(filename):
    md = MDReader(filename)
    return md.get_text()

def check_make_dir(filename):
    dir = os.path.dirname(filename)
    if not os.path.isdir(dir):
        os.makedirs(dir)

def preprocess_filename(filename):
    if re.match("^(./)",filename):
        filename = re.sub("^(./)","",filename)
    path = current_dir
    return os.path.join(path,filename)

def append_mode(file_name, text):

    title = config.BUNDLE_TARGET_TITLE + " " + file_name.split("/")[-1].split(".")[0]
    md = MDReader(text,config.BUNDLE_TARGET_HASH)
    text = md.get_text()
    text_list = text.split("\n")
    for k,v in config.BUNDLE_REGEX_DICT.items():
        text_list = [re.sub(k,v,x) for x in text_list]
    new_text = title + "\n" + "\n".join(text_list) + "\n"

    bundle_path = preprocess_filename(datetime.datetime.now().strftime(config.BUNDLE_FILE_NAME_PATH))

    if not os.path.isfile(bundle_path):
        cmd = "git checkout {};".format(bundle_path)
        pid = sub.Popen(cmd, stdout=sub.PIPE,stderr=sub.PIPE,shell=True,cwd=current_dir)
        out, err = pid.communicate()
        print(out.decode("utf-8"))
        pid.wait()

    if os.path.isfile(bundle_path):
        with open(bundle_path,'r') as f:
            saved_text = f.read()
    else:
        saved_text = ""
    with open(bundle_path,'w') as f:
        f.write(new_text+saved_text)
    
    return bundle_path

def main():
    diary_path = preprocess_filename(config.DIARY_DIR)

    with open(diary_path) as f:
        diary_text = f.read().strip()
    text = get_md_text(diary_text)

    file_name = datetime.datetime.now().strftime(config.FILENAME_PATH)
    file_name_abs = preprocess_filename(file_name)
    check_make_dir(file_name_abs)
    with open(file_name_abs,"w") as f:
        f.write(text)
    bundle_path = append_mode(file_name, text) if config.ALLOW_BUNDLING else ""
    git(file_name,file_name_abs,bundle_path)
    if config.DELETE_AFTER_COMMIT:
        delete_files(file_name_abs,bundle_path)


def git(file_name,file_name_abs,bundle_path):
    cmd = ";".join([
        "git add {}".format(file_name_abs),
        "git add {}".format(bundle_path) if bundle_path != "" else "",
        "git commit -m \"{}\"".format(file_name),
        "git push -f origin master",
        "echo  Push Complete"])
    pid = sub.Popen(cmd, stdout=sub.PIPE,stderr=sub.PIPE,shell=True,cwd=current_dir)
    out, err = pid.communicate()
    print(out.decode("utf-8"))
    print(err.decode("utf-8"))

def delete_files(file_name_abs,bundle_path):
    os.remove(file_name_abs)
    if bundle_path != "":
        os.remove(bundle_path)


if __name__=="__main__":
    main()