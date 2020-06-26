<br>
<div align="center">
  <a href="https://jackal-cogito.tk"><img width="125px" src="logo.webp" alt="logo"></a>
</div>
<h1 align="center">Django Multi-Language with Google Translator</h1>
<div align="center">
  <em>a module could let you auto create django.po file</em>
</div>
<br>

<br>
<div align="center">
  <img src="https://img.shields.io/github/last-commit/shiveringbulbul/django-googletrans" alt="Github Latest Commit">
  <a href="https://github.com/shiveringbulbul/django-googletrans/issues"><img src="https://img.shields.io/github/issues/shiveringbulbul/django-googletrans" alt="Issues"></a>
  <a href="https://github.com/shiveringbulbul/django-googletrans/blob/master/LICENSE"><img src="https://img.shields.io/github/license/shiveringbulbul/django-googletrans" alt="License"></a>
  <img src="https://img.shields.io/github/languages/code-size/shiveringbulbul/django-googletrans">
  <a href="https://jackal-cogito.tk"><img src="https://img.shields.io/website?label=Cogito%20Ergo%20Sum&down_message=maintained&up_message=online&url=https%3A%2F%2Fjackal-cogito.tk"></a>
</div>
<br>

[//]: # (GitHub 關注度)
<div align="center">
  <img src="https://img.shields.io/github/followers/shiveringbulbul?style=social">
  <img src="https://img.shields.io/github/forks/shiveringbulbul/django-googletrans?style=social">
  <img src="https://img.shields.io/github/stars/shiveringbulbul/django-googletrans?style=social">
  <img src="https://img.shields.io/github/watchers/shiveringbulbul/django-googletrans?style=social">
</div>
<br>
<br>


---


[//]: # (╠═══╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬════╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═══╣)
[//]: # (╠═══╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬════╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═══╣)


#### :gem: Usage:

```bash
$ python ./scripts/google_translator.py [dir-name-in-locale] ['--same']
```

If you wanna translate the ".po" file in "./locale/zh_Hans", just run:

```bash
$ python scripts/google_trans.py zh_Hans
```

The translated file will be created in the path of locale.
If you put "same" word after command, target file will be override.


#### :page_facing_up: Other commands:

| parameter     | description |
| :-----        | :----       |
| --all, -a     | translate all language in locale folder |
| --delete, -d  | delete backup django.po |


<br><br>
<p align="right">JackaL at&nbsp; 2020.07<p>
<hr>
<div align="center">
  <p> Copyright &copy; 2020</p>
</div>
