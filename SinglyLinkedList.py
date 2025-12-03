import pygame
from button_template import Button
import Colors

class Node:
    def __init__(self, data, pos, next=None):
        # Logical terms
        self.data = data
        self.next = next

        # UI terms
        self.shape = pygame.Rect(pos[0], pos[1], 70, 60)
        self.text = nodeFont.render(f"{data}",True,Colors.LIGHT_GREY)
    def draw(self, screen):
        pygame.draw.rect(screen,Colors.TEAL,self.shape)
        screen.blit(subFont.render("data: ", True, Colors.LIGHT_GREY),(self.shape.x, self.shape.y))
        screen.blit(self.text,(self.shape.x + 25, self.shape.y + 15))


# Initializing
pygame.init()

# Screen
screen = pygame.display.set_mode((900,700))
screen.fill(color=Colors.GREY)

# Font helper
def get_font(size):
    try:
        return pygame.font.Font("ScienceGothic-Regular.ttf", size)
    except:
        return pygame.font.SysFont('Arial', size)

# Font loaders
titleFont = get_font(28)
paraFont = get_font(17)
subFont = get_font(11)
nodeFont = get_font(22)

# Text rendering
title = titleFont.render("Singly Linked List", True, Colors.TEAL)
cap_value_txt = paraFont.render("Capacity (Max 6): ", True, Colors.LIGHT_GREY)
value_txt = paraFont.render("Value: ", True, Colors.LIGHT_GREY)

# Input Bar Class
class InputBar:
    def __init__(self,x,y,width,height,bg_color,max_chars=1):
        self.shape = pygame.Rect(x,y,width,height)
        self.bg_color = bg_color
        self.inactive_color = Colors.LIGHT_GREY
        self.active_color = Colors.TEAL
        self.color = self.inactive_color
        self.active = False
        self.text = ""
        self.max_chars = max_chars
        self.input_font = get_font(19)
        self.text_rendered = self.input_font.render(self.text,True,Colors.LIGHT_GREY)

    def handle_input(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.shape.collidepoint(event.pos)
            self.color = self.active_color if self.active else self.inactive_color

        if self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(self.text) > 0:
                self.text = self.text[:len(self.text) - 1]
            elif event.key == pygame.K_RETURN:
                pass
            else: # any other key
                if len(self.text) < self.max_chars:
                    self.text += str(event.unicode)

        self.text_rendered = self.input_font.render(self.text,True,Colors.LIGHT_GREY)

    def draw(self, screen):
        pygame.draw.rect(screen,self.bg_color,self.shape, border_radius=5)
        pygame.draw.rect(screen,self.color,self.shape,2, border_radius=5)
        screen.blit(self.text_rendered,(self.shape.x + 2,self.shape.y + 5))

# Text Input
cap_bar = InputBar(50,145,130,40,Colors.BLACK)
node_bar = InputBar(50,230,130,40,Colors.BLACK,4)

# Buttons
set_max_button = Button(190, 145, 120, 40, "Set Max", None, 18)
add_node_button = Button(190, 230, 120, 40, "Add Node", None, 18)
# delete_node_button = Button(50, 220, 140, 50, "Delete Node", None, 18)

# Linked Lists class
class SLL:
    def __init__(self, size, head=None):
        # Logical terms
        self.head = head
        self.size = size
        self.length = 0
        self.tail = None

        # UI terms
        self.initialPos = (90, 400)
        self.currentPos = self.initialPos
        self.nodes = [] # For drawing


    def addNode(self, data):
        if self.length > self.size:
            return
        newNode = Node(data,self.currentPos)

        # Empty List
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        self.currentPos = (self.currentPos[0] + 110, self.currentPos[1])
        self.nodes.append(newNode)

    def destroyList(self):
        temp = self.head
        while self.head is not None:
            temp = temp.next
            del self.head # Delete the Node
            self.head = temp
        self.nodes.clear()



# Main Loop
running = True
clock = pygame.time.Clock()
sll = SLL(6)
while running:
    # 1. CLEAR THE SCREEN FIRST
    screen.fill(Colors.GREY)

    # UI
    # Texts
    screen.blit(title, (50, 30))
    screen.blit(cap_value_txt, (50, 115))
    screen.blit(value_txt, (50, 200))
    # Buttons
    set_max_button.draw(screen)
    # delete_node_button.draw(screen)
    add_node_button.draw(screen)
    # Input Bars
    cap_bar.draw(screen)
    node_bar.draw(screen)
    # List
    for node in sll.nodes:
        node.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if add_node_button.is_clicked(event):
            if node_bar.text != "":
                sll.addNode(node_bar.text)

        if set_max_button.is_clicked(event):
            if set_max_button != "":
                sll.size = int(cap_bar.text)
                sll.destroyList()
        cap_bar.handle_input(event)
        node_bar.handle_input(event)



    pygame.display.update()
    clock.tick(60)