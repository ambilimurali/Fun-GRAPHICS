
import turtle


sc = turtle.Screen()    # screen  object
pen = turtle.Turtle()   # pen object

def draw():   #draw a square
    for i in range(4):  # total size of line
        pen.forward(30)  # 30 size
        pen.left(90) # 90- box shape 
    pen.forward(30)
    

if __name__ == "__main__" :
    sc.setup(600, 600)    # screen size (h,w)
    pen.speed(100)   #turtle object speed
    
    
    
    for i in range(8):
        pen.up()   # not ready to draw
        pen.setpos(0, 30 * i)   # set pos
        pen.down() # rdy to draw
        
        for j in range(8):   # set color
            if (i + j )% 2 == 0 :
                col = 'black'
            
            else :
                col = 'white'
            
            pen.fillcolor(col)
            pen.begin_fill()
            draw()
            pen.end_fill()
    pen.hideturtle()
            
                
    
   
    
        

    