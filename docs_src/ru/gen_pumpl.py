from pathlib import Path
import subprocess

root = "../../"
docs_src = root + "docs_src/ru/"

file_contents = {
    str(file_path): file_path.read_text(encoding='utf-8').splitlines()
    for sub_dir in Path(docs_src).iterdir()
    if sub_dir.is_dir()
    for file_path in sub_dir.glob("file")
}

def generate_plantuml_diagrams(file_dict):
    for file_path, lines in file_dict.items():
        for line in lines:
            print(line)
            subprocess.run(f"hpp2plantuml -i {line} -o {file_path }", shell=True)

        

generate_plantuml_diagrams(file_contents)