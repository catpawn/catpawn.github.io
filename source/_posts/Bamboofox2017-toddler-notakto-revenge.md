---
title: Bamboofox2017-toddler-notakto-revenge
date: 2017-12-31 19:02:59
tags:
---

### Solution
1. 純粹要過三關嬴佢個AI 50次
``` python
from pwn import *

r = remote("bamboofox.cs.nctu.edu.tw",58793)

gameBoard = [[0,1,2],[3,4,5],[6,7,8]]

def insertToGameboard(move):
	if move <= 2:
		gameBoard[0][move] = "X"
	elif move > 2 and move < 6:
		gameBoard[1][move-3] = "X"
	else:
		print move
		gameBoard[2][move-6] = "X"

def countTotalX():
	total = 0
	for i in range(3):
		for j in range(3):
			if gameBoard[i][j] == 'X':
				total += 1
	return total

def isWin(x,y):
	buf = gameBoard[x][y]
	gameBoard[x][y] = "X"
	if gameBoard[x][0] == "X" and gameBoard[x][1] == "X" and gameBoard[x][2] == "X":
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][y] == "X" and gameBoard[1][y] == "X" and gameBoard[2][y] == "X":
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X":
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X":
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[1][1] == "X":
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and countTotalX() == 3:
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][1] == "X" and gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and countTotalX() == 3:
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][1] == "X" and gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and countTotalX() == 3:
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][1] == "X" and gameBoard[1][2] == "X" and gameBoard[1][1] == "X" and countTotalX() == 3:
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][1] == "X" and gameBoard[1][2] == "X" and gameBoard[0][1] == "X" and countTotalX() == 3:
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X" and countTotalX() == 3:
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X" and countTotalX() == 3:
		gameBoard[x][y] = buf
		return True
	if gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[1][1] == "X" and countTotalX() == 3:
		gameBoard[x][y] = buf
		return True
	gameBoard[x][y] = buf
	return False


def findNextMove():
	for i in range(3):
		for j in range(3):
			if gameBoard[i][j] == "X":
				continue
			else:
				if not isWin(i,j):
					out = gameBoard[i][j]
					gameBoard[i][j] = "X"
					return out
	return "-1"

isRestart = True
while True:
	res = r.recv(1024)
	print res
	if "My move" in res:
		move = res[res.find("move: ")+6:res.find("move: ")+7]
		print "[+] AI Inserted " + move
		insertToGameboard(int(move))
	if "Your move" in res and "YOU WIN" not in res:
		if gameBoard == [[0,1,2],[3,4,5],[6,7,8]]:
			r.sendline("4")
			gameBoard[1][1] = "X"
		else:
			nextMove = findNextMove()
			print "[+] Player Inserted" + str(nextMove)
			print gameBoard
			r.sendline(str(nextMove))
	if "YOU WIN" in res:
		gameBoard = [[0,1,2],[3,4,5],[6,7,8]]
		gameBoard[1][1] = "X"
		r.sendline("4")

```

### Flag
```
BAMBOOFOX{N0tkt0_IS_fUn_iS_It}
```