import pandas as pd
import argparse
import MySQLdb


def main(beacons_file, user, password):
    xls_beacons = pd.ExcelFile(beacons_file)
    beacons = pd.read_excel(xls_beacons)
    print(beacons)
    mysql_cn = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=user,
                               passwd=password,
                               db='beacons')

    sql = 'select * from fast_data order by id desc limit 1000;'
    beacons_information = pd.read_sql(sql, con=mysql_cn)
    print(beacons_information)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--beacons_file", type=str, help="excel file with a with columns mac and type", default="./beacons.xlsx")
    parser.add_argument("-u", "--user", type=str, help="mysql user", required=True)
    parser.add_argument("-p", "--password", type=str, help="mysql password", required=True)
    parser_args = parser.parse_args()
    main(parser_args.beacons_file, parser_args.user, parser_args.password)
