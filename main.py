import pyxel

class Game:
  def __init__(self):
    # 画面サイズを 160x120 ピクセルに設定（レトロサイズ）
    pyxel.init(160, 120, title="4人のお悩み解決")

    # ゲームの状態管理
    self.current_room = "ROOM 1"
    self.has_item = False

    # マウス（タップ）を使えるようにする
    pyxel.mouse(True)

    # ゲームの実行（更新処理と描画処理を登録）
    pyxel.run(self.update, self.draw)

  def update(self):
    # もし画面が左クリック（またはタップ）されたら
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
      # クリックされた座標を取得
      mx = pyxel.mouse_x
      my = pyxel.mouse_y

      # 【例】画面の右側をタップしたら次の部屋へ
      if mx > 120:
        self.current_room = "ROOM 2"
      # 【例】画面中央の特定の場所をタップしたらアイテム取得
      elif 60 < mx < 100 and 50 < my < 80:
        self.has_item = True

  def draw(self):
    # 画面をクリア（0は黒、1は紺、7は白...16色から選ぶ）
    pyxel.cls(1)

    # 文字を表示（x座標, y座標, 文字, 色）
    pyxel.text(10, 10, f"ROOM: {self.current_room}", 7)
    pyxel.text(10, 25, f"ITEM: {'KEY' if self.has_item else 'NONE'}", 7)

    # 部屋のオブジェクトに見立てた四角形を描く（タップ用）
    pyxel.rect(60, 50, 40, 30, 9)  # 9はオレンジ色

Game()
