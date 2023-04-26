import win32gui, win32ui
from screen_ocr import Reader as ocr

class Create:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.feedback = False

        if self.feedback:
            self.screen_feedback()

    def read_screen(self):
        screen = ocr.create_fast_reader()
        read = screen.read_screen(self.bounding_box())
        return read.as_string()
    
    def bounding_box(self):
        return (self.x - self.width/2, self.y - self.height/2, self.x + self.width/2, self.y + self.height/2)
    
    def bounding_box_round(self):
        return (round(self.x - self.width/2), round(self.y - self.height/2), round(self.x + self.width/2), round(self.y + self.height/2))
    
    def screen_feedback(self):
        dc = win32gui.GetDC(0)
        dcObj = win32ui.CreateDCFromHandle(dc)
        dcObj.SetBkColor(0x00000)
        dcObj.SetBkMode(0)
        while True:
            dcObj.Rectangle(self.bounding_box_round())