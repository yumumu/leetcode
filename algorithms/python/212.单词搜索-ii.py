#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (45.37%)
# Likes:    332
# Dislikes: 0
# Total Accepted:    30K
# Total Submissions: 66K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
# 
# 单词必须按照字母顺序，通过 相邻的单元格
# 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
# 
# 
# 示例 2：
# 
# 
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n == board[i].length
# 1 
# board[i][j] 是一个小写英文字母
# 1 
# 1 
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同
# 
# 
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True


    def search(self, word):
        if not word:
            return False
        
        node = self.root
        for char in word:
            node = node.children.get(char)
            if not node:
                return False
        return node.isWord


class Solution:
    def dfs(self, board, i, j, path, node, result):
        if node.isWord:
            node.isWord = False
            result.append(path)
        
        row, col = len(board), len(board[0])

        if i < 0 or i >= row or j < 0 or j >= col:
            return
        
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        
        board[i][j] = '#'
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self.dfs(board, i + x, j + y, path + tmp, node, result)
        board[i][j]= tmp


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        # print(trie)
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, '', trie.root, result)
        return result
          
# @lc code=end

