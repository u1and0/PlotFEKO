"""
## extract ver0.1

__USAGE__
.outファイルの以下のようなところを読み込む

```
       LOCATION           ETHETA              EPHI         scattering cross sect.            POLARISATION
   THETA    PHI      magn.    phase     magn.    phase        in m*m                     axial r. angle   direction
   90.00    3.00   4.698E-02  132.97  1.122E+00   29.34      1.58583E+01                 0.0407    90.57   RIGHT 

```


__INTRODUCTION__
FEKOに計算させると吐き出される.outファイルの必要な情報を抽出するスクリプト
ACTIONに示す情報を抜き出して、csvファイルにまとめる

__ACTION__

### 抽出する情報

index : 第1要素
name : THETA
type : float型 0.00
unit : deg

index : 第2要素
name : PHI
type : float型 0.00
unit : deg

index : 第4要素
name : scattering cross sect.
type : 指数型 0.00000E+00
unit : dB

__UPDATE0.1__
First commit

__TODO__
None
"""

import re
# import pygrep as gr
# import subprocess as sp
import pandas as pd
import numpy as np


def extract(file):
    liner = []
    with open(file, 'r', encoding='utf_8') as f:
        liner += f.readlines()
    regex = re.compile('LOCATION')
    for regex in liner:
        print(liner)


def read_greped_text(file: str):
    """
    `grep -A2 <search pattern> <infile> >> <outfile>`
    で抜き出して作成した<outfile>を引数として
    pandas.read_tableで読み込む

    引数:
        file: grepで抜き出したファイル名のフルパス(str型)
    戻り値:
        df: 'THETA[deg]', 'PHI[deg]', 'RCS[W]', 'RCS[dBm]'を列にしたデータフレーム(pd.DataFrame型)
    """
    with open(file, 'r', encoding='utf-8') as f:
        ll = len(f.readlines())
    a = set(i for i in range(3, ll))
    b = set(i for i in range(6, ll, 4))
    skiprows = list(a - b)
    df = pd.read_table(file,
                       delim_whitespace=True,
                       header=1,
                       usecols=[0, 1, 6],
                       skiprows=skiprows,
                       names=['THETA[deg]', 'PHI[deg]', 'RCS[W]'])
    df['RCS[dBm]'] = 10 * np.log10(df['RCS[W]'])  # W -> dBm変換
    return df


def multi_read_greped_text(*files):
    dfs = pd.DataFrame('')
    for file in files:
        dfs[file] = read_greped_text(file)
    return dfs


if __name__ == '__main__':
    # infile = './rcs_161022_03.out'
    # outfile = infile[:-4] + '.outout'
    # search_pattern = 'LOCATION'
    # sp.check_output(['grep', '-A2', search_pattern, infile, '>> %s' % outfile])
    # with open(outfile, 'r', encoding='utf-8') as f:
    #     print(f.read())
    print(read_greped_text('./a.txt'))
