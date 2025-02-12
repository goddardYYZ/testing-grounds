import curses
import random
import time

def snow_fall(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh rate in milliseconds

    height, width = stdscr.getmaxyx()
    snowflakes = []
    
    # Initialize snowflakes at random positions
    for _ in range(width // 3):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        snowflakes.append((y, x))
    
    while True:
        stdscr.clear()
        new_snowflakes = []
        
        for y, x in snowflakes:
            if y + 1 < height:
                new_x = x + random.choice([-1, 0, 1])  # Slight drift
                new_x = max(0, min(width - 1, new_x))  # Keep in bounds
                new_snowflakes.append((y + 1, new_x))
            
        # Generate new snowflakes at the top
        for _ in range(width // 20):
            new_snowflakes.append((0, random.randint(0, width - 1)))
            
        snowflakes = new_snowflakes
        
        # Draw snowflakes
        for y, x in snowflakes:
            stdscr.addch(y, x, '*')
        
        stdscr.refresh()
        time.sleep(0.1)
        
        # Check for exit condition
        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(snow_fall)
