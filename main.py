import pyxel

class Game:
  def __init__(self):
    # 画面サイズ
    pyxel.init(160, 120, title="主人公の実装")

    # 1. さっき作ったドット絵ファイルを読み込む（超重要！）
    pyxel.load("my_resource.pyxres")

    # 主人公の初期位置と速度
    self.player_x = 76  # 画面中央付近
    self.player_y = 56
    self.player_speed = 2

    # ゲームの実行
    pyxel.run(self.update, self.draw)

  def update(self):
    # 2. 矢印キー（方向キー）の入力を判定して、座標を更新する

    # 左 (Left)
    if pyxel.btn(pyxel.KEY_LEFT):
      self.player_x -= self.player_speed

    # 右 (Right)
    if pyxel.btn(pyxel.KEY_RIGHT):
      self.player_x += self.player_speed

    # 上 (Up)
    if pyxel.btn(pyxel.KEY_UP):
      self.player_y -= self.player_speed

    # 下 (Down)
    if pyxel.btn(pyxel.KEY_DOWN):
      self.player_y += self.player_speed

    # 画面外に出ないようにする処理（画面端で止める）
    # 画面の幅 (160) と主人公のドットサイズ (例: 8x8) を考慮します。
    self.player_x = pyxel.clamp(self.player_x, 0, pyxel.width - 8)
    self.player_y = pyxel.clamp(self.player_y, 0, pyxel.height - 8)

  def draw(self):
    # 画面をクリア（黒色で塗りつぶす）
    pyxel.cls(0)

    # 3. 主人公のドット絵を描画する
    # (描画するx, 描画するy, 画像番号, 画像内のx, 画像内のy, 幅, 高さ)
    # ※「Image 0」の「(0, 0)」から「8x8ピクセル」を切り出す例
    pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 8)

    # (オプション) 現在の座標を画面に表示する
    pyxel.text(5, 5, f"X:{self.player_x} Y:{self.player_y}", 7)

# ゲームの実行
Game()
