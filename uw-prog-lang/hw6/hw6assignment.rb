# University of Washington, Programming Languages, Homework 6, hw6runner.rb

# This is the only file you turn in, so do not modify the other files as
# part of your solution.

class MyPiece < Piece
  # The constant All_My_Pieces should be declared here
  All_My_Pieces = All_Pieces +
    [
      rotations([[0,0], [-1, 0], [1, 0], [-1, -1], [0, -1]]),
      [[[0,0],[1,0],[2,0],[-1,0],[-2,0]],
       [[0,0],[0,-1],[0,-2],[0,1],[0,2]]],
      rotations([[0,0], [1,0], [0,-1]])
    ]

  Cheating_Piece = [[[0,0]]]

  # your enhancements here
  def self.next_piece (board, use_cheating = false)
    # if mess up array dimension, 0[1] still works. Wired!!!
    piece = if use_cheating then Cheating_Piece else All_My_Pieces.sample end
    MyPiece.new(piece, board)
  end

  def self.all_my_pieces
    All_My_Pieces
  end
  def self.cheating_piece
    Cheating_Piece
  end
end

class MyBoard < Board
  # your enhancements here
  def initialize(game)
    super
    self.next_piece
    @cheating = false
  end

  def next_piece
    use_cheating = false
    if @cheating and @score >= 100
      @score -= 100
      use_cheating = true
    end
    @cheating = false # clear anyway.
    @current_block = MyPiece.next_piece(self, use_cheating)
    @current_pos = nil
  end

  def handle_cheating
    @cheating = true
  end

  def rotate_updown
    if !game_over? and @game.is_running?
      @current_block.move(0, 1, 2)
    end
    draw
  end

  def store_current
    locations = @current_block.current_rotation
    displacement = @current_block.position
    locations.size.times {|index|
      current = locations[index];
      @grid[current[1]+displacement[1]][current[0]+displacement[0]] =
      @current_pos[index]
    }
    remove_filled
    @delay = [@delay - 2, 80].max
  end
end

class MyTetris < Tetris
  # your enhancements here

  def initialize
    super
    @root.bind('u', proc { @board.rotate_updown })
    @root.bind('c', proc { @board.handle_cheating })
  end

  def set_board
    @canvas = TetrisCanvas.new
    @board = MyBoard.new(self)
    @canvas.place(@board.block_size * @board.num_rows + 3,
                  @board.block_size * @board.num_columns + 6, 24, 80)
    @board.draw
  end
end
