import requests

readmes = [
    "https://raw.githubusercontent.com/brandonvio/trackerp/master/README.md",
    "https://raw.githubusercontent.com/brandonvio/fuzzle-app/master/README.md",
    "https://raw.githubusercontent.com/brandonvio/reallo-app/master/README.md",
    "https://raw.githubusercontent.com/brandonvio/rythm-matrix/master/README.md"
]

readme_string = ""

for url in readmes:
    f = requests.get(url)
    readme_string += f.content.decode("utf-8")

print(readme_string)
open('README.md', 'w').write(readme_string)
