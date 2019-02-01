from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

class Robot():
    # a basic mimic of java robot for moving and clicking mouse on mac using python
    
    def __init__(self):
        pass

    def mouse_event(self, kind, posx, posy):
        event = CGEventCreateMouseEvent(None, kind, (posx,posy), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, event)

    def move_to(self, x, y):
        '''Move to position at x,y
        '''
        self.mouse_event(kCGEventMouseMoved, x, y)

    def click_at(self, x, y):
        '''Click at position x,y (no need to move there first)
        '''
        self.mouse_event(kCGEventLeftMouseDown, x, y)
        self.mouse_event(kCGEventLeftMouseUp, x, y)

if __name__ == '__main__':
    robot = Robot()
    robot.move_to(0,0)
