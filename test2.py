import curses
import random
import time

def snow_fall(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh rate in milliseconds

    height, width = stdscr.getmaxyx()
    snowflakes = []
    fall_speed = 0.1  # Default fall speed
    drift_range = [-1, 0, 1]  # Default drift range
    show_legend = True
    
    # Initialize snowflakes at random positions
    for _ in range(width // 3):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        snowflakes.append((y, x))
    
    running = True
    while running:
        height, width = stdscr.getmaxyx()  # Update terminal size dynamically
        if height < 2 or width < 2:
            continue  # Skip frame if terminal is too small
        
        stdscr.clear()
        new_snowflakes = []
        
        for y, x in snowflakes:
            if 0 <= y < height - 1:
                new_x = x + random.choice(drift_range)  # Adjustable drift
                new_x = max(0, min(width - 1, new_x))  # Keep in bounds
                new_snowflakes.append((y + 1, new_x))
            
        # Generate new snowflakes at the top
        for _ in range(max(1, width // 20)):
            new_snowflakes.append((0, random.randint(0, width - 1)))
            
        snowflakes = [sf for sf in new_snowflakes if 0 <= sf[0] < height and 0 <= sf[1] < width]
        
        # Draw snowflakes
        for y, x in snowflakes:
            if 0 <= y < height and 0 <= x < width:
                try:
                    stdscr.addch(y, x, '*')
                except curses.error:
                    pass  # Ignore drawing errors
        
        # Display legend
        if show_legend:
            legend = [
                "Controls:",
                "Up Arrow   - Slow down snowfall",
                "Down Arrow - Speed up snowfall",
                "Left Arrow - Reduce drift",
                "Right Arrow - Increase drift",
                "H - Toggle this legend",
                "Q - Quit"
            ]
            for i, line in enumerate(legend):
                if i < height - 1:
                    stdscr.addstr(i, 0, line)
        
        stdscr.refresh()
        time.sleep(fall_speed)
        
        # Check for user input
        key = stdscr.getch()
        if key == ord('q'):
            running = False
        elif key == curses.KEY_UP:
            fall_speed = min(fall_speed + 0.02, 0.5)  # Slow down
        elif key == curses.KEY_DOWN:
            fall_speed = max(fall_speed - 0.02, 0.02)  # Speed up
        elif key == curses.KEY_LEFT:
            drift_range = [-1, 0] if len(drift_range) > 2 else [-1, 0, 1]  # Reduce drift
        elif key == curses.KEY_RIGHT:
            drift_range = [-2, -1, 0, 1, 2] if len(drift_range) < 5 else [-1, 0, 1]  # Increase drift
        elif key == ord('h'):
            show_legend = not show_legend  # Toggle legend

if __name__ == "__main__":
    curses.wrapper(snow_fall)
