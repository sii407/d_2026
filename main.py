import pyxel

class Game:
  def __init__(self):
    # 画面サイズ
    pyxel.init(160, 120, title="本物のキャラが動くぞ！")

    # ★さっきコピーした公式のドット絵ファイルを読み込む！
    pyxel.load("my_resource.pyxres")

    # 主人公の初期位置と速度
    self.player_x = 76
    self.player_y = 56
    self.player_speed = 2

    pyxel.run(self.update, self.draw)

  def update(self):
    # 矢印キーでの移動
    if pyxel.btn(pyxel.KEY_LEFT): self.player_x -= self.player_speed
    if pyxel.btn(pyxel.KEY_RIGHT): self.player_x += self.player_speed
    if pyxel.btn(pyxel.KEY_UP): self.player_y -= self.player_speed
    if pyxel.btn(pyxel.KEY_DOWN): self.player_y += self.player_speed

    self.player_x = pyxel.clamp(self.player_x, 0, pyxel.width - 8)
    self.player_y = pyxel.clamp(self.player_y, 0, pyxel.height - 8)

  def draw(self):
    # 画面をクリア（3番＝綺麗な黄緑色。草原っぽくなります！）
    pyxel.cls(3)

    # ★ここが重要！四角(rect)をやめて、ドット絵を描画(blt)します。
    # 公式素材の「Image 0」の「座標(0, 0)」にある「横8px、縦8px」のキャラ（可愛い白いキャラ）を呼び出す設定です。
    # 最後の「0」は、キャラの背景の黒色を透明にする魔法の数字です。
    pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 8, 0)

Game()
