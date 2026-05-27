#!/usr/bin/env python3

#includesHandler.py
from pathlib import Path
import subprocess
from libraries import getLibaries;

LIBRARY_TARGETS = getLibaries()

def includesHandler(includes, project_name):
    if(len(includes) == 0): 
        return {"find_packages": "", "link_libraries": ""}

    find_packages = ""
    link_lines = ""
    define_lines = ""

    for lib in includes:
        find_packages += f"find_package({lib} REQUIRED)\n"
        lib_target = LIBRARY_TARGETS.get(lib)
        link_lines += f"target_link_libraries({project_name}_core PUBLIC {lib_target})\n"
        define_lines += f"target_compile_definitions({project_name}_core PUBLIC HAS_{lib.upper()})\n"

    link_libraries = link_lines + define_lines

    return {
        "find_packages": find_packages,
        "link_libraries": link_libraries,
    }

# TODO: GET PACKAGES

