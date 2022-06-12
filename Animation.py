import simplegui
counter= 0
def draw_handler(canvas):
    global counter
    global x
    global y
    if (counter < 150):
        
        
        x= 12
        y= 450
        draw_caterpillar(canvas, x + counter, y)
        store(canvas)
        sun(canvas)
        hunger(canvas)
        
        
    
        counter=counter+ 2.0
        
    elif(counter < 180):
            draw_cashier(canvas,x+292, y-50)
            counter=counter+ 0.1
            draw_caterpillar(canvas,x + 50,y-23)
            hotdog_sign(canvas,x,y)
            draw_potatochip(canvas, x, y)
            
    elif(counter < 420):
            draw_cashier(canvas,x+292, y-50)
            counter=counter + 1.0
            draw_caterpillar(canvas,x + 50,y-23)
            draw_potatochip(canvas, x, y)
            draw_stealmess(canvas,x,y)
            Mr_Worldwide(canvas)
    elif(counter < 520):
            draw_cashier(canvas,x+292, y-50)
            counter=counter + 0.4
            draw_caterpillar(canvas,x + 50,y-23)
            draw_potatochip(canvas, x, y) 
            draw_roasted(canvas,x,y)
            Pebble_poster(canvas)
    
    
    elif(counter < 770):
        draw_caterpillar(canvas,x + 50,y-23)
        counter=counter + 1.0
        draw_potatochip(canvas, x, y) 
        Metaverse(canvas)
        Oh_no(canvas,x,y)
        Fire(canvas)
        sun(canvas)
        
    elif(counter < 970):
        draw_Psa(canvas)
        
     
        
            
            
    else:
        counter = 0
        
            
        
    
def draw_caterpillar(canvas, x, y):
    
    canvas.draw_circle((x + 30, y+ 15), 70, 100, "Green")
    canvas.draw_circle((x + 30, y+110), 51, 100, "Green")
    canvas.draw_circle((x + 35, y-70), 65, 100, "Green")
    canvas.draw_circle((x -40, y-100), 5, 10, "Black")
    canvas.draw_circle((x +110, y-100), 5, 10, "Black")
    
def sun(canvas):
    canvas.draw_circle((100, 1), 85, 170, "Yellow")
    
def store(canvas):   
    canvas.draw_text("Metaverse 7 Eleven", (280,200), 15, "White")
    canvas.draw_circle((375, 200), 100, 5, "Blue")
    canvas.draw_line((295,400),(500,400), 390,"Blue")
    
def hunger(canvas):
    canvas.draw_text("I am very hungry",(50,250),15,"Green")
    
    
def draw_cashier(canvas, x, y):
     canvas.draw_circle((400,300), 100, 25, "Brown")
     canvas.draw_line((x+112,y-60),(x+190,y+1150), 30,"Brown")
     canvas.draw_circle((440,270), 15, 15, "Blue")
     canvas.draw_circle((360,270), 15, 15, "Blue")
     
def hotdog_sign(canvas,x,y):
    canvas.draw_circle((200,25), 100, 15, "Blue")
    canvas.draw_text("New deal, Trade in your grandma for 2 hot dogs", (80,50), 15, "Aqua")
    canvas.draw_text("Hello sir, plese dont use our toilet it is a mess", (280,180), 15, "Brown")
   
    
def draw_potatochip(canvas, x, y):
    canvas.draw_circle((255,450), 90, 15, "Yellow")
    canvas.draw_text("Lae's", (250,420), 15, "Orange")
    canvas.draw_text("Bag of air(may contain potato chips)", (160,450), 15, "Orange")
    
def draw_stealmess(canvas,x,y):
    canvas.draw_text("I will steal this", (30,229), 15, "Green")
    canvas.draw_text("You can't its illegally bad to do that", (270,170), 15, "Brown")
    
    
def draw_roasted(canvas,x,y):
    canvas.draw_text("I will leave with the unpaid bag of air", (30,229), 15, "Green")
    canvas.draw_text("I will very slowly stop you.", (270,170), 15, "Brown")
    
   
def Metaverse(canvas):
    canvas.draw_text("Metaverse 7 Eleven", (380,200), 15, "White")
    canvas.draw_circle((500, 200), 100, 5, "Blue")
    canvas.draw_line((600,400),(500,455), 390,"Blue")
    
def Oh_no(canvas,x,y):
    canvas.draw_text("Wow, that was eas-, How did the store turn into lava ", (10,200), 15, "Green")
    
def Fire(canvas):
    canvas.draw_line((600,400),(500,455), 390,"Red")
    canvas.draw_circle((500, 400), 5, 10, "Black")
    canvas.draw_circle((500, 290), 5, 10, "Black")
    canvas.draw_circle((500, 270), 5, 10, "Black")
    canvas.draw_circle((500, 250), 5, 10, "Black")
    canvas.draw_circle((500, 450), 5, 10, "Black")
    canvas.draw_circle((510, 400), 5, 10, "Black")
    canvas.draw_circle((510, 275), 5, 10, "Black")
    canvas.draw_circle((520, 375), 5, 10, "Black")
    canvas.draw_circle((520, 425), 5, 10, "Black")
    canvas.draw_text("Glurp Snurp ",(450,300),15,"Orange")
    canvas.draw_text("Idk how to make ",(450,320),15,"Orange")
    canvas.draw_text("lava sounds ",(450,340),15,"Orange")
    
      
    
    
def Mr_Worldwide(canvas):
    canvas.draw_circle((200,25), 100, 15, "Blue")
    canvas.draw_text("Buy my EPIC mixtape for $19.00",(80,50),15,"Red")
    
    
    
def Pebble_poster(canvas):
    canvas.draw_circle((200,25), 100, 15, "Blue")
    canvas.draw_text("Play Two night at Ink Dinosaur for $49.99",(90,50),15,"Orange")
    
def draw_Psa(canvas):
   canvas.draw_text("THE END",(120,60),75,"Orange")
   canvas.draw_text("This is why you don't steal air from 11 seven",(150,200),15,"Orange")
    
frame = simplegui.create_frame("Testing", 600, 600)
frame.set_draw_handler(draw_handler)
frame.start()