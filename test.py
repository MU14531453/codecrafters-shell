import sys
import curses
print('0')
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
#ok
stdscr.keypad(True)

stdscr.addstr('1')
if stdscr.getkey() == curses.KEY_UP:
    stdscr.addstr('sókces')
else:
    stdscr.addstr('tutaj')
stdscr.addstr('2')
curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()