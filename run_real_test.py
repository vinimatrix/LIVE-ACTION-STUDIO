import sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())

from procesar_pagina import main

sys.argv = [
    "procesar_pagina.py",
    "--image", r"C:\Users\vm004458\Downloads\p1.jpg",
    "--char_map", json.dumps({"Boruto": "boruto_tbv", "Kawaki": "kawaki_tbv"}),
    "--max_scenes", "3",
    "--output", "final_output/p1_prompts.txt"
]
main()
