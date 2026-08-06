---
title: archinstall で Arch Linux をインストール
date: 2026-07-28
---

## archinstall とは

[archinstall](https://github.com/archlinux/archinstall) は Arch Linux のインストーラー。ガイドに沿って進めれば、簡単に Arch Linux をインストールできる。

## archinstall を日本語で使用

Arch Linux のISOファイルでは日本語を表示できないので、[EndeavourOS](endeavour_01.html) を使用する。

EndeavourOS を起動。

ブラウザで今見ているページを開く。

ターミナルを開いてウィンドウを最大化。ウィンドウが小さいと表示が崩れる。

次のコマンドを貼り付けて実行。

```
# Arch Linux の公式リポジトリのみを使用する
wget https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/raw/main/pacman.conf
sudo mv pacman.conf /etc/
sudo pacman -Sy

# keyring を更新
sudo pacman -S --needed archlinux-keyring

# 高速なダウンロードサーバを選択
sudo pacman -S --needed reflector rsync
sudo reflector -c jp -f 5 --save /etc/pacman.d/mirrorlist
sudo pacman -Sy

# archinstall をインストール
sudo pacman -S --needed archinstall

sudo archinstall
```

## 実行時の動画

![](images/archinstall/archinstall.mp4)

パーティションのサイズは次のようにしています。

| パーティション  | サイズ    | フォーマット | ファイルシステム |
| -------------- | --------- | ------------ | ---------------- |
| /boot          |  1024 MiB     | する         | fat32            |
| /              | 20480 MiB     | する         | ext4             |
| /home          | 残り全部  | しない       | ext4             |

「/boot」は基本的には [1024 MiB](https://wiki.archlinux.org/title/EFI_system_partition#Create_the_partition) で足りる。
「/」は余裕をもたせるなら 30720 MiB にする。
「/home」は初めて作成する場合のみフォーマット。

インストールが終わったら再起動して[設定を行う](arch_linux_01.html)。

[HOME](index.html)
