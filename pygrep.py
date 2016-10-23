"""
pythonで使えるgrep集
"""
import re
import glob


# def grep(file_name, search_pattern):
#     """
#     pythonで使えるgrep
#     1ファイルの中から検索パターンに適合した行数を抜き出す
#     """
#     with open(file_name, encoding="utf-8") as f:
#         line_number = 1
#         for line in f:
#             m = re.search(search_pattern, line)
#             if m:
#                 yield "%s,%d : %s" % (file_name, line_number, line.strip())
#             line_number = line_number + 1


def grep(search_pattern, file_name_pattern='./*'):
    """
    検索フォルダ内のすべてのファイルからサーチパターンに適合したファイル名と行数を抜き出す
    """
    for file_name in glob.iglob(file_name_pattern):
        try:
            with open(file_name, encoding='utf-8') as f:
                line_number = 1
                for line in f:
                    if re.search(search_pattern, line):
                        yield (file_name, line_number, line.strip())
                    line_number += 1
        except:
            continue




if __name__ == '__main__':
    file = './PlotFEKO/rcs_161022_03.out'
    dirr = './PlotFEKO/'
    dirr = './'
    se = "USAGE"
    for i in grep(se):
        print(*i, sep=':')
