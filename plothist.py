"""
## plothist.py ver1.0
__USAGE__
`run_plothist.bat`から呼び出すか
`python plotter.py`をコマンドラインで実行

__INTRODUCTION__
ヒストグラムを描画
細かい名前定義やグラフのラベルは作成しない

__ACTION__
`read_greped_text`で`.grp`ファイルを読み込み
driverでマージ


### call_plothist
plothistを呼び出す。
コマンドラインなどでこのファイルを呼び出したとき実行
コマンドラインの引数がある -> 引数
コマンドラインの引数がない -> ファイル名を入力させる
`read_greped_text`でgrpファイルを読み込みdfに格納。
`plothist`でプロットする。


__UPDATE1.0__
First commit

__TODO__
None
"""

# __BUILT IN MODULES__________________________
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys
# __USER MODULES__________________________
import driver as dr
from extract import read_greped_text


def loadfile(file):
    """
    データをロード
    １列にするときはdf.stack()
    引数:file:csv ファイルフルパス(str型)
    戻り値:df (dataframe型)
    """
    df = pd.read_csv(file, skiprows=1, index_col=0)
    df = df.stack()  # columns(theta方向)を１列に表示
    return df


def plothist(df: pd.core.frame.DataFrame, title='histgram'):
    """ヒストグラムをplotする
    引数:
        df:プロットするデータ(pd.core.frame.DataFrame)
    戻り値:
        fig:サブプロット(matplotlib.axes._subplots.AxesSubplot)
    """
    fig = df.plot.hist(bins=50)  # ヒストグラムの本数を50本にする
    fig.set_xlabel('RCS[dB]')
    fig.set_ylabel('Count')
    fig.set_title(title)
    return fig


def fig():
    """まだ使えない"""
    # pm1用のデータを作成
    df_v3c_nallow = dr.chu(df_v3c, 'theta', 89, 91)
    df_unic_wo_mast_nallow = dr.chu(df_unic_wo_mast, 'theta', 89, 91)
    pd.merge(df_v3c_nallow, df_unic_wo_mast_nallow, on=[
             'theta', 'phi'], how='outer', suffixes=['v3', 'uni'])  # データの確認


def call_plothist():
    """
    plothistを呼び出す。
    コマンドラインなどでこのファイルを呼び出したとき実行
    コマンドラインの引数がある -> 引数
    コマンドラインの引数がない -> ファイル名を入力させる
    `read_greped_text`でgrpファイルを読み込みdfに格納。
    `plothist`でプロットする。
    """
    try:  # batchから引数としてファイル名受け取ったとき
        file = sys.argv[1]
    except IndexError:  # 引数がないとき(python shellからplothist.pyを実行したときなども含む)
        file = input('grpファイル名を入力してください。 >>> ').strip()  # 入力文字列の空白削除
    finally:
        print('%sにより%sをヒストグラム化します。' % (sys.argv[0], file))
        df = read_greped_text(file)  # データフレーム読み込み
        plothist(df['rcs_d'], file)  # ヒストグラムのプロット
        plt.show()


if __name__ == "__main__":
    call_plothist()
