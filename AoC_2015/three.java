import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class three{
	
	static ArrayList<Point> houses;
	
	static int part1(Scanner sc){
		houses = new ArrayList<Point>();
		Point current = new Point(0,0);
		int lucky = 1;
		
		while(sc.hasNext()){
			char c = sc.next().charAt(0);
			if(c == '<'){
				current.x -= 1;
			}
			if(c == '>'){
				current.x += 1;	
			}
			if(c == '^'){
				current.y += 1;
			}
			if(c == 'v'){
				current.y -= 1;
			}
			
			boolean notThere = true;
			Point temp = new Point(current.x, current.y);
			
			for(Point p: houses){
				if(p.x == temp.x && p.y == temp.y){
					notThere = false;
					break;
				}
			}
			
			if(notThere == true){
				houses.add(temp);
				lucky+=1;
			}
		}
		return lucky;
	}
	
	static int part2(Scanner sc){
		Point santa = new Point(0,0);
		Point robot = new Point(0,0);
		int lucky = 0;//SHOULD BE ONE LESS THAN USUAL BECAUSE ROBO SANTA ALSO STARTS AT ORIGIN SO IT SHOULDNT BE COUNTED TWICE
		houses = new ArrayList<Point>();
		boolean robo = false;
		
		while(sc.hasNext()){
			char c = sc.next().charAt(0);
			if(c == '<'){
				(robo?robot:santa).x -= 1;
			}
			if(c == '>'){
				(robo?robot:santa).x += 1;	
			}
			if(c == '^'){
				(robo?robot:santa).y += 1;
			}
			if(c == 'v'){
				(robo?robot:santa).y -= 1;
			}
			
			boolean notThere = true;
			Point temp = new Point((robo?robot:santa).x, (robo?robot:santa).y);
			
			for(Point p: houses){
				if(p.x == temp.x && p.y == temp.y){
					notThere = false;
					break;
				}
			}
			
			if(notThere == true){
				houses.add(temp);
				lucky+=1;
			}
			robo = !(robo);
		}
		
		return lucky;
	}
	
	public static void main(String [] args) throws FileNotFoundException{
		Scanner sc = new Scanner(new File("3.txt"));
		sc.useDelimiter("");
		System.out.println("Part 1: "+part1(sc));
		sc = new Scanner(new File("3.txt"));
		sc.useDelimiter("");
		System.out.println("Part 2: "+part2(sc));
	}
}


class Point{ int x; int y;
	public Point(int a, int b){ x = a; y = b;}
	public String toString(){ return "("+x+", "+y+")"; }
}