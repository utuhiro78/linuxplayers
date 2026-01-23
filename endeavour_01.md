---
title: EndeavourOS のインストール
date: 2025-12-11
---

## EndeavourOS とは

EndeavourOS は Arch Linux をベースにしたディストリビューション。
Calamares で簡単にインストールできる。
日本語フォントが入っているので文字化けしない。
オンラインインストールを選択できるので、最新の環境をすぐに使える。
CachyOS などと比べて[独自パッケージが少なく](https://github.com/endeavouros-team/repo/tree/master/endeavouros/x86_64)、純正のArch Linuxに近い。

## ダウンロード

[こちら](https://endeavouros.com/)。

## Ventoy をUSBメモリにインストール

[Ventoy](https://github.com/ventoy/Ventoy/releases) はブータブルUSBドライブを作成するツール。Ventoy のインストール後にOSのISOファイルをUSBメモリにコピーすると、そのOSを起動できるようになる。複数のISOファイルをコピーして、起動するOSを選択することもできる。

ventoy-*-linux.tar.gz をダウンロードして展開。

USBメモリを差し込んで Ventoy のインストーラーを起動。

```
./VentoyGUI.x86_64
```

![](images/endeavour_01/endeavour_50.webp)

インストール先を必ず確認。
新規の場合は「Install」を選択。USBメモリ内のファイルはすべて消える。
アップデートの場合は「Update」を選択。USBメモリ内のファイルは維持される。

## EndeavourOS のISOファイルをUSBメモリにコピー

EndeavourOS のISOファイルをUSBメモリにコピーする。
[Kubuntu](https://kubuntu.org/getkubuntu/) などの利用者が多いOSのISOファイルもコピーしておく。EndeavourOS のインストールが失敗したとき、別のOSのISOファイルがないと何もできなくなる。

## EndeavourOS をシステムにインストール

USBメモリを挿してPCの電源を入れ、ブートメニューキーを押す。
ブートメニューキーは次のとおり。

メーカー | ブートメニューキー
-- | --
ASUS | F8
ASRock | F11
GIGABYTE | F12
MSI | F11

ブートメニューキーを押すとブートデバイスの選択画面が出る。
あらかじめUEFIで「CSM Support」を無効にしておくと、UEFIブートに対応していないデバイスが非表示になるので、選択が楽になる。

![](images/endeavour_01/endeavour_51.webp)
Ventoy のメニューでISOファイルを選択。
しばらく待つとデスクトップが起動する。

![](images/endeavour_01/endeavour_01.webp)
文字が小さいときは壁紙を右クリックして「Configure Display Settings...」を選択。

![](images/endeavour_01/endeavour_02.webp)
「Global scale」のスライダーを右に動かして「125%」にする。

![](images/endeavour_01/endeavour_04.webp)
左上の「Start the installer」をクリック。

![](images/endeavour_01/endeavour_05.webp)
インストール方法は「Online」を選択。最新のパッケージをネットからダウンロードしてインストールする。「Offline」を選択するとKDEデスクトップしか選べないし、インストール後のシステムアップデートが膨大になる。

![](images/endeavour_01/endeavour_06.webp)
「日本語」が選択されているのを確認して「次へ」をクリック。

![](images/endeavour_01/endeavour_07.webp)
「Tokyo」が選択されているのを確認。

![](images/endeavour_01/endeavour_08.webp)
キーボードモデルを選択。

![](images/endeavour_01/endeavour_09.webp)
デスクトップを選択。

![](images/endeavour_01/endeavour_10.webp)
インストールするパッケージを選択。

![](images/endeavour_01/endeavour_11.webp)
ブートローダーを選択。デフォルトは systemd-boot 。

![](images/endeavour_01/endeavour_12.webp)
「手動パーティション」を選択。

![](images/endeavour_01/endeavour_13.webp)
パーティションを作成。
私は次のようにしています。余裕をもたせるなら「/」は 30000 MiB にする。

| パーティション  | サイズ    | フォーマット | ファイルシステム | フラグ    |
| -------------- | --------- | ------------ | ---------------- | --------- |
| /efi           | 2048 MiB  | する         | fat32            | boot      |
| /              | 20000 MiB | する         | ext4             | なし      |
| /home          | 残り全部  | しない       | ext4             | なし      |

「/home」は初めて作成する場合のみフォーマット。

![](images/endeavour_01/endeavour_14.webp)
/efi パーティションの編集例。

![](images/endeavour_01/endeavour_15.webp)
ユーザー名とパスワードを設定。

![](images/endeavour_01/endeavour_16.webp)
内容を確認して「インストール」をクリック。

インストールが終わったら再起動して[設定を行う](arch_linux_01.html)。

[HOME](index.html)
