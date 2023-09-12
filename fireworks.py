
#  O(1)



# import random

# def create_show(fireworks, show_time):
#     fireworks.sort()    O(1)

#     show = []             O(1)

#     remaining_time = show_time    O(1)


#     while remaining_time > 0 and fireworks:   O(1)

#            # Select a random firework

#            firework = random.choice(fireworks)    O(1)


#            if firework <= remaining_time:            O(1)

#                # Add the firework to the show

#                show.append(firework)                  O(1)

#                remaining_time -= firework            O(1)

#           else:

#               # This firework is too long, remove it from consideration

#               fireworks.remove(firework)             O(1)

#   return show