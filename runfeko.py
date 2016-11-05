"""
## runtime_scheduler ver1.0

__USAGE__
python runfeko.py <ファイル名の正規表現>

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
import sys
import pandas as pd
from time import sleep
import numpy as np


def countdown(n):
    """
    n秒待って、経過時間を進捗バーで表す
    """
    pbar = tqdm(np.arange(n))
    for _ in pbar:
        pbar.set_description('Now Waiting %dsec' % n)
        sleep(1)


def confirm(files: str) -> str:
    """
    実行ファイルの確認

    引数:
        files: globで探されたファイル名(str型)
    戻り値:
        inp:y -> True / n -> False(bool型)
    """
    for file in files:
        print(file)
    dic = {'y': True, 'yes': True, 'n': False, 'no': False}
    while True:  # 正しい値が入力されるまで繰り返し
        try:
            inp = dic[input('以上のファイルを実行します。よろしいですか？ y/n? >>>').lower()]
            break
        except:
            pass
        print('Error! Input again.')
    return inp


if __name__ == '__main__':
    # files = glob.glob('../*.dat')  # TESTcommand
    try:
        regex = sys.argv[1]
    except:
        regex = input('正規表現でファイル名を入力してください。>>> ')

    try:
        sleeptime = sys.argv[2]
    except:
        sleeptime = input('何秒後に実行？ / Enterで直ちに実行 >>> ')

    dafault_command = ['echo', 'foo']
    files = glob.glob(regex)
    count = 0

    if confirm(files):
        print('--\nyesが入力されました。処理を続行します。\n')
        if sleeptime:
            print('実行待ち...')
            countdown(float(sleeptime))
        for file in tqdm(files):
            count += 1
            print('実行サイクル: %d/%d' % (count, len(files)))

            ts = datetime.today()

            command = []  # 初期化
            command = dafault_command.copy()
            command.insert(1, file)
            print('実行コマンド: ', *command)
            sp.call(command)

            te = datetime.today()

            print('開始時刻: ', ts)
            print('終了時刻: ', te)
            print('実行時間: ', te - ts)
    else:
        print('--\nNoが入力されました。\n処理終了します。')
