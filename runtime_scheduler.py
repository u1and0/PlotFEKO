"""
runfeko  file -np 16

を引数の数だけうけてbatch化
.preなければ警告
スケジュール機能
今から何時間後に実行、みたいな。
"""

import glob
import subprocess as sp
import os

files = glob.iglob('../*.dat')


print(os.getcwd())
for file in files:
    print(file)
    command = ['notepad']
    command.append(file)
    print(command)
    sp.call(command)
