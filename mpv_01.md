---
title: mpv の設定
date: 2026-09-21
---

## mpv の特徴

[mpv](https://mpv.io/) はフリーのメディアプレーヤーで、次の特徴がある。

- 高品質なビデオ出力（OpenGL, Vulkan）
- ビデオのハードウェアデコード
- オンスクリーンコントローラー（マウスを動かすと表示される）
- 活発に[開発中](https://github.com/mpv-player/mpv/commits/master)

## 基本設定

### mpv.conf を設定

~/.config/mpv/mpv.conf を作成して次の行を追加。

```
# ビデオ出力ドライバー
# https://mpv.io/manual/stable/#video-output-drivers
vo=gpu-next

# グラフィックスAPI
# https://mpv.io/manual/stable/#options-gpu-api
gpu-api=auto

# ハードウェアビデオデコードを有効にする
# https://mpv.io/manual/stable/#options-hwdec
hwdec=auto

# ハードウェアデコードを行うコーデック
# 「vainfo | grep AV1」を実行して、何も表示されない場合は「av1,」を削除。
# https://mpv.io/manual/stable/#options-hwdec-codecs
hwdec-codecs=h264,vc1,hevc,vp8,vp9,prores,prores_raw,ffv1,dpx
```

```
# アップスケーラー
# https://mpv.io/manual/stable/#options-scale
scale=lanczos

# ダウンスケーラー
# https://mpv.io/manual/stable/#options-dscale
dscale=lanczos
```

```
# オーディオ出力ドライバー
# https://mpv.io/manual/stable/#audio-output-drivers-ao
ao=pipewire
```

```
# 音声のみのファイルでもウィンドウを表示
# https://mpv.io/manual/stable/#options-force-window
force-window=yes

# ウィンドウを最大化
# https://mpv.io/manual/stable/#options-window-maximized
window-maximized=yes

# ターミナル出力の冗長性を減らす
# https://mpv.io/manual/stable/#options-quiet
quiet=yes

# ウィンドウ右下の「残り時間」を「全体時間」に変更
# https://mpv.io/manual/stable/#on-screen-controller-timetotal
script-opts=osc-timetotal=yes

# ウィンドウのタイトルバーに動画タイトルではなくファイル名を表示
# https://mpv.io/manual/stable/#options-title
title=${filename}

# プレイリストに動画タイトルではなくファイル名を表示
# https://mpv.io/manual/stable/#options-osd-playlist-entry
osd-playlist-entry=filename
```

### input.conf を設定

~/.config/mpv/input.conf を作成して次の行を追加。デフォルトは[こちら](https://github.com/mpv-player/mpv/blob/master/etc/input.conf)。

```
# 右クリックで一時停止しない
MBTN_RIGHT ignore

# マウスホイールで音量を変更しない
WHEEL_UP ignore
WHEEL_DOWN ignore

# チルトホイールで10秒移動しない
WHEEL_LEFT ignore
WHEEL_RIGHT ignore

# PGUP と PGDWN で10分移動
PGUP seek 600
PGDWN seek -600
```

```
# マウスの進むボタンと戻るボタンで次/前のファイルに移動
MBTN_FORWARD playlist-next;show-text ${playlist} 2000
MBTN_BACK playlist-prev;show-text ${playlist} 2000

# . と , で次/前のファイルに移動
. playlist-next;show-text ${playlist} 2000
, playlist-prev;show-text ${playlist} 2000

# \ と / で次/前のチャプターに移動
\ add chapter 1
/ add chapter -1
```

```
# i でファイル情報の表示をトグル
# I でファイル情報を一時的に表示
i script-binding stats/display-stats-toggle
I script-binding stats/display-stats

# Ctrl+d で再生中のファイルをゴミ箱に移動
Ctrl+d run gio trash "${path}"; playlist-remove current; show-text "\"${filename}\" をゴミ箱に移動しました" 5000

# Esc で終了
ESC quit
```

### モニターに超解像技術が搭載されている場合

モニターに超解像技術が搭載されている場合はオフにする。アップスケーラーの効果がわかりづらくなるので。
REGZA を使用している場合は次のようにする。

- 低遅延モード: オン (オフだと黒背景時の赤文字が滲む)
- レゾリューションプラス: オフ
- ヒストグラムバックライト制御: オン
- 質感リアライザー: オート (オフだと全体が白っぽくなる)

## 外部のアップスケーラーをインストール

複数のバリアントがある場合は、内蔵GPUでもコマ落ちしないよう、負荷が軽いものを選んだ。

### RAVU

Google の超解像技術から着想を得たアップスケーラー。
[https://github.com/bjin/mpv-prescalers](https://github.com/bjin/mpv-prescalers)

```
wget https://raw.githubusercontent.com/bjin/mpv-prescalers/refs/heads/master/compute/ravu-lite-ar-r3.hook
mkdir -p ~/.config/mpv/shaders
mv ravu-lite-ar-r3.hook ~/.config/mpv/shaders/
```

[compute](https://github.com/bjin/mpv-prescalers/tree/master/compute) ディレクトリのものが高速。動作しない場合は [gather](https://github.com/bjin/mpv-prescalers/tree/master/gather) か[ルート](https://github.com/bjin/mpv-prescalers/tree/master)のものを使用する。
ファイル名に「-ar」が付くものは、アンチリンギングフィルターが加えられている。リンギングとは、輪郭まわりなどに発生する[リング状のゴースト](https://en.wikipedia.org/wiki/Ringing_artifacts)のこと。

### Anime4K

1080pアニメのアップスケールに最適化されたアップスケーラー。
[https://github.com/bloc97/Anime4K](https://github.com/bloc97/Anime4K)

```
wget https://raw.githubusercontent.com/bloc97/Anime4K/refs/heads/master/glsl/Upscale/Anime4K_Upscale_CNN_x2_M.glsl
wget https://raw.githubusercontent.com/bloc97/Anime4K/refs/heads/master/glsl/Upscale/Anime4K_Upscale_CNN_x2_S.glsl
mv Anime4K_Upscale_CNN_x2_*.glsl ~/.config/mpv/shaders/
```

通常は複数のシェーダーを[組み合わせて](https://github.com/bloc97/Anime4K/tree/master/md/Template/GLSL_Mac_Linux_Low-end)使用するが、アニメに寄せ切ると実写映像が不自然になるので、ここでは「Anime4K_Upscale_Denoise_CNN_x2_M.glsl」のみを使用する。

### ACNetGLSL

Anime4KCPP プロジェクトで使用されている深層学習モデルを GLSL で実装したもの。
[https://github.com/TianZerL/ACNetGLSL](https://github.com/TianZerL/ACNetGLSL)

```
wget https://raw.githubusercontent.com/TianZerL/ACNetGLSL/refs/heads/master/glsl/acnet/acnet_f8b4.glsl
wget https://raw.githubusercontent.com/TianZerL/ACNetGLSL/refs/heads/master/glsl/acnet/acnet_f8b4_box_hdn.glsl
mv acnet_f8b4*.glsl ~/.config/mpv/shaders/
```

ファイル名に「-hdn」が付くものは、軽度のノイズ除去を行うようトレーニングされている。
ファイル名に「-box」が付くものは、ボックスフィルターで劣化させた画像を用いてトレーニングされている。線の復元に適しているが、若干ぼやけて見える場合がある。
ファイル名に「-box-hdn」が付くものは、「-box」をベースとして軽度のノイズ除去を行うようトレーニングされている。
無印のものはニュートラルにトレーニングされている。

### FSRCNNX

FSRCNN（高速超解像畳み込みニューラルネットワーク）を使用したアップスケーラー。
[https://github.com/igv/FSRCNN-TensorFlow](https://github.com/igv/FSRCNN-TensorFlow)

```
wget https://github.com/igv/FSRCNN-TensorFlow/releases/download/1.1/FSRCNNX_x2_8-0-4-1.glsl
mv FSRCNNX_x2_8-0-4-1.glsl ~/.config/mpv/shaders/
```

### ArtCNN

アニメコンテンツを対象としたアップスケーラー。
[https://github.com/Artoriuz/ArtCNN](https://github.com/Artoriuz/ArtCNN)

```
wget https://raw.githubusercontent.com/Artoriuz/ArtCNN/refs/heads/main/GLSL/ArtCNN_C4F16.glsl
wget https://raw.githubusercontent.com/Artoriuz/ArtCNN/refs/heads/main/GLSL/ArtCNN_C4F16_DN.glsl
wget https://raw.githubusercontent.com/Artoriuz/ArtCNN/refs/heads/main/GLSL/ArtCNN_C4F16_DS.glsl
mv ArtCNN_C4F*.glsl ~/.config/mpv/shaders/
```

ファイル名に「_DS」が付くものは、ノイズ除去とシャープ化を行うようトレーニングしている。
ファイル名に「_DN」が付くものは、ノイズ除去とソフト化を行うようを行うようトレーニングしている。
無印のものはニュートラル。

## アップスケーラーの品質を測定

### 人物写真の場合

![](images/mpv/pexels-liam-anderson-411198-1458332_480.jpg)

Source: "[Shallow Focus Photography of Woman](https://www.pexels.com/photo/shallow-focus-photography-of-woman-1458332/)" by Liam Anderson
License: [https://www.pexels.com/ja-JP/license/](https://www.pexels.com/ja-JP/license/)

"[Shallow Focus Photography of Woman](https://www.pexels.com/photo/shallow-focus-photography-of-woman-1458332/)" をクリックして右上の「Free download」をクリック。

ダウンロードした画像を mpv でフルスクリーン表示。
縦長画像の場合は中央部分を最大限に使用する。余白が多いと品質の差が出にくい。

```
image_orig="pexels-liam-anderson-411198-1458332.jpg"
image_base="${image_orig%.*}"

mpv_options="--no-config --load-scripts=no --no-osc --scale=lanczos --screenshot-format=png --screenshot-dir=${PWD} -fs --pause"

mpv ${mpv_options} "${image_base}.jpg" --panscan=1.0 --glsl-shaders="" --screenshot-template="${image_base}_fullscreen"
```

画像が表示されたら「Ctrl+s」でスクリーンショットを撮り、「q」で終了する。
できた画像を「画像A」とする。

「画像A」を縦480にリサイズ。

```
image_orig="pexels-liam-anderson-411198-1458332.jpg"
image_base="${image_orig%.*}"

magick ${image_base}_fullscreen.png -resize x480 -quality 92 "${image_base}_480.jpg"
```

できた画像を「画像B」とする。
「画像B」は JPEG 形式にする。PNG 形式だとアップスケーラーが効かない場合があった。

「画像B」を mpv でフルスクリーンにアップスケール。縦横それぞれ2倍以上にしないと、アップスケーラーの違いが分かりづらい。

```
image_orig="pexels-liam-anderson-411198-1458332.jpg"
image_base="${image_orig%.*}"

mpv_options="--no-config --load-scripts=no --no-osc --scale=lanczos --screenshot-format=png --screenshot-dir=${PWD} -fs --pause"

for shader_file in ~/.config/mpv/shaders/*
do
  shader_base=$(basename "${shader_file}")
  shader_base=${shader_base%.*}
  mpv ${mpv_options} "${image_base}_480.jpg" --glsl-shaders="${shader_file}" --screenshot-template="${image_base}_480-${shader_base}"
done

mpv ${mpv_options} "${image_base}_480.jpg" --glsl-shaders="" --screenshot-template="${image_base}_480-lanczos"
```

画像が表示されたら「Ctrl+s」でスクリーンショットを撮り、「q」で終了する。
自動的に次の画像が表示されるので、同じことを繰り返す。
できた画像を「画像C」とする。

「画像A」と「画像C」の類似度を測定する。

```
image_orig="pexels-liam-anderson-411198-1458332.jpg"
image_base="${image_orig%.*}"

printf "File | Score\n"
printf "%s\n" "-- | --"

for image_file in ${image_base}_fullscreen.png ${image_base}_480-*.png
do
  score=$(magick compare -metric SSIM "${image_base}_fullscreen.png" "${image_file}" null: 2>&1)
  shader_name=${image_file#${image_base}_}
  shader_name=${shader_name#480-}
  shader_name=${shader_name%.*}
  printf "%s | %s\n" "${shader_name}" "${score}"
done | sort -t '|' -k 2 -g
```

### 結果 (低負荷バリアント)

スコアが小さいほど類似度が高い。ただし、100程度の差だと見た目はあまり変わらない。
人物写真の場合は全体のスコア差が小さく、デフォルトの lanczos も十分きれい。

File | Score
-- | --
fullscreen | 0 (0)
FSRCNNX_x2_8-0-4-1 | 1940.95 (0.029617)
acnet_f8b4 | 1950.33 (0.0297601)
acnet_f8b4_box | 1953.98 (0.0298159)
ArtCNN_C4F16 | 1968.67 (0.0300399)
Anime4K_Upscale_CNN_x2_S | 1977.57 (0.0301757)
acnet_f8b4_hdn | 1984.15 (0.0302762)
Anime4K_Upscale_CNN_x2_M | 2004.8 (0.0305913)
SSimSuperRes | 2005.16 (0.0305968)
acnet_f8b4_box_hdn | 2005.66 (0.0306044)
ravu-lite-ar-r3 | 2016.78 (0.0307741)
ArtCNN_C4F16_DS | 2024.89 (0.0308979)
lanczos | 2025.92 (0.0309136)
ArtCNN_C4F16_DN | 2189.47 (0.0334092)

### 結果 (高負荷バリアント)

スコアが小さいほど類似度が高い。ただし、100程度の差だと見た目はあまり変わらない。

File | Score
-- | --
fullscreen | 0 (0)
acnet_f8b18_hdn | 1905.7 (0.0290791)
FSRCNNX_x2_16-0-4-1 | 1927.04 (0.0294047)
acnet_f8b18 | 1939.93 (0.0296014)
ArtCNN_C4F32 | 1943.88 (0.0296618)
Anime4K_Upscale_CNN_x2_UL | 1989.07 (0.0303513)
ArtCNN_C4F32_DS | 2004.32 (0.0305839)
lanczos | 2025.92 (0.0309136)

### アニメ画像の場合

![](images/mpv/chihiro030_480.jpg)

Source: "[千と千尋の神隠し 作品静止画](https://www.ghibli.jp/works/chihiro/#frame)" by STUDIO GHIBLI
License: [画像は常識の範囲でご自由にお使いください。](https://www.ghibli.jp/works/chihiro/#frame)

人物写真のときと同じ方法で測定する。

### 結果 (低負荷バリアント)

スコアが小さいほど類似度が高い。ただし、100程度の差だと見た目はあまり変わらない。
人物写真のときよりアップスケーラーによる差が大きい。

File | Score
-- | --
fullscreen | 0 (0)
ArtCNN_C4F16_DS | 2377.32 (0.0362755)
acnet_f8b4_hdn | 2490.31 (0.0379996)
Anime4K_Upscale_CNN_x2_M | 2572.14 (0.0392484)
acnet_f8b4_box_hdn | 2616.02 (0.0399179)
Anime4K_Upscale_CNN_x2_S | 2745.35 (0.0418913)
acnet_f8b4 | 2812.43 (0.042915)
FSRCNNX_x2_8-0-4-1 | 2856.32 (0.0435847)
acnet_f8b4_box | 2902.71 (0.0442925)
ArtCNN_C4F16 | 2953.2 (0.045063)
ArtCNN_C4F16_DN | 2971.24 (0.0453383)
ravu-lite-ar-r3 | 3197.6 (0.0487923)
SSimSuperRes | 3292.46 (0.0502398)
lanczos | 3631.37 (0.0554111)

### 結果 (高負荷バリアント)

スコアが小さいほど類似度が高い。ただし、100程度の差だと見た目はあまり変わらない。

File | Score
-- | --
fullscreen | 0 (0)
ArtCNN_C4F32_DS | 2321.88 (0.0354297)
acnet_f8b18_hdn | 2424.86 (0.037001)
Anime4K_Upscale_CNN_x2_UL | 2464.49 (0.0376057)
FSRCNNX_x2_16-0-4-1 | 2698.8 (0.041181)
acnet_f8b18 | 2837.28 (0.0432941)
ArtCNN_C4F32 | 2914.45 (0.0444717)
lanczos | 3631.37 (0.0554111)

### デフォルトのアップスケーラーを設定

「acnet_f8b4_box_hdn」をデフォルトにする場合は、~/.config/mpv/mpv.conf に次の行を追加。
内蔵アップスケーラーのみを使用する場合は何も書かない。

```
# 外部アップスケーラー
# https://mpv.io/manual/stable/#options-glsl-shaders
glsl-shader="~~/shaders/acnet_f8b4_box_hdn.glsl"
```

### アップスケーラーにショートカットを割り当てる

~/.config/mpv/input.conf に次の行を追加。

```
# アップスケーラーの切り替え
Ctrl+1 change-list glsl-shaders set "~~/shaders/ravu-lite-ar-r3.hook"
Ctrl+2 change-list glsl-shaders set "~~/shaders/acnet_f8b4_hdn.glsl"
Ctrl+3 change-list glsl-shaders set "~~/shaders/acnet_f8b4_box_hdn.glsl"
Ctrl+4 change-list glsl-shaders set "~~/shaders/ArtCNN_C4F16_DN.glsl"
Ctrl+5 change-list glsl-shaders set "~~/shaders/ArtCNN_C4F16_DS.glsl"
Ctrl+6 change-list glsl-shaders set "~~/shaders/Anime4K_Upscale_CNN_x2_S.glsl"
Ctrl+7 change-list glsl-shaders set "~~/shaders/Anime4K_Upscale_CNN_x2_M.glsl"
Ctrl+8 change-list glsl-shaders set "~~/shaders/FSRCNNX_x2_8-0-4-1.glsl"
Ctrl+0 change-list glsl-shaders set ""; set scale lanczos
```

### アップスケーラーの違いを目視で確認する

人物写真を表示。

```
mpv https://utuhiro78.github.io/linuxplayers/images/mpv/pexels-liam-anderson-411198-1458332_480.jpg --no-osc --fs --pause
```

Ctrl キーを押したまま「0101」「0202」「1212」のように入力して、アップスケーラーをパラパラ漫画のように切り替える。画像の違いが見えやすくなる。

アニメ画像を表示。

```
mpv https://utuhiro78.github.io/linuxplayers/images/mpv/chihiro030_480.jpg --no-osc --fs --pause
```

同様にアップスケーラーをパラパラ漫画のように切り替える。

## アップスケーラーの速度を比較

![](images/mpv/12393381_3840_2160_60fps_480_01.jpg)

Source: "[Aerial view of a boat sailing in the sea](https://www.pexels.com/video/aerial-view-of-a-boat-sailing-in-the-sea-28478483/)" by Burak Evlivan
License: [https://www.pexels.com/ja-JP/license/](https://www.pexels.com/ja-JP/license/)

縦480にリサイズした動画をノーウェイトで全画面再生して、終了までの時間を計測する。

```
wget https://raw.githubusercontent.com/utuhiro78/linuxplayers/refs/heads/main/images/mpv/mpv_shader_benchmark.py

python mpv_shader_benchmark.py ~/.config/mpv/shaders/*
```

縦480へのリサイズは次のように行った。

```
for file in *.mp4
do
  ffmpeg -i "${file}" -vf scale=854:480:flags=lanczos "${file%.mp4}_480.mp4"
done
```

### 結果

GPUによって速度は変わる。
動画の収録時間は25秒なので、25秒以上かかるものはコマ落ちする。

| Upscaler | Time (sec) |
| --- | --- |
| lanczos | 3.32 |
| ravu-lite-ar-r3 | 6.31 |
| Anime4K_Upscale_CNN_x2_S | 7.52 |
| Anime4K_Upscale_CNN_x2_M | 9.22 |
| SSimSuperRes | 9.7 |
| acnet_f8b4_hdn | 11.32 |
| acnet_f8b4 | 11.34 |
| acnet_f8b4_box_hdn | 11.34 |
| acnet_f8b4_box | 11.36 |
| FSRCNNX_x2_8-0-4-1 | 12.52 |
| ArtCNN_C4F16 | 16.97 |
| ArtCNN_C4F16_DS | 17.01 |
| ArtCNN_C4F16_DN | 17.37 |

使用したシステム:

|||
| --- | --- |
| CPU | Ryzen 5 5600G |
| GPU | Integrated graphics |
| Monitor | 1920x1080 |

## シングル曲のピーク音量を 0 dB に揃える（ノーマライズ）

6分以内のファイルであれば自動的にノーマライズする。元のファイルは一切変更しない。
[normalize-short-tracks.lua](https://github.com/utuhiro78/linuxplayers/blob/main/images/mpv/normalize-short-tracks.lua)

```
wget https://raw.githubusercontent.com/utuhiro78/linuxplayers/refs/heads/main/images/mpv/normalize-short-tracks.lua
mkdir -p ~/.config/mpv/scripts
mv normalize-short-tracks.lua ~/.config/mpv/scripts/
```

事前にファイルのピーク音量を検出し、そこが 0 dB になるよう [volume-gain](https://mpv.io/manual/stable/#options-volume-gain) を調整してから再生する。
ピーク音量の検出には時間がかかるので、実行するのは6分以内のファイルのみ。6分あればほとんどのシングル曲をカバーできる。
ノーマライズの結果は画面左上に表示される。

[HOME](index.html)
