# PATTERN PROGRAMMING PRACTICE
# C++ + Python | Easy → Medium → Hard
# 120+ pattern problems covering symbols, numbers, alphabets, pyramids, diamonds, hollow shapes, matrices and advanced logic.
# All questions are intentionally language-neutral so the same problem can be implemented in both C++ and Python.

# How to Use This Book
# - Use n as the main input unless the question specifies rows, columns, or another value.
# - First predict the number of rows and columns. Then identify what changes with i and j.
# - For every problem, try a clean nested-loop solution before looking for shortcuts.
# - Solve each question twice: once in C++ and once in Python.
# - For harder patterns, first draw a small case such as n = 3, 4, or 5 on paper.

# Pattern Families Covered
# 1. Basic symbol patterns
# 2. Half/side pyramids
# 3. Full pyramids and inverted pyramids
# 4. Flipped and rotated pyramids
# 5. Number pyramids
# 6. Floyd's triangle
# 7. Palindromic number patterns
# 8. Alphabet patterns
# 9. Continuous alphabet patterns
# 10. Hollow patterns
# 11. Diamonds and half-diamonds
# 12. Hourglass / sandglass patterns
# 13. Butterfly patterns
# 14. X, plus and cross patterns
# 15. Square and rectangle patterns
# 16. Rhombus and parallelogram patterns
# 17. Concentric / boundary-number patterns
# 18. Binary and alternating patterns
# 19. Multiplication/table patterns
# 20. Pascal's triangle
# 21. Spiral / matrix-style patterns
# 22. Mixed and logic-heavy patterns

# Reference Patterns From Your Images
# These reference sheets are included so you can compare your solutions with the pattern styles you asked to cover.
# Reference Sheet 1 – common symbol, number and alphabet patterns
# Reference Sheet 2 – square, half-pyramid, inverted half-pyramid and number patterns
# Reference Sheet 3 – symmetric grid / diamond-style pattern
# Reference Sheet 4 – additional C++ star and number patterns
# Reference Sheet 5 – hollow / split pattern
# Reference Sheet 6 – Java-style number, star and character pattern collection
# Reference Sheet 7 – number pyramid, number diamond and vertical number pyramid


# ==========================================
# LEVEL 1 — EASY PATTERN QUESTIONS
# Start here. Focus on nested loops, row/column control, spaces, and simple sequences.
# ==========================================
# 1. Print an n × n square of * characters.   [Easy | Basic Symbols]
# 2. Print an n × n square where every row contains the row number repeated n times.   [Easy | Numbers]
# 3. Print an n × n square where every row contains the same letter repeated n times.   [Easy | Alphabets]
# 4. Print a left-aligned half pyramid of * with row i containing i stars.   [Easy | Half Pyramid]
# 5. Print an inverted left-aligned half pyramid of *.   [Easy | Inverted Half Pyramid]
# 6. Print a right-aligned half pyramid of *.   [Easy | Right Pyramid]
# 7. Print an inverted right-aligned half pyramid of *.   [Easy | Inverted Right Pyramid]
# 8. Print a left-aligned number triangle: 1 / 1 2 / 1 2 3 / ...   [Easy | Number Triangle]
# 9. Print a repeated-number triangle: 1 / 2 2 / 3 3 3 / ...   [Easy | Number Triangle]
# 10. Print an alphabet triangle: A / A B / A B C / ...   [Easy | Alphabet Triangle]
# 11. Print a repeated-letter triangle: A / B B / C C C / ...   [Easy | Alphabet Triangle]
# 12. Print a full centered star pyramid with n rows.   [Easy | Pyramid]
# 13. Print an inverted centered star pyramid with n rows.   [Easy | Inverted Pyramid]
# 14. Print a centered number pyramid where row i contains 1 through i.   [Easy | Number Pyramid]
# 15. Print a centered pyramid where row i contains the same number i repeated i times.   [Easy | Number Pyramid]
# 16. Print Floyd's triangle for n rows.   [Easy | Floyd Triangle]
# 17. Print a triangle containing consecutive integers starting from 1.   [Easy | Continuous Numbers]
# 18. Print a triangle containing consecutive alphabets starting from A and restarting at A on every row.   [Easy | Continuous Alphabets]
# 19. Print an n × n matrix of alternating 0 and 1, starting with 1.   [Easy | Binary]
# 20. Print an n × n checkerboard pattern using * and space.   [Easy | Checkerboard]
# 21. Print an n × n square with 1 on the main diagonal and 0 elsewhere.   [Easy | Matrix Diagonal]
# 22. Print an n × n square with * on both diagonals and spaces elsewhere.   [Easy | X Pattern]
# 23. Print an n × n square with * on the border and spaces inside.   [Easy | Hollow Square]
# 24. Print a hollow rectangle with r rows and c columns.   [Easy | Hollow Rectangle]
# 25. Print a plus/cross pattern in an odd-sized n × n grid.   [Easy | Plus Pattern]
# 26. Print an n-row right-aligned triangle of numbers 1 to i.   [Easy | Right Number Triangle]
# 27. Print an inverted number triangle: 1 2 3 ... n, then one fewer number per row.   [Easy | Inverted Number Triangle]
# 28. Print an alphabet pyramid using A, B, C... with letters increasing across each row.   [Easy | Alphabet Pyramid]
# 29. Print a triangle of multiplication values: row i contains i, 2i, 3i, ... i*i.   [Easy | Multiplication Triangle]
# 30. Print an n × n table where cell (i,j) contains i*j.   [Easy | Multiplication Matrix]
# 31. Print an n × n matrix where cell (i,j) contains i+j.   [Easy | Sum Matrix]
# 32. Print an n × n matrix where cell (i,j) contains |i-j|.   [Easy | Difference Matrix]
# 33. Print a hollow right triangle of *.   [Easy | Hollow Triangle]
# 34. Print a hollow inverted right triangle of *.   [Easy | Hollow Inverted Triangle]
# 35. Print a hollow centered pyramid of *.   [Easy | Hollow Pyramid]
# 36. Print a hollow inverted centered pyramid of *.   [Easy | Hollow Inverted Pyramid]
# 37. Print a diamond of * with n rows in the upper half.   [Easy | Diamond]
# 38. Print an inverted diamond of *.   [Easy | Inverted Diamond]
# 39. Print a vertical line of * on both sides of an n-row pattern, with a centered filled row at the middle.   [Easy | Split / Center Pattern]
# 40. Print the first n rows of Pascal's triangle.   [Easy | Pascal Triangle]


# ==========================================
# LEVEL 2 — MEDIUM PATTERN QUESTIONS
# These require symmetry, reversing, continuous sequences, hollow boundaries, or more careful space handling.
# ==========================================
# 1. Print a number pyramid in which each row is a palindrome: 1 / 121 / 12321 / ...   [Medium | Palindromic Numbers]
# 2. Print a palindromic number pyramid with row i using 1..i..1.   [Medium | Number Pyramid]
# 3. Print an alphabet palindrome pyramid: A / ABA / ABCBA / ...   [Medium | Palindromic Alphabets]
# 4. Print a continuous alphabet triangle where letters continue across rows without restarting.   [Medium | Continuous Alphabets]
# 5. Print a continuous number pyramid where counting continues across every row.   [Medium | Continuous Numbers]
# 6. Print a rotated number pyramid: numbers increase from the left edge toward the right.   [Medium | Rotated Pyramid]
# 7. Print a flipped version of the rotated number pyramid.   [Medium | Flipped Pyramid]
# 8. Print a half-diamond: increasing star rows followed by decreasing star rows.   [Medium | Half Diamond]
# 9. Print a flipped half-diamond.   [Medium | Flipped Half Diamond]
# 10. Print a full diamond with hollow interior.   [Medium | Hollow Diamond]
# 11. Print an hourglass/sandglass pattern of *.   [Medium | Hourglass]
# 12. Print a hollow hourglass pattern.   [Medium | Hollow Hourglass]
# 13. Print a butterfly pattern: two mirrored triangles separated by spaces.   [Medium | Butterfly]
# 14. Print an inverted butterfly pattern.   [Medium | Inverted Butterfly]
# 15. Print a bow-tie pattern using stars and spaces.   [Medium | Bow Tie]
# 16. Print an hourglass made of numbers, with row values increasing from the edges toward the center.   [Medium | Number Hourglass]
# 17. Print a diamond where the numbers increase toward the center and decrease symmetrically.   [Medium | Number Diamond]
# 18. Print a vertical number palindrome pattern such as 1, 232, 34543 with a user-defined n.   [Medium | Vertical Number Pyramid]
# 19. Print an n × n hollow square whose border contains the row number on each side.   [Medium | Hollow Number Square]
# 20. Print a hollow square with 1 on the top border, 2 on the next border, etc., forming layers.   [Medium | Concentric Layers]
# 21. Print a concentric square pattern where the outer layer is n and the center is 1.   [Medium | Concentric Numbers]
# 22. Print a concentric square pattern of alternating * and # layers.   [Medium | Concentric Symbols]
# 23. Print an n × n matrix with 1 on the border and 0 inside.   [Medium | Boundary Matrix]
# 24. Print an n × n matrix with increasing values only on the boundary and blanks inside.   [Medium | Boundary Numbers]
# 25. Print a lower triangular matrix of numbers where cell (i,j)=j.   [Medium | Lower Triangle]
# 26. Print an upper triangular matrix of numbers where cell (i,j)=j.   [Medium | Upper Triangle]
# 27. Print an upper triangular matrix of consecutive numbers.   [Medium | Upper Triangle]
# 28. Print a lower triangular matrix of consecutive numbers.   [Medium | Lower Triangle]
# 29. Print a binary triangle: 1 / 01 / 101 / 0101 / ...   [Medium | Binary Triangle]
# 30. Print a binary triangle where the starting bit alternates every row.   [Medium | Binary Triangle]
# 31. Print a checkerboard triangle using 0 and 1.   [Medium | Binary Pattern]
# 32. Print a right-aligned alphabet triangle with A B C... on each row.   [Medium | Right Alphabet Triangle]
# 33. Print an inverted alphabet triangle where each row starts at A and gets shorter.   [Medium | Inverted Alphabet]
# 34. Print an alphabet diamond with A at the top and increasing letters toward the center.   [Medium | Alphabet Diamond]
# 35. Print a hollow alphabet diamond with letters only on the boundary.   [Medium | Hollow Alphabet Diamond]
# 36. Print an n-row pattern in which row i contains the first i multiples of i.   [Medium | Multiplication]
# 37. Print multiplication tables 1 to n in triangular form.   [Medium | Multiplication Pattern]
# 38. Print a triangle where each row contains i repeated i times, but reverse the row order.   [Medium | Repeated Numbers]
# 39. Print a square in which odd rows contain increasing numbers and even rows contain decreasing numbers.   [Medium | Alternating Rows]
# 40. Print a square in which odd rows contain A B C... and even rows contain Z Y X... as far as needed.   [Medium | Alternating Alphabets]
# 41. Print a hollow rectangle with a diagonal from top-left to bottom-right.   [Medium | Mixed Shape]


# ==========================================
# LEVEL 3 — HARD PATTERN QUESTIONS
# These combine multiple loop conditions, symmetry, matrices, transformations, and mathematical logic.
# ==========================================
# 1. Print a butterfly pattern whose upper and lower halves are both hollow.   [Hard | Hollow Butterfly]
# 2. Print a hollow butterfly with stars on both outer boundaries and inner wings.   [Hard | Hollow Butterfly]
# 3. Print a double diamond: two diamonds sharing a center row.   [Hard | Double Diamond]
# 4. Print a mirrored double pyramid joined at the center.   [Hard | Double Pyramid]
# 5. Print a sandglass with a hollow border and a filled center line.   [Hard | Hollow Sandglass]
# 6. Print a diamond in which each row is palindromic numbers and spacing is centered.   [Hard | Palindromic Diamond]
# 7. Print an alphabet diamond where each row is a palindrome and letters continue symmetrically.   [Hard | Alphabet Diamond]
# 8. Print a continuous alphabet diamond using A-Z cyclically when the sequence exceeds Z.   [Hard | Continuous Alphabet Diamond]
# 9. Print a number diamond using consecutive integers, continuing the count across rows.   [Hard | Continuous Number Diamond]
# 10. Print a hollow number diamond whose boundary values follow the row number.   [Hard | Hollow Number Diamond]
# 11. Print a rhombus of * with n rows and n columns.   [Hard | Rhombus]
# 12. Print a hollow rhombus of *.   [Hard | Hollow Rhombus]
# 13. Print a parallelogram of numbers with each row shifted right by one position.   [Hard | Parallelogram]
# 14. Print a hollow parallelogram of *.   [Hard | Hollow Parallelogram]
# 15. Print an X pattern where the two diagonals use increasing numbers instead of stars.   [Hard | Number X]
# 16. Print an X pattern where both diagonals contain the same row-dependent number.   [Hard | Number X]
# 17. Print a plus pattern with increasing numbers on the horizontal and vertical arms.   [Hard | Number Plus]
# 18. Print a plus pattern where the center contains n and values decrease away from it.   [Hard | Number Plus]
# 19. Print a border matrix with clockwise increasing numbers around the perimeter.   [Hard | Boundary Traversal]
# 20. Print a matrix where the outer layer contains n, the next layer n-1, down to 1.   [Hard | Concentric Matrix]
# 21. Print a matrix where each concentric layer contains a different alphabet.   [Hard | Concentric Alphabet Matrix]
# 22. Print a matrix whose top-left quadrant mirrors the top-right and bottom halves mirror the top.   [Hard | Symmetric Matrix]
# 23. Print a square pattern that is horizontally and vertically symmetric using *.   [Hard | Symmetric Pattern]
# 24. Print a pattern where the number of spaces decreases by 2 while the number of stars increases by 2 each row, then reverse it.   [Hard | Diamond Logic]
# 25. Print an hourglass where the number of stars decreases to 1 and then increases, while row numbers remain visible.   [Hard | Numbered Hourglass]
# 26. Print a butterfly whose wings contain consecutive numbers rather than stars.   [Hard | Number Butterfly]
# 27. Print an alphabet butterfly where each wing uses A, B, C... symmetrically.   [Hard | Alphabet Butterfly]
# 28. Print a hollow butterfly with a filled central vertical axis.   [Hard | Advanced Butterfly]
# 29. Print a pattern that alternates between a full row, hollow row, full row, hollow row.   [Hard | Alternating Hollow]
# 30. Print a square where the top-left to bottom-right diagonal contains 1..n and the opposite diagonal contains n..1.   [Hard | Dual Diagonal]
# 31. Print a matrix pattern with values equal to min(i,j,n-i+1,n-j+1).   [Hard | Layer Matrix]
# 32. Print a matrix pattern with values equal to max(i,j,n-i+1,n-j+1).   [Hard | Reverse Layer Matrix]
# 33. Print a matrix whose value at each cell is the Manhattan distance from the center.   [Hard | Center Distance]
# 34. Print a matrix whose value at each cell is the minimum distance to any border.   [Hard | Border Distance]
# 35. Print a spiral matrix containing 1 to n².   [Hard | Spiral Matrix]
# 36. Print an anti-clockwise spiral matrix containing 1 to n².   [Hard | Reverse Spiral]
# 37. Print a matrix filled in a zigzag row-wise pattern with consecutive integers.   [Hard | Zigzag Matrix]
# 38. Print a matrix filled in a zigzag column-wise pattern with consecutive integers.   [Hard | Column Zigzag]
# 39. Print Pascal's triangle centered using proper spacing and n rows.   [Hard | Pascal Triangle]
# 40. Print a Pascal-style triangle but replace each value with '*' whenever it is odd and a space whenever it is even.   [Hard | Pascal Parity]
# 41. Print a pattern combining a hollow diamond with an X inside it.   [Hard | Composite Pattern]
# 42. Print a pattern combining a hollow square, both diagonals and a center plus.   [Hard | Composite Pattern]
# 43. Print a number pyramid in which each row starts from the row number and increases to a peak, then decreases.   [Hard | Peak Pyramid]
# 44. Print a pattern where row i contains i numbers, but the sequence reverses direction on every row.   [Hard | Snake Triangle]
# 45. Print a continuous alphabet pattern that wraps from Z back to A.   [Hard | Cyclic Alphabets]
# 46. Print a cyclic number pattern using digits 1-9 repeatedly.   [Hard | Cyclic Numbers]
# 47. Print a pattern where primes occupy the star positions and composite numbers occupy the blank positions.   [Hard | Prime Pattern]
# 48. Print a pattern where Fibonacci numbers are printed along the rows instead of ordinary counting.   [Hard | Fibonacci Pattern]
# 49. Print a pattern where each row contains the first i Fibonacci numbers.   [Hard | Fibonacci Triangle]
# 50. Print a pattern where each cell contains '*' if i+j is even and '#' otherwise.   [Hard | Parity Grid]
# 51. Print a pattern where each cell contains '*' if i*j is even and '#' otherwise.   [Hard | Product Parity Grid]


# ==========================================
# LEVEL 4 — BONUS CHALLENGES
# Use these after completing the main bank. They test reusable functions and generalized pattern logic.
# ==========================================
# 1. For a given n, print all 4 rotations of a half-pyramid in one output: left, right, inverted-left, inverted-right.   [Challenge | Rotation Set]
# 2. For a given odd n, print square, X, plus, hollow square, and border-number patterns one after another.   [Challenge | Pattern Set]
# 3. Given n and a character ch, generate all basic star patterns using ch instead of '*'.   [Challenge | Parameterized Patterns]
# 4. Given n and two characters a and b, generate an alternating checkerboard pattern.   [Challenge | Parameterized Grid]
# 5. Given n, print a diamond, then its 90-degree rotated equivalent using the same number of symbols.   [Challenge | Transformations]
# 6. Given rows and columns, print every possible border-only rectangle variation: top, bottom, left, right, and full border.   [Challenge | Boundary Variations]
# 7. Generate a menu-driven pattern program that lets the user choose among at least 15 patterns.   [Challenge | Menu Driven]
# 8. Build one reusable function per pattern and call the selected function from a menu.   [Challenge | Functions + Patterns]
# 9. Take n and a symbol from the user and generate hollow square, hollow triangle, hollow diamond and hollow rhombus.   [Challenge | Reusable Logic]
# 10. Generate the same 10 selected patterns in both C++ and Python and ensure their outputs match for n=5.   [Challenge | Cross-Language Validation]


# ==========================================
# Pattern-Solving Checklist
# ==========================================
# - Can I identify the total number of rows?
# - For row i, how many spaces are printed?
# - For row i, how many symbols/numbers/letters are printed?
# - Does the sequence restart on every row or continue globally?
# - Is the pattern left-aligned, right-aligned, or centered?
# - Is the pattern symmetric?
# - If it is hollow, which cells are boundary cells?
# - Can I express the condition using i and j?
# - Can I test the pattern with n = 3 before n = 5?
# - Can I implement the same logic in both C++ and Python?
# - Can I convert the repeated logic into a function?
# - Can I explain the time complexity in terms of n?
#
# Important Note
# The questions are language-neutral. C++ and Python both support the loops, conditions, functions, arithmetic, strings/characters, and output operations needed for this entire set. The goal is to practice the pattern logic rather than memorize language-specific syntax.


# ==========================================
# ADDITIONAL SECTION — ALL PATTERNS FROM THE PROVIDED IMAGES
# This section has been added to the original question bank. It converts the distinct pattern examples visible in the supplied reference images into individual practice questions. Solve these in both C++ and Python.
# ==========================================

# ==========================================
# Image 1
# ==========================================
# 1. Print a Simple Pyramid of stars: 1, 2, 3, ..., n stars centered on each row.   [Image 1]
# 2. Print a Flipped Simple Pyramid of stars, with the alignment reversed.   [Image 1]
# 3. Print an Inverted Pyramid of stars: n stars down to 1 star.   [Image 1]
# 4. Print a Flipped Inverted Pyramid of stars, with the inverted alignment reversed.   [Image 1]
# 5. Print a centered Triangle pattern of stars with increasing row width.   [Image 1]
# 6. Print an Inverted Triangle pattern of stars with decreasing row width.   [Image 1]
# 7. Print a Half Diamond: increasing stars to n, then decreasing back to 1.   [Image 1]
# 8. Print a Flipped Half Diamond with the opposite alignment.   [Image 1]
# 9. Print a full Diamond of stars with equal upper and lower halves.   [Image 1]
# 10. Print an Hourglass/Sandglass pattern of stars.   [Image 1]
# 11. Print a Number Pyramid where row i contains the number i repeated i times.   [Image 1]
# 12. Print a Rotated Number Pyramid with numbers arranged in the rotated triangular form shown in the reference.   [Image 1]
# 13. Print a Palindrome Triangle where each row reads the same forward and backward, such as 1, 232, 34543.   [Image 1]
# 14. Print an Alphabet Pyramid with A, AB, ABC, ... centered by row.   [Image 1]
# 15. Print a Continuous Alphabet Pyramid where alphabet characters continue counting across rows instead of restarting.   [Image 1]

# ==========================================
# Image 2 — C++ Pattern Collection
# ==========================================
# 1. Print a solid n × n star square.   [Image 2]
# 2. Print a left-aligned star half pyramid.   [Image 2]
# 3. Print an inverted left-aligned star half pyramid.   [Image 2]
# 4. Print an n × n square where row i contains i repeated across the row.   [Image 2]
# 5. Print a half pyramid where row i contains i repeated i times.   [Image 2]
# 6. Print an inverted repeated-number half pyramid.   [Image 2]
# 7. Print a square where every row prints 1 2 3 ... n.   [Image 2]
# 8. Print a number half pyramid where counting restarts from 1 on every row.   [Image 2]
# 9. Print an inverted number half pyramid where each row starts at 1 and becomes shorter.   [Image 2]
# 10. Print a square filled with consecutive numbers row-wise from 1 to n².   [Image 2]
# 11. Print a lower triangular consecutive-number pattern, continuing the count across rows.   [Image 2]
# 12. Print an inverted version of the continuous-number triangle.   [Image 2]

# ==========================================
# Image 3 — Symmetric Grid Pattern
# ==========================================
# 1. Print the symmetric star-grid pattern shown in the reference: for each row, stars extend from both left and right edges toward the center, with the middle row completely filled.   [Image 3]
# 2. Generalize the same pattern for any odd n using row distance from the center.   [Image 3]
# 3. Print the horizontally and vertically symmetric version where the number of stars in row i is determined by min(i, n-i+1) on both sides.   [Image 3]

# ==========================================
# Image 4 — Complete C++ Pattern Collection
# ==========================================
# 1. Print a solid star square.   [Image 4]
# 2. Print a left-aligned star half pyramid.   [Image 4]
# 3. Print an inverted half pyramid.   [Image 4]
# 4. Print a square of repeated row numbers: 1 1 1..., 2 2 2..., etc.   [Image 4]
# 5. Print a repeated-number half pyramid: 1 / 2 2 / 3 3 3 / ...   [Image 4]
# 6. Print an inverted repeated-number half pyramid.   [Image 4]
# 7. Print a square where every row is 1 2 3 ... n.   [Image 4]
# 8. Print a left-aligned increasing number triangle where each row restarts at 1.   [Image 4]
# 9. Print an inverted increasing number triangle.   [Image 4]
# 10. Print a square of continuous numbers from 1 to n².   [Image 4]
# 11. Print a continuous-number lower triangle.   [Image 4]
# 12. Print an inverted continuous-number triangle.   [Image 4]
# 13. Print a centered star pyramid.   [Image 4]
# 14. Print an inverted centered star pyramid.   [Image 4]
# 15. Print a centered number pyramid.   [Image 4]
# 16. Print a centered inverted number pyramid.   [Image 4]
# 17. Print a hollow star rectangle with only the boundary printed.   [Image 4]
# 18. Print a hollow star square.   [Image 4]
# 19. Print a hollow centered pyramid.   [Image 4]
# 20. Print a hollow inverted centered pyramid.   [Image 4]
# 21. Print a diamond of stars.   [Image 4]
# 22. Print an inverted diamond/sandglass.   [Image 4]
# 23. Print a butterfly pattern with two mirrored triangular wings.   [Image 4]
# 24. Print an inverted butterfly pattern.   [Image 4]
# 25. Print a hollow diamond.   [Image 4]
# 26. Print a pattern containing stars only on the outer boundary and a separate central line.   [Image 4]

# ==========================================
# Image 5 — Hollow Split / Mirror Pattern
# ==========================================
# 1. Print the exact hollow split pattern shown: the first and last positions are always stars, while the inner star groups expand toward the middle and contract symmetrically.   [Image 5]
# 2. Generalize the pattern for odd n so the center row is completely filled.   [Image 5]
# 3. Create the same pattern using a user-provided symbol instead of *.   [Image 5]

# ==========================================
# Image 6 — Java Pattern Programs Sheet
# ==========================================
# 1. Print a left-aligned number triangle: 1 / 1 2 / 1 2 3 / ...   [Image 6]
# 2. Print an inverted number triangle.   [Image 6]
# 3. Print a right-aligned number triangle.   [Image 6]
# 4. Print a reversed right-aligned number triangle.   [Image 6]
# 5. Print a number triangle with continuous counting across rows.   [Image 6]
# 6. Print a number triangle whose row length decreases from n to 1.   [Image 6]
# 7. Print a star half pyramid.   [Image 6]
# 8. Print a right-aligned star pyramid.   [Image 6]
# 9. Print an inverted star pyramid.   [Image 6]
# 10. Print an inverted right-aligned star pyramid.   [Image 6]
# 11. Print a centered star pyramid.   [Image 6]
# 12. Print a centered inverted star pyramid.   [Image 6]
# 13. Print a hollow centered pyramid.   [Image 6]
# 14. Print a hollow inverted pyramid.   [Image 6]
# 15. Print an alphabet triangle A / AB / ABC / ...   [Image 6]
# 16. Print an inverted alphabet triangle.   [Image 6]
# 17. Print a right-aligned alphabet triangle.   [Image 6]
# 18. Print a reversed/right-to-left alphabet triangle.   [Image 6]
# 19. Print a continuous alphabet triangle.   [Image 6]
# 20. Print an alphabet pattern where each row decreases from the previous row.   [Image 6]
# 21. Print a centered alphabet pyramid.   [Image 6]
# 22. Print an inverted centered alphabet pyramid.   [Image 6]
# 23. Print a hollow alphabet pyramid.   [Image 6]
# 24. Print a hollow inverted alphabet pyramid.   [Image 6]
# 25. Print a diamond-shaped alphabet pattern.   [Image 6]
# 26. Print an inverted diamond-shaped alphabet pattern.   [Image 6]
# 27. Print a number diamond.   [Image 6]
# 28. Print a palindromic number diamond.   [Image 6]
# 29. Print a star diamond.   [Image 6]
# 30. Print a hollow star diamond.   [Image 6]
# 31. Print a butterfly star pattern.   [Image 6]
# 32. Print an inverted butterfly pattern.   [Image 6]
# 33. Print a number butterfly.   [Image 6]
# 34. Print an alphabet butterfly.   [Image 6]
# 35. Print an hourglass star pattern.   [Image 6]
# 36. Print a hollow hourglass.   [Image 6]
# 37. Print a number hourglass.   [Image 6]
# 38. Print a continuous-number hourglass.   [Image 6]
# 39. Print a square of repeated numbers.   [Image 6]
# 40. Print a square of continuous numbers.   [Image 6]
# 41. Print a hollow number square.   [Image 6]
# 42. Print a square of repeated alphabets.   [Image 6]
# 43. Print a continuous alphabet square.   [Image 6]
# 44. Print a hollow alphabet square.   [Image 6]
# 45. Print a checkerboard using stars and spaces.   [Image 6]
# 46. Print alternating 1 and 0 rows.   [Image 6]
# 47. Print an X-shaped star pattern.   [Image 6]
# 48. Print a plus-shaped star pattern.   [Image 6]
# 49. Print a rhombus of stars.   [Image 6]
# 50. Print a hollow rhombus.   [Image 6]
# 51. Print a parallelogram of stars.   [Image 6]
# 52. Print a hollow parallelogram.   [Image 6]
# 53. Print a Pascal triangle.   [Image 6]

# ==========================================
# Image 7 — Number Pyramid / Diamond / Vertical Pyramid
# ==========================================
# 1. Print the Number Pyramid shown: row i contains 1 through i.   [Image 7]
# 2. Print the Number Diamond shown: rows increase from 1..n and then decrease back to 1.   [Image 7]
# 3. Print the Vertical Number Pyramid shown, where each row is a palindrome such as 1, 232, 34543, and the sequence continues downward.   [Image 7]
# 4. Generalize the vertical number pyramid for arbitrary n.   [Image 7]
# 5. Create a centered version of the same palindrome-number pyramid.   [Image 7]

# ==========================================
# IMAGE PATTERN MASTER CHECKLIST
# ==========================================
# The following families are now represented in the combined document: simple, inverted, flipped and rotated pyramids; triangles; half diamonds; diamonds; hourglasses; squares; rectangles; hollow shapes; repeated numbers; continuous numbers; palindromic numbers; alphabets; continuous alphabets; butterflies; rhombuses; parallelograms; X and plus patterns; checkerboards; Pascal triangle; number diamonds; vertical number pyramids; and symmetric/mirror patterns.
# Practice rule: For each image-based question, first reproduce the exact output shown by the reference, then modify n and verify that the logic still works. After that, implement the same question in the other language.
