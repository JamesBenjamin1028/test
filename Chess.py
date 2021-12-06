white_pieces=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
white_start_position=["h7","g7","f7","e7","d7","c7","b7","a7","h8","g8","f8","e8","d8","c8","b8","a8"]
black_pieces=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
black_start_position=["h2","g2","f2","e2","d2","c2","b2","a2","h1","g1","f1","e1","d1","c1","b1","a1"]

def piece_decision():
    global white_start_position,black_start_position
    piece=input("What piece would you like to move:")
    start_position=input("What position is that piece:")
    end_position=input("What position would you like to move too:")
    piece_index=white_start_position.index(start_position.lower())
    return piece,start_position,end_position,piece_index

def pawn_move(piece):
    if piece.lower == "pawn":
        f

def piece_check(piece):
    pawn_move(piece)
    #bishop_move(piece)
    #rook_move(piece)
    #queen_move(piece)
    #king_move(piece)
    #knight_move(piece)

def main():
    piece,start_position,end_position,piece_index=piece_decision()
    piece_check(piece)
    print(piece_index)
main()