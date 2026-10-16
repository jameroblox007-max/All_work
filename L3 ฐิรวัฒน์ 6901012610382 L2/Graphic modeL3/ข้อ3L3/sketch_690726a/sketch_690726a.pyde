import random

screen_state = 0 

target_x = 0
target_y = 0
target_radius = 40  
score = 0
game_timer = 30     
current_time_left = 30 
start_time = 0      
cps_result = 0.0     

ripple_x = 0
ripple_y = 0
ripple_active = False
ripple_frame = 0
RIPPLE_DURATION = 20

active_input_box = 0 
input_string = "" 

def setup():
    size(1280, 720)
    rectMode(CENTER)
    noFill()
    strokeWeight(2)
    noCursor()
    textSize(32)
    respawn_target()

def draw():
    global screen_state, target_x, target_y, target_radius, score
    global ripple_active, ripple_frame, game_timer, current_time_left, start_time
    global active_input_box, input_string, cps_result
    
    background(0)

    if screen_state == 0:
        stroke(255)
        noFill()
        rect(width/2, 250, 200, 60)
        fill(255)
        textAlign(CENTER, CENTER)
        text("Start", width/2, 250)
        
        stroke(255)
        noFill()
        rect(width/2, 350, 200, 60)
        fill(255)
        text("Setting", width/2, 350)

    elif screen_state == 1:
        elapsed_time = (millis() - start_time) / 1000
        current_time_left = game_timer - elapsed_time
        
        if current_time_left <= 0:
            current_time_left = 0
            if game_timer > 0:
                cps_result = float(score) / game_timer
            else:
                cps_result = 0.0
            screen_state = 3
            
        if ripple_active:
            progress = ripple_frame / float(RIPPLE_DURATION)
            r = target_radius + progress * 60
            stroke(255 * (1 - progress))
            noFill()
            ellipse(ripple_x, ripple_y, r * 2, r * 2)
            ripple_frame += 1
            if ripple_frame >= RIPPLE_DURATION:
                ripple_active = False

        noStroke()
        fill(255, 0, 127)
        ellipse(target_x, target_y, target_radius * 2, target_radius * 2)

        fill(255)
        textAlign(LEFT, TOP)
        text("Score: " + str(score), 40, 40)
        text("Time: " + str(int(current_time_left)) + "s", 40, 80)
        
        stroke(255)
        noFill()
        rect(width - 100, 50, 140, 50)
        fill(255)
        textAlign(CENTER, CENTER)
        textSize(20)
        text("Back to Menu", width - 100, 50)
        textSize(32) 

    elif screen_state == 2:
        fill(255)
        textAlign(CENTER, CENTER)
        
        text("in timer (Click box & type number)", width/2, 180)
        stroke(255, 0, 127) if active_input_box == 1 else stroke(255)
        noFill()
        rect(width/2, 240, 300, 60)
        fill(255)
        if active_input_box == 1:
            text(input_string + "|", width/2, 240)
        else:
            text(str(game_timer) + " seconds", width/2, 240)
        
        fill(255)
        text("circle scale (Click box & type number)", width/2, 360)
        stroke(255, 0, 127) if active_input_box == 2 else stroke(255)
        noFill()
        rect(width/2, 420, 300, 60)
        fill(255)
        if active_input_box == 2:
            text(input_string + "|", width/2, 420)
        else:
            text("Radius: " + str(target_radius), width/2, 420)
        
        stroke(255)
        noFill()
        rect(width/2, 560, 200, 60)
        fill(255)
        text("Back", width/2, 560)

    elif screen_state == 3:
        fill(255)
        textAlign(CENTER, CENTER)
        
        textSize(48)
        text("GG", width/2, 220)
        
        textSize(32)
        text("your cps is", width/2, 300)
        
        stroke(255)
        noFill()
        rect(width/2, 370, 200, 60)
        fill(255)
        text(nf(cps_result, 0, 2), width/2, 370)
        
        stroke(255)
        noFill()
        rect(width/2, 500, 250, 60)
        fill(255)
        text("Main Menu", width/2, 500)

    noFill()
    if mousePressed:
        stroke(255, 0, 0) if mouseX < width / 2 else stroke(0, 0, 255)
    else:
        stroke(255)
    draw_positive(mouseX, mouseY, 10)

def mousePressed():
    global screen_state, target_x, target_y, target_radius, score
    global ripple_x, ripple_y, ripple_active, ripple_frame, start_time
    global active_input_box, input_string

    if screen_state == 0:
        if width/2 - 100 < mouseX < width/2 + 100 and 220 < mouseY < 280:
            score = 0 
            start_time = millis() 
            respawn_target() 
            screen_state = 1
        elif width/2 - 100 < mouseX < width/2 + 100 and 320 < mouseY < 380:
            screen_state = 2
            active_input_box = 0
            
    elif screen_state == 1:
        if width - 170 < mouseX < width - 30 and 25 < mouseY < 75:
            screen_state = 0
            return
            
        distance = dist(mouseX, mouseY, target_x, target_y)
        if distance < target_radius:
            score += 1
            ripple_x = target_x
            ripple_y = target_y
            ripple_active = True
            ripple_frame = 0
            respawn_target()

    elif screen_state == 2:
        if width/2 - 150 < mouseX < width/2 + 150 and 210 < mouseY < 270:
            active_input_box = 1
            input_string = "" 
        elif width/2 - 150 < mouseX < width/2 + 150 and 390 < mouseY < 450:
            active_input_box = 2
            input_string = "" 
        elif width/2 - 100 < mouseX < width/2 + 100 and 530 < mouseY < 590:
            screen_state = 0
            active_input_box = 0
        else:
            active_input_box = 0

    elif screen_state == 3:
        if width/2 - 125 < mouseX < width/2 + 125 and 470 < mouseY < 530:
            screen_state = 0

def keyPressed():
    global active_input_box, input_string, game_timer, target_radius
    
    if active_input_box > 0:
        if key == BACKSPACE:
            if len(input_string) > 0:
                input_string = input_string[:-1]
        elif key == ENTER or key == RETURN:
            if input_string != "" and input_string.isdigit():
                val = int(input_string)
                if val > 0:
                    if active_input_box == 1:
                        game_timer = val
                    elif active_input_box == 2:
                        target_radius = val
                        respawn_target()
            active_input_box = 0 
        elif str(key).isdigit():
            if len(input_string) < 3: 
                input_string += str(key)

def respawn_target():
    global target_x, target_y, target_radius
    target_x = random.randint(target_radius, width - target_radius)
    target_y = random.randint(150, height - target_radius)

def draw_square(x, y, size):
    rect(x, y, size, size)            

def draw_positive(x, y, size):        
    draw_square(x, y, size)           
    draw_square(x, y + size, size)    
    draw_square(x, y - size, size)    
    draw_square(x + size, y, size)    
    draw_square(x - size, y, size)
