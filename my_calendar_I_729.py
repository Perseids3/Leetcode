class MyCalendar(object):
    
    def __init__(self):
        self.calendar = [None]


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.calendar == [None]:
            self.calendar = [[start, end]]
            return True

        for i in self.calendar:
            if i[1] <= start or i[0] >= end:
                pass
            else:
                return False
        self.calendar.append([start, end])
        return True

# I think my solution is not bad.
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# obj.book(47,50)
# obj.book(33,41)
# obj.book(39,45)
# obj.book(33,42)
# print(obj.calendar)
