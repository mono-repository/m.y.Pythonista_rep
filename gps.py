# -*- coding:utf-8 -*-
import ui, location, csv, datetime, time


def GetInfo():
    location.start_updates()  # GPSデータ更新を開始
    gps = location.get_location()  # GPSデータを取得する
    location.stop_updates()  # GPSデータ更新を終了

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 現時刻を取得
    gps_text = ""
    for g in gps:
        gps_text += str(g) + ":" + str(gps[g]) + "\n"  # GPSデータをテキストに変換
    return gps, gps_text, now


# NEWボタンをタップすると呼ばれるメソッド
def New(sender):
    label = sender.superview["label1"]

    # GetInfo からデータを取得
    gps, gps_text, now = GetInfo()

    # テキストデータがある場合は、それに追加する形で表示
    if label.text:
        pre_text = label.text
        label.text = pre_text + "\n" + now + "\n" + gps_text
    else:
        label.text = now + "\n" + gps_text

    # 3-1.GPSデータを編集して、csvファイルに保存
    gps_dict = {"time": now + ","}  # GPSデータはディクショナリ型
    gps_dict.update(gps)  # 取得時間とGPSデータをまとめる

    # 3-2.csvファイル用にヘッダー(ディクショナリ型)を作成
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
    # csvファイルを開いて、gps辞書を書き込む
    with open("gps_log.csv", mode="a", encoding="utf-8") as f:
        writer = csv.DictWriter(f, parameters, extrasaction="ignore")
        writer.writerows(gps_rows)


# 新たにGPSデータを取得し、既存のデータに追加して保存
def Add(sender):
    label = sender.superview["label1"]
    gps, gps_text, now = GetInfo()

    # 既存のデータを読み込む


# 保存していたCSVファイルを初期化
def Clear(sender):
    with open("gps_log.csv", mode="w", encoding="utf-8") as f:
        f.write("")
    # ラベルに初期化したことを表示
    sender.superview["label1"].text = ""
    show_alert(sender.superview, "データを初期化しました。")

    # # 5秒後にラベルを空白にする
    # ui.delay(lambda: label_update(sender), 10)

    # def label_update(sender):
    #     sender.superview["label1"].text = ""


def show_alert(view, message, duration=3):
    # ラベルを作成して画面の上に表示
    message_label = ui.Label(frame=(0, 0, view.width, 32))
    message_label.text = message
    message_label.alignment = ui.ALIGN_CENTER
    message_label.background_color = "lightgray"
    message_label.text_color = "black"

    # ラベルをviewに追加
    view.add_subview(message_label)

    # 指定された時間後にラベルを削除する
    ui.delay(lambda: view.remove_subview(message_label), duration)


# UIの読み込みと表示
v = ui.load_view("UI.pyui")
v.present("sheet")
