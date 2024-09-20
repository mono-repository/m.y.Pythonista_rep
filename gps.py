# -*- coding:utf-8 -*-
# location はGPSデータを取得する標準モジュールです
import ui, location, csv, datetime, time


# NEWボタンをタップすると呼ばれるメソッド
def shinki(sender):
    label = sender.superview["label1"]
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 現時刻を取得

    # 1.GPSデータを取得
    location.start_updates()  # GPSデータ更新を開始
    gps = location.get_location()  # GPSデータを取得する
    location.stop_updates()  # GPSデータ更新を終了

    # 2.GPSデータを画面に表示
    gps_text = ""
    for g in gps:
        gps_text = gps_text + str(g) + ":" + str(gps[g]) + "\n"
    label.text = now + "\n" + gps_text  # UIのテキストビューにGPSデータを代入

    # 3-1.GPSデータを編集して、csvファイルに保存
    gps_dict = {"time": now}  # GPSデータはディクショナリ型。
    gps_dict.update(gps)  # 先に取得時間を入れ、次にGPSデータを追加

    # 3-2.csvファイル用にヘッダー(ディクショナリ型)を作成
    gps_rows = []  # 空のリストを作成
    gps_rows.append(gps_dict)
    parameters = [
        "time",
        "latitude",
        "longitude",
        "altitude",
        "timestamp",
        "horizontal_accuracy",
        "vertical_accuracy",
        "speed",
        "course",
    ]
    header = dict([(val, val) for val in parameters])

    # csvファイルを開いて、gps辞書を書き込むshinki_button
    with open("gps_log.csv", mode="w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, parameters, extrasaction="ignore")
        writer.writerows(gps_rows)


v = ui.load_view("UI.pyui")
v.present("sheet")
