##### VARIABLES ########
x = 0
y = 1  

game_over = False
new_high_score = None

pressed = ()
window = False 


# 2.1 colours 
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# 2.2 window
win_width = 600
win_height = 400

# 2.3 ball
radius = 20 
ball_vel = []# [random.randrange(2,4), random.randrange(1,3)]
#if random.randrange(0,2) == 0:
#    ball_vel[x] *= -1
#if random.randrange(0,2) == 0:
#    ball_vel[y] *= -1
ball_pos = []#= [win_width//2, win_height//2]
#set_ball( x_dir=(random.randrange(0,2) == 0) )
print(ball_vel)
print(ball_pos)  
# 2.4 paddles
pad_width = 40
pad_height = 120
pad1_vel = [0,0]
pad2_vel = [0,0]
pad1_pos = [0,                       win_height//2 - pad_height//2]
pad2_pos = [win_width - pad_width,   win_height//2 - pad_height//2] 

pad_pos = [pad1_pos, pad2_pos]
pad_vel = [pad1_vel, pad2_vel]

# 2.5 scores
l_score = 0
r_score = 0 

