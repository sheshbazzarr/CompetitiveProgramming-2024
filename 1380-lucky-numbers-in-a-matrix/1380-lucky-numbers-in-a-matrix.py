class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_rows={min(row) for row in matrix}
        max_in_columns={max(column) for column in zip(*matrix)}
        luck_nums=list(min_in_rows & max_in_columns)
        
        return luck_nums