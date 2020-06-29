import os
import re
import config
import datetime
import subprocess as sub


class MDReader:
    def __init__(self,file):
        self.res = []
        with open(file) as f:
            line_array = f.read().strip().split("\n")
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
        res = re.sub("^#{1}","",x).strip()
        print(res)
        return res 

    def is_target_header(self,x):
        return x in config.TARGET_HASH

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
    path = os.getcwd()
    return os.path.join(path,filename)

def main():
    diary_path = preprocess_filename(config.DIARY_DIR)
    text = get_md_text(diary_path)
    file_name = datetime.datetime.now().strftime(config.FILENAME_DIR)
    file_name_abs = preprocess_filename(file_name)
    check_make_dir(file_name_abs)
    with open(file_name_abs,"w") as f:
        f.write(text)

def git(file_name,file_name_abs):
    cmd = [
        "git add {}".format(file_name_abs),
        "git commit -m \"{}\"",format(file_name),
        "git push origin master"]
    pid = sub.Popen(cmd, stdout=sub.PIPE,stderr=sub.PIPE)
    out, err = pid.communicate()
    print(out.decode("utf-8"))
    print(err.decode("utf-8"))

def after_commit(file_name_abs):
    if config.DELETE_AFTER_COMMIT:
        os.remove(file_name_abs)

if __name__=="__main__":
    main()