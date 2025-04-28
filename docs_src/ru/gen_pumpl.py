from pathlib import Path
import subprocess
import re

root = "../../"
docs_src = root + "docs_src/ru/"

file_contents = {
    str(file_path): file_path.read_text(encoding='utf-8').splitlines()
    for sub_dir in Path(docs_src).iterdir()
    if sub_dir.is_dir()
    for file_path in sub_dir.glob("file")
}

def generate_plantuml_diagrams(file_dict):
    i = 0
    for file_path, lines in file_dict.items():
        
        for line in lines:
            dir_name = Path(file_path).parent.name
            base_output_path = Path(file_path).parent / f"class_{dir_name}.puml"
            print(dir_name)
            #print(base_output_path)
            #subprocess.run(f"hpp2plantuml -i {line} -o {file_path }", shell=True)


generate_plantuml_diagrams(file_contents)