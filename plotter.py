"""
## plotter.py ver1.0

__USAGE__
Just build

__INTRODUCTION__
csvデータをplotする
hoge.pngに図を保存する

__ACTION__
fileに指定したファイルから
pd.dateframeとしてロード
列方向は見たくないので全部を１カラムに表示(stack)
ヒストグラムとしてプロットする
.ipynbファイルのほうが対話形式で見やすいかも

__UPDATE--version--__
First commit

__TODO__
plotの日本語表示
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def loadfile(file):
    """
    データをロード
    １列にするときはdf.stack()
    引数:file:csv ファイルフルパス(str型)
    戻り値:(dataframe)
    """
    df = pd.read_csv(file, skiprows=1, index_col=0)
    dft = df.stack()  # columns(theta方向)を１列に表示
    return dft


def plot(dft):
    """plotする"""
    fig = dft.plot.hist(bins=50)  # ヒストグラムの本数を59本にする
    fig.set_xlabel('RCS[dB]')
    fig.set_ylabel('Count[times]')
    return fig


if __name__ == "__main__":
    file = './DATA/rcs_161022_04_0p1ind.outout'
    plot(loadfile(file))
    plt.savefig('./DATA/hoge.png')
