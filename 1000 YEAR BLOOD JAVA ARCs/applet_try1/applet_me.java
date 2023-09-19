import java.awt.Graphics;
import java.awt.Font;
import java.awt.Color;


class Hello_World_Applet extends java.applet.Applet {

    Font f = new Font("TimesRoman", Font.BOLD,36);

    public void paint(Graphics g) {
        g.setFont(f);
        g.setColor(Color.red);
        g.drawString("HELL TO ZA WARUDO!", 5, 25);
    }
}