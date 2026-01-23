---
title: CachyOS のインストール
date: 2025-12-05
---

## CachyOS とは

CachyOS は Arch Linux をベースにしたディストリビューション。
Calamares で簡単にインストールできる。
日本語フォントが入っているので文字化けしない。
オンラインインストールを行うので、最新の環境をすぐに使える。
CPUに応じて最適化されたパッケージを使用するので、性能が向上する。

## ダウンロード

[こちら](https://cachyos.org/download/)。

## Ventoy をUSBメモリにインストール

[Ventoy](https://github.com/ventoy/Ventoy/releases) はブータブルUSBドライブを作成するツール。Ventoy のインストール後にOSのISOファイルをUSBメモリにコピーすると、そのOSを起動できるようになる。複数のISOファイルをコピーして、起動するOSを選択することもできる。

ventoy-*-linux.tar.gz をダウンロードして展開。

USBメモリを差し込んで Ventoy のインストーラーを起動。

```
./VentoyGUI.x86_64
```

![](images/cachyos_01/cachyos_50.webp)

インストール先を必ず確認。
新規の場合は「Install」を選択。USBメモリ内のファイルはすべて消える。
アップデートの場合は「Update」を選択。USBメモリ内のファイルは維持される。

## CachyOS のISOファイルをUSBメモリにコピー

CachyOS のISOファイルをUSBメモリにコピーする。
[Kubuntu](https://kubuntu.org/getkubuntu/) などの利用者が多いOSのISOファイルもコピーしておく。CachyOS のインストールが失敗したとき、別のOSのISOファイルがないと何もできなくなる。

## CachyOS をシステムにインストール

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

![](images/cachyos_01/cachyos_51.webp)
Ventoy のメニューでISOファイルを選択。
しばらく待つとデスクトップが起動する。

![](images/cachyos_01/cachyos_52.webp)
文字が小さいときは壁紙を右クリックして「Configure Display Settings...」を選択。

![](images/cachyos_01/cachyos_53.webp)
「Global scale」のスライダーを右に動かして「125%」にする。

![](images/cachyos_01/cachyos_01.webp)
「Launch installer」をクリック。

![](images/cachyos_01/cachyos_02.webp)
「Systemd-boot (Default)」をクリック。

![](images/cachyos_01/cachyos_04.webp)
ゾーンが「Tokyo」になっているのを確認。「次へ」をクリック。

![](images/cachyos_01/cachyos_05.webp)
キーボードモデルが「Japanese」になっているのを確認。

![](images/cachyos_01/cachyos_06.webp)
「手動パーティション」を選択。

![](images/cachyos_01/cachyos_07.webp)
パーティションを作成。
私は次のようにしています。余裕をもたせるなら「/」は 30000 MiB にする。

| パーティション  | サイズ    | フォーマット | ファイルシステム | フラグ    |
| -------------- | --------- | ------------ | ---------------- | --------- |
| /boot          | 2048 MiB  | する         | fat32            | boot      |
| /              | 20000 MiB | する         | ext4             | なし      |
| /home          | 残り全部  | しない       | ext4             | なし      |

「/home」は初めて作成する場合のみフォーマット。

![](images/cachyos_01/cachyos_08.webp)
/boot パーティションの編集例。

![](images/cachyos_01/cachyos_09.webp)
デスクトップを選択。

![](images/cachyos_01/cachyos_10.webp)
インストールするパッケージを選択。

![](images/cachyos_01/cachyos_11.webp)
ユーザー名とパスワードを設定。

![](images/cachyos_01/cachyos_12.webp)
内容を確認して「インストール」をクリック。

インストールが終わったら再起動して[設定を行う](arch_linux_01.html)。

[HOME](index.html)
