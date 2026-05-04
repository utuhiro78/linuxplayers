---
title: LXQt + Wayland の設定
date: 2026-05-04
---

## LXQt をインストール

```
yay -S lxqt lxqt-wayland-session labwc
```

## Labwc を設定

### キーボードレイアウトを「jp」に変更

```
mousepad ~/.config/labwc/environment
```

「# XKB_DEFAULT_LAYOUT=se」を
「XKB_DEFAULT_LAYOUT=jp」に変更。

設定を反映させる。

```
labwc --reconfigure
```

### マウスカーソルのテーマを変更

```
mousepad ~/.config/labwc/environment
```

「# XCURSOR_THEME=」を
「XCURSOR_THEME=Future-cursors」に変更。
「# XCURSOR_SIZE=」を
「XCURSOR_SIZE=24」に変更。

### マウスホイールでウィンドウを上に出す

```
mousepad ~/.config/labwc/rc.xml
```

「\<context name=\"Client\"\>」の部分に次の行を追加。

```
      <mousebind direction="Up" action="Scroll">
        <action name="Focus" />
        <action name="Raise" />
      </mousebind>
      <mousebind direction="Down" action="Scroll">
        <action name="Focus" />
        <action name="Raise" />
      </mousebind>
```

### 中クリックでのテキスト貼り付けを有効にする

```
gsettings set org.gnome.desktop.interface gtk-enable-primary-paste true
```

### 音量変更のショートカットを設定

「lxqt-config-globalkeyshortcuts」は Wayland ではサポートされていない。

```
mousepad ~/.config/labwc/rc.xml
```

「Ctrl+PageUp」「Ctrl+PageDown」で音量を変更する場合は次のように設定。

```
    <keybind key="C-Next">
      <action name="Execute" command="lxqt-qdbus volume down" />
    </keybind>
    <keybind key="C-Prior">
      <action name="Execute" command="lxqt-qdbus volume up" />
    </keybind>
```

### Labwc のテーマを変更

Labwc では Openbox のテーマを利用できる。
インストール済みの Openbox テーマを確認。

```
ls /usr/share/themes/*/openbox-3/themerc
```

テーマを「Clearlooks」に変更する場合:

```
mousepad ~/.config/labwc/rc.xml
```

次のように変更する。

```
  <theme>
    <name>Clearlooks</name>
```

## その他の設定

### 「Noto Sans Mono CJK JP」を等幅フォントとして認識させる

LXQt では「Noto Sans Mono CJK JP」が等幅フォントとして[認識されない](https://github.com/notofonts/noto-fonts/issues/2393)。

```
mkdir -p ~/.config/fontconfig/conf.d
mousepad ~/.config/fontconfig/conf.d/70-noto-mono.conf
```

次の内容を貼り付けて保存。

```
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
    <match target="scan">
        <test name="family">
            <string>Noto Sans Mono CJK JP</string>
        </test>
        <edit name="spacing" mode="assign">
            <int>100</int>
        </edit>
    </match>
</fontconfig>
```

フォント情報のキャッシュを更新。

```
fc-cache -f -v
```

次のコマンドでフォントファイルが表示されるのを確認。

```
fc-list :spacing=100 | grep -i "Noto Sans Mono CJK JP:style=Regular"
```

### 時計の表示形式を設定

「形式を詳しく指定する」にチェックを入れて、
「MM月dd日 (ddd) HH:mm」と指定する。

### パネルの設定

幅: 38 ピクセル
アイコン: 36 ピクセル
場所: 画面上部

### LXQt セッションの設定

「セッション終了時に確認する」のチェックを外す。
「サスペンド/ハイバネートの前に画面をロックする」のチェックを外す。

### ファンシーメニューの設定

「カテゴリの位置」を「左」にする。

### パネルに CPU の温度と使用率を表示

「ウィジェットの管理」で「カスタムコマンド」を追加。
コマンドの内容は次のようにする。

```
python ~/get_cpu_usage_and_temp.py
```

get_cpu_usage_and_temp.py

```
#!/usr/bin/env python
# coding: utf-8

# Author: UTUMI Hirosi (utuhiro78 at yahoo dot co dot jp)
# License: Apache License, Version 2.0

import psutil


def main():
    cpu_temp = get_cpu_temperature()
    cpu_usage = get_cpu_usage()
    print(f'{cpu_temp} | {cpu_usage}')


def get_cpu_temperature():
    temps = psutil.sensors_temperatures()
    if not temps:
        return "N/A"

    for name, entries in temps.items():
        if name in ['k10temp', 'coretemp']:
            cpu_temp = entries[0].current
            break

    cpu_temp = round(float(cpu_temp))
    cpu_temp = f'{cpu_temp:2} °C'
    return cpu_temp


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1.0)
    cpu_usage = round(float(cpu_usage))
    cpu_usage = f'{cpu_usage:2} %'
    return cpu_usage


if __name__ == '__main__':
    main()
```

[HOME](index.html)
