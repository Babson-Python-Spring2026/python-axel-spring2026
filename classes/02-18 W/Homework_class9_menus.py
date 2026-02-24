'''
We want to create a command line driven menu system with 4 levels

1. Clients
    1. Select Client
        1. View Client Summary
        2. Manage Client Cash
    2. Create Client
        1. New Individual
        2. New Joint

2. Portfolios
    1. Trade
        1. Buy
        2. Sell
    2. Performance
        1. Holdings Snapshot
        2. P/L Report

1st level                                   (Clients LHS,                             |                  Portfolios RHS)
2nd level              (Select Client,                         Create Client)         |        (Trade,                  Performance)
3rd level (View Client Summary, Manage Client Cash)    (New Individual, New Joint)    |      (Buy, Sell)         (Holdings Snapshot, P/L Report)
4th leaf  (View Client Summary, Manage Client Cash)    (New Individual, New Joint)    |      (Buy, Sell)         (Holdings Snapshot, P/L Report)


The left hand side (LHS) is provided below. Your job:

1) complete the right hand side (RHS)
    a) Hint: this is copy and paste
    b) changing what gets printed

2) explain in your own words what the program does
    a) Try to include state, transitions and invariants
    b) Does menu control come from logic or program structure

3) assume you are at a leaf endpoint. Instead of returning to level 3
   return to level 1

4) How many discrete paths are in this menu system
'''
'''
OIM 3600 - Menu Navigation Assignment Rubric
--------------------------------------------

Student Name: Axel Petochi
Score: ______ / 100


FUNCTIONAL REQUIREMENTS (70 pts)
--------------------------------

TOP / CLIENTS / PORTFOLIOS NAVIGATION (30 pts)

[ ] TOP menu displays correctly
[ ] Can navigate TOP → CLIENTS → back to TOP
[ ] Can navigate TOP → PORTFOLIOS → back to TOP
[ ] No infinite loops
[ ] No accidental fall-through (one choice triggers one action)


PORTFOLIO BRANCH IMPLEMENTATION (20 pts)

[ ] Portfolio branch fully implemented
[ ] At least one working leaf under PORTFOLIOS
[ ] Back behavior correct within portfolio branch


EXIT-TO-TOP BEHAVIOR (20 pts - A-level feature)

[ ] “Return to Top” works from at least one CLIENT leaf
[ ] “Return to Top” works from at least one PORTFOLIO leaf
[ ] No duplicate menus printed after return
[ ] No stuck loops after return
[ ] to_top cleared only at TOP level


CONTROL FLOW QUALITY (15 pts)

[ ] Correct one-level unwind via break
[ ] Each loop checks to_top appropriately
[ ] No unnecessary nested flag logic
[ ] Code readable and logically structured


STI EXPLANATION (15 pts)

[ ] Identifies key state variables (to_top, etc.)
[ ] Correctly defines transitions
[ ] States invariant about unwinding
[ ] Distinguishes state vs control flow


GRADE BANDS
-----------

C (70-79)
- Honest attempt
- Portfolio branch partially implemented
- Some unwind logic present
- STI explanation minimal or partially incorrect

B (80-89)
- Both branches work correctly
- One-level back behavior correct
- No infinite loops
- STI explanation identifies state, transitions, invariant

A (90-100)
- Exit-to-top works from leaf level (both branches)
- No duplicate menus or stuck loops
- to_top handled cleanly
- STI explanation clearly distinguishes state vs control flow
'''


'''
THIS ASSIGNMENT WILL BE DUE 2/25 (NEXT WEDNESDAY) SO YOU CAN ASK QUESTIONS NEXT MONDAY (2/23)
'''



import functions2 as fn2

while True:
    # reset exit-to-top flag ONLY at top level (invariant)
    to_top = False

    fn2.clear_screen()
    fn2.print_header('Top Menu level 1')
    options = ['Clients', 'Portfolios']
    fn2.display_menu(options)
    choice = fn2.get_menu_choice(options)

    if choice is None:
        print('exit top level menu')
        fn2.pause(1)
        break

    # ===================== CLIENTS =====================
    elif choice == 1:
        while True:
            fn2.clear_screen()
            fn2.print_header('Clients level 2')
            options = ['Select Client', 'Create Client']
            fn2.display_menu(options)
            choice = fn2.get_menu_choice(options)

            if choice is None:
                print('return to level 1')
                fn2.pause(1)
                break

            # -------- Select Client --------
            elif choice == 1:
                while True:
                    fn2.clear_screen()
                    fn2.print_header('Select Client level 3')
                    options = ['View Client Summary', 'Manage Client Cash']
                    fn2.display_menu(options)
                    choice = fn2.get_menu_choice(options)

                    if choice is None:
                        print('return to level 2')
                        fn2.pause(1)
                        break

                    elif choice == 1:
                        fn2.clear_screen()
                        fn2.print_header('View Client Summary level 4')
                        print('you have reached View Client Summary')
                        print('returning to TOP level 1')
                        fn2.pause(1)

                        to_top = True
                        break

                    elif choice == 2:
                        fn2.clear_screen()
                        fn2.print_header('Manage Client Cash level 4')
                        print('you have reached Manage Client Cash')
                        print('returning to TOP level 1')
                        fn2.pause(1)

                        to_top = True
                        break

                if to_top:
                    break

            # -------- Create Client --------
            elif choice == 2:
                while True:
                    fn2.clear_screen()
                    fn2.print_header('Create Client level 3')
                    options = ['New Individual', 'New Joint']
                    fn2.display_menu(options)
                    choice = fn2.get_menu_choice(options)

                    if choice is None:
                        print('return to level 2')
                        fn2.pause(1)
                        break

                    elif choice == 1:
                        fn2.clear_screen()
                        fn2.print_header('New Individual level 4')
                        print('you have reached New Individual')
                        print('returning to TOP level 1')
                        fn2.pause(1)

                        to_top = True
                        break

                    elif choice == 2:
                        fn2.clear_screen()
                        fn2.print_header('New Joint level 4')
                        print('you have reached New Joint')
                        print('returning to TOP level 1')
                        fn2.pause(1)

                        to_top = True
                        break

                if to_top:
                    break

    # ===================== PORTFOLIOS =====================
    elif choice == 2:
        while True:
            fn2.clear_screen()
            fn2.print_header('Portfolios level 2')
            options = ['Trade', 'Performance']
            fn2.display_menu(options)
            choice = fn2.get_menu_choice(options)

            if choice is None:
                print('return to level 1')
                fn2.pause(1)
                break

            # -------- Trade --------
            elif choice == 1:
                while True:
                    fn2.clear_screen()
                    fn2.print_header('Trade level 3')
                    options = ['Buy', 'Sell']
                    fn2.display_menu(options)
                    choice = fn2.get_menu_choice(options)

                    if choice is None:
                        print('return to level 2')
                        fn2.pause(1)
                        break

                    elif choice == 1:
                        fn2.clear_screen()
                        fn2.print_header('Buy level 4')
                        print('you have reached Buy')
                        print('returning to TOP level 1')
                        fn2.pause(1)

                        to_top = True
                        break

                    elif choice == 2:
                        fn2.clear_screen()
                        fn2.print_header('Sell level 4')
                        print('you have reached Sell')
                        print('returning to TOP level 1')
                        fn2.pause(1)

                        to_top = True
                        break

                if to_top:
                    break

            # -------- Performance --------
            elif choice == 2:
                while True:
                    fn2.clear_screen()
                    fn2.print_header('Performance level 3')
                    options = ['Holdings Snapshot', 'P/L Report']
                    fn2.display_menu(options)
                    choice = fn2.get_menu_choice(options)

                    if choice is None:
                        print('return to level 2')
                        fn2.pause(1)
                        break

                    elif choice == 1:
                        fn2.clear_screen()
                        fn2.print_header('Holdings Snapshot level 4')
                        print('you have reached Holdings Snapshot')
                        print('returning to TOP level 1')
                        fn2.pause(1)

                        to_top = True
                        break

                    elif choice == 2:
                        fn2.clear_screen()
                        fn2.print_header('P/L Report level 4')
                        print('you have reached P/L Report')
                        print('returning to TOP level 1')
                        fn2.pause(1)

                        to_top = True
                        break

                if to_top:
                    break




#STI Explanation

#State

# State variables = choice, to_top 
#choice stores the users current selection and determines what to execute next 
#to_top is a yes/no flag - if it's set to true it tells the program that it should return to the top menu 


#Transitions 

#There are 3 transitions in this code 1) downward 2) upward 3) exit to top 
#the downward transition moves down 1 menu at any given point ie from top - clients or clients - select client
#the upward transition moves back 1 menu in the opposite direction
#the exit transition checks if to_top is true and returns to the 1st menu 

#Invariants 
# 
# 1) only 1 menu is displayed at any given time 
# if choice = none always go back one level 
# 3) to_top only resets the top level 
# 4)) each loop represents exactly one menu option
 


#Discrete Paths 

#The total # of discrete paths is 8 given that there are 4 paths for the client side and 4 paths for the porfolios side


#Professor while I wrote the STI expalanations and have a storng understanding of these I struggled 
#with the code aspect and relied heavily on AI for this assignment - I would love to meet and discuss this so I can be best prepared for the exam 