import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script = "main.py", icon = "data/drag ic.ico"
)]

cx_Freeze.setup(
    name = "ShotterDragon",
    options = {"build_exe": {"packages": [
        "pygame"] , "include_files":["data"] }},
    executables = arquivo

)