![InstagramPy](https://socialify.git.ci/Devansh3712/InstagramPy/image?forks=1&language=1&owner=1&stargazers=1&theme=Dark)

<h1 align = "center">InstagramPy</h1>
<p align = "center"><i>Library for scraping basic Instagram data</i></p>

<p align = "center">
	<a href = "https://www.python.org"><img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/></a>
	<a href = "./LICENSE"><img src = "https://img.shields.io/github/license/Devansh3712/InstagramPy?style=for-the-badge"></a>
</p>

---

### Installation

- PyPI package

> Windows
```console
pip install igpy
```

> Linux/MacOS
```console
pip3 install igpy
```

- Clone the repository to your local machine and install
```console
git clone https://github.com/Devansh3712/InstagramPy.git
cd InstagramPy
python setup.py install
```

---

### Usage

- Fetch user data
```python
from instagrampy import Instagrammer

obj = Instagrammer()
user = obj.user(username = "whodevansh")
print(user)
```

- Fetch post data
```python
from instagrampy import Instagram

obj = Instagram(url = "https://www.instagram.com/p/BsOGulcndj-/")
user = obj.post()
print(user)
```
