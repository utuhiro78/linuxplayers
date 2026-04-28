---
title: archinstall で Arch Linux をインストール
date: 2026-04-28
---

## archinstall とは

[archinstall](https://github.com/archlinux/archinstall) は Arch Linux のインストーラー。ガイドに沿って進めれば、簡単に Arch Linux をインストールできる。

## archinstall を日本語で使用

Arch Linux のISOファイルでは日本語を表示できないので、[EndeavourOS](endeavour_01.html) を使用する。

EndeavourOS を起動。

ブラウザで今見ているページを開く。

ターミナルを開いてウィンドウを最大化。ウィンドウが小さいと archinstall の表示が崩れる。

次のコマンドを貼り付けて実行。

```
# Arch Linux の公式リポジトリのみを使用する
wget https://gitlab.archlinux.org/archlinux/packaging/\
packages/pacman/-/raw/main/pacman.conf
sudo mv pacman.conf /etc/
sudo pacman -Sy

# keyring を更新
sudo pacman -S --needed archlinux-keyring

# 高速なダウンロードサーバを選択。しばらく待つ
sudo pacman -S --needed reflector rsync
sudo reflector -c jp -f 5 --save /etc/pacman.d/mirrorlist
sudo pacman -Sy

# 必要なパッケージをインストール
sudo pacman -S --needed wget python python-sphinx_rtd_theme \
python-typing_extensions python-pydantic \
python-pydantic-core python-annotated-types python-cryptography \
python-pyparted python-textual

# archinstall の開発版をダウンロード
wget https://github.com/archlinux/archinstall/archive/\
refs/heads/master.zip -O archinstall-master.zip
bsdunzip archinstall-master.zip

# archinstall を実行
cd archinstall-master/
sudo python -m archinstall
```

## 実行時の動画

動画は vokoscreenNG で作成した。

![](images/archinstall/archinstall.mp4)

カーソルで移動。Enter で決定。「/」で選択肢を絞り込む。
例えば「/ja」と入力すれば、「ja」を含む選択肢が表示される。

パーティションのサイズは次のようにする。

| パーティション  | サイズ    | フォーマット | ファイルシステム |
| -------------- | --------- | ------------ | ---------------- |
| /boot          |  2048 MiB     | する         | fat32            |
| /              | 20480 MiB     | する         | ext4             |
| /home          | 残り全部  | しない       | ext4             |

「/」は余裕をもたせるなら 30720 MiB（30 GiB）にする。
「/home」は初めて作成する場合のみフォーマット。
「/boot」は複数のカーネルや Limine ブートローダー（Btrfs のスナップショットからの起動をサポート）を使用しないのであれば、1024 MiB で[足りる](https://wiki.archlinux.org/title/EFI_system_partition#Create_the_partition)。

インストールが終わったら再起動して[設定を行う](arch_linux_01.html)。

[HOME](index.html)
