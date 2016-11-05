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


def confirm(files:str) -> str:
    """
    実行ファイルの確認
    正しい値が入力されるまで繰り返し。

    引数:
        files: globで探されたファイル名(str型)
    戻り値:
        inp:y -> True / n -> False(bool型)
    """
    for file in files:
        print(file)
    dic = {'y': True, 'yes': True, 'n': False, 'no': False}
    while True:
        try:
            inp = dic[input('以上のファイルを実行します。よろしいですか？ y/n? >>>').lower()]
            break
        except:
            pass
        print('Error! Input again.')
    return inp


def excute(default_command:list, *files:str):
    """
    runfekoの実行

    引数: 
        dafault_command:(リスト型)
        dafault_files:ファイル名(str型)
    戻り値:なし
    """
    count = 0
    if confirm(files):
        print('--\nyesが入力されました。処理を続行します。\n')
        for file in tqdm(files):
            count += 1
            print('実行サイクル: %d/%d' % (count, len(files)))

            ts = datetime.today()

            command = []  # 初期化
            command = default_command.copy()
            command.insert(1, file)
            print('実行コマンド: ', *command)
            sp.call(command)

            te = datetime.today()

            print('開始時刻: ', ts)
            print('終了時刻: ', te)
            print('実行時間: ', te - ts)
    else:
        print('--\nNoが入力されました。\n処理終了します。')


if __name__ == '__main__':
    # files = glob.glob('../*.dat')  # TESTcommand
    files = glob.glob(input('正規表現でファイル名を入力してください。>>> '))
    command = ['echo', 'foo']
    excute(command, *files)
