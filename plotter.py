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

# __BUILT IN MODULES__________________________
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# __USER MODULES__________________________
import driver as dr


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


def plot(dft, title):
    """plotする"""
    fig = dft.plot.hist(bins=50)  # ヒストグラムの本数を50本にする
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


if __name__ == "__main__":
    file = './DATA/rcs_161022_04_0p1ind.outout'
    plot(loadfile(file))
    plt.savefig('./DATA/hoge.png')
