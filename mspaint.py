#!/usr/bin/env python3
"""
Cross-platform launcher to replace and/or wrap 'mspaint'

Opens the image file specified in argv[1] if given;
otherwise, open the first `.bmp` file found in the
current working directory or a subdirectory.

Installation:
=============

  Windows
  -------
    Simply run your desired script from the directory 
    containing this file, or otherwise copy `mspaint.py`
    to a directory in your environment PATH variable.
    
    You may also add the directory containing this
    file (`mspaint.py`) to your PATH variable in 
    "Modify Environment Variables."
    
    Ensure `.PY` is in your `PATHEXT` environment
    variable and that Python >= 3.8 is installed.

  Unix/Mac/Linux/Android
  ----------------------
    ### One-Step Run
      Replace `./Hello_World_Italic.py` with the script
      you want to run and execute in terminal:
      ```
        PATH=$PWD:$PATH python3 ./Hello_World_Italic.py
      ```
    ### Installation
      Simply copy this script into your 
      `~/.local/bin/` directory (or preferred `bin`
      directory such as `/usr/local/bin/`) and ensure
      the new copy has read+execute permissions,
      e.g. in terminal:
      ```
        cp mspaint.py ~/.local/bin/mspaint && \
           chmod 0755 ~/.local/bin/mspaint
      ```
"""
from subprocess import CalledProcessError, check_output
from pathlib import Path
from sys import argv, platform
from urllib.parse import ParseResult, urlunparse

# The path tp the file we want to open
file: Path = Path(
  argv[1:] and argv[1]
  or str(
    next(
      Path.cwd().rglob("*.bmp")
    )
  )
).resolve().absolute()


is_windows: bool = platform == "win32"
is_android: bool
try:
  is_android = check_output(
    [
      "toolbox",
      "getprop",
      "ro.product.system.manufacturer"
    ],
    encoding="UTF-8"
  ).strip() == "Android"
except (CalledProcessError, FileNotFoundException):
  is_android = False


if is_windows:
  print(check_output(
    [
      "cmd.exe", "/C", "start", "", "mspaint.exe",
      str(file)
    ],
    shell=False,
  ))
else:
  if is_android:
    url: str = urlunparse(
      ParseResult(
        scheme="file",
        netloc="",
        path=file.as_posix(),
        params="",
        query="",
        fragment="",
      )
    )
    # Prefixes that indicate file is on internal SD card
    sd_prefixes = (
      ("data","media"),
      ("storage","emulated"),
      ("mnt", "shell", "emulated"),
    )
    # Adjust path to a globally-readable form if Android
    # and path is on internal SD card
    file = (
      Path(
        *(
          "/",
          "sdcard",
        )
        + next(
          file.parts[1 + len(sl) :]
          for sl in sd_prefixes
          if file.parts[1 : 1 + len(sl)] == sl
        )[1:]
      )
      if any(
        file.parts[1 : 1 + len(sl)] == sl 
        for sl in sd_prefixes
      )
      else file
    )
    print(
      check_output(
        [
          "am",
          "start",
          "--user",
          "0",
          "-a",
          "android.intent.action.VIEW",
          "-c",
          "android.intent.category.DEFAULT",
          "-t",
          "image/*",
          "--grant-read-uri-permission",
          "--grant-write-uri-permission",
          "--grant-persistable-uri-permission",
          "--grant-prefix-uri-permission",
          "-d",
          url,
        ]
      )
    )
  else:
    # Linux, Mac
    print(check_output(
      [
        "xdg-open", file.as_posix()
      ],
      shell=False,
    ))


