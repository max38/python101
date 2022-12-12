class JPEG:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        print('JPEG image created')

    def dimension(self):
        print('Image dimension:', self.w, 'x', (self.h)) 
