import os
import re
import sys
import time
from dataclasses import dataclass, field
from shutil import copyfile
from typing import List, ClassVar

from googletrans import Translator


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')


@dataclass
class Trans:
    '''
    obj = Trans([target='dir-name-in-locale'], [same='same'])

    If you wanna translate the ".po" file in "./locale/zh_Hant", use: `obj = Trans('zh_Hant')`
    Default target is folder "./locale/en".
    The translated file will be created in the path of locale by default.
    By putting the "same" word after target, target file will be override.
    Use `obj = Trans('ko', 'same')` will override "./locale/ko/LC_MESSAGES/django.po".
    '''

    target: str = 'en'
    same: bool = False
    target_path: str = field(init=False)
    result_path: str = field(init=False)
    lines: List[str] = field(default_factory=list, init=False, repr=False)
    translator: ClassVar = Translator()

    def __post_init__(self):
        self.target_path = os.path.join(
            LOCALE_DIR, self.target, 'LC_MESSAGES', 'django.po'
        )

        if self.same:
            self.result_path = self.target_path
            backup_path = self.target_path[:-3]\
                + str(time.strftime("%Y%m%d%H%M%S", time.localtime())) + '.po'
            copyfile(self.target_path, backup_path)
        else:
            self.result_path = os.path.join(LOCALE_DIR, 'django.po')

        if self.target == 'zh_Hant':
            self.target = 'zh-TW'
        elif self.target == 'zh_Hans':
            self.target = 'zh-CN'

    def __fix_format_string(self, text):
        text_list = re.split(r'%\((\w+)\)s', text)
        new_text = str()
        for count, piece in enumerate(text_list):
            if count % 2:
                new_text += '%(' + piece + ')s'
            else:
                if piece:
                    new_text += self.translator.translate(
                        piece, dest=self.target
                    ).text
                else:
                    new_text += 'msgstr ""\n'

        new_text = new_text.replace('  ', ' ')
        new_text = new_text.replace('s>%', 's > %')
        new_text = new_text.replace('s>=%', 's >= %')
        new_text = new_text.replace('s=%', 's = %')
        new_text = new_text.replace('s<%', 's < %')
        new_text = new_text.replace('s<=%', 's <= %')
        new_text = new_text.replace('s+%', 's+%')
        new_text = new_text.replace('s-%', 's-%')
        new_text = new_text.replace('s×%', 's×%')
        new_text = new_text.replace('s÷%', 's÷%')
        new_text = new_text.replace('s%', 's%')

        return new_text

    def __clean_target(self):
        with open(self.target_path, 'r') as f:
            line = f.readline()
            while line:
                container = ''  # sentence need to be translated
                if line.startswith('msgid "'):
                    if line[7:-2]:
                        self.lines.append(line)
                        container = line[7:-2]
                    else:
                        self.lines.append(line)
                        line = f.readline()
                        while not line.startswith('msgstr "'):
                            self.lines.append(line)
                            container += line[1:-2]
                            line = f.readline()

                    if container:
                        if '%(' in container:
                            container = self.__fix_format_string(container)
                        else:
                            container = self.translator.translate(
                                container, dest=self.target
                            ).text
                        container = f'msgstr "{container}"\n'
                    else:
                        container += 'msgstr ""\n'

                    self.lines.append(container)

                elif line.startswith('msgstr "'):
                    pass
                else:
                    self.lines.append(line)
                line = f.readline()

        # convert lines to generator
        self.lines = (line for line in self.lines)

    def trans(self):
        '''controller'''

        print(f'\nTarget: {self.target_path}')

        self.__clean_target()

        with open(self.result_path, 'w') as f:
            for line in self.lines:
                f.write(line)

        print(f'Result: {self.target.upper()} translated successfully!!')
        print(f'See:    {self.result_path}.\n')


@dataclass
class Main:
    '''
    Usage:

    >> $ python ./scripts/google_translator.py [dir-name-in-locale] ['--same']

    If you wanna translate the ".po" file in "./locale/zh_Hans", just run:
    >> $ python scripts/google_trans.py zh_Hans

    The translated file will be created in the path of locale.
    If you put "same" word after command, target file will be override.

    Other commands:
      1. --all, -a: translate all language in locale folder.
      2. --delete, -d: delete backup django.po.


    made by JackaL at 2020.07
    '''

    parameters: List[str] = field(default_factory=list)
    success: int = field(default=0, repr=False)
    failure: int = field(default=0, repr=False)

    def __post_init__(self):
        self.parameters = self.parameters[1:3]

    def get_help(self):
        '''print manual'''
        print(self.__doc__)

    def delete_backup(self):
        '''delete all backup django.po'''
        for path, _, files in os.walk(LOCALE_DIR):
            for file in files:
                if file.endswith('.po') and not file.endswith('django.po'):
                    os.remove(os.path.join(path, file))
        print('\n\nAll backups deleted!\n\n')

    def __msg_fileNotFound(self):
        print('File not found.')
        print(
            'Run `python manage.py makemessages -l en -l zh_Hant -l zh_Hans'
            ' -l de -l es -l fr -l ja -l ko -l ru -l th -l vi` first!'
        )

    def __msg_success(self):
        print('\nTask Finished!')
        if self.success + self.failure > 1:
            print(f'Success: {self.success}, Failure: {self.failure}.')
        print('You could run `python manage.py compilemessages` now!\n')

    def __get_language_list(self):
        '''get existing language in locale dir'''
        language_list = []
        for _, dirs, _ in os.walk(LOCALE_DIR):
            language_list.extend(dirs)
            break
        return language_list

    def __check_file_exists(self, language):
        if language in self.__get_language_list():
            return True
        else:
            self.__msg_fileNotFound()
            return False

    def __run_trans(self, language):
        '''trans single file in locale'''
        if self.__check_file_exists(language):
            obj = Trans(target=language, same=True)
            obj.trans()
            self.__msg_success()
        else:
            return False

    def __run_trans_all(self):
        '''trans all files in the locale'''
        language_list = self.__get_language_list()
        if language_list:
            self.success = 0
            self.failure = 0
            for lang in self.__get_language_list():
                try:
                    obj = Trans(target=lang, same=True)
                    obj.trans()
                    self.success += 1
                except TypeError:
                    self.failure += 1
                    print(f'{lang.upper()} failed via Google Translator')
            self.__msg_success()
        else:
            self.__msg_fileNotFound()
            return False

    def run(self):
        '''controller'''

        if self.parameters[0] in ['--help', '-h']:
            self.get_help()

        elif self.parameters[0] in ['--delete', '-d']:
            self.delete_backup()

        elif self.parameters[0] in ['--same', '-s']:
            if self.parameters[1]:
                return self.__run_trans(self.parameters[1])
            else:
                return self.__run_trans('en')

        elif self.parameters[0] in ['--all', '-a']:
            self.__run_trans_all()

        else:
            # input more than 1 parameter
            if self.parameters[1]:
                self.get_help()
            else:
                return self.__run_trans(self.parameters[0])


if __name__ == '__main__':
    argv = sys.argv + [None, None]
    case = Main(argv)
    case.run()
