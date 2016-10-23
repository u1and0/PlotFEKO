"""
## extracy ver0.1

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


def extract(file):
    liner = []
    with open(file, 'r', encoding='utf_8') as f:
        liner += f.readlines()
    regex = re.compile('LOCATION')
    for regex in liner:
        print(liner)


if __name__ == '__main__':
    file = './rcs_161022_03.out'
    print(extract(file))
