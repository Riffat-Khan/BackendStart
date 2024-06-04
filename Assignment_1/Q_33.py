# In class, we discussed the logical operators and, or, and not. De Morgan‟s Laws can
# sometimes make it more convenient for us to express a logical expression. These laws
# state that the expression not(condition1 and condition2) is logically equivalent to the
# expression (not(condition1)or not(condition2)). Also, the expression not(condition1
# orcondition2) is logically equivalent to the expression (not(condition1)and
# not(condition2)). Use De Morgan‟s Laws to write equivalent expressions for each of the
# following, and then write a program to show that both the original expression and the
# new expression in each case are equivalent.


# a) not( x <5 ) and not( y >= 7 )
x = 8
y = 3

condition_1 = x<5
condition_2 = y >=7

print( "!( x <5 ) and !( y >= 7 ) = " , "!(( x <5 ) or ( y >= 7 ))"  )

print("L.H.S = R.H.S" )
LHS = not(condition_1) and not(condition_2)
RHS = not((condition_1) or (condition_2))
print(LHS , " : " , RHS)



# b) not( a == b ) or not( g != 5 )
a = 3
b = 5
g = 6
condition_1 = a == b
condition_2 = g != 5

print( "!( a == b) or !( g != 5 ) = " , "!(( a == b ) and ( g != 5))"  )

print("L.H.S = R.H.S" )
LHS = not(condition_1) or not(condition_2)
RHS = not((condition_1) and (condition_2))
print(LHS , " : " , RHS)


# c) not( ( x <= 8 ) and ( y >4 ) )
condition_1 = x <= 8 
condition_2 = y >4

print( "!(( x <= 8  ) and ( y >4 )) = "  , "!( x <= 8  ) or !( y >4 )" )

print("L.H.S = R.H.S" )
LHS = not((condition_1) and (condition_2))
RHS = not(condition_1) or not(condition_2)
print(LHS , " : " , RHS)


# d) not( ( i >4 ) or ( j <= 6 ) )
i = 3
j = 4
condition_1 = i > 4
condition_2 = j <= 6 

print( "!(( i > 4 ) or ( j <= 6  )) = " , "!( i > 4 ) and !( j <= 6  )"  )

print("L.H.S = R.H.S" )
LHS = not((condition_1) or (condition_2))
RHS = not(condition_1) and not(condition_2)
print(LHS , " : " , RHS)