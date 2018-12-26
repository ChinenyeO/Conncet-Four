import random
import sys





class board:
    def __init__(self , rows , column , empty_or_nah):
        self.board = []

        self.rows = rows

        self.column = column

        self.empty_or_nah = empty_or_nah

        self.faller = None

        self.new_game_board()


        






    def set_board(self,board):
        self.board = board
        


    def displayboard(self):
        for row in range(len(self.board)):
            
            print('|', end = '')
            line = ''
            
            for col in range(len(self.board[0])):
                line += self.board[row][col]
                
            line += '|'
            print(line)
            
        print( '', '_' * (len(self.board[0])* 3) , end = '')

        print('\n')



        


        
    def horizontal_match(self):
        count = 0
        result = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])-2):
                count+=1
                if self.board[row][col] == self.board[row][col+1] and self.board[row][col+1] == self.board[row][col+2]:
                    # append to list

                    start = self.board[row][col] 
                    self.board[row][col] = '  '
                    self.board[row][col + 1] = '   '
                    self.board[row][col + 2] = '   '

                    for var in range(col + 3 , len(self.board[0])):
                        if start == self.board[row][var]:
                            self.board[row][var] = '   '
                        else:
                            break
##
###                   
        return self.board
    def vertical_match(self):
        for row in range(len(self.board)-2):
            for col in range(len(self.board[0])):
                if self.board[row][col] == self.board[row+1][col] and self.board[row+1][col] == self.board[row+2][col]:

                    start = self.board[row][col]
                    self.board[row][col] = '   '
                    self.board[row+1][col] = '   '
                    self.board[row+2][col] = '   '

                    for var in range(row + 3 , len(self.board)):
                        if start == self.board[row][var]:
                            self.board[row][var] == '   '
                        else:
                            break
                                    
        return self.board


        
        


    def new_game_board(self):
        for row in range(self.rows):
            self.board.append([])
            for col in range(self.column):
                self.board[row].append('   ')

        return self.board
    

    

    def getboard(self):
        return self.board()

    def exit(self):
        sys.exit()

##    def set_faller(self,jewel1,jewel2,jewel3 , col_num):
##        self.faller = faller(jewel1,jewel2,jewel3,col_num)
##
####    def fall(self , jewel1, jewel2 , jewel3 , col_num , board):
####        board[
        


class faller:
    
    def __init__(self,jewel_list, col_num):
        ''' initializes all jewels '''


        self.jewel_list = jewel_list
      

        self.col_num = col_num

        self.row_num = 0

        self.land = False

        self.frozen = False

        self.next_turn_land = False

##    def frozen(self , board):
##        frozen = False
##        
##        if self.row_num == -1:
##            frozen = True 
##            


    def drop(self, board):
        '''drops color down row'''

       
            
        
        

        if self.row_num == 0:
            board.board[self.row_num][self.col_num-1] = '[' + self.jewel_list[-1] + ']'


        elif self.land == True: 
            board.board[self.row_num ][self.col_num-1] = ' ' + self.jewel_list[-1] + ' '
            board.board[self.row_num -1][self.col_num-1] = ' ' +self.jewel_list[-2] + ' '
            board.board[self.row_num -2][self.col_num-1] = ' ' + self.jewel_list[0] + ' '
            
            

            self.land = False
            self.frozen = True
            
        elif self.frozen == True:
            pass

       
        elif self.row_num == 1 and board.board[self.row_num+1][self.col_num-1][1] != ' ':
            self.land = True 
            board.board[self.row_num][self.col_num-1] = '|'+ self.jewel_list[-1] + '|'
            board.board[self.row_num -1][self.col_num-1] = '|' + self.jewel_list[-2] + '|'

            raise GameOverError()




        elif self.row_num == 1:
            board.board[self.row_num][self.col_num-1] = '['+ self.jewel_list[-1] + ']'
            board.board[self.row_num -1][self.col_num-1] = '[' + self.jewel_list[-2] + ']'

     
        elif self.row_num == 2 and board.board[self.row_num+1][self.col_num-1][1] != ' ':
            self.land = True 
            
            board.board[self.row_num][self.col_num-1] = '|' + self.jewel_list[-1] + '|'
            

            board.board[self.row_num -1][self.col_num-1] = '|' + self.jewel_list[-2] + '|'

            board.board[self.row_num -2][self.col_num-1] = '|'+ self.jewel_list[0] + '|'


        elif self.row_num == 2:
            board.board[self.row_num][self.col_num-1] = '[' + self.jewel_list[-1] + ']'

            board.board[self.row_num -1][self.col_num-1] = '[' + self.jewel_list[-2] + ']'

            board.board[self.row_num -2][self.col_num-1] = '['+ self.jewel_list[0] + ']'

       
        elif self.row_num == len(board.board) - 1 or board.board[self.row_num+1][self.col_num-1][1] != ' ':

            
            self.land = True
            board.board[self.row_num][self.col_num-1] = '|'  + self.jewel_list[-1] + '|'

            board.board[self.row_num -1][self.col_num-1] = '|' + self.jewel_list[-2] + '|'

            board.board[self.row_num -2][self.col_num-1] = '|' +self.jewel_list[0] + '|'

            board.board[self.row_num -3][self.col_num-1] = '   '

            
         


        elif self.row_num != len(board.board):

            

            print('x' , board.board[self.row_num+1][self.col_num][1])
            
            board.board[self.row_num][self.col_num-1] = '['  + self.jewel_list[-1] + ']'

            board.board[self.row_num -1][self.col_num-1] = '[' + self.jewel_list[-2] + ']'

            board.board[self.row_num -2][self.col_num-1] = '[' +self.jewel_list[0] + ']'

            board.board[self.row_num -3][self.col_num-1] = '   '

            if self.row_num == len(board.board)-1:
                self.next_turn_land = True

        ##
##    def dropped(self,board):
##
##        board.board[self.row_num ][self.col_num] = 

     
                  


            

     



                    
                




                    


                



                
        if self.land == False:
            self.row_num += 1 

        return board





        

        

        
                
        

    def rotate(self , board,jewel_list):
        ''' roates board'''
        if self.land == False:
            a = self.jewel_list[0]

            b = self.jewel_list[-1]

            c = self.jewel_list[-2]

            self.jewel_list[0] = c

            self.jewel_list[-1] = a

            self.jewel_list[-2] = b

##
##        board.board[self.row_num][self.col_num-1] == '['+ self.jewel_list[-2] + ']'
##
##        board.board[self.row_num -2][self.col_num-1] == '[' + self.jewel_list[-1] + ']'

        return board
        



    def move_right(self, board):
        ''' moves all col or right '''

        if self.land == False:

            
            board.board[self.row_num -3][self.col_num-1] = '   '


            board.board[self.row_num][self.col_num - 1] = '   ' 

                    
            board.board[self.row_num -1][self.col_num - 1] = '   '

            
            board.board[self.row_num -2][self.col_num - 1] = '   '
            


            self.col_num +=1

##            board.board[self.row_num][self.col_num] == '[' + self.jewel_list[-1] +  ']'


            
                

        return board
        

    def move_left(self, board):
        ''' moves a col to left '''
        if self.land == False:
            
            board.board[self.row_num -3][self.col_num - 1] = '   '


            board.board[self.row_num][self.col_num - 1] = '   ' 

                    
            board.board[self.row_num -1][self.col_num - 1 ] = '   '

            
            board.board[self.row_num -2][self.col_num - 1 ] = '   '
            
            self.col_num -=1

        return board




    
                
        

class color:
    def __init__(self,colors):
        self.colors = colors
        
class GameOverError(Exception):
    ''' raises gameover error'''
    pass
    

        
        
        

    
        
        
##        self.field() 
##
##    def faller(b:'board' , col_num:int , command :str):
##        num = int(col_num)
##        for row in range(rows):
##            b[row].extend(new_command)
##
##
##    def field():
##        results = []
##        if empty_or_nah == "EMPTY":
##            displayboard(b)
##            print('\n')
##
##        command = input()
##
##        if command[0] == 'F':
##            new_board = faller(b, command[1], command[3])
##            displayboard(new_board)
##            
##            
##            newboard = b[row][column].append(command[4])
##            displayboard(newboard)
##            
##            print(command[3])
##            print(command[2])
##        
##
##
##
##
##    def faller(b:'board' , col_num:int , command :str):
##        command = input()
##        new_command = '[' + command + ']'
##        
##        num = int(col_num) 
##        for row in range(rows):
##            b[row].extend(new_command)
####
##    def faller(b:board):
##        command = input()
##        
##        new_command = '[' + command + ']'
##
##        if command[0] == 'F':
##            new_board = faller(
##        
##        for row in range(rows):
##            b[row].append(new_command)
##        
##        
##
####                command = input()
####
####                if command[0] == 'F':
####                    new_board = faller(b, command[1], command[3])
####                    displayboard(new_board)
####
##            
##
####def field(b:'board'):
####    results = []
####
####    if empty_or_nah == "EMPTY":
####        displayboard(b)
####        print('\n')
####
####        command = input()
####
####        if command[0] == 'F':
####            new_board = faller(b, command[1], command[3])
####            displayboard(new_board)
####            
####            
######            newboard = b[row][column].append(command[4])
######            displayboard(newboard)
####            
######            print(command[3])
######            print(command[2])
####            
####
####        
####        
####
####
####
####    elif empty_or_nah == "CONTENTS":
####        for r in range(rows):
####            
####            cont = input()
####
####        if len(cont) == column:
####            results.append(cont)
####        return results
####
####
####    
####            
####            
####        
####                    
####
####
####
####def new_game_board()-> [[int]]:
####    ''' Creates a board'''
####   
####    
####    
####    board = []
####
####    
####    for row in range(rows):
####        board.append([])
####        for col in range(column):
####            board[row].append('   ')
####
####    return board
####
#### 
####def copy_game_board(b:'board'):
####    board_copy = []
####    for row in range(rows):
####        board_copy.append([])
####        for col in range(column):
####            board_copy[-1].append(b[row][col])
####    return board
####
####def faller(b:'board' , col_num:int , command :str):
####    board_copy = []
####    new_command = '[' + command + ']'
####    num = int(col_num) 
####    for row in range(rows):
####        b[row].extend(new_command)
####
####    
####    
####    return b
####            
####
####
####
##def displayboard(b:'board'):
##    ''' print board '''
##    for row in range(len(b)):
##        print('|', end = '')
##
##        line = ''
##
##        for col in range(len(b[0])):
##            line += b[row][col] 
##            
##        line += '|'
##        print(line)
##
##    print( '', '_' * (len(b[0])* 3) , end = '')
##
##
##
##
##
##        
##
##
##            
##        
##    
##    
##    
##
##def check_board(b:'board'):
##    print('\n')
##    command = input()
##
##    while True:
##        for rows in b:
##            for col in rows:
##                if col == '':
##                    continue
##                
##                elif col in command:
##                    try:
##                        b[row+1][col+1] in command
##                        print('HI')
##                    except:
##                        print('ERRORINOOOOOOOOOOOO')
##    
##
##
##




                
                    
                    
                



        







##def main():
##    new_board = board()
##   
##
##
##    
####    board = new_game_board()
####
####    field(board)
####
####
######    check_board(board)
####    
####    
##
##
##
##if __name__ == "__main__":
##    main()
