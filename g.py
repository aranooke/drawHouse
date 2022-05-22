import graphics as gr

window = gr.GraphWin("Russian game",300,300);
points = 50;
radius = 10;

def air():
    nebo = gr.Rectangle(gr.Point(0,0),gr.Point(300,150));
    nebo.setFill("blue");
    nebo.draw(window);
def ground():
    earth = gr.Rectangle(gr.Point(0,150),gr.Point(300,300));
    earth.setFill("grey");
    earth.draw(window);
def sun():
    soln = gr.Circle(gr.Point(200,60),50);
    soln.setFill("yellow");
    soln.draw(window);
    
def oblaka():
    point= 50;
    for i in range(6):
        oblako = gr.Circle(gr.Point(point,50),20);
        oblako.setFill("grey");
        oblako.draw(window);
        point = point + 5;

def text():
    t = gr.Text(gr.Point(50,50),"Hello people1")
    t.setSize(10);
    t.setTextColor("red");
    t.draw(window);
text();







def house():
    dom = gr.Rectangle(gr.Point(150,150),gr.Point(250,250));
    dom.setFill("brown");
    dom.setWidth(5);
    dom.draw(window);

    
    
    def wind():
        w = gr.Rectangle(gr.Point(170,170),gr.Point(220,220));
        w.setFill("yellow");
        w.setWidth(5);
        w.draw(window);

        def lines():
            l = gr.Line(gr.Point(195,170),gr.Point(195,220));
            l.setWidth(5);
            l.draw(window);

            l2 = gr.Line(gr.Point(170,195),gr.Point(220,195));
            l2.setWidth(5);
            l2.draw(window);


        lines();
            

    wind();
    
        
air();
ground();
sun();
oblaka();
house();
text();
