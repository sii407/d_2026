import pyxel

class Game:
  def __init__(self):
    # 画面サイズを 160x120 ピクセルに設定
    pyxel.init(160, 120, title="主人公（四角）が動くぞ！")

    # エラーの原因になるので、ドット絵ファイルの読み込みはしません！

    # 主人公の初期位置 (画面の真ん中あたり)
    self.player_x = 76
    self.player_y = 56
    self.player_speed = 2  # 移動するスピード

    # ゲームの開始
    pyxel.run(self.update, self.draw)

  def update(self):
    # 矢印キーが押されたら、その方向に座標をプラスマイナスする
    if pyxel.btn(pyxel.KEY_LEFT):
      self.player_x -= self.player_speed
    if pyxel.btn(pyxel.KEY_RIGHT):
      self.player_x += self.player_speed
    if pyxel.btn(pyxel.KEY_UP):
      self.player_y -= self.player_speed
    if pyxel.btn(pyxel.KEY_DOWN):
      self.player_y += self.player_speed

    # 主人公が画面の外に飛び出さないように引き留める処理
    self.player_x = pyxel.clamp(self.player_x, 0, pyxel.width - 8)
    self.player_y = pyxel.clamp(self.player_y, 0, pyxel.height - 8)

  def draw(self):
    # 画面を一度クリア（0番＝真っ黒にする）
    pyxel.cls(0)

    # 主人公の代わりに「オレンジ色の四角形」を描く！
    # (x座標, y座標, 横幅8px, 縦幅8px, 9番の色＝オレンジ)
    pyxel.rect(self.player_x, self.player_y, 8, 8, 9)

    # おまけ：画面の左上に今の座標を出す
    pyxel.text(5, 5, f"X:{self.player_x} Y:{self.player_y}", 7)

# ゲームの実行
Game()
