---
title: Arch Linux のインストール
date: 2026-10-01
---

## ダウンロード

[こちら](https://archlinux.org/download/)からISOファイルをダウンロード。

## Ventoy をUSBメモリにインストール

[こちら](https://github.com/ventoy/Ventoy/releases)から Ventoy をダウンロード。

USBメモリを差し込んでデバイスのパスを確認。

```
lsblk -p | grep disk

# /dev/sda           8:0    1 28.7G  0 disk 
# /dev/zram0       253:0    0    4G  0 disk [SWAP]
# /dev/nvme0n1     259:0    0  1.8T  0 disk 
```

ディスクのサイズから /dev/sda がUSBデバイスのパスだと判断。

Ventoy を /dev/sda にインストール。
Wayland ではGUI版を起動できないのでCUI版を使用する。
以下のコマンドでは無確認でフォーマットすることがないよう、パスを /dev/sdX にしている。

新規の場合（USBメモリがフォーマットされる）:

```
sudo sh Ventoy2Disk.sh -i /dev/sdX
```

アップデートの場合:

```
sudo sh Ventoy2Disk.sh -u /dev/sdX
```

## Arch Linux のISOファイルをUSBメモリにコピー

USBメモリに Arch Linux のISOファイルをコピー。
Arch Linux のインストールがうまくいかない場合に備えて、[Ubuntu](https://ubuntu.com/download/desktop) のISOファイルもコピーしておく。

## Arch Linux をシステムにインストール

PCの電源を入れ、ブートメニューキーを押す。
ブートメニューキーは次のとおり。

メーカー | ブートメニューキー
-- | --
ASUS | F8
ASRock | F11
GIGABYTE | F12
MSI | F11

ブートメニューキーを押したらUSBメモリを選択してEnter。
UEFIで CSM サポートを無効にしておくと、UEFIブートに対応していないデバイスが非表示になるので、選択が楽になる。

Ventoy のメニューが表示されたら Arch Linux のISOファイルを選択。

### インストーラーの日本語が文字化けしないようにする

Arch Linux が起動したら kmscon をインストール。Linux コンソールだと日本語が文字化けする。

```
localectl set-keymap jp106
pacman -Sy kmscon
kmscon
```

ログイン画面が表示されたら root と入力してEnter。

### インストーラーを実行

```
archinstall
```

![](images/archinstall/archinstall.mp4)

動画は次のコマンドで作成した。

```
wf-recorder -c h264_vaapi -d /dev/dri/renderD128 -p pix_fmt=nv12 \
  -r 30 -g "$(slurp)" -f archinstall.mp4
```

デフォルトのパーティションレイアウトは次の通り（ext4 を選択した場合）。

| パーティション  | サイズ    | フォーマット | ファイルシステム |
| -------------- | --------- | ------------ | ---------------- |
| /boot          |  1 GiB    | する         | fat32            |
| /              |  50 GiB   | する         | ext4             |
| /home          | 残り全部  | する         | ext4             |

インストールが終わったら再起動して[設定を行う](arch_linux_01.html)。

## 参考: 日本語表示に対応したISOファイルを作成

```
# archiso のプロファイル「releng」から「reljp」を作成
rm -rf reljp/
cp -r /usr/share/archiso/configs/releng/ reljp

# 日本語表示用のパッケージをISOファイルに追加
# 日本語フォントにはサイズが小さい otf-ipaexfont を使用
cat << 'EOF' >> reljp/packages.x86_64
kmscon
otf-ipaexfont
pango
EOF

sort -u reljp/packages.x86_64 -o reljp/packages.x86_64

# kmscon の設定ファイルを作成
# フォント名の調べ方は次の通り
# fc-scan --format "%{family}\n" /usr/share/fonts/OTF/ipaexg.ttf
mkdir -p reljp/airootfs/etc/kmscon/
cat << 'EOF' > reljp/airootfs/etc/kmscon/kmscon.conf
login=/usr/bin/bash --login
xkb-layout=jp
font-engine=pango
font-name="IPAexGothic"
font-size=20
EOF

# getty@tty1 をマスク
ln -sf /dev/null reljp/airootfs/etc/systemd/system/getty@tty1.service

# kmsconvt@tty1 を自動起動
mkdir -p reljp/airootfs/etc/systemd/system/getty.target.wants
ln -sf /usr/lib/systemd/system/kmsconvt@.service \
  reljp/airootfs/etc/systemd/system/getty.target.wants/kmsconvt@tty1.service

# ISOファイルを archiso-reljp/ に出力
rm -rf archiso-reljp/
mkarchiso -v -r -w /tmp/archiso-tmp -o archiso-reljp reljp
```

このISOファイルを使用すると、kmscon が自動的に起動する。
あとは archinstall で Arch Linux をインストール。

[HOME](index.html)
