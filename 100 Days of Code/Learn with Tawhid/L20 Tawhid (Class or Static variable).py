class player:
    team_run = 0     #static or class variable
    def __init__(self,run):
        self.run = run  #instance variable
    def hit_four(self):
        self.run += 4
        player.team_run +=4
    def hit_six(self):
        self.run += 6
        player.team_run += 6
        
#==============================================

sakib = player(0)
sakib.hit_four()
sakib.hit_six()
tamim = player(0)
tamim.hit_six()
tamim.hit_four()
tamim.hit_four()
print("Sakib:",sakib.run)
print("Tamim:",tamim.run)
print("Tamim",tamim.__dict__)
print("Sakib",sakib.__dict__)
print("Team Run:",player.team_run)