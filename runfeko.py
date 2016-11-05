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
from datetime import datetime
from tqdm import tqdm

files = glob.glob('../*.dat')
default_command = ['echo', 'foo']
count = 0


for file in tqdm(files):
    count += 1
    print('実行サイクル: %d/%d' % (count, len(files)))
    ts = datetime.today()
    command = []
    command = default_command.copy()
    command.insert(1, file)
    print('実行コマンド: ', *command)
    sp.call(command)
    te = datetime.today()
    print('開始時刻: ', ts)
    print('終了時刻: ', te)
    print('実行時間: ', te - ts)
