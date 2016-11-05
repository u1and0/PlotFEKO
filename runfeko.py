"""
## runtime_scheduler ver1.0

__USAGE__
python runfeko <ファイル名の正規表現>

__INTRODUCTION__
cmdに渡すコマンド
`runfeko <file> -np 16`
を作り出して、FEKOを実行する。

__ACTION__
globで正規表現に基づいたファイル名を
commandという変数に格納していく。
変数commnandにはあらかじめ`runtime <filename> -np 16`が指定されている。

__UPDATE1.0__
First commit

__TODO__
何時間後に実行するか指定する
"""

import glob
import subprocess as sp
import os

files = glob.iglob('../*.dat')
default_command = ['cat']

print(os.getcwd())
for file in files:
    print(file)
    command = default_command
    command.insert(1, file)
    print(command)
    sp.call(command)
