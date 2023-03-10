

#Hello world
robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}                              
      Defense: {head_defense}
      Energy consumption: {head_energy_consumption}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consumption}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consumption}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consumption}
\__/  _|||        |||_  \__/        
      | ||        || |          |4: {left_leg_name} 
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consumption}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consumption}
                                
"""

#print(robot_art)

class Part:

  def __init__(self, name, attack_level, defense_level, energy_consumptions):
    self.name=name
    self.attack_level=attack_level
    self.defense_level=defense_level
    self.energy_consumptions=energy_consumptions

  def get_status_dict(self):
    formatted_name=self.name.replace(" ","_").lower()
    return {
        "{}_name".format(formatted_name): self.name.upper(),
        "{}_status".format(formatted_name): self.is_available(),
        "{}_attack".format(formatted_name): self.attack_level,
        "{}_defense".format(formatted_name): self.defense_level,
        "{}_energy_consumption".format(formatted_name): self.energy_consumptions,
    }

  def is_available(self):
    return not self.defense_level <= 0

colors = {
    "black":'\x1b[90m',
    "blue":'\x1b[94m',
    "cyan":'\x1b[96m',
    "green":'\x1b[92m',
    "magenta":'\x1b[95m',
    "red":'\x1b[91m',
    "white":'\x1b[97m',
    "yellow":'\x1b[93m',
}


class Robot:
  def __init__(self, name, color_code):
    self.name=name
    self.color_code=color_code 
    self.energy=10 
    self.on=True  
    self.parts = [
        Part("Head", attack_level=5, defense_level=10, energy_consumptions=5 ),
        Part("Weapon", attack_level=15, defense_level=0, energy_consumptions=10),
        Part("Left_arm", attack_level=3, defense_level=20, energy_consumptions=10),
        Part("Right_arm", attack_level=6, defense_level=20, energy_consumptions=10),
        Part("Left_leg", attack_level=4, defense_level=20, energy_consumptions=15),
        Part("Right_leg", attack_level=8, defense_level=20, energy_consumptions=15),
    ]
    

  def greet(self):    
    print("Hello, my name is", self.name)
  
  def print_energy(self):
    print("We have", self.energy, "percent energy left")
  
  def attack(self, enemy_robot, part_to_use, part_to_attack):
    enemy_robot.parts[part_to_attack].defense_level -= self.parts[part_to_use].attack_level
    self.energy -= self.parts[part_to_use].energy_consumptions

  def is_no(self):
    return self.energy > 0 
  
  def is_there_available_parts(self):
    for part in self.parts:
      if part.is_available():
        return True
    return False

  def print_status(self):
    print(self.color_code)
    str_robot = robot_art.format(**self.get_part_status())
    self.greet()
    self.print_energy()
    print(str_robot)
    print(colors["black"])

  def get_part_status(self):
    part_status = {}
    for part in self.parts:
      status_dict = part.get_status_dict()
      part_status.update(status_dict)
    return part_status

def build_robot():
  robot_name=input("Robot name:  ")
  choose_color()
  color = input("Choose the color you want: ").lower()
  color_code = colors[color]
  robot = Robot(robot_name, color_code)
  robot.print_status()
  return robot

def choose_color():
  print(colors["black"] + "1). Black\n",
        colors["blue"] + "2). Blue\n",
        colors["cyan"] + "3). Cyan\n",
        colors["green"] + "4). Green\n",
        colors["magenta"] + "5). Magenta\n",
        colors["red"] + "6). Red\n",
        colors["black"] + "7). White\n",
        colors["yellow"] + "8).??Yellow\n",)

def play(): 
  playing = True
  print("Welcome to the game")
  print("Datas for player 1")
  robot_one = build_robot()
  print("Datas for player 2")
  robot_two = build_robot()
  rount = 0
  while playing:
    if rount % 2 == 0:
      current_robot = robot_one
      enemy_robot = robot_two
    else:
      current_robot = robot_two 
      enemy_robot = robot_one   
      
    
    current_robot.print_status()
    print("What part should I use to attack?")
    part_to_use = int(input("Chosse a number part: "))
    
    enemy_robot.print_status()
    print("Which part to the enemy should we attack?")
    part_to_attack = int(input("Chosse a enemy part to attack: "))
    
    
    current_robot.attack(enemy_robot, part_to_use, part_to_attack)
    rount += 1

    
    if (not enemy_robot.is_no()) or enemy_robot.is_there_available_parts() == False:
      playing=False
      print("Congratulation, you won")
      print(current_robot.name)

play()

