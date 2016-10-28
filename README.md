# PlotFEKO README

FEKOの計算により吐き出されたoutファイルの処理を行うpythonスクリプト

__USAGE__

outファイルからデータを抜き出したgrpファイルを用意する。
まだ作成していない場合は`grepout.bat`を実行。
a-いずれの方法でも実行できる。

## a
`run_plothist.bat`をダブルクリック
"grpファイル名を入力してください。 >>>"と聞かれるのでファイル名(.grp)を入力

## b
コマンドライン上に`run_plothist.bat <ファイル名.grp>`と入力

## c
コマンドラインに`python plothist.py`と入力して
"grpファイル名を入力してください。 >>>"と聞かれるのでファイル名(.grp)を入力

## d
コマンドラインに`python plothist.py <ファイル名.grp>`と入力

## e
ipython上で`%run plothist <ファイル名.grp>`と入力

## f
ipython上で`%run plothist`と入力して
"grpファイル名を入力してください。 >>>"と聞かれるのでファイル名(.grp)を入力





## extract ver1.0

__USAGE__
`import`して呼び出す。各関数の使い方はdoc参照。


__INTRODUCTION__
FEKOに計算させると吐き出される.outファイルの必要な情報を抽出するスクリプト
ACTIONに示す情報を抜き出して、csvファイルにまとめる



__ACTION__

### なにをするのか

.outファイルの以下のようなところを読み込む

```
       LOCATION           ETHETA              EPHI         scattering cross sect.            POLARISATION
   THETA    PHI      magn.    phase     magn.    phase        in m*m                     axial r. angle   direction
   90.00    3.00   4.698E-02  132.97  1.122E+00   29.34      1.58583E+01                 0.0407    90.57   RIGHT 

```



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

__UPDATE1.0__
* chu追加
* README修正

__UPDATE0.1__
First commit

__TODO__
None




### read_greped_text

`grep -A2 <search pattern> <infile> >> <outfile>`で抜き出して作成した<outfile>を引数としてpandas.read_tableで読み込む

引数:
    file: grepで抜き出したファイル名のフルパス(str型)
戻り値:
    df: 'theta', 'phi', 'rcs_w', 'rcs_d'を列にしたデータフレーム(pd.DataFrame型)















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



### merge

一つのデータフレームにまとめる
引数:
    ser_list: シリーズが入ったリスト(list of pd.Series type)
    nameargs: 作成されるdfのcolumn名が入ったリスト(list of string type)
戻り値:
    df: シリーズがマージされたデータフレーム(pd.DataFrame type)






### chu

df_inのcolumns_nameの列からlow以上high以下の値を示す部分を抽出する
引数:
    df_in: (pd.DataFrame type)
戻り値:
    df_out: 値が抽出されたデータフレーム(pd.DataFrame type)












__USAGE__
`run_plothist.bat`から呼び出すか
`python plotter.py`をコマンドラインで実行

__INTRODUCTION__
ヒストグラムを描画
細かい名前定義やグラフのラベルは作成しない

__ACTION__
`read_greped_text`で`.grp`ファイルを読み込み
driverでマージ



### plothist
ヒストグラムをplotする
引数:
    df:プロットするデータ(pd.core.frame.DataFrame)
戻り値:
    fig:サブプロット(matplotlib.axes._subplots.AxesSubplot)



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
