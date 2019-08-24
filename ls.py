# 模拟linux的ls命令

from pathlib import *
import sys
import stat
import argparse


# version 1.0
# if len(sys.argv) >1:
#     s_path = sys.argv[-1]
#
#     if s_path[0] == '-':
#         p = Path('.')
#     else:
#         p = Path(s_path)
# else:
#     p = Path('.')
# path_list = []
# stat_code = ''
# if len(sys.argv) > 1:
#     for opt in sys.argv[1:]:
#         if opt[0] == '-':
#             stat_code = opt
#         else:
#             p = Path(opt)
#             path_list.append(p)
#
# if not len(path_list):
#     p = Path('.')
#     path_list.append(p)
# mode_list = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
#
#
# def a_print(p):
#     s = ''
#     # if p.is_dir(): s += 'd'
#     # if p.is_file(): s += '-'
#     # if p.is_symlink(): s += '-'
#     # mode_code = oct(p.stat().st_mode)
#     # s += (mode_list[int(mode_code[-3])] + mode_list[int(mode_code[-2])] + mode_list[int(mode_code[-1])])
#     s += stat.filemode(p.stat().st_mode)
#     s += (' ' + str(p.stat().st_nlink)+ ' ' + p.owner() + ' ' + p.group() + ' ' + str(p.stat().st_size))
#     return s
#
#
# for p in path_list:
#     if p.is_dir():
#         for child in sorted(p.iterdir()):
#             if 'a' in stat_code:
#                 print(a_print(child) + ' ' + child.name)
#             else:
#                 print(child.name)
#     else:
#         if 'a' in stat_code:
#             print(a_print(p) + ' ' + p.name)
#         else:
#             print(p.name)


# version 2.0


def list_dir(path, all=False, detail=False):
    def _show_dir(path, all=False, detail=False):
        for item in path:
            p = Path(item)
            for file in p.iterdir():
                if not all and str(file.name).startswith('.'):
                    continue

                if detail:
                    st = file.stat()

                    yield '{} {:>2} {} {} {:>10} {}'.format(stat.filemode(st.st_mode), st.st_nlink, file.owner(),
                                                            file.group(), st.st_size, file.name)
                else:
                    yield '{}'.format(file.name)

    yield from sorted(_show_dir(path, all, detail), key=lambda x: x[-1])


parser = argparse.ArgumentParser(prog='test', add_help=False, description='just to Test')
parser.add_argument('-a', action='store_true', help='show all files that content hidden files')
parser.add_argument('-l', action='store_true', help='list display details')
parser.add_argument('-h', action='store_true')
# parser.add_argument('-al',action='store_true',help='-a and -l')
parser.add_argument('path', nargs='*', default='.', help='give  paths (file or diretory)')

if __name__ == '__main__':
    args = parser.parse_args()
    #    print(args.path)

    for st in list_dir(args.path, args.a, args.l):
        print(st)
