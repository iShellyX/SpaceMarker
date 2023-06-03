import cx_Freeze

executables = [
    cx_Freeze.Executable(script= "main.py", icon= "space.png")
]

cx_Freeze.setup(
    name= "Space Marker",
    options= {
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["arquivo.py",
                            "bg.jpg",
                            "nome.txt",
                            "Space_Machine_Power.mp3",
                            "space.png"]
        }
    }, executables= executables
)