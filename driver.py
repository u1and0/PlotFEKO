"""
## driver.py ver1.0

__USAGE__
`import`して呼び出す。各関数の使い方はdoc参照。

__INTRODUCTION__
データ操作系の関数群

__ACTION__

* merge
    * 一つのデータフレームにまとめる
* chu
    * df_inのcolumns_nameの列からlow以上high以下の値を示す部分を抽出する





__UPDATE1.0__
First commit

__TODO__
None
"""

import pandas as pd
import numpy as np


def merge(ser_list: list, nameargs: list) -> pd.core.frame.DataFrame:
    """
    一つのデータフレームにまとめる
    引数:
        ser_list: シリーズが入ったリスト(list of pd.Series type)
        nameargs: 作成されるdfのcolumn名が入ったリスト(list of string type)
    戻り値:
        df: シリーズがマージされたデータフレーム(pd.DataFrame type)
    """
    cc = pd.DataFrame(ser_list)
    df = cc.T
    df.columns = nameargs
    return df


def chu(df_in: pd.core.frame.DataFrame,
        columns_name: str,
        low: float,
        high: float) -> pd.core.frame.DataFrame:
    """
    df_inのcolumns_nameの列からlow以上high以下の
    値を示す部分を抽出する
    引数:
        df_in: (pd.DataFrame type)
    戻り値:
        df_out: 値が抽出されたデータフレーム(pd.DataFrame type)
    """
    a = df_in[df_in[columns_name] >= low]
    df_out = a[a[columns_name] <= high]
    return df_out


if __name__ == '__main__':
    ddd = pd.DataFrame(np.arange(10), columns=['go'])
    chu(ddd, 'go', 2, 4)  # 234のデータフレームが返る
    # ccc=pd.Series(np.arange(10), name='go')
    # chu(ccc, 'go', 2, 4)  # エラーが返る
    # aaa=np.arange(10)
    # chu(aaa, 'go', 2, 4)  # エラーが返る
