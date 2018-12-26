import Project4Input

rows = int(input())
column = int(input())
empty_or_nah = input()


##def get_rows():
##    rows = int(input())
##
##def get_column():
##    column = int(input())
##
##def get_empty_or_nah():
##    empty_or_nah = input()
##    6
##    
##
def main():
    new_board = Project4Input.board(rows, column , empty_or_nah)
##    jewels = None

    

    

    if empty_or_nah == 'CONTENTS':
        board = []
        for num_input in range(rows):
            row = []
            color = input()
            for char in color:
                a = ' ' + char + ' '
                row.append(a)
            board.append(row)
        new_board.set_board(board)               
                
        new_board.displayboard()

        while True:
            color = input().split()








            if len(color) == 0:
                
                new_board = jewels.drop(new_board)
                

                        
                

                
            elif color[0] == 'F':
                jewels = Project4Input.faller(color[2:], int(color[1]))
                new_board = jewels.drop(new_board)


            elif color[0] == 'Q':
                new_board.exit()
            
            elif color[0] == '>':
                new_board = jewels.move_right(new_board)
                new_board = jewels.drop(new_board)



            elif color[0] == '<':
                new_board = jewels.move_left(new_board)
                new_board = jewels.drop(new_board)


            elif color[0] == 'R':
                new_board = jewels.rotate(new_board,color)
                new_board = jewels.drop(new_board)



                if jewels.frozen == True:
                    new_board.horizontal_match()
                    new_board.vertical_match()
                    
                    new_board.diaganol_match()


            
        

    elif empty_or_nah == 'EMPTY':
        new_board.displayboard()

        
        while True:

            color = input().split()








            if len(color) == 0:
                
                new_board = jewels.drop(new_board)
##                new_board.displayboard()
                

                        
                

                
            elif color[0] == 'F':
                 #new_board.set_faller(color[4] , color[6] , color[8] ,color[2])
                jewels = Project4Input.faller(color[2:], int(color[1]))
                new_board = jewels.drop(new_board)


            elif color[0] == 'Q':
                new_board.exit()
##                    raise GameOverError()
            
            elif color[0] == '>':
                new_board = jewels.move_right(new_board)
                new_board = jewels.drop(new_board)

##                jewels = Project4Input.faller(color[2:], int(color[1]))
                
##                new_board.displayboard()

            elif color[0] == '<':
                new_board = jewels.move_left(new_board)
                new_board = jewels.drop(new_board)

##                jewels = Project4Input.faller(color[2:], int(color[1]))
                
##                new_board.displayboard()

            elif color[0] == 'R':
                new_board = jewels.rotate(new_board,color)
                new_board = jewels.drop(new_board)

##                jewels = Project4Input.faller(color[2:], int(color[1]))
                
##                new_board.displayboard()
##                
##            else:
##                if self.land == True:
##                    new_board.horizontal_match()
##                    new_board.vertical_match()
##                    new_board.diaganol_match()
##                        
##
                if jewels.frozen == True:
                    new_board.horizontal_match()
                    new_board.vertical_match()
                    


            
            new_board.displayboard()


                 

            

            
            









if __name__ == "__main__":
    main()
