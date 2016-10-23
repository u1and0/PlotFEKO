"""
# pygrep.py ver1.0

__USAGE__
grep(<検索文字列(正規表現)>, [<検索対象ファイル(正規表現)>], <オプション>←未実装)

__INTRODUCTION__
pythonで使えるgrep集

__ACTION__
with openでファイル名を開く

検索フォルダ内のすべてのファイルからサーチパターンに適合したファイル名と行数を抜き出す
* 引数:
    * search_pattern:検索文字列(str型regex)
    * file_name_pattern:検索対象ファイルのフルパス(str型regex)
* 戻り値:
    * tupleをyieldする
        * file_name:検索文字列が見つかったファイル名
        * line_number:検索文字列が見つかった行数
        * line.strip()):検索文字列が含まれる列

__UPDATE1.0__
First commit

__TODO__
* オプション引数追加
    * p: 結果をprintする
    * A=<数字>: 結果の後<数字>行を返す
    * B=<数字>: 結果の前<数字>行を返す
    * C=<数字>: 結果の前後<数字>行を返す
"""
import re
import glob
import subprocess as sp
import doctest


def grep(search_pattern: str, file_name_pattern: str ='./*', *args, **kwargs) -> list:
    """
    検索フォルダ内のすべてのファイルからサーチパターンに適合したファイル名と行数を抜き出す

    * 引数:
        * search_pattern:検索文字列(str型regex)
        * file_name_pattern:検索対象ファイルのフルパス(str型regex)
        * __ここから未実装
        * args: 
        * kwargs:
            A=1:後(After)の1行を表示
            B=3:前(Before)の3行を表示
            C=4:前後の4行を表示
    * 戻り値:
        * tupleをreturnする
            * file_name:検索文字列が見つかったファイル名
            * line_number:検索文字列が見つかった行数
            * line:検索文字列が含まれる列
    """
    ret = []
    for file_name in glob.iglob(file_name_pattern):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                line_number = 1
                for line in f:
                    if re.search(search_pattern, line):
                        line_info = (file_name, line_number, line)
                    line_number += 1
                    ret += line_info
        except:
            continue
    else:
        if 'p' in args:
            print(*ret, sep=':')
        return ret


def igrep(search_pattern: str, file_name_pattern: str ='./*', *args) -> tuple:
    """
    検索フォルダ内のすべてのファイルからサーチパターンに適合したファイル名と行数を抜き出す
    * 引数:
        * search_pattern:検索文字列(str型regex)
        * file_name_pattern:検索対象ファイルのフルパス(str型regex)
    * 戻り値:
        * tupleをyieldする
            * file_name:検索文字列が見つかったファイル名
            * line_number:検索文字列が見つかった行数
            * line.strip()):検索文字列が含まれる列から改行\nを取り除いたもの

    TEST
    >>>for i in igrep('USAGE', './*','p'):
            >>> print(*i, sep=':')
    .\extract.py:4:__USAGE__
    .\plotter.py:4:__USAGE__
    .\pygrep.py:4:__USAGE__
    .\pygrep.py:99:for i in igrep('USAGE', './*','p'):
    .\pygrep.py:101:# grep('USAGE', './*')
    .\rcs_161022_03.out:2931:DATA FOR MEMORY USAGE
    .\README.md:5:__USAGE__
    .\README.md:53:__USAGE__
    """
    for file_name in glob.iglob(file_name_pattern):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                line_number = 1
                for line in f:
                    if re.search(search_pattern, line):
                        ret = (file_name, line_number, line.strip())
                        yield ret
                    line_number += 1
        except:
            continue


def osgrep(*args):
    one_string = sp.check_output(args).decode('utf-8')
    return one_string


if __name__ == '__main__':
    # doctest.testmod()

    # for i in igrep('USAGE', './*','p'):
    #     print(*i, sep=':')

    # print(grep('USAGE', './*'))  # カレントディレクトリ以下のすべてのファイルで'USAGE'を含むものすべて探索
    # print(grep('USAGE'))  # 第二引数のサーチファイルパターンはデフォルト引数なのでなくても走る
    # print(grep('USAGE', './*', 'p'))  # 第3引数のオプションにpが入るとprintする

    print(osgrep('grep', '-A2', 'LOCATION', '.out'))
