import pyxel

# 演習用のキャラクタークラス
class Character:
  def __init__(self, x, y, name):
    self.x = x
    self.y = y
    self.name = name
    self.problem_resolved = False

  def reset_problem(self):
    self.problem_resolved = False

# ゲームのメインクラス
class Game:
  def __init__(self):
    pyxel.init(160, 120, caption="Problem Solving Game")
    pyxel.load("assets.pyxres")  # アセットファイルの読み込み
    self.player_x = 80
    self.player_y = 60

    # キャラクターのリスト
    self.characters = [
        Character(30, 30, "Alice"),
        Character(130, 30, "Bob"),
        Character(30, 90, "Charlie"),
        Character(130, 90, "Daisy"),
    ]

    self.current_dialogue = ""
    self.wallpaper_acquired = False

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btn(pyxel.KEY_LEFT):
      self.player_x -= 1
    if pyxel.btn(pyxel.KEY_RIGHT):
      self.player_x += 1
    if pyxel.btn(pyxel.KEY_UP):
      self.player_y -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
      self.player_y += 1

    # タップでのアクション
    if pyxel.btnp(pyxel.KEY_SPACE):
      self.check_interaction()

  def check_interaction(self):
    for character in self.characters:
      if (self.player_x in range(character.x - 10, character.x + 10) and
              self.player_y in range(character.y - 10, character.y + 10)):
        if not character.problem_resolved:
          self.current_dialogue = f"{character.name}: \"Please help me find my lost item!\""
          # 問題を解決するロジックをここに追加する
          # 例えば、条件を満たすと:
          character.problem_resolved = True
          self.current_dialogue = f"{character.name}の問題を解決しました！"
          break
        else:
          self.current_dialogue = f"{character.name}: \"Thank you for your help!\""
          break

  def draw(self):
    pyxel.cls(0)

    # プレイヤーを描画
    pyxel.rect(self.player_x, self.player_y, 5, 5, 6)

    # キャラクターを描画
    for character in self.characters:
      pyxel.rect(character.x, character.y, 5, 5, 7)

    # ダイアログを描画
    pyxel.text(5, 5, self.current_dialogue, 8)

    # 壁紙取得のメッセージ
    if all(char.problem_resolved for char in self.characters) and not self.wallpaper_acquired:
      self.wallpaper_acquired = True
      pyxel.text(5, 15, "All problems solved! Wallpaper unlocked!", 10)


if __name__ == "__main__":
  Game()
