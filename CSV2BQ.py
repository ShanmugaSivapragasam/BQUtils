from os import listdir
from os import system
from os.path import isfile, join

dataset = "smartcs"


def upload_csvs():
    source_dir = "./output/"
    onlyfiles = [file for file in listdir(source_dir) if isfile(join(source_dir, file))]
    print(f' uploading total {len(onlyfiles)} to BQ')
    for file in onlyfiles:
        table = file[:-4]
        cmd = f'bq load --autodetect --source_format=CSV {dataset}.{table} {source_dir}{file}'
        print(cmd)
        system(cmd)


if __name__ == '__main__':
    upload_csvs()

# bq load --autodetect --source_format=CSV mydataset.mytable ./myfile.csv
