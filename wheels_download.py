import subprocess
from pathlib import Path
import os
cuvers=  [
    "117",
]

pyvers = [
    "310",
]

archs = [
    "win_amd64",
    "linux_x86_64"
]


targets = [
    "torch-2.0.1",
    "torchaudio-2.0.2",
    "torchvision-0.15.2",

    "pyg_lib-0.2.0",
    "torch_cluster-1.6.1",
    "torch_scatter-2.1.1",
    "torch_sparse-0.6.17",
    "torch_spline_conv-1.2.2"
]

curl = lambda url: ["curl", "-OL#", url]

torch_o, torch_g = targets[:3], targets[3:]

root = Path("/")
wheels = (root / "wheels")
wheels.mkdir(exist_ok=True, parents=True)
urls = []
poetry_commands = []
for cuver in cuvers:
    for pyver in pyvers:
        for arch in archs:
            for target in torch_o:
                url = f"https://download.pytorch.org/whl/cu{cuver}/{target}%2Bcu{cuver}-cp{pyver}-cp{pyver}-{arch}.whl"
                urls.append(url)
                command = ["poetry", "add", f'"{wheels / Path(url).name}"', f'--python="={pyver[0]}.{pyver[1:]}"', f'--platform="{arch}"']
                poetry_commands.append(" ".join(command))
            for target in torch_g:
                url = f"https://data.pyg.org/whl/torch-2.0.0%2Bcu{cuver}/{target}%2Bpt20cu{cuver}-cp{pyver}-cp{pyver}-{arch}.whl"
                urls.append(url)
                command = ["poetry", "add", f'"{wheels / Path(url).name}"', f'--python="={pyver[0]}.{pyver[1:]}"', f'--platform="{arch}"']
                poetry_commands.append(" ".join(command))
pwd = Path.cwd()
os.chdir(wheels)

for url in urls:
    local_path = (wheels / Path(url).name).resolve()
    if local_path.exists():
        print(f"Already downloaded: {url} (at {local_path}))")
        continue
    try:
        print(f"Downloading: {url}")
        subprocess.call(curl(url))
        local_path.rename(str(local_path).replace("%2B", "+"))
    except:
        print(f"Skipped: {url}")

os.chdir(pwd)


print("Please add the following lines to pyproject.toml:")

print("finish!")