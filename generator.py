#!/usr/bin/env python3

#generator.py
import os
import sys
from pathlib import Path
import subprocess
from includesHandler import includesHandler

def load_template(name: str) -> str:
    template_path = Path(__file__).parent / "templates" / name
    return template_path.read_text()


def generator(args):
    project_name = args.n
    includes = args.inc.split(";") if args.inc else [];
    root = Path(project_name)

    CMAKE_TEMPLATE = load_template("CMakeLists.txt")
    conan_includes = includesHandler(includes, project_name)   
    cmake = CMAKE_TEMPLATE.format(
        name=project_name,
        find_packages=conan_includes["find_packages"],
        link_libraries=conan_includes["link_libraries"],
    )

    Path(f"{project_name}").mkdir(exist_ok=True)
    Path(f"{project_name}/src").mkdir(exist_ok=True)
    Path(f"{project_name}/include").mkdir(exist_ok=True)

    CMAIN_TEMPLATE = load_template("main.cpp")
    HEADER_TEMPLATE = load_template("header.h")

    with open(f"{project_name}/src/main.cpp", "w") as f:
        f.write(CMAIN_TEMPLATE)

    with open(f"{project_name}/include/initpp.h", "w") as f:
        f.write(HEADER_TEMPLATE);

    with open(f"{project_name}/CMakeLists.txt", "w") as f:
        f.write(cmake);

    subprocess.run(["cmake", "-S", ".", "-B", "build"], cwd=root, check=True)
    subprocess.run(["ln", "-s", "build/compile_commands.json", "."], cwd=root, check=True)
    subprocess.run(["make"], cwd=f"{root}/build", check=True)



