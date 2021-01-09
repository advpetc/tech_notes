# Past Interview: Design a Minesweeper

> https://techdevguide.witgoogle.com/resources/coding-question-minesweeper/#code-challenge

## Problem Statement

Given a matrix:

```
0  0  0  0  0
0  0  0  0  0
1  1  1  0  0
1  9  1  0  0
1  2  2  1  0
0  1  9  1  0
0  1  1  1  0
```

where 9 indicates mine, 0 to 8 represents the number of mines in the 8 directions.

The game start with a matrix with all "-", and if player clicks any position that is 0, it will keep expanding until to all the boundary:

```
0  0  0  0  0 < clicked this point
0  0  0  0  0
1  1  1  0  0
-  -  1  0  0
-  -  2  1  0
-  -  -  1  0
-  -  -  1  0
```

You are given a `Matrix` class:

```c
template<typename T> 
class Matrix { 
  void resize(int rows, int cols); 
  T& at(int row, int col); 
  int rows(); 
  int cols(); 
}; 
```

Your task is to design the play function.

## Analysis

1. construct the initial matrix: to start with the initial configuration, we need some considerations for the number of mines `m` and the matrix size `n`.
  1. An important part of this question is figuring out a way to place the mines. The most naive implementation is to pick two random numbers (row and column) and place a mine there, but this will cause the board to have less mines than expected if the same coordinates are picked twice. Re-trying if the picked coordinates already have a mine fixes the immediate problem, but will take a very long time for cases such as a 100x100 board with 9999 mines.
2. mimic user play:
  1. for each spot, there are three states: visable or not -> mine or not -> 0 (need to keep expanding) or 1 to 8
  2. for the 0 case, we can use recursion to do the expanding.

## Code: [link](https://gist.github.com/dgossow/d28083522608771e1c65f49822820ba9)

```c
#include <stdlib.h>
#include <iostream>
#include <vector>

template <typename T>
class Matrix {
 public:
  void resize(int rows, int cols) {
    data_.resize(rows * cols);
    rows_ = rows;
    cols_ = cols;
  }

  T& at(int row, int col) { return data_.at(row * cols_ + col); }
  int rows() const { return rows_; }
  int cols() const { return cols_; }

 private:
  std::vector<T> data_;
  int rows_ = 0;
  int cols_ = 0;
};

constexpr int kMine = 9;
using std::min;
using std::max;

class MineField {
 private:
  struct Cell {
    int value = 0;
    bool visible = false;
  };
  Matrix<Cell> field;

 public:
  MineField(int rows, int cols, int num_mines) {
    field.resize(rows, cols);
    int mines_placed = 0;
    while (mines_placed < num_mines) {
      int row = rand() % rows;
      int col = rand() % cols;
      if (field.at(row, col).value == kMine) {
        continue;
      }
      mines_placed++;
      for (int i = max(0, row - 1); i <= min(rows - 1, row + 1); ++i) {
        for (int j = max(0, col - 1); j <= min(cols - 1, col + 1); ++j) {
          if (i == row && j == col) {
            field.at(i, j).value = kMine;
          } else if (field.at(i, j).value != kMine) {
            field.at(i, j).value++;
          }
        }
      }
    }
  }

  bool OnClick(int row, int col) {
    if (row < 0 || row >= field.rows() || col < 0 || col >= field.cols()) {
      return false;
    }
    if (field.at(row, col).visible) {
      return false;
    }
    field.at(row, col).visible = true;
    if (field.at(row, col).value == kMine) {
      std::cout << "BOOM!" << std::endl << std::endl;
      return true;
    }
    if (field.at(row, col).value != 0) {
      return false;
    }
    OnClick(row - 1, col);
    OnClick(row + 1, col);
    OnClick(row, col - 1);
    OnClick(row, col + 1);
    return false;
  }

  void Print(bool show_hidden) {
    for (int i = 0; i < field.rows(); ++i) {
      for (int j = 0; j < field.cols(); ++j) {
        if (field.at(i, j).visible || show_hidden) {
          std::cout << field.at(i, j).value << " ";
        } else {
          std::cout << ". ";
        }
      }
      std::cout << std::endl;
    }
    std::cout << std::endl;
  }
};

int main() {
  srand(1);
  MineField mine_field(10, 10, 7);
  mine_field.Print(true);
  mine_field.OnClick(5, 1);
  mine_field.Print(false);
  mine_field.OnClick(2, 6);
  mine_field.Print(false);
  mine_field.OnClick(9, 3);
  mine_field.Print(false);
  mine_field.OnClick(0, 0);
  mine_field.Print(false);
  mine_field.OnClick(3, 5);
  mine_field.Print(false);
  return 0;
}

```