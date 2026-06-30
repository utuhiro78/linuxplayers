---
title: Firefox の設定
date: 2026-06-30
---

## 最初に行うこと

### マウスホイールでタブを切り替える

about:config を開く。
「toolkit.tabbox.switchByScrolling」を検索。
右端の「切り替え」アイコンをクリックして「true」にする。

### ブックマークとパスワードをインポート

about:preferences#general を開く。
「データをインポート」をクリック。
「パスワード（CSV ファイルから）」を選んでインポート。
「ブックマーク（HTML ファイルから）」を選んでインポート。

### フォントを設定

about:preferences#general を開く。
「フォント」の詳細設定を開き、「日本語」「ラテン文字」「その他の表記体系」のフォントを設定。
私は次のようにしています。

```
プロポーショナル: ゴシック体, サイズ: 20
明朝体: Noto Sans CJK JP, サイズ: 20
ゴシック体: Noto Sans CJK JP, サイズ: 20
等幅: Noto Sans Mono CJK JP, サイズ: 20
最小フォントサイズ: 18
```

### ファイルの保存場所を毎回指定

about:preferences#general を開く。
「次のフォルダーに保存する」に書かれているフォルダーを変更。
「ファイルごとに保存先を指定する」にチェックをいれる。

### DRM 制御のコンテンツを再生

about:preferences#general を開く。
「DRM 制御のコンテンツを再生する」にチェックをいれる。
こうしないと TVer などが再生できない。

### 起動時のページを空白にする

about:preferences#home を開く。
次のように設定する。

```
ホームページと新しいウィンドウ: 空白ページ
新しいタブ: 空白ページ
```

### 内蔵翻訳ツールを自動で開かない

about:config を開く。
「browser.translations.automaticallyPopup」を検索。
右端の「切り替え」アイコンをクリックして「false」にする。

### 右クリックメニューの「AI チャットボットに尋ねる」を消す

about:config を開く。
「browser.ml.chat.menu」を検索。
右端の「切り替え」アイコンをクリックして「false」にする。

### 「現在全画面表示モードです」のメッセージを無効にする

about:config を開く。
「full-screen-api.warning.timeout」を検索。
右側の鉛筆アイコンをクリックして「0」にする。
右側の「✓」をクリック。

### ブックマークをミドルクリックで開いたあとにメニューを閉じない

about:config を開く。
「browser.bookmarks.openInTabClosesMenu」を検索。
右端の「切り替え」アイコンをクリックして「false」にする。

### 動画にカーソルを載せたとき PinP のアイコンを表示しない

about:preferences#general を開く。
「ピクチャーインピクチャーの動画の操作を有効にする」のチェックを外す。

### アドレスバーに入力候補を表示しない

about:preferences#search を開く。
「検索エンジンからの検索候補の表示方法を選択」のチェックをすべて外す。
「アドレスバーに表示する候補を選択」のチェックをすべて外す。

### Firefox の終了時に履歴を消去

about:preferences#privacy を開く。
「Firefox の終了時に履歴を消去する」にチェックをいれる。
右側の「設定」クリックして「Cookie とサイトデータ」以外にチェックをいれる。

### Mozilla へのデータ送信をやめる

about:preferences#privacy を開く。
「Firefox のデータ収集と利用について」のチェックをすべて外す。

### テーマを変更

[Google Chrome Light](https://addons.mozilla.org/ja/firefox/addon/google-chrome-light/)

## 拡張機能を追加

[Authenticator](https://addons.mozilla.org/ja/firefox/addon/auth-helper/)
[Close Left Tabs Button](https://addons.mozilla.org/ja/firefox/addon/close-left-tabs-button/)
[Close Other Tabs Button](https://addons.mozilla.org/ja/firefox/addon/close-other-tabs-btn/)
[Close Right Tabs Button](https://addons.mozilla.org/ja/firefox/addon/close-right-tabs-button/)
[Selection Search](https://addons.mozilla.org/ja/firefox/addon/selection-search-ff/)
[Cookie Whitelist](https://addons.mozilla.org/ja/firefox/addon/cookiewhitelist/)
[ShowPassword](https://addons.mozilla.org/ja/firefox/addon/471ae3f875c443e48e1f/)
[TWP - Translate Web Pages](https://addons.mozilla.org/ja/firefox/addon/traduzir-paginas-web/)
[uBlock Origin](https://addons.mozilla.org/ja/firefox/addon/ublock-origin/)
[コントロールパネル for YouTube](https://addons.mozilla.org/ja/firefox/addon/control-panel-for-youtube/)

## 検索エンジンを追加

about:preferences#search を開く。
「検索ショートカット」の「追加」をクリック。

検索エンジン | キーワード | URL（%s=検索語句）
--- | --- | ---
Google Ja | g | https://www.google.co.jp/search?q=%s
Google En | ge | https://www.google.co.jp/search?q=%s&hl=en&lr=lang_en
Amazon | a | https://www.amazon.co.jp/s?k=%s
ヨドバシ | yo | https://www.yodobashi.com/?word=%s
楽天 | r | https://search.rakuten.co.jp/search/mall/%s
ビック | b | https://www.biccamera.com/bc/category/?q=%s
TVer | t | https://tver.jp/search/%s
YouTube | y | https://www.youtube.com/results?search_query=%s
X | x | https://nitter.net/search?f=tweets&q=%s

## デフォルトの検索エンジンを変更

about:preferences#search を開く。
「既定の検索エンジン」を変更。

## ブックマークをエクスポート

ブラウザの右上にある「≡」をクリック。
「ブックマーク」をクリック。
一番下の「ブックマークを管理」をクリック。
「インポートとバックアップ」→「HTML としてエクスポート」を選択。

## パスワードをエクスポート

about:preferences#privacy を開く。
「保存されたパスワード」を選択。
画面右上の「⋯」をクリック→「パスワードをエクスポート」を選択。

[HOME](index.html)
