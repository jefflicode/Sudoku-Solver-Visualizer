import pygame 

pygame.font.init() 

screen = pygame.display.set_mode((700, 850)) 

pygame.display.set_caption("Sudoku Solver - Backtracking Algorithm") 

grid = [ 
		[0, 0, 0, 0, 0, 0, 0, 7, 0], 
		[0, 7, 0, 0, 1, 0, 5, 9, 0], 
		[0, 8, 0, 3, 0, 2, 0, 1, 6], 
		[6, 5, 0, 4, 0, 9, 0, 0, 3], 
		[0, 0, 4, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 7, 6, 0, 0, 0, 0], 
		[9, 1, 0, 6, 0, 0, 0, 0, 0], 
		[0, 2, 7, 9, 0, 0, 0, 4, 0], 
		[4, 0, 5, 1, 0, 0, 0, 0, 0] 
	] 

x, y, val = 0, 0, 0
box = 700 / 9

font1 = pygame.font.SysFont("calibri", 45) 
font2 = pygame.font.SysFont("georgia", 23)  
		 
def draw(): 
	for i in range(2, 13): 
		if i == 5 or i == 8 or i == 11 or i == 2:
			pygame.draw.line(screen, (0, 0, 0), (0, i * box), (700, i * box), 4) 
		else:
			pygame.draw.line(screen, (0, 0, 0), (0, i * box), (700, i * box), 2) 

	for i in range(10):  
		if i % 3 == 0:
			pygame.draw.line(screen, (0, 0, 0), (i * box, box*2), (i * box, 850), 4)
		else:
			pygame.draw.line(screen, (0, 0, 0), (i * box, box*2), (i * box, 850), 2)

	for i in range (9): 
		for j in range (9): 
			if grid[i][j]!= 0: 
				text1 = font1.render(str(grid[i][j]), True, (0, 0, 0)) 
				screen.blit(text1, (j * box + 25, i * box + box * 2 + 25)) 

def solve(s):
	empty_box = find_empty(s)
	if empty_box:
		row, col = empty_box
	else:
		return True

	for num in range(1, 10):
		if check_valid(s, num, row, col):
			s[row][col] = num
			if solve(s):
				return True
			else:
				s[row][col] = 0
	return False

def highlight(i, j):
	pygame.draw.rect(screen, (51, 153, 255), (j * box+2, i * box + box*2+2, box - 1, box - 1))

def select(i, j): 			
	pygame.draw.rect(screen, (83, 198, 140), (j * box+2, i * box+2, box - 1, box - 1))	
	draw()

def instruction():
	text_color = (0, 0, 0)
	text1 = font2.render("Press E to empty the board", True, text_color)
	text2 = font2.render("Press D to set the board back to default", True, text_color)
	text3 = font2.render("Press RETURN to visualize the solving process", True, text_color)
	text4 = font2.render("Press SPACEBAR to instantly solve the sudoku", True, text_color) 
	text5 = font2.render("Feel free to empty the board and input a new sudoku! Have fun!", True, text_color) 
	screen.blit(text1, (0, 1))
	screen.blit(text2, (0, 25))
	screen.blit(text3, (0, 50))
	screen.blit(text4, (0, 75))
	screen.blit(text5, (0, 120))

def visualize(s):
    empty_box = find_empty(s)
    if empty_box:
        row, col = empty_box
    else:
    	return True
    pygame.event.pump()
    for num in range(1,10):
        if check_valid(s, num, row, col):
            s[row][col] = num  
            global x, y
            x = row
            y = col
            screen.fill((255, 255, 255))
            highlight(row, col)
            draw()
            instruction()
            pygame.display.update()
            pygame.time.delay(80) 
            if visualize(s):
                return True
            else:
            	s[row][col] = 0
			
            screen.fill((255, 255, 255))
            highlight(row, col)
            draw()
            instruction()
            pygame.display.update()
            pygame.time.delay(100) 
    return False

def locate(pos): 
	global x 
	x = pos[0]//box
	global y 
	y = pos[1]//box 

def check_valid(s, number, row, col):
	for i in range(9):
		if s[row][i] == number and col != i:
			return False
		if s[i][col] == number and row != i:
			return False

	row_position = row // 3
	col_position = col // 3
	for i in range(row_position * 3, row_position * 3 + 3):
		for j in range(col_position * 3, col_position * 3 + 3):
			if s[i][j] == number and (i, j) != (row, col):
				return False
	return True

def find_empty(s):
	for i in range(9):
		for j in range(9):
			if s[i][j] == 0:
				return (i, j)
	return None

loop = True
select_box = False

while loop: 
	screen.fill((255, 255, 255)) 		
	draw()  
	instruction()
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			loop = False
		if event.type == pygame.MOUSEBUTTONDOWN: 
			select_box = True 
			pos = pygame.mouse.get_pos() 
			locate(pos) 
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_LEFT: 
				x-= 1
				select_box = True
			if event.key == pygame.K_RIGHT: 
				x+= 1
				select_box = True
			if event.key == pygame.K_UP: 
				y-= 1
				select_box = True
			if event.key == pygame.K_DOWN: 
				y+= 1
				select_box = True	
			if event.key == pygame.K_1: 
				val = 1
			if event.key == pygame.K_2: 
				val = 2	
			if event.key == pygame.K_3: 
				val = 3
			if event.key == pygame.K_4: 
				val = 4
			if event.key == pygame.K_5: 
				val = 5
			if event.key == pygame.K_6: 
				val = 6
			if event.key == pygame.K_7: 
				val = 7
			if event.key == pygame.K_8: 
				val = 8
			if event.key == pygame.K_9: 
				val = 9
			if event.key == pygame.K_RETURN: 
				visualize(grid)
			if event.key == pygame.K_SPACE: 
				solve(grid)
			if event.key == pygame.K_e: 
				grid = [ 
						[0, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 0] 
					] 
			if event.key == pygame.K_d: 
				grid = [ 
						[0, 0, 0, 0, 0, 0, 0, 7, 0], 
						[0, 7, 0, 0, 1, 0, 5, 9, 0], 
						[0, 8, 0, 3, 0, 2, 0, 1, 6], 
						[6, 5, 0, 4, 0, 9, 0, 0, 3], 
						[0, 0, 4, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 7, 6, 0, 0, 0, 0], 
						[9, 1, 0, 6, 0, 0, 0, 0, 0], 
						[0, 2, 7, 9, 0, 0, 0, 4, 0], 
						[4, 0, 5, 1, 0, 0, 0, 0, 0] 
					] 
	if select_box:
		if 2 <= y <= 11:
			select(y, x)
	if val != 0:      
		grid[int(y) - 2][int(x)] = val
		val = 0  

	pygame.display.update() 

pygame.quit()	 