from cmu_graphics import *

# Set background color
app.background = gradient('lightCyan', 'lavender')

# Draw head
Circle(200, 200, 200, fill='lightblue') 

# Draw shirt
Oval(200, 380, 240, 120, fill='black')
# Draw buttons on the shirt
for button_y in range(300, 400, 20):
    Circle(200, button_y, 5, fill='white')


# Draw hair background
Oval(200, 170, 230, 290, fill='black')

# Draw neck
Rect(175, 220, 40, 100, fill='brown')

# Draw face
Oval(200, 170, 180, 220, fill='brown')

# Pink Blush
Oval(250, 170, 5, 3, fill='pink')  # Left Blush
Oval(150, 170, 5, 3, fill='pink')  # Right Blush

# Wider Red Lips
Line(190, 270, 210, 270, lineWidth=10, fill='red')  # Top Lip
Line(195, 270, 205, 270, lineWidth=10, fill='red')  # Bottom Lip

# Larger Black Eyes
Oval(250, 150, 30, 20, fill='black')  # Left Eye
Oval(150, 150, 30, 20, fill='black')  # Right Eye






# Gold Earrings
Circle(110, 200, 5, fill='gold')  # Left Earring
Circle(290, 200, 5, fill='gold')  # Right Earring



# Draw additional circle at the side of the head
Circle(165, 10, 20, fill='black')
Circle(235, 10, 20, fill='black')


cmu_graphics.run()



