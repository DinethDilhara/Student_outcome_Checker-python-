

from graphics import *

def main1():

    progress_count = int(input("enter progress count"))
    trailer_count = int(input("enter trailer count"))
    retriever_count = int(input("enter retriever count"))
    exclude_count = int(input("enter exclude count"))
    

    total_outcomes=progress_count+trailer_count+exclude_count+retriever_count

    #insert window and make background white size and window heading
    win = GraphWin("Histogram", 600, 550)
    win.setBackground("White")

    #add topic to bar chart
    text0 = Text(Point(150,50),"Histogram Results")
    text0.setFace("arial")
    text0.setSize(22)
    text0.setStyle("bold")
    text0.setTextColor("black")
    text0.draw(win)

    #add perment line of chart
    aLine = Line(Point(50,450), Point(550,450))
    aLine.draw(win)

    #frist bar to represent outcome of progress
    aRectangle1 = Rectangle(Point(70,450), Point(170,450-(progress_count*10)))
    aRectangle1.setFill("pale green")
    aRectangle1.draw(win)

    #add title to frist bar as progress blowe it
    text1 = Text(Point(120,475),"Progress")
    text1.setSize(18)
    text1.setStyle("bold")
    text1.setTextColor("slate gray")
    text1.draw(win)

    #add the count of progress top of the 1st bar
    text6 = Text(Point(120,((450-(progress_count*10))-20)),f"{progress_count}")
    text6.setSize(18)
    text6.setStyle("bold")
    text6.setTextColor("slate gray")
    text6.draw(win)
    
    
    # second bar to represent outcome of trailer
    aRectangle2 = Rectangle(Point(190,450), Point(290,450-(trailer_count*10)))
    aRectangle2.setFill("dark sea green3")
    aRectangle2.draw(win)

    #add title to 2nd bar as Trailer blowe it
    text2 = Text(Point(240,475),"Trailer")
    text2.setSize(18)
    text2.setStyle("bold")
    text2.setTextColor("slate gray")
    text2.draw(win)

    #add the count of trailer top of the 2nd  bar
    text7 = Text(Point(240,((450-(trailer_count*10))-20)),f"{trailer_count}")
    text7.setSize(18)
    text7.setStyle("bold")
    text7.setTextColor("slate gray")
    text7.draw(win)

    
    #third bar to represent outcome of retriever
    aRectangle3 = Rectangle(Point(310,450), Point(410,450-(retriever_count*10)))
    aRectangle3.setFill("DarkOliveGreen3")
    aRectangle3.draw(win)

    #add title to 3rd bar as retriever blowe it
    text3 = Text(Point(360,475),"Retriever")
    text3.setSize(18)
    text3.setStyle("bold")
    text3.setTextColor("slate gray")
    text3.draw(win)

    #add the count of retriever top of the 3rd bar
    text8 = Text(Point(360,((450-(retriever_count*10))-20)),f"{retriever_count}")
    text8.setSize(18)
    text8.setStyle("bold")
    text8.setTextColor("slate gray")
    text8.draw(win)

    
    #4th bar to represent outcome of exclude
    aRectangle4 = Rectangle(Point(430,450), Point(530,450-(exclude_count*10)))
    aRectangle4.setFill("RosyBrown2")
    aRectangle4.draw(win)

    
    #add title to 4th bar as exclude blowe it
    text4 = Text(Point(480,475),"Excluded")
    text4.setSize(18)
    text4.setStyle("bold")
    text4.setTextColor("slate gray")
    text4.draw(win)

    #add the count of exclude top of the 4tg bar
    text9 = Text(Point(480,((450-(exclude_count*10))-20)),f"{exclude_count}")
    text9.setSize(18)
    text9.setStyle("bold")
    text9.setTextColor("slate gray")
    text9.draw(win)


    text5 = Text(Point(175,525),f"{total_outcomes} Outcomes in total.")
    text5.setSize(22)
    text5.setStyle("bold")
    text5.setTextColor("slate gray")
    text5.draw(win)
    

main1()


