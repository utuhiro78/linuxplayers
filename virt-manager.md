---
title: virt-manager の使い方
date: 2026-02-08
---

## AMD-V が有効になっているか確認

```
LC_ALL=C lscpu | grep Virtualization
```

「Virtualization: AMD-V」と表示されればOK。

何も表示されないときは BIOS で AMD-V を有効にする。
GIGABYTE 製マザーボードの場合は次のように行う。

1. 「Tweaker」タブを選択

1. 「Advanced CPU Settings」をクリック

1. 「SVM Mode」を「Enabled」にする

## virt-manager と qemu をインストール

```
yay -S --needed virt-manager qemu-full
```

## ファイアウォールのバックエンドを変更

バックエンドを変更しないと[ネットに接続できなかった](https://bbs.archlinux.org/viewtopic.php?id=296590)。

```
cp /etc/libvirt/network.conf network.conf

sed -i -e 's,#firewall_backend\ =\ "nftables",firewall_backend\ =\ "iptables",g' network.conf

sudo mv network.conf /etc/libvirt/network.conf

sudo systemctl start iptables

# システム起動時に実行する場合
sudo systemctl enable iptables
```

## libvirtd を実行

```
sudo systemctl start libvirtd

# システム起動時に実行する場合
sudo systemctl enable libvirtd
```

## virt-manager を実行

```
sudo virt-manager
```

1. 「ファイル」→「接続を追加」をクリック
![](images/virt/virt_01.webp)

1. ハイパーバイザーを選択
「QEMU/KVM」を選択し、「接続」をクリック
![](images/virt/virt_02.webp)

1. 新しい仮想マシンを作成
メイン画面の「QEMU/KVM」を右クリックして「新規」を選択
![](images/virt/virt_03.webp)

1. 「オペレーティングシステムのインストール方法」を選択
「ローカルのインストールメディア（ISO イメージまたは CD-ROM ドライブ）」を選択。
![](images/virt/virt_04.webp)

1. ISO ファイルを指定
![](images/virt/virt_05.webp)

1. 「オペレーティングシステムの選択」に「何も検出されませんでした」と表示された場合
「インストールメディアまたはソースから自動検出」のチェックを外す。
検索ボックスに「generic」と入力し、「Generic Linux 2024」を選択。
![](images/virt/virt_06.webp)

1. メモリの使用量とCPUの個数を設定
「このホストでは n MiB まで使用できます」「最大 n 個まで利用できます」と表示されているので、最大数の半分を指定。
![](images/virt/virt_07.webp)

1. 仮想マシンのストレージを作成
「カスタムストレージの選択または作成」にチェックをいれて「管理」をクリック。
![](images/virt/virt_08.webp)

1. 左側の欄でホームディレクトリを選択し、「ボリューム」の右側にある「＋」をクリック
![](images/virt/virt_09.webp)

1. ストレージファイルの名前を設定
ここでは「EndeavourOS」にする。
![](images/virt/virt_10.webp)

1. qcow2 ファイルをストレージとして選択
![](images/virt/virt_11.webp)

1. 「次へ」をクリック
![](images/virt/virt_12.webp)

1. 仮想マシンの名前を設定
 ここでは「EndeavourOS」にする。
「完了」を押すと仮想マシンが起動する。
![](images/virt/virt_13.webp)

1. ブートローダー画面で OS を選択
![](images/virt/virt_14.webp)

1. 仮想マシンをシャットダウン
シャットダウンするときは左上の赤い電源ボタンをクリック。
インストールせずにシャットダウンした場合は、ストレージが空なので次回の起動では ISO ファイルの選択からやり直す。
![](images/virt/virt_15.webp)

## 仮想マシンを削除

virt-manager の「EndeavourOS」を右クリックして「削除」を選択。

[HOME](index.html)
